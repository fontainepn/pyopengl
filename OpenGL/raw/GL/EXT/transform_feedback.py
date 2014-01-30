'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_transform_feedback'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_transform_feedback')
GL_INTERLEAVED_ATTRIBS_EXT=_C('GL_INTERLEAVED_ATTRIBS_EXT',0x8C8C)
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT=_C('GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT',0x8C8A)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT',0x8C8B)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT',0x8C80)
GL_PRIMITIVES_GENERATED_EXT=_C('GL_PRIMITIVES_GENERATED_EXT',0x8C87)
GL_RASTERIZER_DISCARD_EXT=_C('GL_RASTERIZER_DISCARD_EXT',0x8C89)
GL_SEPARATE_ATTRIBS_EXT=_C('GL_SEPARATE_ATTRIBS_EXT',0x8C8D)
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT=_C('GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT',0x8C8F)
GL_TRANSFORM_FEEDBACK_BUFFER_EXT=_C('GL_TRANSFORM_FEEDBACK_BUFFER_EXT',0x8C8E)
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT=_C('GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT',0x8C7F)
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT=_C('GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT',0x8C85)
GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT=_C('GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT',0x8C84)
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT=_C('GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT',0x8C88)
GL_TRANSFORM_FEEDBACK_VARYINGS_EXT=_C('GL_TRANSFORM_FEEDBACK_VARYINGS_EXT',0x8C83)
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT=_C('GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT',0x8C76)
@_f
@_p.types(None,_cs.GLenum)
def glBeginTransformFeedbackEXT(primitiveMode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBaseEXT(target,index,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr)
def glBindBufferOffsetEXT(target,index,buffer,offset):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRangeEXT(target,index,buffer,offset,size):pass
@_f
@_p.types(None,)
def glEndTransformFeedbackEXT():pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetTransformFeedbackVaryingEXT(program,index,bufSize,length,size,type,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),_cs.GLenum)
def glTransformFeedbackVaryingsEXT(program,count,varyings,bufferMode):pass
