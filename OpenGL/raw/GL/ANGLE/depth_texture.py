'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ANGLE_depth_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ANGLE_depth_texture')
GL_DEPTH24_STENCIL8_OES=_C('GL_DEPTH24_STENCIL8_OES',0x88F0)
GL_DEPTH_COMPONENT=_C('GL_DEPTH_COMPONENT',0x1902)
GL_DEPTH_COMPONENT16=_C('GL_DEPTH_COMPONENT16',0x81A5)
GL_DEPTH_COMPONENT32_OES=_C('GL_DEPTH_COMPONENT32_OES',0x81A7)
GL_DEPTH_STENCIL_OES=_C('GL_DEPTH_STENCIL_OES',0x84F9)
GL_UNSIGNED_INT=_C('GL_UNSIGNED_INT',0x1405)
GL_UNSIGNED_INT_24_8_OES=_C('GL_UNSIGNED_INT_24_8_OES',0x84FA)
GL_UNSIGNED_SHORT=_C('GL_UNSIGNED_SHORT',0x1403)

