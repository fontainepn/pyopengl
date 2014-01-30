'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_sharpen_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_sharpen_texture')
GL_LINEAR_SHARPEN_ALPHA_SGIS=_C('GL_LINEAR_SHARPEN_ALPHA_SGIS',0x80AE)
GL_LINEAR_SHARPEN_COLOR_SGIS=_C('GL_LINEAR_SHARPEN_COLOR_SGIS',0x80AF)
GL_LINEAR_SHARPEN_SGIS=_C('GL_LINEAR_SHARPEN_SGIS',0x80AD)
GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS=_C('GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS',0x80B0)
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetSharpenTexFuncSGIS(target,points):pass
# Calculate length of points from target:TextureTarget
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glSharpenTexFuncSGIS(target,n,points):pass
