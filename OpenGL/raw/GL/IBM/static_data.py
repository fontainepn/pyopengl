'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_IBM_static_data'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_IBM_static_data',error_checker=_errors._error_checker)
GL_ALL_STATIC_DATA_IBM=_C('GL_ALL_STATIC_DATA_IBM',103060)
GL_STATIC_VERTEX_ARRAY_IBM=_C('GL_STATIC_VERTEX_ARRAY_IBM',103061)
@_f
@_p.types(None,_cs.GLenum)
def glFlushStaticDataIBM(target):pass