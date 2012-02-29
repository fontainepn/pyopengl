'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_texture_multisample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_texture_multisample',False)
_p.unpack_constants( """GL_TEXTURE_COVERAGE_SAMPLES_NV 0x9045
GL_TEXTURE_COLOR_SAMPLES_NV 0x9046""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexImage2DMultisampleCoverageNV( target,coverageSamples,colorSamples,internalFormat,width,height,fixedSampleLocations ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexImage3DMultisampleCoverageNV( target,coverageSamples,colorSamples,internalFormat,width,height,depth,fixedSampleLocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureImage2DMultisampleNV( texture,target,samples,internalFormat,width,height,fixedSampleLocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureImage3DMultisampleNV( texture,target,samples,internalFormat,width,height,depth,fixedSampleLocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureImage2DMultisampleCoverageNV( texture,target,coverageSamples,colorSamples,internalFormat,width,height,fixedSampleLocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureImage3DMultisampleCoverageNV( texture,target,coverageSamples,colorSamples,internalFormat,width,height,depth,fixedSampleLocations ):pass


def glInitTextureMultisampleNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )