'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_vertex_array_bgra'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_vertex_array_bgra')
GL_BGRA=_C('GL_BGRA',0x80E1)

