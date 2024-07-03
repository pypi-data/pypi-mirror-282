"""
imfusion - ImFusion SDK for Medical Imaging
===========================================

This module provides Python bindings for the C++ ImFusion libraries.
"""

import os
import sys
import importlib

# For Python 3.8+ on Windows, we need to explicitly add some folders to the DLL directory
if sys.platform == "win32" and (sys.version_info.major, sys.version_info.minor) >= (3, 8):
    imfusionlib_dir = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(os.path.join(imfusionlib_dir, "ImFusionLib.dll")):
        # In the wheel the dlls are directly in the module directory, while in
        # the msi installer they are one directory up
        imfusionlib_dir = os.path.dirname(imfusionlib_dir)
    for extra_dir in ["", "plugins", "plugins/Release"]:
        cur_dir = os.path.join(imfusionlib_dir, extra_dir)
        if os.path.isdir(cur_dir):
            os.add_dll_directory(cur_dir)
    del imfusionlib_dir, extra_dir, cur_dir

try:
    from ._devenv import *
except ImportError:
    pass

try:
    import numpy
except ImportError as e:
    raise ImportError("The imfusion package requires numpy to be installed in the current environment") from e

from ._bindings import *
from ._bindings import _register_algorithm

if 'machinelearning' in locals():
    del machinelearning

# we need to make submodules known in this scope directly for stubgen to consider them
module_dir = os.path.dirname(__file__)
submodules = set(
    [submodule for submodule in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, submodule))])
if 'machinelearning' in submodules:
    from . import machinelearning
if 'io' in submodules:
    from . import io
if 'reg' in submodules:
    from . import reg
if 'anatomy' in submodules:
    from . import anatomy

    if 'spine' in submodules:
        from . import spine
for submodule in submodules:
    if submodule not in locals() and os.path.isfile(os.path.join(module_dir, submodule, '__init__.py')):
        try:
            importlib.import_module(f'.{submodule}', __name__)
        except ImportError:
            print(f'Failed to import submodule {submodule}')
del module_dir

from .Algorithm import *


def keep_data_alive(cls):
    import functools
    import itertools

    def init_wrapper(init):
        """
        Decorator intended to wrap the __init__ of a class that requires instances of Data.
        The decorator will store references of the Data instances in a protected list attribute.
        This is needed in case the Data instance was a temporary object (constructed in the class type's  __call__),
        otherwise we would encounter crashes as python would hold references to already deleted objects.
        """

        @functools.wraps(init)
        def init_with_save(self, *args, **kwargs):
            self._stored_data = []
            for arg in itertools.chain(args, kwargs.values()):
                if isinstance(arg, Data):
                    self._stored_data.append(arg)
            init(self, *args, **kwargs)

        return init_with_save

    @functools.wraps(cls.__init_subclass__)
    def init_subclass(cls, *args, **kwargs):
        """Automatically applies the init_wrapper decorator on the __init__ of any derived class."""
        super(cls).__init_subclass__(*args, **kwargs)
        cls.__init__ = init_wrapper(cls.__init__)

    # Perform the actual wrapping
    cls.__init__ = init_wrapper(cls.__init__)
    cls.__init_subclass__ = classmethod(init_subclass)

    return cls


to_wrap = [name for name, cls in locals().items() if name.endswith('Algorithm') and isinstance(cls, type)]
for name in to_wrap:
    exec(f'{name} = keep_data_alive({name})')

app = None

import atexit


@atexit.register
def __cleanup():
    """
    Deletes the ApplicationController on exit and calls deinit().
    This assures the OpenGL context is cleaned-up correctly.
    """
    global app
    if app is not None:
        del app
    deinit()


del atexit


def register_algorithm(id, name, cls):
    """
    Register an Algorithm to the framework.

    The Algorithm will be accessible through the given id.
    If the id is already used, the registration will fail.

    cls must derive from Algorithm otherwise a TypeError is
    raised.
    """
    if not issubclass(cls, Algorithm):
        raise TypeError('cls does not derive from Algorithm')

    def create_compatible(data, create):
        try:
            input = cls.convert_input(data)
            if type(input) is not dict:
                # if input is a generator, this evaluates it
                input = list(input)
                if not create:
                    return (True, None)

            try:
                # convert list of tuples to dict (e.g. from a generator)
                input_dict = dict(input)
                # only use dicts that contain named parameters
                if all(type(k) == str for k in input_dict.keys()):
                    input = input_dict
            except (TypeError, ValueError):
                pass

            # create an instance with the input as arguments
            if type(input) is dict:
                return (True, cls(**input))
            else:
                return (True, cls(*input))
        except IncompatibleError as e:
            if create and app and str(e):
                log_error('The algorithm could not be created: ' + str(e))
            return (False, None)

    _register_algorithm(id, name, create_compatible)


def __MI_array(self):
    """
    Convenience method for converting MI to a newly created numpy array with scale and shift already applied.

    :param self: instance of MI
    :return: numpy.ndarray
    """
    mi_type = self.type
    if mi_type == Image.BYTE:
        np_type = numpy.byte
    elif mi_type == Image.UBYTE:
        np_type = numpy.ubyte
    elif mi_type == Image.SHORT:
        np_type = numpy.short
    elif mi_type == Image.USHORT:
        np_type = numpy.ushort
    elif mi_type == Image.INT:
        np_type = numpy.int_
    elif mi_type == Image.UINT:
        np_type = numpy.uint
    elif mi_type == Image.FLOAT:
        np_type = numpy.single
    elif mi_type == Image.DOUBLE:
        np_type = numpy.double
    elif mi_type == Image.HFLOAT:
        np_type = numpy.single
    else:
        np_type = numpy.single
    return ((numpy.array(self) / self.scale) - self.shift).astype(np_type)


MemImage.numpy = __MI_array


def __SI_apply_shift_and_scale(self, arr):
    """
    Return a copy of the array with storage values converted to original values.
    The dtype of the returned array is always DOUBLE.
    """
    return (arr / self.scale) - self.shift


SharedImage.apply_shift_and_scale = __SI_apply_shift_and_scale

def __SI_array(self):
    """
    Convenience method for converting SI to a newly created numpy array with scale and shift already applied.

    :param self: instance of SI
    :return: numpy.ndarray
    """
    si_type = self.descriptor.pixel_type
    if si_type == PixelType.BYTE:
        np_type = numpy.byte
    elif si_type == PixelType.UBYTE:
        np_type = numpy.ubyte
    elif si_type == PixelType.SHORT:
        np_type = numpy.short
    elif si_type == PixelType.USHORT:
        np_type = numpy.ushort
    elif si_type == PixelType.INT:
        np_type = numpy.int_
    elif si_type == PixelType.UINT:
        np_type = numpy.uint
    elif si_type == PixelType.FLOAT:
        np_type = numpy.single
    elif si_type == PixelType.DOUBLE:
        np_type = numpy.double
    elif si_type == PixelType.HFLOAT:
        np_type = numpy.single
    else:
        np_type = numpy.single
    return __SI_apply_shift_and_scale(self, numpy.array(self)).astype(np_type)


SharedImage.numpy = __SI_array

def __SIS_apply_shift_and_scale(self, arr):
    """
    Return a copy of the array with storage values converted to original values.
    The dtype of the returned array is always DOUBLE.
    """
    arrays = []
    for i, si in enumerate(self):
        arrays.append(si.apply_shift_and_scale(arr[i]))
    return numpy.stack(arrays, axis=0)


SharedImageSet.apply_shift_and_scale = __SIS_apply_shift_and_scale


def __SI_assign_array(self, arr, casting='same_kind'):
    """
    Copies the contents of arr to the SharedImage.
    Automatically calls setDirtyMem.

    The casting parameters behaves like numpy.copyto.
    """
    mem = numpy.array(self, copy=False)
    numpy.copyto(mem, arr, casting=casting)
    self.set_dirty_mem()


SharedImage.assign_array = __SI_assign_array


def __SIS_array(self):
    # this is much easier than doing that in C++
    arrays = []
    for i in range(len(self)):
        arrays.append(numpy.array(self.get(i), copy=False))
    return numpy.stack(arrays, axis=0)


SharedImageSet.__array__ = __SIS_array
SharedImageSet.numpy = __SIS_array


def __SIS_assign_array(self, arr):
    """
    Copies the contents of arr to the MemImage.
    Automatically calls setDirtyMem.
    """
    num_frames = arr.shape[0]

    for i in range(num_frames):
        if i < self.size:
            mem = numpy.array(self[i], copy=False)
            numpy.copyto(mem, arr[i])
        else:
            self.add(SharedImage(arr[i]))
        self[i].set_dirty_mem()

    while num_frames < self.size:
        self.remove(self[-1])


SharedImageSet.assign_array = __SIS_assign_array
