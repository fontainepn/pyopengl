'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_EXT_create_context_robustness'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_EXT_create_context_robustness')
EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_EXT=_C('EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_EXT',0x3138)
EGL_CONTEXT_OPENGL_ROBUST_ACCESS_EXT=_C('EGL_CONTEXT_OPENGL_ROBUST_ACCESS_EXT',0x30BF)
EGL_LOSE_CONTEXT_ON_RESET_EXT=_C('EGL_LOSE_CONTEXT_ON_RESET_EXT',0x31BF)
EGL_NO_RESET_NOTIFICATION_EXT=_C('EGL_NO_RESET_NOTIFICATION_EXT',0x31BE)

