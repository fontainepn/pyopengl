import ctypes
import OpenGL
from OpenGL import constants, plugins
from OpenGL import logs
log = logs.getLog( 'OpenGL.arrays.arraydatatype' )

cdef extern from "Python.h":
	cdef object PyObject_Type( object )
	cdef object PyDict_GetItem( object, object )


cdef class HandlerRegistry:
	cdef dict registry
	cdef object match
	cdef object output_handler
	cdef object preferredOutput
	GENERIC_OUTPUT_PREFERENCES = ['numpy','numeric','ctypesarrays']
	cdef object all_output_handlers
	def __init__( self, plugin_match ):
		self.registry = {}
		self.match = plugin_match
		self.output_handler = None 
		self.preferredOutput = None
		self.all_output_handlers = []
	def __setitem__( self,key,value ):
		self.registry[key] = value
	def __call__( self, value ):
		return self.c_lookup( value )
	
	cdef object c_lookup( self, object value ):
		"""C-level lookup of handler for given value"""
		cdef object typ, handler,base
		try:
			typ = value.__class__
		except AttributeError, err:
			typ = PyObject_Type(value)
		handler = self.registry.get( typ )
		if not handler:
			if hasattr( typ, '__mro__' ):
				for base in typ.__mro__:
					handler = self.registry.get( base )
					if not handler:
						handler = self.match( base )
					if handler:
						handler = self.registry[ base ]
						self.registry[ typ ] = handler 
						return handler
			raise TypeError(
				"""No array-type handler for type %r (value: %s) registered"""%(
					typ, repr(value)[:50]
				)
			)
		return handler
	
	cdef object c_get_output_handler( self ):
		"""Fast-path lookup for output handler object"""
		if self.output_handler is None:
			if self.preferredOutput is not None:
				self.output_handler = self.registry.get( self.preferredOutput )
			if not self.output_handler:
				for preferred in self.GENERIC_OUTPUT_PREFERENCES:
					self.output_handler = self.registry.get( preferred )
					if self.output_handler:
						break
			if not self.output_handler:
				# look for anything that can do output...
				for handler in self.all_output_handlers:
					self.output_handler = handler 
					break
			if not self.output_handler:
				raise RuntimeError(
					"""Unable to find any output handler at all (not even ctypes/numpy ones!)"""
				)
		return self.output_handler
			
	def register( self, handler, types=None ):
		"""Register this class as handler for given set of types"""
		if not isinstance( types, (list,tuple)):
			types = [ types ]
		for type in types:
			self.registry[ type ] = handler
		if handler.isOutput:
			self.all_output_handlers.append( handler )
		
	def registerReturn( self, handler ):
		"""Register this handler as the default return-type handler"""
		self.preferredOutput = handler 
		self.output_handler = None
	

cdef HandlerRegistry GLOBAL_REGISTRY = HandlerRegistry(plugins.FormatHandler.match)

cdef class ArrayDatatype:
	"""Mix-in for array datatype classes
	
	The ArrayDatatype marker essentially is used to mark a particular argument
	as having an "array" type, which means that it is eligible for handling 
	via the arrays sub-package and its registered handlers.
	"""
	cdef HandlerRegistry handler 
	cdef public object typeConstant
	cdef public object baseType
	def __init__( self, typeConstant=None, baseType=None ):
		"""Initialize, grabbing our handler registry"""
		self.typeConstant = typeConstant
		self.baseType = baseType
		self.handler = GLOBAL_REGISTRY
		from OpenGL.arrays import formathandler
		formathandler.FormatHandler.TYPE_REGISTRY = self.handler
		formathandler.FormatHandler.loadAll( )
	
	def getRegistry( self ):
		"""Get our handler registry"""
		return self.handler 
	def getHandler( self, value ):
		"""Retrieve FormatHandler for given value 
		
		This method is replaced by the FormatHandler registry
		once the registry is initialized...
		"""
		return self.handler.c_lookup( value )
	
	def from_param( self, object value ):
		"""Given a value in a known data-pointer type, convert to a ctypes pointer"""
		return self.handler.c_lookup( value ).from_param( value, self.typeConstant )
	
	def dataPointer( self, value ):
		"""Given a value in a known data-pointer type, return long for pointer"""
		return self.handler.c_lookup( value ).dataPointer( value )
	def voidDataPointer( self, value ):
		"""Given value in a known data-pointer type, return void_p for pointer"""
		return ctypes.c_void_p( self.handler.c_lookup( value ).dataPointer( value ))
	def typedPointer( self, value ):
		"""Return a pointer-to-base-type pointer for given value"""
		return ctypes.cast( 
			self.dataPointer(value), 
			ctypes.POINTER( self.baseType )
		)
	def asArray( self, value, typeCode=None ):
		"""Given a value, convert to preferred array representation"""
		return self.handler.c_lookup( value ).asArray( 
			value, typeCode or self.typeConstant 
		)
	def arrayToGLType( self, value ):
		"""Given a data-value, guess the OpenGL type of the corresponding pointer
		
		Note: this is not currently used in PyOpenGL and may be removed 
		eventually.
		"""
		return self.handler.c_lookup( value ).arrayToGLType( value )
	def arraySize( self, value, typeCode = None ):
		"""Given a data-value, calculate dimensions for the array (number-of-units)"""
		return self.handler.c_lookup( value ).arraySize( 
			value, typeCode or self.typeConstant 
		)
	def unitSize( self, value, typeCode=None ):
		"""Determine unit size of an array (if possible)
		
		Uses our local type if defined, otherwise asks the handler to guess...
		"""
		return self.handler.c_lookup( value ).unitSize( 
			value, typeCode or self.typeConstant 
		)
	def returnHandler( self ):
		"""Get the default return-handler"""
		return self.handler.c_get_output_handler( )
	def zeros( self, dims, typeCode=None ):
		"""Allocate a return array of the given dimensions filled with zeros"""
		return self.c_zeros( dims, typeCode )
	cdef c_zeros( self, dims, typeCode ):
		"""C-level function to create empty array"""
		return self.handler.c_get_output_handler().zeros( 
			dims, typeCode or self.typeConstant 
		)
		
		
	def dimensions( self, value ):
		"""Given a data-value, get the dimensions (assumes full structure info)"""
		return self.handler.c_lookup( value ).dimensions( value )
	
	def arrayByteCount( self, value ):
		"""Given a data-value, try to determine number of bytes it's final form occupies
		
		For most data-types this is arraySize() * atomic-unit-size
		"""
		return self.handler.c_lookup( value ).arrayByteCount( value )

# Now some array helper functions...

class Output:
	"""CConverter generating static-size typed output arrays
	
	Produces an output array of given type (arrayType) and 
	size using self.lookup() to determine the size of the 
	array to be produced, where the lookup function is passed 
	as an initialisation argument.
	
	Provides also:
	
		oldStyleReturn( ... ) for use in the default case of
			PyOpenGL compatability mode, where result arrays of
			size (1,) are returned as scalar values.
	"""
	cdef str name 
	cdef tuple size
	cdef int doOldStyle
	cdef ArrayDatatype arrayType
	cdef int outIndex
	def __init__( self, str name, tuple size, ArrayDatatype arrayType ):
		self.name = name 
		self.size = size 
		self.arrayType = arrayType
	def finalise( self, wrapper ):
		self.outIndex = wrapper.cArgIndex( self.name )
		
	cdef c_getSize( self, tuple pyArgs ):
		"""Retrieve the array size for this argument"""
		return self.size
	
	def __call__( self, tuple pyArgs, int index, object baseOperation ):
		"""Return pyArgs[ self.index ]"""
		return self.arrayType.c_zeros( self.c_getSize(pyArgs) )
	
	def oldStyleReturn( self, object result, object baseOperation, tuple pyArgs, tuple cArgs ):
		"""Retrieve cArgs[ self.index ]"""
		object result = cArgs[ self.outIndex ]
		cdef tuple thisSize = self.c_getSize(pyArgs)
		if thisSize == (1,):
			try:
				return result[0]
			except TypeError, err:
				return result
		else:
			return result

class SizedOutput( Output ):
	def __init__( self, str name, tuple size, ArrayDatatype arrayType ):
		self.name = name 
		self.size = size 
		self.arrayType = arrayType
	
	'name','specifier','lookup','arrayType'