# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/pet/Pet3502.proto',
  package='protoFile.pet.Pet3502',
  serialized_pb='\n\x1bprotoFile/pet/Pet3502.proto\x12\x15protoFile.pet.Pet3502\"+\n\x0eGet3502Request\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05npcId\x18\x02 \x02(\x05\"@\n\x0fGet3502Response\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04gold\x18\x03 \x01(\x05')




_GET3502REQUEST = descriptor.Descriptor(
  name='Get3502Request',
  full_name='protoFile.pet.Pet3502.Get3502Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.pet.Pet3502.Get3502Request.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npcId', full_name='protoFile.pet.Pet3502.Get3502Request.npcId', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=54,
  serialized_end=97,
)


_GET3502RESPONSE = descriptor.Descriptor(
  name='Get3502Response',
  full_name='protoFile.pet.Pet3502.Get3502Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.pet.Pet3502.Get3502Response.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.pet.Pet3502.Get3502Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gold', full_name='protoFile.pet.Pet3502.Get3502Response.gold', index=2,
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
  serialized_start=99,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['Get3502Request'] = _GET3502REQUEST
DESCRIPTOR.message_types_by_name['Get3502Response'] = _GET3502RESPONSE

class Get3502Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GET3502REQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.Pet3502.Get3502Request)

class Get3502Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GET3502RESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.Pet3502.Get3502Response)

# @@protoc_insertion_point(module_scope)