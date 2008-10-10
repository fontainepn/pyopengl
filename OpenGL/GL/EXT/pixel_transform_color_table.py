'''OpenGL extension EXT.pixel_transform_color_table

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.pixel_transform_color_table to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.pixel_transform_color_table import *
### END AUTOGENERATED SECTION