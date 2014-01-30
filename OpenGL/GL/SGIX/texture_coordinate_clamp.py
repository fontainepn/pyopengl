'''OpenGL extension SGIX.texture_coordinate_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.texture_coordinate_clamp to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/texture_coordinate_clamp.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SGIX.texture_coordinate_clamp import *
from OpenGL.raw.GL.SGIX.texture_coordinate_clamp import _EXTENSION_NAME

def glInitTextureCoordinateClampSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION