# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/consignment/RevokeCommission1205.proto',
  package='protoFile.consignment.RevokeCommission1205',
  serialized_pb='\n0protoFile/consignment/RevokeCommission1205.proto\x12*protoFile.consignment.RevokeCommission1205\"G\n\x17RevokeCommissionRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x12\n\nitemConsId\x18\x02 \x02(\x05\x12\x0c\n\x04type\x18\x03 \x02(\x05\";\n\x18RevokeCommissionResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_REVOKECOMMISSIONREQUEST = descriptor.Descriptor(
  name='RevokeCommissionRequest',
  full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemConsId', full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionRequest.itemConsId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionRequest.type', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=96,
  serialized_end=167,
)


_REVOKECOMMISSIONRESPONSE = descriptor.Descriptor(
  name='RevokeCommissionResponse',
  full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.consignment.RevokeCommission1205.RevokeCommissionResponse.message', index=1,
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
  serialized_start=169,
  serialized_end=228,
)

DESCRIPTOR.message_types_by_name['RevokeCommissionRequest'] = _REVOKECOMMISSIONREQUEST
DESCRIPTOR.message_types_by_name['RevokeCommissionResponse'] = _REVOKECOMMISSIONRESPONSE

class RevokeCommissionRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REVOKECOMMISSIONREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.consignment.RevokeCommission1205.RevokeCommissionRequest)

class RevokeCommissionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REVOKECOMMISSIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.consignment.RevokeCommission1205.RevokeCommissionResponse)

# @@protoc_insertion_point(module_scope)
