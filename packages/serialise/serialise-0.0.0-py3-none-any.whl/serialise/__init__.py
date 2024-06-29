
from ._lib import DeserialiseError, CURRENT_VERSION, Serialiser, write_size, read_size
from ._lib import write_sized_bytes, read_sized_bytes, serialise, serialise_with_header
from ._lib import deserialise, deserialise_with_header, deserialise_bytes

__all__ = [
	"DeserialiseError",
	"CURRENT_VERSION",
	"Serialiser",
	"write_size",
	"read_size",
	"write_sized_bytes",
	"read_sized_bytes",
	"serialise",
	"serialise_with_header",
	"deserialise",
	"deserialise_with_header",
	"deserialise_bytes"
]

def main():
	import sys
	if len(sys.argv) == 2:
		try:
			with open(sys.argv[1], "rb") as f:print(deserialise_with_header(f))
		except OSError as e: print(f"File Error: {e}", file=sys.stderr)
		except DeserialiseError as e:print(f"Deserialise Error: {e}", file=sys.stderr)
	else:print("When run as an executable pass one arguemnt of the file to decode", file=sys.stderr)

if __name__ == "__main__":main()
