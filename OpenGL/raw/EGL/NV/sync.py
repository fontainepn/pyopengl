'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_NV_sync'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_NV_sync')
EGL_ALREADY_SIGNALED_NV=_C('EGL_ALREADY_SIGNALED_NV',0x30EA)
EGL_CONDITION_SATISFIED_NV=_C('EGL_CONDITION_SATISFIED_NV',0x30EC)
EGL_FOREVER_NV=_C('EGL_FOREVER_NV',0xFFFFFFFFFFFFFFFF)
# EGL_NO_SYNC_NV=_C('EGL_NO_SYNC_NV',((EGLSyncNV)0))
EGL_SIGNALED_NV=_C('EGL_SIGNALED_NV',0x30E8)
EGL_SYNC_CONDITION_NV=_C('EGL_SYNC_CONDITION_NV',0x30EE)
EGL_SYNC_FENCE_NV=_C('EGL_SYNC_FENCE_NV',0x30EF)
EGL_SYNC_FLUSH_COMMANDS_BIT_NV=_C('EGL_SYNC_FLUSH_COMMANDS_BIT_NV',0x0001)
EGL_SYNC_PRIOR_COMMANDS_COMPLETE_NV=_C('EGL_SYNC_PRIOR_COMMANDS_COMPLETE_NV',0x30E6)
EGL_SYNC_STATUS_NV=_C('EGL_SYNC_STATUS_NV',0x30E7)
EGL_SYNC_TYPE_NV=_C('EGL_SYNC_TYPE_NV',0x30ED)
EGL_TIMEOUT_EXPIRED_NV=_C('EGL_TIMEOUT_EXPIRED_NV',0x30EB)
EGL_UNSIGNALED_NV=_C('EGL_UNSIGNALED_NV',0x30E9)
@_f
@_p.types(_cs.EGLint,_cs.EGLSyncNV,_cs.EGLint,_cs.EGLTimeNV)
def eglClientWaitSyncNV(sync,flags,timeout):pass
@_f
@_p.types(_cs.EGLSyncNV,_cs.EGLDisplay,_cs.EGLenum,arrays.GLintArray)
def eglCreateFenceSyncNV(dpy,condition,attrib_list):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLSyncNV)
def eglDestroySyncNV(sync):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLSyncNV)
def eglFenceNV(sync):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLSyncNV,_cs.EGLint,arrays.GLintArray)
def eglGetSyncAttribNV(sync,attribute,value):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLSyncNV,_cs.EGLenum)
def eglSignalSyncNV(sync,mode):pass
