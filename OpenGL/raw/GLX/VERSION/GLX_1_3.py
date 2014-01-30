'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_VERSION_GLX_1_3'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_VERSION_GLX_1_3')
GLX_ACCUM_BUFFER_BIT=_C('GLX_ACCUM_BUFFER_BIT',0x00000080)
GLX_AUX_BUFFERS_BIT=_C('GLX_AUX_BUFFERS_BIT',0x00000010)
GLX_BACK_LEFT_BUFFER_BIT=_C('GLX_BACK_LEFT_BUFFER_BIT',0x00000004)
GLX_BACK_RIGHT_BUFFER_BIT=_C('GLX_BACK_RIGHT_BUFFER_BIT',0x00000008)
GLX_COLOR_INDEX_BIT=_C('GLX_COLOR_INDEX_BIT',0x00000002)
GLX_COLOR_INDEX_TYPE=_C('GLX_COLOR_INDEX_TYPE',0x8015)
GLX_CONFIG_CAVEAT=_C('GLX_CONFIG_CAVEAT',0x20)
GLX_DAMAGED=_C('GLX_DAMAGED',0x8020)
GLX_DEPTH_BUFFER_BIT=_C('GLX_DEPTH_BUFFER_BIT',0x00000020)
GLX_DIRECT_COLOR=_C('GLX_DIRECT_COLOR',0x8003)
GLX_DONT_CARE=_C('GLX_DONT_CARE',0xFFFFFFFF)
GLX_DRAWABLE_TYPE=_C('GLX_DRAWABLE_TYPE',0x8010)
GLX_EVENT_MASK=_C('GLX_EVENT_MASK',0x801F)
GLX_FBCONFIG_ID=_C('GLX_FBCONFIG_ID',0x8013)
GLX_FRONT_LEFT_BUFFER_BIT=_C('GLX_FRONT_LEFT_BUFFER_BIT',0x00000001)
GLX_FRONT_RIGHT_BUFFER_BIT=_C('GLX_FRONT_RIGHT_BUFFER_BIT',0x00000002)
GLX_GRAY_SCALE=_C('GLX_GRAY_SCALE',0x8006)
GLX_HEIGHT=_C('GLX_HEIGHT',0x801E)
GLX_LARGEST_PBUFFER=_C('GLX_LARGEST_PBUFFER',0x801C)
GLX_MAX_PBUFFER_HEIGHT=_C('GLX_MAX_PBUFFER_HEIGHT',0x8017)
GLX_MAX_PBUFFER_PIXELS=_C('GLX_MAX_PBUFFER_PIXELS',0x8018)
GLX_MAX_PBUFFER_WIDTH=_C('GLX_MAX_PBUFFER_WIDTH',0x8016)
GLX_NONE=_C('GLX_NONE',0x8000)
GLX_NON_CONFORMANT_CONFIG=_C('GLX_NON_CONFORMANT_CONFIG',0x800D)
GLX_PBUFFER=_C('GLX_PBUFFER',0x8023)
GLX_PBUFFER_BIT=_C('GLX_PBUFFER_BIT',0x00000004)
GLX_PBUFFER_CLOBBER_MASK=_C('GLX_PBUFFER_CLOBBER_MASK',0x08000000)
GLX_PBUFFER_HEIGHT=_C('GLX_PBUFFER_HEIGHT',0x8040)
GLX_PBUFFER_WIDTH=_C('GLX_PBUFFER_WIDTH',0x8041)
GLX_PIXMAP_BIT=_C('GLX_PIXMAP_BIT',0x00000002)
GLX_PRESERVED_CONTENTS=_C('GLX_PRESERVED_CONTENTS',0x801B)
GLX_PSEUDO_COLOR=_C('GLX_PSEUDO_COLOR',0x8004)
GLX_RENDER_TYPE=_C('GLX_RENDER_TYPE',0x8011)
GLX_RGBA_BIT=_C('GLX_RGBA_BIT',0x00000001)
GLX_RGBA_TYPE=_C('GLX_RGBA_TYPE',0x8014)
GLX_SAVED=_C('GLX_SAVED',0x8021)
GLX_SCREEN=_C('GLX_SCREEN',0x800C)
GLX_SLOW_CONFIG=_C('GLX_SLOW_CONFIG',0x8001)
GLX_STATIC_COLOR=_C('GLX_STATIC_COLOR',0x8005)
GLX_STATIC_GRAY=_C('GLX_STATIC_GRAY',0x8007)
GLX_STENCIL_BUFFER_BIT=_C('GLX_STENCIL_BUFFER_BIT',0x00000040)
GLX_TRANSPARENT_ALPHA_VALUE=_C('GLX_TRANSPARENT_ALPHA_VALUE',0x28)
GLX_TRANSPARENT_BLUE_VALUE=_C('GLX_TRANSPARENT_BLUE_VALUE',0x27)
GLX_TRANSPARENT_GREEN_VALUE=_C('GLX_TRANSPARENT_GREEN_VALUE',0x26)
GLX_TRANSPARENT_INDEX=_C('GLX_TRANSPARENT_INDEX',0x8009)
GLX_TRANSPARENT_INDEX_VALUE=_C('GLX_TRANSPARENT_INDEX_VALUE',0x24)
GLX_TRANSPARENT_RED_VALUE=_C('GLX_TRANSPARENT_RED_VALUE',0x25)
GLX_TRANSPARENT_RGB=_C('GLX_TRANSPARENT_RGB',0x8008)
GLX_TRANSPARENT_TYPE=_C('GLX_TRANSPARENT_TYPE',0x23)
GLX_TRUE_COLOR=_C('GLX_TRUE_COLOR',0x8002)
GLX_VISUAL_ID=_C('GLX_VISUAL_ID',0x800B)
GLX_WIDTH=_C('GLX_WIDTH',0x801D)
GLX_WINDOW=_C('GLX_WINDOW',0x8022)
GLX_WINDOW_BIT=_C('GLX_WINDOW_BIT',0x00000001)
GLX_X_RENDERABLE=_C('GLX_X_RENDERABLE',0x8012)
GLX_X_VISUAL_TYPE=_C('GLX_X_VISUAL_TYPE',0x22)
@_f
@_p.types(ctypes.POINTER(_cs.GLXFBConfig),ctypes.POINTER(_cs.Display),_cs.c_int,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.c_int))
def glXChooseFBConfig(dpy,screen,attrib_list,nelements):pass
@_f
@_p.types(_cs.GLXContext,ctypes.POINTER(_cs.Display),_cs.GLXFBConfig,_cs.c_int,_cs.GLXContext,_cs.Bool)
def glXCreateNewContext(dpy,config,render_type,share_list,direct):pass
@_f
@_p.types(_cs.GLXPbuffer,ctypes.POINTER(_cs.Display),_cs.GLXFBConfig,ctypes.POINTER(_cs.c_int))
def glXCreatePbuffer(dpy,config,attrib_list):pass
@_f
@_p.types(_cs.GLXPixmap,ctypes.POINTER(_cs.Display),_cs.GLXFBConfig,_cs.Pixmap,ctypes.POINTER(_cs.c_int))
def glXCreatePixmap(dpy,config,pixmap,attrib_list):pass
@_f
@_p.types(_cs.GLXWindow,ctypes.POINTER(_cs.Display),_cs.GLXFBConfig,_cs.Window,ctypes.POINTER(_cs.c_int))
def glXCreateWindow(dpy,config,win,attrib_list):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXPbuffer)
def glXDestroyPbuffer(dpy,pbuf):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXPixmap)
def glXDestroyPixmap(dpy,pixmap):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXWindow)
def glXDestroyWindow(dpy,win):pass
@_f
@_p.types(_cs.GLXDrawable,)
def glXGetCurrentReadDrawable():pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.GLXFBConfig,_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXGetFBConfigAttrib(dpy,config,attribute,value):pass
@_f
@_p.types(ctypes.POINTER(_cs.GLXFBConfig),ctypes.POINTER(_cs.Display),_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXGetFBConfigs(dpy,screen,nelements):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,ctypes.POINTER(_cs.c_ulong))
def glXGetSelectedEvent(dpy,draw,event_mask):pass
@_f
@_p.types(ctypes.POINTER(_cs.XVisualInfo),ctypes.POINTER(_cs.Display),_cs.GLXFBConfig)
def glXGetVisualFromFBConfig(dpy,config):pass
@_f
@_p.types(_cs.Bool,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.GLXDrawable,_cs.GLXContext)
def glXMakeContextCurrent(dpy,draw,read,ctx):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.GLXContext,_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXQueryContext(dpy,ctx,attribute,value):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.c_int,ctypes.POINTER(_cs.c_uint))
def glXQueryDrawable(dpy,draw,attribute,value):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.c_ulong)
def glXSelectEvent(dpy,draw,event_mask):pass
