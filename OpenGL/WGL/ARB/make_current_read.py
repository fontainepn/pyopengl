'''OpenGL extension ARB.make_current_read

This module customises the behaviour of the 
OpenGL.raw.WGL.ARB.make_current_read to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/make_current_read.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.ARB.make_current_read import *
from OpenGL.raw.WGL.ARB.make_current_read import _EXTENSION_NAME

def glInitMakeCurrentReadARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION