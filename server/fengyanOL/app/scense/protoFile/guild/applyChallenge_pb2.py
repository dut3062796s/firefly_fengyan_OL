# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/applyChallenge.proto',
  package='protoFile.guild.applyChallenge',
  serialized_pb='\n$protoFile/guild/applyChallenge.proto\x12\x1eprotoFile.guild.applyChallenge\"8\n\x15\x61pplyChallengeRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x13\n\x0b\x65\x61\x63hGuildId\x18\x02 \x02(\x05\"9\n\x16\x61pplyChallengeResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_APPLYCHALLENGEREQUEST = descriptor.Descriptor(
  name='applyChallengeRequest',
  full_name='protoFile.guild.applyChallenge.applyChallengeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.applyChallenge.applyChallengeRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='eachGuildId', full_name='protoFile.guild.applyChallenge.applyChallengeRequest.eachGuildId', index=1,
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
  serialized_start=72,
  serialized_end=128,
)


_APPLYCHALLENGERESPONSE = descriptor.Descriptor(
  name='applyChallengeResponse',
  full_name='protoFile.guild.applyChallenge.applyChallengeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.applyChallenge.applyChallengeResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.applyChallenge.applyChallengeResponse.message', index=1,
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
  serialized_start=130,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['applyChallengeRequest'] = _APPLYCHALLENGEREQUEST
DESCRIPTOR.message_types_by_name['applyChallengeResponse'] = _APPLYCHALLENGERESPONSE

class applyChallengeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPLYCHALLENGEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.applyChallenge.applyChallengeRequest)

class applyChallengeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPLYCHALLENGERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.applyChallenge.applyChallengeResponse)

# @@protoc_insertion_point(module_scope)