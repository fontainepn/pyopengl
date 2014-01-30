'''OpenGL extension SUN.global_alpha

This module customises the behaviour of the 
OpenGL.raw.GL.SUN.global_alpha to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SUN/global_alpha.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SUN.global_alpha import *
from OpenGL.raw.GL.SUN.global_alpha import _EXTENSION_NAME

def glInitGlobalAlphaSUN():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION