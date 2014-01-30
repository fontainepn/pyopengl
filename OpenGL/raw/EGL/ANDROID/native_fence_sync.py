'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_ANDROID_native_fence_sync'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_ANDROID_native_fence_sync')
EGL_NO_NATIVE_FENCE_FD_ANDROID=_C('EGL_NO_NATIVE_FENCE_FD_ANDROID',-1)
EGL_SYNC_NATIVE_FENCE_ANDROID=_C('EGL_SYNC_NATIVE_FENCE_ANDROID',0x3144)
EGL_SYNC_NATIVE_FENCE_FD_ANDROID=_C('EGL_SYNC_NATIVE_FENCE_FD_ANDROID',0x3145)
EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID=_C('EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID',0x3146)
@_f
@_p.types(_cs.EGLint,_cs.EGLDisplay,_cs.EGLSyncKHR)
def eglDupNativeFenceFDANDROID(dpy,sync):pass
