'''OpenGL extension EXT.read_format_bgra

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.read_format_bgra to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/read_format_bgra.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.read_format_bgra import *
from OpenGL.raw.GL.EXT.read_format_bgra import _EXTENSION_NAME

def glInitReadFormatBgraEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION