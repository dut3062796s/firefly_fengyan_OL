# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/login/loginToServer101.proto',
  package='protoFile.login.loginToServer101',
  serialized_pb='\n&protoFile/login/loginToServer101.proto\x12 protoFile.login.loginToServer101\"6\n\x14loginToServerRequest\x12\x0c\n\x04user\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"r\n\x15loginToServerResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32*.protoFile.login.loginToServer101.UserInfo\">\n\x08UserInfo\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0f\n\x07hasRole\x18\x02 \x01(\x08\x12\x11\n\tdefaultId\x18\x03 \x01(\x05')




_LOGINTOSERVERREQUEST = descriptor.Descriptor(
  name='loginToServerRequest',
  full_name='protoFile.login.loginToServer101.loginToServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user', full_name='protoFile.login.loginToServer101.loginToServerRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='protoFile.login.loginToServer101.loginToServerRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=76,
  serialized_end=130,
)


_LOGINTOSERVERRESPONSE = descriptor.Descriptor(
  name='loginToServerResponse',
  full_name='protoFile.login.loginToServer101.loginToServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.login.loginToServer101.loginToServerResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.login.loginToServer101.loginToServerResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.login.loginToServer101.loginToServerResponse.data', index=2,
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
  serialized_start=132,
  serialized_end=246,
)


_USERINFO = descriptor.Descriptor(
  name='UserInfo',
  full_name='protoFile.login.loginToServer101.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userId', full_name='protoFile.login.loginToServer101.UserInfo.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hasRole', full_name='protoFile.login.loginToServer101.UserInfo.hasRole', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='defaultId', full_name='protoFile.login.loginToServer101.UserInfo.defaultId', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=248,
  serialized_end=310,
)

_LOGINTOSERVERRESPONSE.fields_by_name['data'].message_type = _USERINFO
DESCRIPTOR.message_types_by_name['loginToServerRequest'] = _LOGINTOSERVERREQUEST
DESCRIPTOR.message_types_by_name['loginToServerResponse'] = _LOGINTOSERVERRESPONSE
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO

class loginToServerRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOSERVERREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer101.loginToServerRequest)

class loginToServerResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOSERVERRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer101.loginToServerResponse)

class UserInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer101.UserInfo)

# @@protoc_insertion_point(module_scope)