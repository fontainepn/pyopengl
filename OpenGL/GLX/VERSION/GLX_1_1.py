'''OpenGL extension VERSION.GLX_1_1

This module customises the behaviour of the 
OpenGL.raw.GLX.VERSION.GLX_1_1 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GLX_1_1.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.VERSION.GLX_1_1 import *
from OpenGL.raw.GLX.VERSION.GLX_1_1 import _EXTENSION_NAME

def glInitGlx11VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION