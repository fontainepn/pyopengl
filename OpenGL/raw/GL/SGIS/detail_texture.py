'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_detail_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_detail_texture')
GL_DETAIL_TEXTURE_2D_BINDING_SGIS=_C('GL_DETAIL_TEXTURE_2D_BINDING_SGIS',0x8096)
GL_DETAIL_TEXTURE_2D_SGIS=_C('GL_DETAIL_TEXTURE_2D_SGIS',0x8095)
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS=_C('GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS',0x809C)
GL_DETAIL_TEXTURE_LEVEL_SGIS=_C('GL_DETAIL_TEXTURE_LEVEL_SGIS',0x809A)
GL_DETAIL_TEXTURE_MODE_SGIS=_C('GL_DETAIL_TEXTURE_MODE_SGIS',0x809B)
GL_LINEAR_DETAIL_ALPHA_SGIS=_C('GL_LINEAR_DETAIL_ALPHA_SGIS',0x8098)
GL_LINEAR_DETAIL_COLOR_SGIS=_C('GL_LINEAR_DETAIL_COLOR_SGIS',0x8099)
GL_LINEAR_DETAIL_SGIS=_C('GL_LINEAR_DETAIL_SGIS',0x8097)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glDetailTexFuncSGIS(target,n,points):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetDetailTexFuncSGIS(target,points):pass
# Calculate length of points from target:TextureTarget
