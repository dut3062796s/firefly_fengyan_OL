# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/login/enterPlace.proto',
  package='protoFile.login.enterPlace',
  serialized_pb='\n protoFile/login/enterPlace.proto\x12\x1aprotoFile.login.enterPlace\"?\n\x11\x65nterPlaceRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07placeId\x18\x02 \x02(\x05\x12\r\n\x05\x66orce\x18\x03 \x01(\x08\"o\n\x12\x65nterPlaceResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32*.protoFile.login.enterPlace.EnterPlaceData\"Y\n\x0e\x45nterPlaceData\x12\x0f\n\x07placeId\x18\x01 \x01(\x05\x12\x0e\n\x06isboos\x18\x02 \x01(\x08\x12\x13\n\x0b\x63opySceneId\x18\x03 \x01(\x05\x12\x11\n\tsceneType\x18\x04 \x01(\x05')




_ENTERPLACEREQUEST = descriptor.Descriptor(
  name='enterPlaceRequest',
  full_name='protoFile.login.enterPlace.enterPlaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.login.enterPlace.enterPlaceRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='placeId', full_name='protoFile.login.enterPlace.enterPlaceRequest.placeId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='force', full_name='protoFile.login.enterPlace.enterPlaceRequest.force', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=64,
  serialized_end=127,
)


_ENTERPLACERESPONSE = descriptor.Descriptor(
  name='enterPlaceResponse',
  full_name='protoFile.login.enterPlace.enterPlaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.login.enterPlace.enterPlaceResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.login.enterPlace.enterPlaceResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.login.enterPlace.enterPlaceResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=129,
  serialized_end=240,
)


_ENTERPLACEDATA = descriptor.Descriptor(
  name='EnterPlaceData',
  full_name='protoFile.login.enterPlace.EnterPlaceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='placeId', full_name='protoFile.login.enterPlace.EnterPlaceData.placeId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isboos', full_name='protoFile.login.enterPlace.EnterPlaceData.isboos', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='copySceneId', full_name='protoFile.login.enterPlace.EnterPlaceData.copySceneId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sceneType', full_name='protoFile.login.enterPlace.EnterPlaceData.sceneType', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=242,
  serialized_end=331,
)

_ENTERPLACERESPONSE.fields_by_name['data'].message_type = _ENTERPLACEDATA
DESCRIPTOR.message_types_by_name['enterPlaceRequest'] = _ENTERPLACEREQUEST
DESCRIPTOR.message_types_by_name['enterPlaceResponse'] = _ENTERPLACERESPONSE
DESCRIPTOR.message_types_by_name['EnterPlaceData'] = _ENTERPLACEDATA

class enterPlaceRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERPLACEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.login.enterPlace.enterPlaceRequest)

class enterPlaceResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERPLACERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.login.enterPlace.enterPlaceResponse)

class EnterPlaceData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERPLACEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.login.enterPlace.EnterPlaceData)

# @@protoc_insertion_point(module_scope)
