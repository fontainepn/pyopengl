'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_point_parameters'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_point_parameters')
GL_DISTANCE_ATTENUATION_EXT=_C('GL_DISTANCE_ATTENUATION_EXT',0x8129)
GL_POINT_FADE_THRESHOLD_SIZE_EXT=_C('GL_POINT_FADE_THRESHOLD_SIZE_EXT',0x8128)
GL_POINT_SIZE_MAX_EXT=_C('GL_POINT_SIZE_MAX_EXT',0x8127)
GL_POINT_SIZE_MIN_EXT=_C('GL_POINT_SIZE_MIN_EXT',0x8126)
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPointParameterfEXT(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPointParameterfvEXT(pname,params):pass
# Calculate length of params from pname:PointParameterNameARB
