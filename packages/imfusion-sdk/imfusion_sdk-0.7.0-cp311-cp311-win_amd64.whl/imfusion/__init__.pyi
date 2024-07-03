"""

imfusion - ImFusion SDK for Medical Imaging
===========================================

This module provides Python bindings for the C++ ImFusion libraries.
"""
from __future__ import annotations
from imfusion.Algorithm import Algorithm
from imfusion._bindings import Annotation
from imfusion._bindings import AnnotationModel
from imfusion._bindings import ApplicationController
from imfusion._bindings import BaseAlgorithm
from imfusion._bindings import Configurable
from imfusion._bindings import ConsoleController
from imfusion._bindings import CroppingMask
from imfusion._bindings import Data
from imfusion._bindings import DataComponent
from imfusion._bindings import DataComponentBase
from imfusion._bindings import DataComponentList
from imfusion._bindings import DataGroup
from imfusion._bindings import DataList
from imfusion._bindings import DataModel
from imfusion._bindings import DataSourceComponent
from imfusion._bindings import DatasetLicenseComponent
from imfusion._bindings import Deformation
from imfusion._bindings import Display
from imfusion._bindings import DisplayOptions2d
from imfusion._bindings import DisplayOptions3d
from imfusion._bindings import ExplicitIntensityMask
from imfusion._bindings import ExplicitMask
from imfusion._bindings import FileNotFoundError
from imfusion._bindings import FrameworkInfo
from imfusion._bindings import GeneralEquipmentModuleDataComponent
from imfusion._bindings import GlPlatformInfo
from imfusion._bindings import IOError
from imfusion._bindings import Image
from imfusion._bindings import ImageDescriptor
from imfusion._bindings import ImageDescriptorWorld
from imfusion._bindings import ImageInfoDataComponent
from imfusion._bindings import ImageResamplingAlgorithm
from imfusion._bindings import ImageView2D
from imfusion._bindings import ImageView3D
from imfusion._bindings import IncompatibleError
from imfusion._bindings import IntensityMask
from imfusion._bindings import LabelDataComponent
from imfusion._bindings import LayoutMode
from imfusion._bindings import LicenseInfo
from imfusion._bindings import Mask
from imfusion._bindings import MemImage
from imfusion._bindings import Mesh
from imfusion._bindings import MissingLicenseError
from imfusion._bindings import Optimizer
from imfusion._bindings import PaddingMode
from imfusion._bindings import ParametricDeformation
from imfusion._bindings import PixelType
from imfusion._bindings import PluginInfo
from imfusion._bindings import PointCloud
from imfusion._bindings import Properties
from imfusion._bindings import RealWorldMappingDataComponent
from imfusion._bindings import ReferenceImageDataComponent
from imfusion._bindings import ReferencedInstancesComponent
from imfusion._bindings import RegionOfInterest
from imfusion._bindings import Selection
from imfusion._bindings import SharedImage
from imfusion._bindings import SharedImageSet
from imfusion._bindings import SignalConnection
from imfusion._bindings import SkippingMask
from imfusion._bindings import SourceInfoComponent
from imfusion._bindings import TrackedSharedImageSet
from imfusion._bindings import TrackingSequence
from imfusion._bindings import TrackingSequence as TrackingStream
from imfusion._bindings import TransformationStashDataComponent
from imfusion._bindings import View
from imfusion._bindings import _register_algorithm
from imfusion._bindings import algorithmName
from imfusion._bindings import algorithm_properties
from imfusion._bindings import auto_window
from imfusion._bindings import available_algorithms
from imfusion._bindings import available_data_components
from imfusion._bindings import create_algorithm
from imfusion._bindings import create_data_component
from imfusion._bindings import deinit
from imfusion._bindings import execute_algorithm
from imfusion._bindings import gpu_info
from imfusion._bindings import has_gl_context
from imfusion._bindings import imagemath
from imfusion._bindings import info
from imfusion._bindings import init
from imfusion._bindings import io
from imfusion._bindings import load
from imfusion._bindings import load_plugin
from imfusion._bindings import load_plugins
from imfusion._bindings import log_debug
from imfusion._bindings import log_error
from imfusion._bindings import log_fatal
from imfusion._bindings import log_info
from imfusion._bindings import log_level
from imfusion._bindings import log_trace
from imfusion._bindings import log_warn
from imfusion._bindings import open
from imfusion._bindings import open_in_suite
from imfusion._bindings import py_doc_url
from imfusion._bindings import reg
from imfusion._bindings import save
from imfusion._bindings import set_log_level
from imfusion._bindings import transfer_logging_to_python
from imfusion._bindings import unregister_algorithm
import importlib as importlib
import numpy as numpy
import os as os
import sys as sys
from . import _bindings
from . import _devenv
from . import labels
from . import machinelearning
__all__ = ['Algorithm', 'Annotation', 'AnnotationModel', 'ApplicationController', 'BaseAlgorithm', 'Configurable', 'ConsoleController', 'CroppingMask', 'Data', 'DataComponent', 'DataComponentBase', 'DataComponentList', 'DataGroup', 'DataList', 'DataModel', 'DataSourceComponent', 'DatasetLicenseComponent', 'Deformation', 'Display', 'DisplayOptions2d', 'DisplayOptions3d', 'ExplicitIntensityMask', 'ExplicitMask', 'FileNotFoundError', 'FrameworkInfo', 'GeneralEquipmentModuleDataComponent', 'GlPlatformInfo', 'IOError', 'Image', 'ImageDescriptor', 'ImageDescriptorWorld', 'ImageInfoDataComponent', 'ImageResamplingAlgorithm', 'ImageView2D', 'ImageView3D', 'IncompatibleError', 'IntensityMask', 'LabelDataComponent', 'LayoutMode', 'LicenseInfo', 'Mask', 'MemImage', 'Mesh', 'MissingLicenseError', 'Optimizer', 'PaddingMode', 'ParametricDeformation', 'PixelType', 'PluginInfo', 'PointCloud', 'Properties', 'RealWorldMappingDataComponent', 'ReferenceImageDataComponent', 'ReferencedInstancesComponent', 'RegionOfInterest', 'Selection', 'SharedImage', 'SharedImageSet', 'SignalConnection', 'SkippingMask', 'SourceInfoComponent', 'TrackedSharedImageSet', 'TrackingSequence', 'TrackingStream', 'TransformationStashDataComponent', 'View', 'algorithmName', 'algorithm_properties', 'app', 'auto_window', 'available_algorithms', 'available_data_components', 'create_algorithm', 'create_data_component', 'deinit', 'execute_algorithm', 'gpu_info', 'has_gl_context', 'imagemath', 'importlib', 'info', 'init', 'io', 'keep_data_alive', 'labels', 'load', 'load_plugin', 'load_plugins', 'log_debug', 'log_error', 'log_fatal', 'log_info', 'log_level', 'log_trace', 'log_warn', 'machinelearning', 'name', 'numpy', 'open', 'open_in_suite', 'os', 'py_doc_url', 'reg', 'register_algorithm', 'save', 'set_log_level', 'submodule', 'submodules', 'sys', 'to_wrap', 'transfer_logging_to_python', 'unregister_algorithm']
def __MI_array(self):
    """
    
        Convenience method for converting MI to a newly created numpy array with scale and shift already applied.
    
        :param self: instance of MI
        :return: numpy.ndarray
        
    """
def __SIS_apply_shift_and_scale(self, arr):
    """
    
        Return a copy of the array with storage values converted to original values.
        The dtype of the returned array is always DOUBLE.
        
    """
def __SIS_array(self):
    ...
def __SIS_assign_array(self, arr):
    """
    
        Copies the contents of arr to the MemImage.
        Automatically calls setDirtyMem.
        
    """
def __SI_apply_shift_and_scale(self, arr):
    """
    
        Return a copy of the array with storage values converted to original values.
        The dtype of the returned array is always DOUBLE.
        
    """
def __SI_array(self):
    """
    
        Convenience method for converting SI to a newly created numpy array with scale and shift already applied.
    
        :param self: instance of SI
        :return: numpy.ndarray
        
    """
def __SI_assign_array(self, arr, casting = 'same_kind'):
    """
    
        Copies the contents of arr to the SharedImage.
        Automatically calls setDirtyMem.
    
        The casting parameters behaves like numpy.copyto.
        
    """
def __cleanup():
    """
    
        Deletes the ApplicationController on exit and calls deinit().
        This assures the OpenGL context is cleaned-up correctly.
        
    """
def keep_data_alive(cls):
    ...
def register_algorithm(id, name, cls):
    """
    
        Register an Algorithm to the framework.
    
        The Algorithm will be accessible through the given id.
        If the id is already used, the registration will fail.
    
        cls must derive from Algorithm otherwise a TypeError is
        raised.
        
    """
app = None
name: str = 'Algorithm'
submodule: str = 'machinelearning'
submodules: set = {'__pycache__', 'labels', 'machinelearning'}
to_wrap: list = ['BaseAlgorithm', 'ImageResamplingAlgorithm', 'Algorithm']
