'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_blend_subtract'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_blend_subtract')
GL_FUNC_REVERSE_SUBTRACT_EXT=_C('GL_FUNC_REVERSE_SUBTRACT_EXT',0x800B)
GL_FUNC_SUBTRACT_EXT=_C('GL_FUNC_SUBTRACT_EXT',0x800A)

