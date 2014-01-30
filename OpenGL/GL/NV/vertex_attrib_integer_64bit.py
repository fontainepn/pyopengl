'''OpenGL extension NV.vertex_attrib_integer_64bit

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_attrib_integer_64bit to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/vertex_attrib_integer_64bit.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.vertex_attrib_integer_64bit import *
from OpenGL.raw.GL.NV.vertex_attrib_integer_64bit import _EXTENSION_NAME

def glInitVertexAttribInteger64BitNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION