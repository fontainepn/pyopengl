'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_VERSION_EGL_1_2'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_VERSION_EGL_1_2')
EGL_ALPHA_FORMAT=_C('EGL_ALPHA_FORMAT',0x3088)
EGL_ALPHA_FORMAT_NONPRE=_C('EGL_ALPHA_FORMAT_NONPRE',0x308B)
EGL_ALPHA_FORMAT_PRE=_C('EGL_ALPHA_FORMAT_PRE',0x308C)
EGL_ALPHA_MASK_SIZE=_C('EGL_ALPHA_MASK_SIZE',0x303E)
EGL_BUFFER_DESTROYED=_C('EGL_BUFFER_DESTROYED',0x3095)
EGL_BUFFER_PRESERVED=_C('EGL_BUFFER_PRESERVED',0x3094)
EGL_CLIENT_APIS=_C('EGL_CLIENT_APIS',0x308D)
EGL_COLORSPACE=_C('EGL_COLORSPACE',0x3087)
EGL_COLORSPACE_LINEAR=_C('EGL_COLORSPACE_LINEAR',0x308A)
EGL_COLORSPACE_sRGB=_C('EGL_COLORSPACE_sRGB',0x3089)
EGL_COLOR_BUFFER_TYPE=_C('EGL_COLOR_BUFFER_TYPE',0x303F)
EGL_CONTEXT_CLIENT_TYPE=_C('EGL_CONTEXT_CLIENT_TYPE',0x3097)
EGL_DISPLAY_SCALING=_C('EGL_DISPLAY_SCALING',10000)
EGL_HORIZONTAL_RESOLUTION=_C('EGL_HORIZONTAL_RESOLUTION',0x3090)
EGL_LUMINANCE_BUFFER=_C('EGL_LUMINANCE_BUFFER',0x308F)
EGL_LUMINANCE_SIZE=_C('EGL_LUMINANCE_SIZE',0x303D)
EGL_OPENGL_ES_API=_C('EGL_OPENGL_ES_API',0x30A0)
EGL_OPENGL_ES_BIT=_C('EGL_OPENGL_ES_BIT',0x0001)
EGL_OPENVG_API=_C('EGL_OPENVG_API',0x30A1)
EGL_OPENVG_BIT=_C('EGL_OPENVG_BIT',0x0002)
EGL_OPENVG_IMAGE=_C('EGL_OPENVG_IMAGE',0x3096)
EGL_PIXEL_ASPECT_RATIO=_C('EGL_PIXEL_ASPECT_RATIO',0x3092)
EGL_RENDERABLE_TYPE=_C('EGL_RENDERABLE_TYPE',0x3040)
EGL_RENDER_BUFFER=_C('EGL_RENDER_BUFFER',0x3086)
EGL_RGB_BUFFER=_C('EGL_RGB_BUFFER',0x308E)
EGL_SINGLE_BUFFER=_C('EGL_SINGLE_BUFFER',0x3085)
EGL_SWAP_BEHAVIOR=_C('EGL_SWAP_BEHAVIOR',0x3093)
# EGL_UNKNOWN=_C('EGL_UNKNOWN',((EGLint)-1))
EGL_VERTICAL_RESOLUTION=_C('EGL_VERTICAL_RESOLUTION',0x3091)
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLenum)
def eglBindAPI(api):pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLenum,_cs.EGLClientBuffer,_cs.EGLConfig,arrays.GLintArray)
def eglCreatePbufferFromClientBuffer(dpy,buftype,buffer,config,attrib_list):pass
@_f
@_p.types(_cs.EGLenum,)
def eglQueryAPI():pass
@_f
@_p.types(_cs.EGLBoolean,)
def eglReleaseThread():pass
@_f
@_p.types(_cs.EGLBoolean,)
def eglWaitClient():pass
