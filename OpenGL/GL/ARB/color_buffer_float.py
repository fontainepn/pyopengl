'''OpenGL extension ARB.color_buffer_float

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.color_buffer_float to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/color_buffer_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.color_buffer_float import *
from OpenGL.raw.GL.ARB.color_buffer_float import _EXTENSION_NAME

def glInitColorBufferFloatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.GL import glget
glget.addGLGetConstant( GL_RGBA_FLOAT_MODE_ARB, (1,) )