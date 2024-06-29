# serialise

this is a simple library to serialise and deserialise python
objects. it can serialise any object given it has a serialiser
written for it. Many python builtins already have serialisers

to create a serialiser you use the Serialiser class

here is an example (the default list serialiser but more friendly)
```py
from serialiser import Serialiser, read_size, write_size, serialise, deserialise
from io import BytesIO
def list_serialiser(data: list)->bytes:
	# create a bytearray this is a more convient way of creating bytes
	rv = bytearray()
	# add the length of the list
	# write size writes an int
	rv.extend(write_size(len(data)))
	# for each element in the list add the serialised element
	for el in data: rv.extend(serialise(el))
	return bytes(rv)
def list_deserialiser(data: bytes)->list:
	# the serialiser in reverse
	# create a BytesIO which is a more convient way of reading bytes
	data = BytesIO(data)
	# first read the length
	length = read_size(data, "list length")
	# then deserialise length elements from the data and reutrn them in an array
	return [deserialise(data) for _ in range(length)]
# register the Serialiser by createing a new instance of the Serialiser class
Serialiser(
	list,
	list_serialiser,
	list_deserialiser
)
```