'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_shared_exponent'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_shared_exponent')
GL_RGB9_E5_EXT=_C('GL_RGB9_E5_EXT',0x8C3D)
GL_TEXTURE_SHARED_SIZE_EXT=_C('GL_TEXTURE_SHARED_SIZE_EXT',0x8C3F)
GL_UNSIGNED_INT_5_9_9_9_REV_EXT=_C('GL_UNSIGNED_INT_5_9_9_9_REV_EXT',0x8C3E)

