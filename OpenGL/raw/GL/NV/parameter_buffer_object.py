'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_parameter_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_parameter_buffer_object')
GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV=_C('GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV',0x8DA4)
GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV=_C('GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV',0x8DA3)
GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV=_C('GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV',0x8DA0)
GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV=_C('GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV',0x8DA1)
GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV=_C('GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV',0x8DA2)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLintArray)
def glProgramBufferParametersIivNV(target,bindingIndex,wordIndex,count,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glProgramBufferParametersIuivNV(target,bindingIndex,wordIndex,count,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramBufferParametersfvNV(target,bindingIndex,wordIndex,count,params):pass
