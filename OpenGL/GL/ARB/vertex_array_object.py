'''OpenGL extension ARB.vertex_array_object

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_array_object to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_array_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.vertex_array_object import *
from OpenGL.raw.GL.ARB.vertex_array_object import _EXTENSION_NAME

def glInitVertexArrayObjectARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION

glGenVertexArrays = wrapper.wrapper(glGenVertexArrays).setOutput('arrays', lambda n: (n,), 'n', arrayType = arrays.GLuintArray )
