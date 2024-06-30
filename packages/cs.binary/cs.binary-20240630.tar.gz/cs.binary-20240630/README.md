Facilities associated with binary data parsing and transcription.
The classes in this module support easy parsing of binary data
structures,
returning instances with the binary data decoded into attributes
and capable of transcribing themselves in binary form
(trivially via `bytes(instance)` and also otherwise).

*Latest release 20240630*:
* flatten: do not yield empty str-as-ascii-bytes - we want to ensure that flatten never yields an empty bytes instance.
* New AbstractBinary.write(f) method to write the binary form of this object to a file.
* New BinarySingleValue.value_from_bytes(bytes) class method to return the value from a bytes instance.
* Drop BinaryMixin, now folded directly into AbstractBinary.
* AbstractBinary.scan: pass extra keyword arguments to AbstractBinary.parse, supporting plumbing eg a logging parameter through.

Note: this module requires Python 3.6+ because various default
behaviours rely on `dict`s preserving their insert order.

See `cs.iso14496` for an ISO 14496 (eg MPEG4) parser
built using this module.

Terminology used below:
* buffer:
  an instance of `cs.buffer.CornuCopyBuffer`,
  which manages an iterable of bytes-like values
  and has various useful methods;
  it also has a few factory methods to make one from a variety of sources
  such as bytes, iterables, binary files, `mmap`ped files,
  TCP data streams, etc.
* chunk:
  a piece of binary data obeying the buffer protocol,
  almost always a `bytes` instance or a `memoryview`,
  but in principle also things like `bytearray`.

There are 5 main classes on which an implementor should base their data structures:
* `BinarySingleStruct`: a factory for classes based
  on a `struct.struct` format string with a single value;
  this builds a `namedtuple` subclass
* `BinaryMultiStruct`: a factory for classes based
  on a `struct.struct` format string with multiple values;
  this also builds a `namedtuple` subclass
* `BinarySingleValue`: a base class for subclasses
  parsing and transcribing a single value
* `BinaryMultiValue`: a base class for subclasses
  parsing and transcribing multiple values
  with no variation
* `SimpleBinary`: a base class for subclasses
  with custom `.parse` and `.transcribe` methods,
  for structures with variable fields

Any the classes derived from the above inherit all the methods
of `AbstractBinary`.
Amongst other things, this means that the binary transcription
can be had simply from `bytes(instance)`,
although there are more transcription methods provided
for when greater flexibility is desired.
It also means that all classes have `parse`* and `scan`* methods
for parsing binary data streams.

You can also instantiate objects directly;
there's no requirement for the source information to be binary.

There are several presupplied subclasses for common basic types
such as `UInt32BE` (an unsigned 32 bit big endian integer).

## Class `AbstractBinary`

Abstract class for all `Binary`* implementations,
specifying the abstract `parse` and `transcribe` methods
and providing various helper methods.

Naming conventions:
- `parse`* methods parse a single instance from a buffer
- `scan`* methods are generators yielding successive instances from a buffer

*Method `AbstractBinary.__bytes__(self)`*:
The binary transcription as a single `bytes` object.

*Method `AbstractBinary.__len__(self)`*:
Compute the length by running a transcription and measuring it.

*Method `AbstractBinary.from_bytes(bs, **parse_bytes_kw)`*:
Factory to parse an instance from the
bytes `bs` starting at `offset`.
Returns the new instance.

Raises `ValueError` if `bs` is not entirely consumed.
Raises `EOFError` if `bs` has insufficient data.

Keyword parameters are passed to the `.parse_bytes` method.

This relies on the `cls.parse` method for the parse.

*Method `AbstractBinary.load(f)`*:
Load an instance from the file `f`
which may be a filename or an open file as for `AbstractBinary.scan`.
Return the instance or `None` if the file is empty.

*Method `AbstractBinary.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse an instance of `cls` from the buffer `bfr`.

*Method `AbstractBinary.parse_bytes(bs, offset=0, length=None, **parse_kw)`*:
Factory to parse an instance from the
bytes `bs` starting at `offset`.
Returns `(instance,offset)` being the new instance and the post offset.

Raises `EOFError` if `bs` has insufficient data.

The parameters `offset` and `length` are passed to the
`CornuCopyBuffer.from_bytes` factory.

Other keyword parameters are passed to the `.parse` method.

This relies on the `cls.parse` method for the parse.

*Method `AbstractBinary.save(self, f)`*:
Save this instance to the file `f`
which may be a filename or an open file.
Return the length of the transcription.

*Method `AbstractBinary.scan(bfr: cs.buffer.CornuCopyBuffer, count=None, *, min_count=None, max_count=None, with_offsets=False, **parse_kw)`*:
Function to scan the buffer `bfr` for repeated instances of `cls`
until end of input and yield them.

Parameters:
* `bfr`: the buffer to scan, or any object suitable for `CornuCopyBuffer.promote`
* `count`: the required number of instances to scan,
  equivalent to setting `min_count=count` and `max_count=count`
* `min_count`: the minimum number of instances to scan
* `max_count`: the maximum number of instances to scan
* `with_offsets`: optional flag, default `False`;
  if true yield `(pre_offset,obj,post_offset)`, otherwise just `obj`
It is in error to specify both `count` and one of `min_count` or `max_count`.

Other keyword arguments are passed to `self.parse()`.

Scanning stops after `max_count` instances (if specified).
If fewer than `min_count` instances (if specified) are scanned
a warning is issued.
This is to accomodate nonconformant streams
without raising exceptions.
Callers wanting to validate `max_count` may want to probe `bfr.at_eof()`
after return.
Callers not wanting a warning over `min_count` should not specify it,
and instead check the number of instances returned themselves.

*Method `AbstractBinary.scan_fspath(fspath: str, *, with_offsets=False, **kw)`*:
Open the file with filesystenm path `fspath` for read
and yield from `self.scan(..,**kw)` or
`self.scan_with_offsets(..,**kw)` according to the
`with_offsets` parameter.

*Deprecated; please just call `scan` with a filesystem pathname.

Parameters:
* `fspath`: the filesystem path of the file to scan
* `with_offsets`: optional flag, default `False`;
  if true then scan with `scan_with_offsets` instead of
  with `scan`
Other keyword parameters are passed to `scan` or
`scan_with_offsets`.

*Method `AbstractBinary.scan_with_offsets(bfr: cs.buffer.CornuCopyBuffer, count=None, min_count=None, max_count=None)`*:
Wrapper for `scan()` which yields `(pre_offset,instance,post_offset)`
indicating the start and end offsets of the yielded instances.
All parameters are as for `scan()`.

*Deprecated; please just call `scan` with the `with_offsets=True` parameter.

*Method `AbstractBinary.self_check(self)`*:
Internal self check. Returns `True` if passed.

If the structure has a `FIELD_TYPES` attribute, normally a
class attribute, then check the fields against it. The
`FIELD_TYPES` attribute is a mapping of `field_name` to
a specification of `required` and `types`. The specification
may take one of 2 forms:
* a tuple of `(required,types)`
* a single `type`; this is equivalent to `(True,(type,))`
Their meanings are as follows:
* `required`: a Boolean. If true, the field must be present
  in the packet `field_map`, otherwise it need not be present.
* `types`: a tuple of acceptable field types

There are some special semantics involved here.

An implementation of a structure may choose to make some
fields plain instance attributes instead of binary objects
in the `field_map` mapping, particularly variable structures
such as a `cs.iso14496.BoxHeader`, whose `.length` may be parsed
directly from its binary form or computed from other fields
depending on the `box_size` value. Therefore, checking for
a field is first done via the `field_map` mapping, then by
`getattr`, and as such the acceptable `types` may include
nonstructure types such as `int`.

Here is the `cs.iso14496` `Box.FIELD_TYPES` definition as an example:

    FIELD_TYPES = {
        'header': BoxHeader,
        'body': BoxBody,
        'unparsed': list,
        'offset': int,
        'unparsed_offset': int,
        'end_offset': int,
    }

Note that `length` includes some nonstructure types,
and that it is written as a tuple of `(True,types)` because
it has more than one acceptable type.

*Method `AbstractBinary.transcribe(self)`*:
Return or yield `bytes`, ASCII string, `None` or iterables
comprising the binary form of this instance.

This aims for maximum convenience when transcribing a data structure.

This may be implemented as a generator, yielding parts of the structure.

This may be implemented as a normal function, returning:
* `None`: no bytes of data,
  for example for an omitted or empty structure
* a `bytes`-like object: the full data bytes for the structure
* an ASCII compatible string:
  this will be encoded with the `'ascii'` encoding to make `bytes`
* an iterable:
  the components of the structure,
  including substranscriptions which themselves
  adhere to this protocol - they may be `None`, `bytes`-like objects,
  ASCII compatible strings or iterables.
  This supports directly returning or yielding the result of a field's
  `.transcribe` method.

*Method `AbstractBinary.transcribe_flat(self)`*:
Return a flat iterable of chunks transcribing this field.

*Method `AbstractBinary.transcribed_length(self)`*:
Compute the length by running a transcription and measuring it.

*Method `AbstractBinary.write(self, file, *, flush=False)`*:
Write this instance to `file`, a file-like object supporting
`.write(bytes)` and `.flush()`.
Return the number of bytes written.

## Class `BinaryByteses(AbstractBinary)`

A list of `bytes` parsed directly from the native iteration of the buffer.

## Function `BinaryFixedBytes(class_name: str, length: int)`

Factory for an `AbstractBinary` subclass matching `length` bytes of data.
The bytes are saved as the attribute `.data`.

## Class `BinaryListValues(AbstractBinary)`

A list of values with a common parse specification,
such as sample or Boxes in an ISO14496 Box structure.

*Method `BinaryListValues.parse(bfr: cs.buffer.CornuCopyBuffer, count=None, *, end_offset=None, min_count=None, max_count=None, pt)`*:
Read values from `bfr`.
Return a `BinaryListValue` containing the values.

Parameters:
* `count`: optional count of values to read;
  if specified, exactly this many values are expected.
* `end_offset`: an optional bounding end offset of the buffer.
* `min_count`: the least acceptable number of values.
* `max_count`: the most acceptable number of values.
* `pt`: a parse/transcribe specification
  as accepted by the `pt_spec()` factory.
  The values will be returned by its parse function.

*Method `BinaryListValues.transcribe(self)`*:
Transcribe all the values.

## Function `BinaryMultiStruct(class_name: str, struct_format: str, field_names: Union[str, List[str]])`

A class factory for `AbstractBinary` `namedtuple` subclasses
built around complex `struct` formats.

Parameters:
* `class_name`: name for the generated class
* `struct_format`: the `struct` format string
* `field_names`: field name list,
  a space separated string or an interable of strings

Example:

    # an "access point" record from the .ap file
    Enigma2APInfo = BinaryMultiStruct('Enigma2APInfo', '>QQ', 'pts offset')

    # a "cut" record from the .cuts file
    Enigma2Cut = BinaryMultiStruct('Enigma2Cut', '>QL', 'pts type')

## Function `BinaryMultiValue(class_name, field_map, field_order=None)`

Construct a `SimpleBinary` subclass named `class_name`
whose fields are specified by the mapping `field_map`.

The `field_map` is a mapping of field name to buffer parsers and transcribers.

*Note*:
if `field_order` is not specified
it is constructed by iterating over `field_map`.
Prior to Python 3.6, `dict`s do not provide a reliable order
and should be accompanied by an explicit `field_order`.
From 3.6 onward a `dict` is enough and its insertion order
will dictate the default `field_order`.

For a fixed record structure
the default `.parse` and `.transcribe` methods will suffice;
they parse or transcribe each field in turn.
Subclasses with variable records should override
the `.parse` and `.transcribe` methods
accordingly.

The `field_map` is a mapping of field name
to a class returned by the `pt_spec()` function.

If the class has both `parse_value` and `transcribe_value` methods
then the value itself will be directly stored.
Otherwise the class it presumed to be more complex subclass
of `AbstractBinary` and the instance is stored.

Here is an example exhibiting various ways of defining each field:
* `n1`: defined with the *`_value` methods of `UInt8`,
  which return or transcribe the `int` from an unsigned 8 bit value;
  this stores a `BinarySingleValue` whose `.value` is an `int`
* `n2`: defined from the `UInt8` class,
  which parses an unsigned 8 bit value;
  this stores an `UInt8` instance
  (also a `BinarySingleValue` whole `.value` is an `int`)
* `n3`: like `n2`
* `data1`: defined with the *`_value` methods of `BSData`,
  which return or transcribe the data `bytes`
  from a run length encoded data chunk;
  this stores a `BinarySingleValue` whose `.value` is a `bytes`
* `data2`: defined from the `BSData` class
  which parses a run length encoded data chunk;
  this is a `BinarySingleValue` so we store its `bytes` value directly.

      >>> class BMV(BinaryMultiValue("BMV", {
      ...         'n1': (UInt8.parse_value, UInt8.transcribe_value),
      ...         'n2': UInt8,
      ...         'n3': UInt8,
      ...         'nd': ('>H4s', 'short bs'),
      ...         'data1': (
      ...             BSData.parse_value,
      ...             BSData.transcribe_value,
      ...         ),
      ...         'data2': BSData,
      ... })):
      ...     pass
      >>> BMV.FIELD_ORDER
      ['n1', 'n2', 'n3', 'nd', 'data1', 'data2']
      >>> bmv = BMV.from_bytes(b'\x11\x22\x77\x81\x82zyxw\x02AB\x04DEFG')
      >>> bmv.n1  #doctest: +ELLIPSIS
      17
      >>> bmv.n2
      34
      >>> bmv  #doctest: +ELLIPSIS
      BMV(n1=17, n2=34, n3=119, nd=nd_1_short__bs(short=33154, bs=b'zyxw'), data1=b'AB', data2=b'DEFG')
      >>> bmv.nd  #doctest: +ELLIPSIS
      nd_1_short__bs(short=33154, bs=b'zyxw')
      >>> bmv.nd.bs
      b'zyxw'
      >>> bytes(bmv.nd)
      b'zyxw'
      >>> bmv.data1
      b'AB'
      >>> bmv.data2
      b'DEFG'
      >>> bytes(bmv)
      b'\x11"w\x81\x82zyxw\x02AB\x04DEFG'
      >>> list(bmv.transcribe_flat())
      [b'\x11', b'"', b'w', b'\x81\x82zyxw', b'\x02', b'AB', b'\x04', b'DEFG']

## Function `BinarySingleStruct(class_name: str, struct_format: str, field_name: Optional[str] = None)`

A convenience wrapper for `BinaryMultiStruct`
for `struct_format`s with a single field.

Parameters:
* `class_name`: the class name for the generated class
* `struct_format`: the struct format string, specifying a
  single struct field
* `field_name`: optional field name for the value,
  default `'value'`

Example:

    >>> UInt16BE = BinarySingleStruct('UInt16BE', '>H')
    >>> UInt16BE.__name__
    'UInt16BE'
    >>> UInt16BE.format
    '>H'
    >>> UInt16BE.struct   #doctest: +ELLIPSIS
    <_struct.Struct object at ...>
    >>> field = UInt16BE.from_bytes(bytes((2,3)))
    >>> field
    UInt16BE(value=515)
    >>> field.value
    515

## Class `BinarySingleValue(AbstractBinary)`

A representation of a single value as the attribute `.value`.

Subclasses must implement:
* `parse` or `parse_value`
* `transcribe` or `transcribe_value`

*Method `BinarySingleValue.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse an instance from `bfr`.

Subclasses must implement this method or `parse_value`.

*Method `BinarySingleValue.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr` based on this class.

Subclasses must implement this method or `parse`.

*Method `BinarySingleValue.parse_value_from_bytes(bs, offset=0, length=None, **kw)`*:
Parse a value from the bytes `bs` based on this class.
Return `(value,offset)`.

*Method `BinarySingleValue.scan_values(bfr: cs.buffer.CornuCopyBuffer, **kw)`*:
Scan `bfr`, yield values.

*Method `BinarySingleValue.transcribe(self)`*:
Transcribe this instance as bytes.

Subclasses must implement this method or `transcribe_value`.

*Method `BinarySingleValue.transcribe_value(value)`*:
Transcribe `value` as bytes based on this class.

Subclasses must implement this method or `transcribe`.

*Method `BinarySingleValue.value_from_bytes(bs, **from_bytes_kw)`*:
Decode an instance from `bs` using `.from_bytes`
and return the `.value` attribute.
Keyword arguments are passed to `cls.from_bytes`.

## Class `BinaryUTF16NUL(BinarySingleValue)`

A NUL terminated UTF-16 string.

*Method `BinaryUTF16NUL.__init__(self, value: str, *, encoding: str)`*:
pylint: disable=super-init-not-called

*Method `BinaryUTF16NUL.parse(bfr: cs.buffer.CornuCopyBuffer, *, encoding: str)`*:
Parse the encoding and value and construct an instance.

*Method `BinaryUTF16NUL.parse_value(bfr: cs.buffer.CornuCopyBuffer, *, encoding: str) -> str`*:
Read a NUL terminated UTF-16 string from `bfr`, return a `UTF16NULField`.
The mandatory parameter `encoding` specifies the UTF16 encoding to use
(`'utf_16_be'` or `'utf_16_le'`).

*Method `BinaryUTF16NUL.transcribe(self)`*:
Transcribe `self.value` in UTF-16 with a terminating NUL.

*Method `BinaryUTF16NUL.transcribe_value(value: str, encoding='utf-16')`*:
Transcribe `value` in UTF-16 with a terminating NUL.

## Class `BinaryUTF8NUL(BinarySingleValue)`

A NUL terminated UTF-8 string.

*Method `BinaryUTF8NUL.parse_value(bfr: cs.buffer.CornuCopyBuffer) -> str`*:
Read a NUL terminated UTF-8 string from `bfr`, return field.

*Method `BinaryUTF8NUL.transcribe_value(s)`*:
Transcribe the `value` in UTF-8 with a terminating NUL.

## Class `BSData(BinarySingleValue)`

A run length encoded data chunk, with the length encoded as a `BSUInt`.

*Property `BSData.data`*:
An alias for the `.value` attribute.

*Property `BSData.data_offset`*:
The length of the length indicator,
useful for computing the location of the raw data.

*Method `BSData.data_offset_for(bs) -> int`*:
Compute the `data_offset` which would obtain for the bytes `bs`.

*Method `BSData.parse_value(bfr: cs.buffer.CornuCopyBuffer) -> bytes`*:
Parse the data from `bfr`.

*Method `BSData.transcribe_value(data)`*:
Transcribe the payload length and then the payload.

## Class `BSSFloat(BinarySingleValue)`

A float transcribed as a `BSString` of `str(float)`.

*Method `BSSFloat.parse_value(bfr: cs.buffer.CornuCopyBuffer) -> float`*:
Parse a `BSSFloat` from a buffer and return the `float`.

*Method `BSSFloat.transcribe_value(f)`*:
Transcribe a `float`.

## Class `BSString(BinarySingleValue)`

A run length encoded string, with the length encoded as a BSUInt.

*Method `BSString.parse_value(bfr: cs.buffer.CornuCopyBuffer, encoding='utf-8', errors='strict') -> str`*:
Parse a run length encoded string from `bfr`.

*Method `BSString.transcribe_value(value: str, encoding='utf-8')`*:
Transcribe a string.

## Class `BSUInt(BinarySingleValue)`

A binary serialised unsigned `int`.

This uses a big endian byte encoding where continuation octets
have their high bit set. The bits contributing to the value
are in the low order 7 bits.

*Method `BSUInt.decode_bytes(data, offset=0) -> Tuple[int, int]`*:
Decode an extensible byte serialised unsigned `int` from `data` at `offset`.
Return value and new offset.

Continuation octets have their high bit set.
The octets are big-endian.

If you just have a `bytes` instance, this is the go. If you're
reading from a stream you're better off with `parse` or `parse_value`.

Examples:

    >>> BSUInt.decode_bytes(b'\0')
    (0, 1)

Note: there is of course the usual `AbstractBinary.parse_bytes`
but that constructs a buffer to obtain the individual bytes;
this static method will be more performant
if all you are doing is reading this serialisation
and do not already have a buffer.

*Method `BSUInt.parse_value(bfr: cs.buffer.CornuCopyBuffer) -> int`*:
Parse an extensible byte serialised unsigned `int` from a buffer.

Continuation octets have their high bit set.
The value is big-endian.

This is the go for reading from a stream. If you already have
a bare bytes instance then the `.decode_bytes` static method
is probably most efficient;
there is of course the usual `AbstractBinary.parse_bytes`
but that constructs a buffer to obtain the individual bytes.

*Method `BSUInt.transcribe_value(n)`*:
Encode an unsigned int as an entensible byte serialised octet
sequence for decode. Return the bytes object.

## Function `flatten(chunks)`

Flatten `chunks` into an iterable of `bytes`-like instances.
None of the `bytes` instances will be empty.

This exists to allow subclass methods to easily return
transcribeable things (having a `.transcribe` method), ASCII
strings or bytes or iterables or even `None`, in turn allowing
them simply to return their superclass' chunks iterators
directly instead of having to unpack them.

An example from the `cs.iso14496.METABoxBody` class:

    def transcribe(self):
        yield super().transcribe()
        yield self.theHandler
        yield self.boxes

The binary classes `flatten` the result of the `.transcribe`
method to obtain `bytes` insteances for the object's bnary
transcription.

## Class `Float64BE(Float64BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>d'` and presents the attributes ('value',).

*Method `Float64BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Float64BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Float64BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Float64BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `Float64LE(Float64LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<d'` and presents the attributes ('value',).

*Method `Float64LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Float64LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Float64LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Float64LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `Int16BE(Int16BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>h'` and presents the attributes ('value',).

*Method `Int16BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Int16BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Int16BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Int16BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `Int16LE(Int16LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<h'` and presents the attributes ('value',).

*Method `Int16LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Int16LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Int16LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Int16LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `Int32BE(Int32BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>l'` and presents the attributes ('value',).

*Method `Int32BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Int32BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Int32BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Int32BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `Int32LE(Int32LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<l'` and presents the attributes ('value',).

*Method `Int32LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `Int32LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `Int32LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `Int32LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Function `pt_spec(pt, name=None)`

Convert a parse/transcribe specification `pt`
into an `AbstractBinary` subclass.

This is largely used to provide flexibility
in the specifications for the `BinaryMultiValue` factory
but can be used as a factory for other simple classes.

If the specification `pt` is a subclass of `AbstractBinary`
this is returned directly.

If `pt` is a 2-tuple of `str`
the values are presumed to be a format string for `struct.struct`
and filed names separated by spaces;
a new `BinaryMultiStruct` class is created from these and returned.

Otherwise two functions
`f_parse_value(bfr)` and `f_transcribe_value(value)`
are obtained and used to construct a new `BinarySingleValue` class
as follows:

If `pt` has `.parse_value` and `.transcribe_value` callable attributes,
use those for `f_parse_value` and `f_transcribe_value` respectively.

Otherwise, if `pt` is an `int`
define `f_parse_value` to obtain exactly that many bytes from a buffer
and `f_transcribe_value` to return those bytes directly.

Otherwise presume `pt` is a 2-tuple of `(f_parse_value,f_transcribe_value)`.

## Class `SimpleBinary(types.SimpleNamespace, AbstractBinary)`

Abstract binary class based on a `SimpleNamespace`,
thus providing a nice `__str__` and a keyword based `__init__`.
Implementors must still define `.parse` and `.transcribe`.

To constrain the arguments passed to `__init__`,
define an `__init__` which accepts specific keyword arguments
and pass through to `super().__init__()`. Example:

    def __init__(self, *, field1=None, field2):
        """ Accept only `field1` (optional)
            and `field2` (mandatory).
        """
        super().__init__(field1=field1, field2=field2)

## Class `UInt16BE(UInt16BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>H'` and presents the attributes ('value',).

*Method `UInt16BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt16BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt16BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt16BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt16LE(UInt16LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<H'` and presents the attributes ('value',).

*Method `UInt16LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt16LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt16LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt16LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt32BE(UInt32BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>L'` and presents the attributes ('value',).

*Method `UInt32BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt32BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt32BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt32BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt32LE(UInt32LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<L'` and presents the attributes ('value',).

*Method `UInt32LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt32LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt32LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt32LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt64BE(UInt64BE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'>Q'` and presents the attributes ('value',).

*Method `UInt64BE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt64BE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt64BE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt64BE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt64LE(UInt64LE, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'<Q'` and presents the attributes ('value',).

*Method `UInt64LE.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt64LE.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt64LE.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt64LE.transcribe_value(value)`*:
Transcribe a value back into bytes.

## Class `UInt8(UInt8, AbstractBinary)`

An `AbstractBinary` `namedtuple` which parses and transcribes
the struct format `'B'` and presents the attributes ('value',).

*Method `UInt8.parse(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse from `bfr` via `struct.unpack`.

*Method `UInt8.parse_value(bfr: cs.buffer.CornuCopyBuffer)`*:
Parse a value from `bfr`, return the value.

*Method `UInt8.transcribe(self)`*:
Transcribe via `struct.pack`.

*Method `UInt8.transcribe_value(value)`*:
Transcribe a value back into bytes.

# Release Log



*Release 20240630*:
* flatten: do not yield empty str-as-ascii-bytes - we want to ensure that flatten never yields an empty bytes instance.
* New AbstractBinary.write(f) method to write the binary form of this object to a file.
* New BinarySingleValue.value_from_bytes(bytes) class method to return the value from a bytes instance.
* Drop BinaryMixin, now folded directly into AbstractBinary.
* AbstractBinary.scan: pass extra keyword arguments to AbstractBinary.parse, supporting plumbing eg a logging parameter through.

*Release 20240422*:
New _BinaryMultiValue_Base.for_json() method returning a dict containing the fields.

*Release 20240316*:
Fixed release upload artifacts.

*Release 20240201*:
BREAKING CHANGE: drop the long deprecated PacketField related classes.

*Release 20231129*:
BinaryMultiStruct.parse: promote the buffer arguments to a CornuCopyBuffer.

*Release 20230401*:
* BinaryMixin.scan: `bfr` parameter may be any object acceptable to CornuCopyBuffer.promote.
* BinaryMixin.scan: accept new optional with_offsets parameter; deprecate scan_with_offsets and scan_fspathi in favour of scan.

*Release 20230212*:
* BinaryMixin: new load(file) and save(file) methods.
* BinaryMixin.scan: promote the bfr argument.

*Release 20221206*:
Documentation fix.

*Release 20220605*:
BinaryMixin: replace scan_file with scan_fspath, as the former left uncertainty about the amount of the file consumed.

*Release 20210316*:
* BSUInt: rename parse_bytes to decode_bytes, the former name conflicted with BinaryMixin.parse_bytes and broken the semantics.
* Minor refactors.

*Release 20210306*:
MAJOR RELEASE: The PacketField classes and friends were hard to use; this release supplied a suite of easier to use and more consistent Binary* classes, and ports most of those things based on the old scheme to the new scheme.

*Release 20200229*:
* ListField: replace transcribe method with transcribe_value method, aids external use.
* Add `.length` attribute to struct based packet classes providing the data length of the structure (struct.Struct.size).
* Packet: new `add_deferred_field` method to consume the raw data for a field for parsing later (done automatically if the attribute is accessed).
* New `@deferred_field` decorator for the parser for that stashed data.

*Release 20191230.3*:
Docstring tweak.

*Release 20191230.2*:
Documentation updates.

*Release 20191230.1*:
Docstring updates. Semantic changes were in the previous release.

*Release 20191230*:
* ListField: new __iter__ method.
* Packet: __str__: accept optional `skip_fields` parameter to omit some field names.
* Packet: new .add_from_value method to add a named field with a presupplied value.
* Packet: new remove_field(field_name) and pop_field() methods to remove fields.
* BytesesField: __iter__ yields the bytes values, transcribe=__iter__.
* PacketField: propagate keyword arguments through various methods, required for parameterised PacketFields.
* New UTF16NULField, a NUL terminated UTF16 string.
* PacketField: provide a default `.transcribe_value` method which makes a new instance and calls its `.transcribe` method.
* Documentation update and several minor changes.

*Release 20190220*:
* Packet.self_check: fields without a sanity check cause a warning, not a ValueError.
* New Float64BE, Float64LE and BSSFloat classes for IEEE floats and floats-as-strings.
* Additional module docstringage on subclassing Packet and PacketField.
* BSString: drop redundant from_buffer class method.
* PacketField.__init__: default to value=None if omitted.

*Release 20181231*:
flatten: do not yield zero length bytelike objects, can be misread as EOF on some streams.

*Release 20181108*:
* New PacketField.transcribe_value_flat convenience method to return a flat iterable of bytes-like objects.
* New PacketField.parse_buffer generator method to parse instances of the PacketField from a buffer until end of input.
* New PacketField.parse_buffer_values generator method to parse instances of the PacketField from a buffer and yield the `.value` attribute until end of input.

*Release 20180823*:
* Some bugfixes.
* Define PacketField.__eq__.
* BSUInt, BSData and BSString classes implementing the serialisations from cs.serialise.
* New PacketField.value_from_bytes class method.
* New PacketField.value_from_buffer method.

*Release 20180810.2*:
Documentation improvements.

*Release 20180810.1*:
Improve module description.

*Release 20180810*:
BytesesField.from_buffer: make use of the buffer's skipto method if discard_data is true.

*Release 20180805*:
* Packet: now an abstract class, new self_check method initially checking the
* PACKET_FIELDS class attribute against the instance, new methods get_field
* and set_field to fetch or replace existing fields, allow keyword arguments
* to initialise the Packet fields and document the dependency on keyword
* argument ordering.
* PacketField: __len__ computed directory from a transcribe, drop other __len__
* methods.
* EmptyField singleton to use as a placeholder for missing optional fields.
* BytesField: implement value_s and from_buffer.
* multi_struct_field: implement __len__ for generated class.
* flatten: treat memoryviews like bytes.
* Assorted docstrings and fixes.

*Release 20180801*:
Initial PyPI release.
