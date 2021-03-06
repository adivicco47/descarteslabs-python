# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/xyz/xyz.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from descarteslabs.common.proto.types import types_pb2 as descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2
from descarteslabs.common.proto.typespec import typespec_pb2 as descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2
from descarteslabs.common.proto.errors import errors_pb2 as descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/xyz/xyz.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(descarteslabs/common/proto/xyz/xyz.proto\x12\x17\x64\x65scarteslabs.workflows\x1a,descarteslabs/common/proto/types/types.proto\x1a\x32\x64\x65scarteslabs/common/proto/typespec/typespec.proto\x1a.descarteslabs/common/proto/errors/errors.proto\"\xbd\x03\n\x03XYZ\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12+\n\x11\x63reated_timestamp\x18\x02 \x01(\x03R\x10\x63reatedTimestamp\x12+\n\x11updated_timestamp\x18\x03 \x01(\x03R\x10updatedTimestamp\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x37\n\x04type\x18\t \x01(\x0e\x32#.descarteslabs.workflows.ResultTypeR\x04type\x12\x18\n\x07\x63hannel\x18\n \x01(\tR\x07\x63hannel\x12)\n\x10serialized_graft\x18\x15 \x01(\tR\x0fserializedGraft\x12\x33\n\x13serialized_typespec\x18\x16 \x01(\tB\x02\x18\x01R\x12serializedTypespec\x12=\n\x08typespec\x18\x19 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x08typespec\x12\x12\n\x04user\x18\x17 \x01(\tR\x04user\x12\x10\n\x03org\x18\x18 \x01(\tR\x03org\"B\n\x10\x43reateXYZRequest\x12.\n\x03xyz\x18\x01 \x01(\x0b\x32\x1c.descarteslabs.workflows.XYZR\x03xyz\"&\n\rGetXYZRequest\x12\x15\n\x06xyz_id\x18\x01 \x01(\tR\x05xyzId\"{\n\x1aGetXYZSessionErrorsRequest\x12\x15\n\x06xyz_id\x18\x01 \x01(\tR\x05xyzId\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\x12\'\n\x0fstart_timestamp\x18\x03 \x01(\x03R\x0estartTimestamp\"\x99\x01\n\x08XYZError\x12\x36\n\x04\x63ode\x18\x01 \x01(\x0e\x32\".descarteslabs.workflows.ErrorCodeR\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x1d\n\nsession_id\x18\x04 \x01(\tR\tsessionId2\xa5\x02\n\x06XYZAPI\x12V\n\tCreateXYZ\x12).descarteslabs.workflows.CreateXYZRequest\x1a\x1c.descarteslabs.workflows.XYZ\"\x00\x12P\n\x06GetXYZ\x12&.descarteslabs.workflows.GetXYZRequest\x1a\x1c.descarteslabs.workflows.XYZ\"\x00\x12q\n\x13GetXYZSessionErrors\x12\x33.descarteslabs.workflows.GetXYZSessionErrorsRequest\x1a!.descarteslabs.workflows.XYZError\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2.DESCRIPTOR,])




_XYZ = _descriptor.Descriptor(
  name='XYZ',
  full_name='descarteslabs.workflows.XYZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.XYZ.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='descarteslabs.workflows.XYZ.created_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createdTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='descarteslabs.workflows.XYZ.updated_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updatedTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='descarteslabs.workflows.XYZ.name', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='descarteslabs.workflows.XYZ.description', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.XYZ.type', index=5,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.XYZ.channel', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.XYZ.serialized_graft', index=7,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedGraft', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_typespec', full_name='descarteslabs.workflows.XYZ.serialized_typespec', index=8,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='serializedTypespec', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typespec', full_name='descarteslabs.workflows.XYZ.typespec', index=9,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='typespec', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='descarteslabs.workflows.XYZ.user', index=10,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='descarteslabs.workflows.XYZ.org', index=11,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='org', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=661,
)


_CREATEXYZREQUEST = _descriptor.Descriptor(
  name='CreateXYZRequest',
  full_name='descarteslabs.workflows.CreateXYZRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xyz', full_name='descarteslabs.workflows.CreateXYZRequest.xyz', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='xyz', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=729,
)


_GETXYZREQUEST = _descriptor.Descriptor(
  name='GetXYZRequest',
  full_name='descarteslabs.workflows.GetXYZRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xyz_id', full_name='descarteslabs.workflows.GetXYZRequest.xyz_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='xyzId', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=769,
)


_GETXYZSESSIONERRORSREQUEST = _descriptor.Descriptor(
  name='GetXYZSessionErrorsRequest',
  full_name='descarteslabs.workflows.GetXYZSessionErrorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xyz_id', full_name='descarteslabs.workflows.GetXYZSessionErrorsRequest.xyz_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='xyzId', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='descarteslabs.workflows.GetXYZSessionErrorsRequest.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sessionId', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='descarteslabs.workflows.GetXYZSessionErrorsRequest.start_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='startTimestamp', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=894,
)


_XYZERROR = _descriptor.Descriptor(
  name='XYZError',
  full_name='descarteslabs.workflows.XYZError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='descarteslabs.workflows.XYZError.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='code', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='descarteslabs.workflows.XYZError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='message', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='descarteslabs.workflows.XYZError.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='descarteslabs.workflows.XYZError.session_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sessionId', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=897,
  serialized_end=1050,
)

_XYZ.fields_by_name['type'].enum_type = descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2._RESULTTYPE
_XYZ.fields_by_name['typespec'].message_type = descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2._TYPESPEC
_CREATEXYZREQUEST.fields_by_name['xyz'].message_type = _XYZ
_XYZERROR.fields_by_name['code'].enum_type = descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['XYZ'] = _XYZ
DESCRIPTOR.message_types_by_name['CreateXYZRequest'] = _CREATEXYZREQUEST
DESCRIPTOR.message_types_by_name['GetXYZRequest'] = _GETXYZREQUEST
DESCRIPTOR.message_types_by_name['GetXYZSessionErrorsRequest'] = _GETXYZSESSIONERRORSREQUEST
DESCRIPTOR.message_types_by_name['XYZError'] = _XYZERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XYZ = _reflection.GeneratedProtocolMessageType('XYZ', (_message.Message,), {
  'DESCRIPTOR' : _XYZ,
  '__module__' : 'descarteslabs.common.proto.xyz.xyz_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.XYZ)
  })
_sym_db.RegisterMessage(XYZ)

CreateXYZRequest = _reflection.GeneratedProtocolMessageType('CreateXYZRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEXYZREQUEST,
  '__module__' : 'descarteslabs.common.proto.xyz.xyz_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CreateXYZRequest)
  })
_sym_db.RegisterMessage(CreateXYZRequest)

GetXYZRequest = _reflection.GeneratedProtocolMessageType('GetXYZRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETXYZREQUEST,
  '__module__' : 'descarteslabs.common.proto.xyz.xyz_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetXYZRequest)
  })
_sym_db.RegisterMessage(GetXYZRequest)

GetXYZSessionErrorsRequest = _reflection.GeneratedProtocolMessageType('GetXYZSessionErrorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETXYZSESSIONERRORSREQUEST,
  '__module__' : 'descarteslabs.common.proto.xyz.xyz_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetXYZSessionErrorsRequest)
  })
_sym_db.RegisterMessage(GetXYZSessionErrorsRequest)

XYZError = _reflection.GeneratedProtocolMessageType('XYZError', (_message.Message,), {
  'DESCRIPTOR' : _XYZERROR,
  '__module__' : 'descarteslabs.common.proto.xyz.xyz_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.XYZError)
  })
_sym_db.RegisterMessage(XYZError)


_XYZ.fields_by_name['serialized_typespec']._options = None

_XYZAPI = _descriptor.ServiceDescriptor(
  name='XYZAPI',
  full_name='descarteslabs.workflows.XYZAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1053,
  serialized_end=1346,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateXYZ',
    full_name='descarteslabs.workflows.XYZAPI.CreateXYZ',
    index=0,
    containing_service=None,
    input_type=_CREATEXYZREQUEST,
    output_type=_XYZ,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetXYZ',
    full_name='descarteslabs.workflows.XYZAPI.GetXYZ',
    index=1,
    containing_service=None,
    input_type=_GETXYZREQUEST,
    output_type=_XYZ,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetXYZSessionErrors',
    full_name='descarteslabs.workflows.XYZAPI.GetXYZSessionErrors',
    index=2,
    containing_service=None,
    input_type=_GETXYZSESSIONERRORSREQUEST,
    output_type=_XYZERROR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_XYZAPI)

DESCRIPTOR.services_by_name['XYZAPI'] = _XYZAPI

# @@protoc_insertion_point(module_scope)
