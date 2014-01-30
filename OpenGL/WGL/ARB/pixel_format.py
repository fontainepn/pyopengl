'''OpenGL extension ARB.pixel_format

This module customises the behaviour of the 
OpenGL.raw.WGL.ARB.pixel_format to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/pixel_format.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.ARB.pixel_format import *
from OpenGL.raw.WGL.ARB.pixel_format import _EXTENSION_NAME

def glInitPixelFormatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION