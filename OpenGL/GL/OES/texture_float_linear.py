'''OpenGL extension OES.texture_float_linear

This module customises the behaviour of the 
OpenGL.raw.GL.OES.texture_float_linear to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/texture_float_linear.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.OES.texture_float_linear import *
from OpenGL.raw.GL.OES.texture_float_linear import _EXTENSION_NAME

def glInitTextureFloatLinearOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION