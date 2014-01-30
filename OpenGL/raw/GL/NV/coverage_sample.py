'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_coverage_sample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_coverage_sample')
GL_COVERAGE_ALL_FRAGMENTS_NV=_C('GL_COVERAGE_ALL_FRAGMENTS_NV',0x8ED5)
GL_COVERAGE_ATTACHMENT_NV=_C('GL_COVERAGE_ATTACHMENT_NV',0x8ED2)
GL_COVERAGE_AUTOMATIC_NV=_C('GL_COVERAGE_AUTOMATIC_NV',0x8ED7)
GL_COVERAGE_BUFFERS_NV=_C('GL_COVERAGE_BUFFERS_NV',0x8ED3)
GL_COVERAGE_BUFFER_BIT_NV=_C('GL_COVERAGE_BUFFER_BIT_NV',0x00008000)
GL_COVERAGE_COMPONENT4_NV=_C('GL_COVERAGE_COMPONENT4_NV',0x8ED1)
GL_COVERAGE_COMPONENT_NV=_C('GL_COVERAGE_COMPONENT_NV',0x8ED0)
GL_COVERAGE_EDGE_FRAGMENTS_NV=_C('GL_COVERAGE_EDGE_FRAGMENTS_NV',0x8ED6)
GL_COVERAGE_SAMPLES_NV=_C('GL_COVERAGE_SAMPLES_NV',0x8ED4)
@_f
@_p.types(None,_cs.GLboolean)
def glCoverageMaskNV(mask):pass
@_f
@_p.types(None,_cs.GLenum)
def glCoverageOperationNV(operation):pass
