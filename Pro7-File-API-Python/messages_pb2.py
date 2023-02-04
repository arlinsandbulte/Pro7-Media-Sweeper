# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import templateIdentification_pb2 as templateIdentification__pb2
import timers_pb2 as timers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x1ctemplateIdentification.proto\x1a\x0ctimers.proto\"\xbf\t\n\x07Message\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\r\n\x05title\x18\x02 \x01(\t\x12\x16\n\x0etime_to_remove\x18\x03 \x01(\x01\x12\x1a\n\x12visible_on_network\x18\x04 \x01(\x08\x12\x31\n\x08template\x18\x06 \x01(\x0b\x32\x1f.rv.data.TemplateIdentification\x12.\n\nclear_type\x18\t \x01(\x0e\x32\x1a.rv.data.Message.ClearType\x12\x14\n\x0cmessage_text\x18\n \x01(\t\x12&\n\x06tokens\x18\x0b \x03(\x0b\x32\x16.rv.data.Message.Token\x12\x31\n\x0ctoken_values\x18\x0c \x03(\x0b\x32\x1b.rv.data.Message.TokenValue\x1a\xcb\x02\n\x05Token\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x34\n\x04text\x18\x02 \x01(\x0b\x32$.rv.data.Message.Token.TokenTypeTextH\x00\x12\x36\n\x05timer\x18\x03 \x01(\x0b\x32%.rv.data.Message.Token.TokenTypeTimerH\x00\x12\x36\n\x05\x63lock\x18\x04 \x01(\x0b\x32%.rv.data.Message.Token.TokenTypeClockH\x00\x1a\x1d\n\rTokenTypeText\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x41\n\x0eTokenTypeTimer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\ntimer_uuid\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x1a\x10\n\x0eTokenTypeClockB\x0b\n\tTokenType\x1a\xd5\x03\n\nTokenValue\x12\x1f\n\x08token_id\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x12\n\ntoken_name\x18\x05 \x01(\t\x12:\n\x04text\x18\x02 \x01(\x0b\x32*.rv.data.Message.TokenValue.TokenValueTextH\x00\x12<\n\x05timer\x18\x03 \x01(\x0b\x32+.rv.data.Message.TokenValue.TokenValueTimerH\x00\x12<\n\x05\x63lock\x18\x04 \x01(\x0b\x32+.rv.data.Message.TokenValue.TokenValueClockH\x00\x1a\x1f\n\x0eTokenValueText\x12\r\n\x05value\x18\x01 \x01(\t\x1am\n\x0fTokenValueTimer\x12\x33\n\rconfiguration\x18\x01 \x01(\x0b\x32\x1c.rv.data.Timer.Configuration\x12%\n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x15.rv.data.Timer.Format\x1a\x38\n\x0fTokenValueClock\x12%\n\x06\x66ormat\x18\x01 \x01(\x0b\x32\x15.rv.data.Clock.FormatB\x10\n\x0eTokenValueType\"Z\n\tClearType\x12\x15\n\x11\x43LEAR_TYPE_MANUAL\x10\x00\x12\x19\n\x15\x43LEAR_TYPE_AFTER_TIME\x10\x01\x12\x1b\n\x17\x43LEAR_TYPE_AFTER_TIMERS\x10\x02\"i\n\x0fMessageDocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12\"\n\x08messages\x18\x02 \x03(\x0b\x32\x10.rv.data.Messageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=90
  _MESSAGE._serialized_end=1305
  _MESSAGE_TOKEN._serialized_start=410
  _MESSAGE_TOKEN._serialized_end=741
  _MESSAGE_TOKEN_TOKENTYPETEXT._serialized_start=614
  _MESSAGE_TOKEN_TOKENTYPETEXT._serialized_end=643
  _MESSAGE_TOKEN_TOKENTYPETIMER._serialized_start=645
  _MESSAGE_TOKEN_TOKENTYPETIMER._serialized_end=710
  _MESSAGE_TOKEN_TOKENTYPECLOCK._serialized_start=712
  _MESSAGE_TOKEN_TOKENTYPECLOCK._serialized_end=728
  _MESSAGE_TOKENVALUE._serialized_start=744
  _MESSAGE_TOKENVALUE._serialized_end=1213
  _MESSAGE_TOKENVALUE_TOKENVALUETEXT._serialized_start=995
  _MESSAGE_TOKENVALUE_TOKENVALUETEXT._serialized_end=1026
  _MESSAGE_TOKENVALUE_TOKENVALUETIMER._serialized_start=1028
  _MESSAGE_TOKENVALUE_TOKENVALUETIMER._serialized_end=1137
  _MESSAGE_TOKENVALUE_TOKENVALUECLOCK._serialized_start=1139
  _MESSAGE_TOKENVALUE_TOKENVALUECLOCK._serialized_end=1195
  _MESSAGE_CLEARTYPE._serialized_start=1215
  _MESSAGE_CLEARTYPE._serialized_end=1305
  _MESSAGEDOCUMENT._serialized_start=1307
  _MESSAGEDOCUMENT._serialized_end=1412
# @@protoc_insertion_point(module_scope)
