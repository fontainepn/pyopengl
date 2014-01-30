'''OpenGL extension MESA.release_buffers

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.release_buffers to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/release_buffers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.MESA.release_buffers import *
from OpenGL.raw.GLX.MESA.release_buffers import _EXTENSION_NAME

def glInitReleaseBuffersMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION