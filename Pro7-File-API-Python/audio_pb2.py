# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udio.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\"\xaa\x08\n\x05\x41udio\x1a\x8d\x01\n\x10SettingsDocument\x12\x30\n\x0coutput_setup\x18\x01 \x01(\x0b\x32\x1a.rv.data.Audio.OutputSetup\x12-\n\x0emonitor_device\x18\x02 \x01(\x0b\x32\x15.rv.data.Audio.Device\x12\x18\n\x10monitor_on_mains\x18\x03 \x01(\x08\x1a\xf5\x01\n\x0bOutputSetup\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12+\n\x0c\x61udio_device\x18\x02 \x01(\x0b\x32\x15.rv.data.Audio.Device\x12\x37\n\x10logical_channels\x18\x03 \x03(\x0b\x32\x1d.rv.data.Audio.LogicalChannel\x12\x13\n\x0b\x61udio_delay\x18\x04 \x01(\x01\x12\x14\n\x0cmaster_level\x18\x05 \x01(\x01\x12\x38\n\x10physical_chanels\x18\x06 \x03(\x0b\x32\x1e.rv.data.Audio.PhysicalChannel\x1a\x9c\x02\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08renderID\x18\x02 \x01(\t\x12\x1b\n\x13input_channel_count\x18\x03 \x01(\r\x12\x1c\n\x14output_channel_count\x18\x04 \x01(\r\x12-\n\x07\x66ormats\x18\x05 \x03(\x0b\x32\x1c.rv.data.Audio.Device.Format\x1a\x87\x01\n\x06\x46ormat\x12\x13\n\x0bsample_rate\x18\x01 \x01(\r\x12\x11\n\tbit_depth\x18\x02 \x01(\r\x12/\n\x04type\x18\x03 \x01(\x0e\x32!.rv.data.Audio.Device.Format.Type\"$\n\x04Type\x12\x0c\n\x08TYPE_INT\x10\x00\x12\x0e\n\nTYPE_FLOAT\x10\x01\x1a\x98\x02\n\x0eLogicalChannel\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\r\x12\r\n\x05muted\x18\x04 \x01(\x08\x12L\n\x17physical_audio_channels\x18\x05 \x03(\x0b\x32+.rv.data.Audio.LogicalChannel.OutputChannel\x12\x0c\n\x04solo\x18\x06 \x01(\x08\x12\x11\n\ttest_tone\x18\x07 \x01(\x08\x1aN\n\rOutputChannel\x12\r\n\x05index\x18\x01 \x01(\r\x12\r\n\x05muted\x18\x02 \x01(\x08\x12\x0c\n\x04solo\x18\x03 \x01(\x08\x12\x11\n\ttest_tone\x18\x04 \x01(\x08\x1a_\n\x0fPhysicalChannel\x12\r\n\x05index\x18\x01 \x01(\r\x12\x13\n\x0bmute_enable\x18\x02 \x01(\x08\x12\x13\n\x0bsolo_enable\x18\x03 \x01(\x08\x12\x13\n\x0btone_enable\x18\x04 \x01(\x08\x62\x06proto3')



_AUDIO = DESCRIPTOR.message_types_by_name['Audio']
_AUDIO_SETTINGSDOCUMENT = _AUDIO.nested_types_by_name['SettingsDocument']
_AUDIO_OUTPUTSETUP = _AUDIO.nested_types_by_name['OutputSetup']
_AUDIO_DEVICE = _AUDIO.nested_types_by_name['Device']
_AUDIO_DEVICE_FORMAT = _AUDIO_DEVICE.nested_types_by_name['Format']
_AUDIO_LOGICALCHANNEL = _AUDIO.nested_types_by_name['LogicalChannel']
_AUDIO_LOGICALCHANNEL_OUTPUTCHANNEL = _AUDIO_LOGICALCHANNEL.nested_types_by_name['OutputChannel']
_AUDIO_PHYSICALCHANNEL = _AUDIO.nested_types_by_name['PhysicalChannel']
_AUDIO_DEVICE_FORMAT_TYPE = _AUDIO_DEVICE_FORMAT.enum_types_by_name['Type']
Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), {

  'SettingsDocument' : _reflection.GeneratedProtocolMessageType('SettingsDocument', (_message.Message,), {
    'DESCRIPTOR' : _AUDIO_SETTINGSDOCUMENT,
    '__module__' : 'audio_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Audio.SettingsDocument)
    })
  ,

  'OutputSetup' : _reflection.GeneratedProtocolMessageType('OutputSetup', (_message.Message,), {
    'DESCRIPTOR' : _AUDIO_OUTPUTSETUP,
    '__module__' : 'audio_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Audio.OutputSetup)
    })
  ,

  'Device' : _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {

    'Format' : _reflection.GeneratedProtocolMessageType('Format', (_message.Message,), {
      'DESCRIPTOR' : _AUDIO_DEVICE_FORMAT,
      '__module__' : 'audio_pb2'
      # @@protoc_insertion_point(class_scope:rv.data.Audio.Device.Format)
      })
    ,
    'DESCRIPTOR' : _AUDIO_DEVICE,
    '__module__' : 'audio_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Audio.Device)
    })
  ,

  'LogicalChannel' : _reflection.GeneratedProtocolMessageType('LogicalChannel', (_message.Message,), {

    'OutputChannel' : _reflection.GeneratedProtocolMessageType('OutputChannel', (_message.Message,), {
      'DESCRIPTOR' : _AUDIO_LOGICALCHANNEL_OUTPUTCHANNEL,
      '__module__' : 'audio_pb2'
      # @@protoc_insertion_point(class_scope:rv.data.Audio.LogicalChannel.OutputChannel)
      })
    ,
    'DESCRIPTOR' : _AUDIO_LOGICALCHANNEL,
    '__module__' : 'audio_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Audio.LogicalChannel)
    })
  ,

  'PhysicalChannel' : _reflection.GeneratedProtocolMessageType('PhysicalChannel', (_message.Message,), {
    'DESCRIPTOR' : _AUDIO_PHYSICALCHANNEL,
    '__module__' : 'audio_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Audio.PhysicalChannel)
    })
  ,
  'DESCRIPTOR' : _AUDIO,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Audio)
  })
_sym_db.RegisterMessage(Audio)
_sym_db.RegisterMessage(Audio.SettingsDocument)
_sym_db.RegisterMessage(Audio.OutputSetup)
_sym_db.RegisterMessage(Audio.Device)
_sym_db.RegisterMessage(Audio.Device.Format)
_sym_db.RegisterMessage(Audio.LogicalChannel)
_sym_db.RegisterMessage(Audio.LogicalChannel.OutputChannel)
_sym_db.RegisterMessage(Audio.PhysicalChannel)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUDIO._serialized_start=43
  _AUDIO._serialized_end=1109
  _AUDIO_SETTINGSDOCUMENT._serialized_start=53
  _AUDIO_SETTINGSDOCUMENT._serialized_end=194
  _AUDIO_OUTPUTSETUP._serialized_start=197
  _AUDIO_OUTPUTSETUP._serialized_end=442
  _AUDIO_DEVICE._serialized_start=445
  _AUDIO_DEVICE._serialized_end=729
  _AUDIO_DEVICE_FORMAT._serialized_start=594
  _AUDIO_DEVICE_FORMAT._serialized_end=729
  _AUDIO_DEVICE_FORMAT_TYPE._serialized_start=693
  _AUDIO_DEVICE_FORMAT_TYPE._serialized_end=729
  _AUDIO_LOGICALCHANNEL._serialized_start=732
  _AUDIO_LOGICALCHANNEL._serialized_end=1012
  _AUDIO_LOGICALCHANNEL_OUTPUTCHANNEL._serialized_start=934
  _AUDIO_LOGICALCHANNEL_OUTPUTCHANNEL._serialized_end=1012
  _AUDIO_PHYSICALCHANNEL._serialized_start=1014
  _AUDIO_PHYSICALCHANNEL._serialized_end=1109
# @@protoc_insertion_point(module_scope)
