'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_vertex_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_buffer_object')
GL_ARRAY_BUFFER_ARB=_C('GL_ARRAY_BUFFER_ARB',0x8892)
GL_ARRAY_BUFFER_BINDING_ARB=_C('GL_ARRAY_BUFFER_BINDING_ARB',0x8894)
GL_BUFFER_ACCESS_ARB=_C('GL_BUFFER_ACCESS_ARB',0x88BB)
GL_BUFFER_MAPPED_ARB=_C('GL_BUFFER_MAPPED_ARB',0x88BC)
GL_BUFFER_MAP_POINTER_ARB=_C('GL_BUFFER_MAP_POINTER_ARB',0x88BD)
GL_BUFFER_SIZE_ARB=_C('GL_BUFFER_SIZE_ARB',0x8764)
GL_BUFFER_USAGE_ARB=_C('GL_BUFFER_USAGE_ARB',0x8765)
GL_COLOR_ARRAY_BUFFER_BINDING_ARB=_C('GL_COLOR_ARRAY_BUFFER_BINDING_ARB',0x8898)
GL_DYNAMIC_COPY_ARB=_C('GL_DYNAMIC_COPY_ARB',0x88EA)
GL_DYNAMIC_DRAW_ARB=_C('GL_DYNAMIC_DRAW_ARB',0x88E8)
GL_DYNAMIC_READ_ARB=_C('GL_DYNAMIC_READ_ARB',0x88E9)
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB=_C('GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB',0x889B)
GL_ELEMENT_ARRAY_BUFFER_ARB=_C('GL_ELEMENT_ARRAY_BUFFER_ARB',0x8893)
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB=_C('GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB',0x8895)
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB=_C('GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB',0x889D)
GL_INDEX_ARRAY_BUFFER_BINDING_ARB=_C('GL_INDEX_ARRAY_BUFFER_BINDING_ARB',0x8899)
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB=_C('GL_NORMAL_ARRAY_BUFFER_BINDING_ARB',0x8897)
GL_READ_ONLY_ARB=_C('GL_READ_ONLY_ARB',0x88B8)
GL_READ_WRITE_ARB=_C('GL_READ_WRITE_ARB',0x88BA)
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB=_C('GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB',0x889C)
GL_STATIC_COPY_ARB=_C('GL_STATIC_COPY_ARB',0x88E6)
GL_STATIC_DRAW_ARB=_C('GL_STATIC_DRAW_ARB',0x88E4)
GL_STATIC_READ_ARB=_C('GL_STATIC_READ_ARB',0x88E5)
GL_STREAM_COPY_ARB=_C('GL_STREAM_COPY_ARB',0x88E2)
GL_STREAM_DRAW_ARB=_C('GL_STREAM_DRAW_ARB',0x88E0)
GL_STREAM_READ_ARB=_C('GL_STREAM_READ_ARB',0x88E1)
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB=_C('GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB',0x889A)
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB=_C('GL_VERTEX_ARRAY_BUFFER_BINDING_ARB',0x8896)
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB=_C('GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB',0x889F)
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB=_C('GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB',0x889E)
GL_WRITE_ONLY_ARB=_C('GL_WRITE_ONLY_ARB',0x88B9)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindBufferARB(target,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizeiptrARB,ctypes.c_void_p,_cs.GLenum)
def glBufferDataARB(target,size,data,usage):pass
# Calculate length of data from size:BufferSizeARB
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptrARB,_cs.GLsizeiptrARB,ctypes.c_void_p)
def glBufferSubDataARB(target,offset,size,data):pass
# Calculate length of data from size:BufferSizeARB
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteBuffersARB(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenBuffersARB(n,buffers):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetBufferParameterivARB(target,pname,params):pass
# Calculate length of params from pname:BufferPNameARB
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLvoidpArray)
def glGetBufferPointervARB(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptrARB,_cs.GLsizeiptrARB,ctypes.c_void_p)
def glGetBufferSubDataARB(target,offset,size,data):pass
# Calculate length of data from size:BufferSizeARB
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsBufferARB(buffer):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLenum,_cs.GLenum)
def glMapBufferARB(target,access):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glUnmapBufferARB(target):pass
