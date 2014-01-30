'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_vertex_blend'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_blend')
GL_ACTIVE_VERTEX_UNITS_ARB=_C('GL_ACTIVE_VERTEX_UNITS_ARB',0x86A5)
GL_CURRENT_WEIGHT_ARB=_C('GL_CURRENT_WEIGHT_ARB',0x86A8)
GL_MAX_VERTEX_UNITS_ARB=_C('GL_MAX_VERTEX_UNITS_ARB',0x86A4)
GL_MODELVIEW0_ARB=_C('GL_MODELVIEW0_ARB',0x1700)
GL_MODELVIEW10_ARB=_C('GL_MODELVIEW10_ARB',0x872A)
GL_MODELVIEW11_ARB=_C('GL_MODELVIEW11_ARB',0x872B)
GL_MODELVIEW12_ARB=_C('GL_MODELVIEW12_ARB',0x872C)
GL_MODELVIEW13_ARB=_C('GL_MODELVIEW13_ARB',0x872D)
GL_MODELVIEW14_ARB=_C('GL_MODELVIEW14_ARB',0x872E)
GL_MODELVIEW15_ARB=_C('GL_MODELVIEW15_ARB',0x872F)
GL_MODELVIEW16_ARB=_C('GL_MODELVIEW16_ARB',0x8730)
GL_MODELVIEW17_ARB=_C('GL_MODELVIEW17_ARB',0x8731)
GL_MODELVIEW18_ARB=_C('GL_MODELVIEW18_ARB',0x8732)
GL_MODELVIEW19_ARB=_C('GL_MODELVIEW19_ARB',0x8733)
GL_MODELVIEW1_ARB=_C('GL_MODELVIEW1_ARB',0x850A)
GL_MODELVIEW20_ARB=_C('GL_MODELVIEW20_ARB',0x8734)
GL_MODELVIEW21_ARB=_C('GL_MODELVIEW21_ARB',0x8735)
GL_MODELVIEW22_ARB=_C('GL_MODELVIEW22_ARB',0x8736)
GL_MODELVIEW23_ARB=_C('GL_MODELVIEW23_ARB',0x8737)
GL_MODELVIEW24_ARB=_C('GL_MODELVIEW24_ARB',0x8738)
GL_MODELVIEW25_ARB=_C('GL_MODELVIEW25_ARB',0x8739)
GL_MODELVIEW26_ARB=_C('GL_MODELVIEW26_ARB',0x873A)
GL_MODELVIEW27_ARB=_C('GL_MODELVIEW27_ARB',0x873B)
GL_MODELVIEW28_ARB=_C('GL_MODELVIEW28_ARB',0x873C)
GL_MODELVIEW29_ARB=_C('GL_MODELVIEW29_ARB',0x873D)
GL_MODELVIEW2_ARB=_C('GL_MODELVIEW2_ARB',0x8722)
GL_MODELVIEW30_ARB=_C('GL_MODELVIEW30_ARB',0x873E)
GL_MODELVIEW31_ARB=_C('GL_MODELVIEW31_ARB',0x873F)
GL_MODELVIEW3_ARB=_C('GL_MODELVIEW3_ARB',0x8723)
GL_MODELVIEW4_ARB=_C('GL_MODELVIEW4_ARB',0x8724)
GL_MODELVIEW5_ARB=_C('GL_MODELVIEW5_ARB',0x8725)
GL_MODELVIEW6_ARB=_C('GL_MODELVIEW6_ARB',0x8726)
GL_MODELVIEW7_ARB=_C('GL_MODELVIEW7_ARB',0x8727)
GL_MODELVIEW8_ARB=_C('GL_MODELVIEW8_ARB',0x8728)
GL_MODELVIEW9_ARB=_C('GL_MODELVIEW9_ARB',0x8729)
GL_VERTEX_BLEND_ARB=_C('GL_VERTEX_BLEND_ARB',0x86A7)
GL_WEIGHT_ARRAY_ARB=_C('GL_WEIGHT_ARRAY_ARB',0x86AD)
GL_WEIGHT_ARRAY_POINTER_ARB=_C('GL_WEIGHT_ARRAY_POINTER_ARB',0x86AC)
GL_WEIGHT_ARRAY_SIZE_ARB=_C('GL_WEIGHT_ARRAY_SIZE_ARB',0x86AB)
GL_WEIGHT_ARRAY_STRIDE_ARB=_C('GL_WEIGHT_ARRAY_STRIDE_ARB',0x86AA)
GL_WEIGHT_ARRAY_TYPE_ARB=_C('GL_WEIGHT_ARRAY_TYPE_ARB',0x86A9)
GL_WEIGHT_SUM_UNITY_ARB=_C('GL_WEIGHT_SUM_UNITY_ARB',0x86A6)
@_f
@_p.types(None,_cs.GLint)
def glVertexBlendARB(count):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glWeightPointerARB(size,type,stride,pointer):pass
# Calculate length of pointer from type:WeightPointerTypeARB
@_f
@_p.types(None,_cs.GLint,arrays.GLbyteArray)
def glWeightbvARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLdoubleArray)
def glWeightdvARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLfloatArray)
def glWeightfvARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLintArray)
def glWeightivARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLshortArray)
def glWeightsvARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLubyteArray)
def glWeightubvARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLuintArray)
def glWeightuivARB(size,weights):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLushortArray)
def glWeightusvARB(size,weights):pass
