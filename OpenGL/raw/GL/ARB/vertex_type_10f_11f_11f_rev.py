'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_vertex_type_10f_11f_11f_rev'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_type_10f_11f_11f_rev')
GL_UNSIGNED_INT_10F_11F_11F_REV=_C('GL_UNSIGNED_INT_10F_11F_11F_REV',0x8C3B)

