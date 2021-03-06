# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/defence/GetRewardList2401.proto',
  package='protoFile.defence.GetRewardList2401',
  serialized_pb='\n)protoFile/defence/GetRewardList2401.proto\x12#protoFile.defence.GetRewardList2401\"0\n\x14GetRewardListRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04page\x18\x02 \x02(\x05\"\x85\x01\n\x15GetRewardListResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12K\n\x0erewardListInfo\x18\x03 \x01(\x0b\x32\x33.protoFile.defence.GetRewardList2401.RewardListInfo\"w\n\x0eRewardListInfo\x12\x0f\n\x07\x63urPage\x18\x01 \x01(\x05\x12\x0f\n\x07maxPage\x18\x02 \x01(\x05\x12\x43\n\nrewardInfo\x18\x03 \x03(\x0b\x32/.protoFile.defence.GetRewardList2401.RewardInfo\"r\n\nRewardInfo\x12\x0c\n\x04r_id\x18\x01 \x01(\x05\x12\x0e\n\x06r_type\x18\x02 \x01(\x05\x12\x0e\n\x06t_name\x18\x03 \x01(\t\x12\x0c\n\x04t_e1\x18\x04 \x01(\t\x12\x0c\n\x04t_e2\x18\x05 \x01(\t\x12\x0c\n\x04t_e3\x18\x06 \x01(\t\x12\x0c\n\x04t_e4\x18\x07 \x01(\x08')




_GETREWARDLISTREQUEST = descriptor.Descriptor(
  name='GetRewardListRequest',
  full_name='protoFile.defence.GetRewardList2401.GetRewardListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.defence.GetRewardList2401.GetRewardListRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page', full_name='protoFile.defence.GetRewardList2401.GetRewardListRequest.page', index=1,
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
  serialized_start=82,
  serialized_end=130,
)


_GETREWARDLISTRESPONSE = descriptor.Descriptor(
  name='GetRewardListResponse',
  full_name='protoFile.defence.GetRewardList2401.GetRewardListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.defence.GetRewardList2401.GetRewardListResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.defence.GetRewardList2401.GetRewardListResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rewardListInfo', full_name='protoFile.defence.GetRewardList2401.GetRewardListResponse.rewardListInfo', index=2,
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
  serialized_start=133,
  serialized_end=266,
)


_REWARDLISTINFO = descriptor.Descriptor(
  name='RewardListInfo',
  full_name='protoFile.defence.GetRewardList2401.RewardListInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='curPage', full_name='protoFile.defence.GetRewardList2401.RewardListInfo.curPage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxPage', full_name='protoFile.defence.GetRewardList2401.RewardListInfo.maxPage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rewardInfo', full_name='protoFile.defence.GetRewardList2401.RewardListInfo.rewardInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=387,
)


_REWARDINFO = descriptor.Descriptor(
  name='RewardInfo',
  full_name='protoFile.defence.GetRewardList2401.RewardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='r_id', full_name='protoFile.defence.GetRewardList2401.RewardInfo.r_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r_type', full_name='protoFile.defence.GetRewardList2401.RewardInfo.r_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_name', full_name='protoFile.defence.GetRewardList2401.RewardInfo.t_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_e1', full_name='protoFile.defence.GetRewardList2401.RewardInfo.t_e1', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_e2', full_name='protoFile.defence.GetRewardList2401.RewardInfo.t_e2', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_e3', full_name='protoFile.defence.GetRewardList2401.RewardInfo.t_e3', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_e4', full_name='protoFile.defence.GetRewardList2401.RewardInfo.t_e4', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=389,
  serialized_end=503,
)

_GETREWARDLISTRESPONSE.fields_by_name['rewardListInfo'].message_type = _REWARDLISTINFO
_REWARDLISTINFO.fields_by_name['rewardInfo'].message_type = _REWARDINFO
DESCRIPTOR.message_types_by_name['GetRewardListRequest'] = _GETREWARDLISTREQUEST
DESCRIPTOR.message_types_by_name['GetRewardListResponse'] = _GETREWARDLISTRESPONSE
DESCRIPTOR.message_types_by_name['RewardListInfo'] = _REWARDLISTINFO
DESCRIPTOR.message_types_by_name['RewardInfo'] = _REWARDINFO

class GetRewardListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETREWARDLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.defence.GetRewardList2401.GetRewardListRequest)

class GetRewardListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETREWARDLISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.defence.GetRewardList2401.GetRewardListResponse)

class RewardListInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REWARDLISTINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.defence.GetRewardList2401.RewardListInfo)

class RewardInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REWARDINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.defence.GetRewardList2401.RewardInfo)

# @@protoc_insertion_point(module_scope)
