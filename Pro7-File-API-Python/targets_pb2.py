# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: targets.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import graphicsData_pb2 as graphicsData__pb2
import testPattern_pb2 as testPattern__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtargets.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x12graphicsData.proto\x1a\x11testPattern.proto\"\xf7\x01\n\tTargetSet\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x0e.rv.data.Color\x12%\n\x0ftest_image_path\x18\x04 \x01(\x0b\x32\x0c.rv.data.URL\x12+\n\x0bsource_size\x18\x05 \x01(\x0b\x32\x16.rv.data.Graphics.Size\x12 \n\x07targets\x18\x06 \x03(\x0b\x32\x0f.rv.data.Target\x12*\n\x0ctest_pattern\x18\x07 \x01(\x0b\x32\x14.rv.data.TestPattern\"\xca\x02\n\x06Target\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\x10source_unit_rect\x18\x03 \x01(\x0b\x32\x16.rv.data.Graphics.Rect\x12\'\n\x0ftest_image_fill\x18\x04 \x01(\x0b\x32\x0e.rv.data.Media\x12(\n\x05shape\x18\x05 \x01(\x0b\x32\x19.rv.data.Graphics.Element\x12*\n\x08\x66lipMode\x18\x06 \x01(\x0e\x32\x18.rv.data.Target.FlipMode\"d\n\x08\x46lipMode\x12\x12\n\x0e\x46LIP_MODE_NONE\x10\x00\x12\x16\n\x12\x46LIP_MODE_VERTICAL\x10\x01\x12\x18\n\x14\x46LIP_MODE_HORIZONTAL\x10\x02\x12\x12\n\x0e\x46LIP_MODE_BOTH\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'targets_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TARGETSET._serialized_start=84
  _TARGETSET._serialized_end=331
  _TARGET._serialized_start=334
  _TARGET._serialized_end=664
  _TARGET_FLIPMODE._serialized_start=564
  _TARGET_FLIPMODE._serialized_end=664
# @@protoc_insertion_point(module_scope)
