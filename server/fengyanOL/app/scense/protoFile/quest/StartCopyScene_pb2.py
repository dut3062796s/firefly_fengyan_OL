# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='StartCopyScene.proto',
  package='proto.groupHall.groupHall1816',
  serialized_pb='\n\x14StartCopyScene.proto\x12\x1dproto.groupHall.groupHall1816\"6\n\x15startCopySceneRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tvipMatrix\x18\x02 \x01(\x05\"9\n\x16startCopySceneResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_STARTCOPYSCENEREQUEST = descriptor.Descriptor(
  name='startCopySceneRequest',
  full_name='proto.groupHall.groupHall1816.startCopySceneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='proto.groupHall.groupHall1816.startCopySceneRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vipMatrix', full_name='proto.groupHall.groupHall1816.startCopySceneRequest.vipMatrix', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=55,
  serialized_end=109,
)


_STARTCOPYSCENERESPONSE = descriptor.Descriptor(
  name='startCopySceneResponse',
  full_name='proto.groupHall.groupHall1816.startCopySceneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='proto.groupHall.groupHall1816.startCopySceneResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='proto.groupHall.groupHall1816.startCopySceneResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=111,
  serialized_end=168,
)

DESCRIPTOR.message_types_by_name['startCopySceneRequest'] = _STARTCOPYSCENEREQUEST
DESCRIPTOR.message_types_by_name['startCopySceneResponse'] = _STARTCOPYSCENERESPONSE

class startCopySceneRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTCOPYSCENEREQUEST
  
  # @@protoc_insertion_point(class_scope:proto.groupHall.groupHall1816.startCopySceneRequest)

class startCopySceneResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTCOPYSCENERESPONSE
  
  # @@protoc_insertion_point(class_scope:proto.groupHall.groupHall1816.startCopySceneResponse)

# @@protoc_insertion_point(module_scope)