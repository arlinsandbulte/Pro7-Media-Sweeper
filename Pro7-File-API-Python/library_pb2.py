# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\"\x8c\x02\n\x07Library\x12\x19\n\x03url\x18\x01 \x01(\x0b\x32\x0c.rv.data.URL\x12\x38\n\x0flibraryChildren\x18\x02 \x01(\x0b\x32\x1d.rv.data.Library.LibraryArrayH\x00\x12\x35\n\x0clibraryItems\x18\x03 \x01(\x0b\x32\x1d.rv.data.Library.LibraryItemsH\x00\x1a\x33\n\x0cLibraryArray\x12#\n\tlibraries\x18\x01 \x03(\x0b\x32\x10.rv.data.Library\x1a\x33\n\x0cLibraryItems\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.rv.data.LibraryItemB\x0b\n\tChildType\"(\n\x0bLibraryItem\x12\x19\n\x03url\x18\x01 \x01(\x0b\x32\x0c.rv.data.URLb\x06proto3')



_LIBRARY = DESCRIPTOR.message_types_by_name['Library']
_LIBRARY_LIBRARYARRAY = _LIBRARY.nested_types_by_name['LibraryArray']
_LIBRARY_LIBRARYITEMS = _LIBRARY.nested_types_by_name['LibraryItems']
_LIBRARYITEM = DESCRIPTOR.message_types_by_name['LibraryItem']
Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), {

  'LibraryArray' : _reflection.GeneratedProtocolMessageType('LibraryArray', (_message.Message,), {
    'DESCRIPTOR' : _LIBRARY_LIBRARYARRAY,
    '__module__' : 'library_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Library.LibraryArray)
    })
  ,

  'LibraryItems' : _reflection.GeneratedProtocolMessageType('LibraryItems', (_message.Message,), {
    'DESCRIPTOR' : _LIBRARY_LIBRARYITEMS,
    '__module__' : 'library_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Library.LibraryItems)
    })
  ,
  'DESCRIPTOR' : _LIBRARY,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Library)
  })
_sym_db.RegisterMessage(Library)
_sym_db.RegisterMessage(Library.LibraryArray)
_sym_db.RegisterMessage(Library.LibraryItems)

LibraryItem = _reflection.GeneratedProtocolMessageType('LibraryItem', (_message.Message,), {
  'DESCRIPTOR' : _LIBRARYITEM,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.LibraryItem)
  })
_sym_db.RegisterMessage(LibraryItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIBRARY._serialized_start=45
  _LIBRARY._serialized_end=313
  _LIBRARY_LIBRARYARRAY._serialized_start=196
  _LIBRARY_LIBRARYARRAY._serialized_end=247
  _LIBRARY_LIBRARYITEMS._serialized_start=249
  _LIBRARY_LIBRARYITEMS._serialized_end=300
  _LIBRARYITEM._serialized_start=315
  _LIBRARYITEM._serialized_end=355
# @@protoc_insertion_point(module_scope)
