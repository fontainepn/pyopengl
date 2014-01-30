'''OpenGL extension KHR.gl_renderbuffer_image

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.gl_renderbuffer_image to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/gl_renderbuffer_image.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.KHR.gl_renderbuffer_image import *
from OpenGL.raw.EGL.KHR.gl_renderbuffer_image import _EXTENSION_NAME

def glInitGlRenderbufferImageKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION