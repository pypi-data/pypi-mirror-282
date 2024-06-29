from typing import Any, Callable, Optional
from dataclasses import dataclass
from io import BytesIO, BufferedIOBase
import ctypes
import collections
import queue
import math

class DeserialiseError(Exception):
	"""
	this is the error class for deserialising any errors ocuring during the
	deserialisation process will raise this class
	"""

"""this is the current version of the serialiser"""
CURRENT_VERSION = 0


def create_serialiser(props: list[str])->Callable:
	"""
	note you probably dont want to use this directly instead invoke it automaticly
	through the `Serialiser.with_props` function or by passing in a list of props
	as a `serialiser` when creating a new Serialiser instance

	this is the inverse to `create_deserialiser`

	:param props: a list of props to serialise
	
	:returns: a callable that serialise the props that are in the object passed to the
	returned function. This is done by concatinating each serialised property
	"""
	return lambda obj: b"".join([serialise(getattr(obj, prop)) for prop in props])
def create_deserialiser(typ: type, props: list[str])->Callable[[bytes], Any]:
	"""
	note you probably dont want to use this directly instead invoke it automaticly
	through the `Serialiser.with_props` function or by passing in a list of props
	as a `deserialiser` when creating a new Serialiser instance

	note the type will be created in a way such that the `__init __` will not be called

	this is the inverse to `create_serialiser`

	note this will not work with a slots object

	:param typ: the type the deserialiser will create
	
	:param props: the properties that are put into the created type in the order that
	they are stored in the data (use the same order as create_serialiser)
	
	:returns: a callable that deserialises data in the form that the returned function
	of `create_serialiser` will serialise
	"""
	def inner(data: bytes):
		data = BytesIO(data)
		rv = typ.__new__(typ)
		rv.__dict__.update({prop: deserialise(data) for prop in props})
		return rv
	return inner

_serialisers:list["Serialiser"] = []
@dataclass
class Serialiser[T]:
	"""
	this is the serialiser class

	to create a new serialiser just create an instance of this class

	the init accepts the type and the serialiser and deserialiser functions they can
	either be in the form of Callables that accept a type instace and return bytes or
	vice versa if you are passing in the serialiser or deserialise respectivly

	you can also pass lists of property to serialise and/or deserialise instead of the
	Callables this will by automaticly converted to functions with one of `create_serialiser`
	or `create_deserialiser` (check these for details of the serialisation)
	
	you can also use the convienice methods `alias` and `with_props`.

	`alias` will make a new serialiser with the same serialiser and deserialiser as the
	impl type (with optional functions to convert between these formats) see `alias`
	for details
	
	`with_props` acts as if you have passed in a list of props for both serialier and
	deserialiser but with less overhead
	"""
	s_type: type[T]
	serialise: Callable[[T], bytes]
	deserialise: Callable[[bytes], T]
	def __post_init__(self):
		# if the user passed in props instead of callables check user the create
		# (de)serialiser functions to resolve to callables
		if isinstance(self.serialise, list):self.serialise = create_serialiser(self.serialise)
		if isinstance(self.deserialise, list):
			self.deserialise = create_deserialiser(self.s_type, self.deserialise)
		_serialisers.append(self)
	@staticmethod
	def alias(
		impl_type:type,
		alias_type:type,
		convert_from_alias:Optional[Callable]=None,
		convert_to_alias:Optional[Callable]=None
	):
		"""
		this method will create a new Serialiser with the same serialise and
		deserialise functions

		:param impl_type: the type that has already got a Serialiser associated

		:param alias_type: the type you want to create a new alised Serialiser for
		
		:param convert_from_alias: a conversion function from the new type to the
		already defined type. By default this function does nothing and assumes that
		the two types are duck type compatible
		
		:param convert_to_alias: a conversion function from the already defined type to
		the new type. By default this function just calls the constructor for the new
		type with the impl type as the only argument. Note: this function should return
		the alias_type not just a duck compatible type

		:raises TypeError: raised if there is no serialiser registered for the `impl_type`
		"""
		if convert_to_alias == None: convert_to_alias:Callable = alias_type
		if convert_from_alias == None: convert_from_alias:Callable = lambda x:x
		serialiser = next((s for s in _serialisers if s.s_type == impl_type), None)
		if serialiser == None: raise TypeError(f"no serialiser for {impl_type.__qualname__}. (have you got the arguments backwards?)")
		Serialiser(
			alias_type,
			lambda d:convert_from_alias(serialiser.serialise(d)),
			lambda d:convert_to_alias(serialiser.deserialise(d))
		)
	@staticmethod
	def with_props(impl_type: type, props: list[str]):
		"""
		this is a convinece function to create a serialiser and deserialiser from props
		it is functionaly equivilent to calling
		```
		Serialiser(impl_type, props, props)
		# is the same as
		Serialiser.with_props(impl_type, props)
		```
		but with less overhead

		:param impl_type: this is the type you want to create a `Serialiser` for

		:param props: this is the list of props that will be serialised
		"""
		Serialiser(
			impl_type,
			create_serialiser(props),
			create_deserialiser(impl_type, props)
		)



# default serialisers
Serialiser(bytes, lambda d:d, lambda d:d)
Serialiser(bytearray, lambda d:bytes(d), lambda d:bytearray(d))
Serialiser(str, lambda d:d.encode("utf-8"), lambda d:d.decode("utf-8"))
Serialiser.alias(str, collections.UserString)
Serialiser(type(None), lambda _:b"", lambda _:None)
Serialiser(int, lambda d:(
	b"" if d == 0
	else d.to_bytes(math.ceil((d.bit_length()+1)/8),"big",signed=True)
), lambda d:int.from_bytes(d, "big", signed=True))
Serialiser(
	bool,
	lambda d:(1 if d else 0).to_bytes(1, "big", signed=True),
	lambda d:int.from_bytes(d, "big", signed=True)>0
)

def _list_serialiser(data: list)->bytes:
	rv = bytearray()
	rv.extend(write_size(len(data)))
	for el in data: rv.extend(serialise(el))
	return bytes(rv)
def _list_deserialiser(data: bytes)->list:
	data = BytesIO(data)
	length = read_size(data, "list length")
	return [deserialise(data) for _ in range(length)]
Serialiser(
	list,
	_list_serialiser,
	_list_deserialiser
)
Serialiser.alias(list, tuple)
Serialiser.alias(list, set)
Serialiser.alias(list, frozenset)
Serialiser.alias(list, collections.deque)
Serialiser.alias(list, collections.UserList)
def _list_to_q(l):
	q = queue.Queue()
	[q.put(i) for i in l]
	return q
Serialiser.alias(list, queue.Queue, (lambda q:q.queue), _list_to_q)
Serialiser.alias(queue.Queue, queue.LifoQueue)
Serialiser.alias(queue.Queue, queue.PriorityQueue)
Serialiser.alias(queue.Queue, queue.SimpleQueue)

def _dict_serialiser(data: dict)->bytes:
	rv = bytearray()
	rv.extend(write_size(len(data)))
	for key, value in data.items():
		rv.extend(serialise(key))
		rv.extend(serialise(value))
	return bytes(rv)
def _dict_deserialiser(data: bytes)->dict:
	data = BytesIO(data)
	length = read_size(data, "dict length")
	return {deserialise(data):deserialise(data) for _ in range(length)}
# the dict should always work with an ordered dict
Serialiser(
	dict,
	_dict_serialiser,
	_dict_deserialiser
)
Serialiser.alias(dict, collections.OrderedDict)
Serialiser.alias(dict, collections.ChainMap)
Serialiser.alias(dict, collections.Counter)
Serialiser.alias(dict, collections.defaultdict)
Serialiser.alias(dict, collections.UserDict)

def _complex_deserialiser(data: bytes)->complex:
	data = BytesIO(data)
	return complex(deserialise(data), deserialise(data))
Serialiser(complex, ["real", "imag"], _complex_deserialiser)

class _native_float(ctypes.Union):_fields_=[
	("double",ctypes.c_double),
	("ui64",ctypes.c_uint64)
]
def _float_serialiser(d: float)->bytes:
	data = _native_float()
	data.double = d
	return data.ui64.to_bytes(8, "big")
def _float_deserialiser(b: bytes)->float:
	data = _native_float()
	data.ui64 = int.from_bytes(b, "big")
	return data.double
Serialiser(
	float,
	_float_serialiser,
	_float_deserialiser
)

def write_size(size: int)->bytes:
	"""
	essentialy encodes the an unbound positive int (`size`) into bytes however this is
	done using an encoding that encodes the width of itsself so it needs no extra
	length data to be stored alongside it (which is how the `int` class is stored)

	this is done using a custom encoding that starts with a number of `0xff`s for each
	one there is one extra byte used with a default of 1 byte

	i.e. if the number does not start with `0xff` it will only by one byte long if it
	starts with one `0xff` it will be two bytes long (exculding the initial `0xff`s)

	if you want to store a number that starts with `0xff` then you can increase the
	byte count and precede it with `0x00`

	this does show a potential downside to the algorithm which is that there are
	multiple ways to store any number however this function will always write the
	smallest length version

	this also only works if the numbers are encoded using big endian which they always
	are in the default serialisers (including this function)`

	:param size: the number to encode

	:returns: the encoded number
	"""
	if size == 0:return bytes(1) # emtpy array length 1
	size = size.to_bytes(math.ceil(size.bit_length()/8),"big")
	if size[0] == 0xff:size = bytes(1)+size
	return ((len(size)-1)*b"\xff")+size
def read_size(data: BufferedIOBase, err_type: str)->int:
	"""
	this is the inverse function to `write_size` and takes data as BufferedIOBase
	(meaning it accepts data from `open(file, "rb")` or other variants and `BytesIO`
	or anything else that impliments a read function that advances a cursor and accepts
	the count)
	
	despite `write_size` only writing the smallest version of the integers this can
	read any version of the encoding however like its inverse only uses big endian

	:param data: the binary IO stream to read the size from (it reads from the cursor).

	:param err_type: a string to use if an error occurs. This should be what you are
	trying to read

	:returns: the decoded size as an int

	:raises DeserialiseError: raised if the function reaches a EOF when reading the size
	"""
	length = 0
	while True:
		prec = data.read(1)
		if len(prec) == 0:raise DeserialiseError(f"Reached EOF trying to read {err_type}")
		if ord(prec) == 0xFF:length+=1
		else:
			val = data.read(length)
			if len(val) < length:raise DeserialiseError(f"Reached EOF trying to read {err_type}")
			return int.from_bytes(prec+val, "big")
def write_sized_bytes(data: bytes, arr: bytearray):
	"""
	this function writes bytes with a header that is a size (as used by `read_size` and
	`write_size`) this means that it can be easily read without reading too many or few
	bytes by its corresponding function `read_sized_bytes`

	the arguments are in the order source, dest.

	:param data: the data to write

	:param arr: bytearray to write bytes to.
	"""
	arr.extend(write_size(len(data)))
	arr.extend(data)
def read_sized_bytes(data: BufferedIOBase, err_type: str)->bytes:
	"""
	this function reads sized bytes in the format created by `write_sized_bytes`

	:param data: the Binary IO stream to read the data from

	:param err_type: a string to use if an error occurs. This should be what you are
	trying to read

	:returns: the bytes that have been read from the file (excluding the size)

	:raises DeserialiseError: raised if the function reaches a EOF when reading the data
	"""
	bytes_len = read_size(data, f"the length of the {err_type}")
	bytes_data = data.read(bytes_len)
	if len(bytes_data) < bytes_len:raise DeserialiseError(f"Reached EOF trying to read the {err_type}")
	return bytes_data

def serialise(data: Any)->bytes:
	"""
	this function is probably the most usefull in the package. it takes a python object
	and serialises it into bytes in a format that can be read by `deserialise`

	you usualy dont want this function but instead `serialise_with_header`

	this is not the function to be called when you want to serialise an object for
	saving as it has incomplete information about how to deserialise this function is
	however the one that you should be using to serialise if you are writing a
	serialiser and want to serialise part of your object

	this is the inverse to `deserialise`

	:param data: this is the object that will be serialised. it must have a serialiser
	defined. (note that most of the builtin types have a serialiser builtin)

	:returns: the serialised data

	:raises TypeError: this is raised if the `data` has no Serialiser
	"""
	serialiser = next((s for s in _serialisers if s.s_type == type(data)), None)
	type_name = type(data).__qualname__
	if serialiser == None: raise TypeError(f"no serialiser defined for type {type_name}")
	rv = bytearray()

	# encode the type it only uses the name therefore you cannot serialise two different types with the same name
	write_sized_bytes(type_name.encode("utf-8"), rv)
	write_sized_bytes(serialiser.serialise(data), rv)
	return bytes(rv)

def serialise_with_header(data: Any)->bytes:
	"""
	this is the main function you want to use for serialising objects to store them

	:param data: this is the object that will be serialised. it must have a serialiser
	defined. (note that most of the builtin types have a serialiser builtin)

	:returns: the serialised data

	:raises TypeError: this is raised if the `data` has no Serialiser
	"""
	return b"RJS" + CURRENT_VERSION.to_bytes(2, "big") + serialise(data)

def deserialise_bytes(data: bytes)->Any:
	"""
	this is a wrapper around `deserialise` and is there so you dont assume there is a
	cursor attached to the data

	you usualy dont want this function but instead `deserialise_with_header`

	:param data: this is the bytes that are to be deserialised

	:returns: the data deserialised

	:raises DeserialiseError: raised if the function reaches a EOF when reading the data
	"""
	return deserialise(BytesIO(data))
def deserialise(data: BufferedIOBase)->Any:
	"""
	this function takes data as a Binary IO Stream and returns the object that is in
	serialised form in the stream. it only reads as much as is needed and will ignore
	any data that is after the serialised data leaving the cursor at the beginging of
	whatever is after in the IO stream

	:param data: this is the Binary IO Stream that are to be deserialised

	:returns: the data deserialised

	:raises DeserialiseError: raised if the function reaches a EOF when reading the data
	"""
	# make sure dingus' like me use the correct function and show them the alternative
	if isinstance(data, bytes): raise TypeError("deserialise only takes a file like object (it uses read to advance a cursor) if you have bytes try `deserialise_bytes`")

	try:type_name = read_sized_bytes(data, "type name").decode("utf-8")
	except UnicodeError:raise DeserialiseError("Failed to decode the type name as it was invalid utf-8 (are you sure this is the correct file)")

	data = read_sized_bytes(data, "data")
	serialiser = next((s for s in _serialisers if s.s_type.__qualname__ == type_name), None)
	if serialiser == None: raise DeserialiseError(f"Could not find a deserialiser for the type `{type_name}` make sure it has been loaded.")
	return serialiser.deserialise(data)


def deserialise_with_header(data: BufferedIOBase|bytes)->Any:
	"""
	this is the function that you can use to deserialise saved seralised data

	it takes data created by `serialise_with_header` and return 

	:param data: this is the Binary IO Stream (i.e. anything with a read
	function that could be the return to a call to open BytesIO ect) or bytes
	that are to be deserialised

	:returns: the data deserialised

	:raises DeserialiseError: raised if the function reaches a EOF when reading the data
	"""
	if isinstance(data, bytes):data = BytesIO(data)
	if data.read(3) != b"RJS":raise DeserialiseError("file had invalid magic number probably not the correct file (or it is corrupt)")
	version = data.read(2)
	if len(version) < 2:raise DeserialiseError("Reached EOF trying to read the version")
	version = int.from_bytes(version, "big")
	if version != CURRENT_VERSION: raise DeserialiseError("file had old version. try using an old version of this software")
	return deserialise(data)
