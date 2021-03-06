# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/petInfo.proto',
  package='protoFile',
  serialized_pb='\n\x17protoFile/petInfo.proto\x12\tprotoFile\"\xee\x04\n\x07PetInfo\x12\r\n\x05petId\x18\x01 \x01(\x05\x12\x10\n\x08resPetId\x18\x02 \x01(\x05\x12\x0f\n\x07petName\x18\x03 \x01(\t\x12\x10\n\x08petLevel\x18\x04 \x01(\x05\x12\x14\n\x0cinMatrixFlag\x18\x05 \x01(\x08\x12\x0e\n\x06petDes\x18\x06 \x01(\t\x12\x0e\n\x06\x62\x61seHp\x18\x07 \x01(\x05\x12\x10\n\x08manualHp\x18\x08 \x01(\x05\x12\x15\n\rbasePhyAttack\x18\t \x01(\x05\x12\x17\n\x0fmanualPhyAttack\x18\n \x01(\x05\x12\x17\n\x0f\x62\x61seMagicAttack\x18\x0b \x01(\x05\x12\x19\n\x11manualMagicAttack\x18\x0c \x01(\x05\x12\x16\n\x0e\x62\x61sePhyDefense\x18\r \x01(\x05\x12\x18\n\x10manualPhyDefense\x18\x0e \x01(\x05\x12\x18\n\x10\x62\x61seMagicDefense\x18\x0f \x01(\x05\x12\x1a\n\x12manualMagicDefense\x18\x10 \x01(\x05\x12\x13\n\x0b\x62\x61seHitRate\x18\x11 \x01(\x05\x12\x15\n\rmanualHitRate\x18\x12 \x01(\x05\x12\x15\n\rbaseDodgeRate\x18\x13 \x01(\x05\x12\x17\n\x0fmanualDodgeRate\x18\x14 \x01(\x05\x12\x11\n\tbaseSpeed\x18\x15 \x01(\x05\x12\x13\n\x0bmanualSpeed\x18\x16 \x01(\x05\x12\x14\n\x0c\x62\x61seCritRate\x18\x17 \x01(\x05\x12\x16\n\x0emanualCritRate\x18\x18 \x01(\x05\x12\x0c\n\x04icon\x18\x19 \x01(\x05\x12\x0c\n\x04type\x18\x1a \x01(\x05\x12-\n\x0cpetSkillInfo\x18\x1b \x03(\x0b\x32\x17.protoFile.PetSkillInfo\x12\x0e\n\x06slogan\x18\x1c \x01(\t\"\xb5\x01\n\x0cPetSkillInfo\x12\x19\n\x11hasActivationFlag\x18\x01 \x01(\x08\x12\x12\n\npetSkillId\x18\x02 \x01(\x05\x12\x0c\n\x04icon\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x14\n\x0cpetSkillName\x18\x05 \x01(\t\x12\x15\n\rpetSkillLevel\x18\x06 \x01(\x05\x12\x13\n\x0bpetSkillDes\x18\x07 \x01(\t\x12\x18\n\x10petSkillMaxLevel\x18\x08 \x01(\x05')




_PETINFO = descriptor.Descriptor(
  name='PetInfo',
  full_name='protoFile.PetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='petId', full_name='protoFile.PetInfo.petId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='resPetId', full_name='protoFile.PetInfo.resPetId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petName', full_name='protoFile.PetInfo.petName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petLevel', full_name='protoFile.PetInfo.petLevel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inMatrixFlag', full_name='protoFile.PetInfo.inMatrixFlag', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petDes', full_name='protoFile.PetInfo.petDes', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseHp', full_name='protoFile.PetInfo.baseHp', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualHp', full_name='protoFile.PetInfo.manualHp', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='basePhyAttack', full_name='protoFile.PetInfo.basePhyAttack', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualPhyAttack', full_name='protoFile.PetInfo.manualPhyAttack', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseMagicAttack', full_name='protoFile.PetInfo.baseMagicAttack', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualMagicAttack', full_name='protoFile.PetInfo.manualMagicAttack', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='basePhyDefense', full_name='protoFile.PetInfo.basePhyDefense', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualPhyDefense', full_name='protoFile.PetInfo.manualPhyDefense', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseMagicDefense', full_name='protoFile.PetInfo.baseMagicDefense', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualMagicDefense', full_name='protoFile.PetInfo.manualMagicDefense', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseHitRate', full_name='protoFile.PetInfo.baseHitRate', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualHitRate', full_name='protoFile.PetInfo.manualHitRate', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseDodgeRate', full_name='protoFile.PetInfo.baseDodgeRate', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualDodgeRate', full_name='protoFile.PetInfo.manualDodgeRate', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseSpeed', full_name='protoFile.PetInfo.baseSpeed', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualSpeed', full_name='protoFile.PetInfo.manualSpeed', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseCritRate', full_name='protoFile.PetInfo.baseCritRate', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='manualCritRate', full_name='protoFile.PetInfo.manualCritRate', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.PetInfo.icon', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.PetInfo.type', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillInfo', full_name='protoFile.PetInfo.petSkillInfo', index=26,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slogan', full_name='protoFile.PetInfo.slogan', index=27,
      number=28, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=661,
)


_PETSKILLINFO = descriptor.Descriptor(
  name='PetSkillInfo',
  full_name='protoFile.PetSkillInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hasActivationFlag', full_name='protoFile.PetSkillInfo.hasActivationFlag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillId', full_name='protoFile.PetSkillInfo.petSkillId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.PetSkillInfo.icon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.PetSkillInfo.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillName', full_name='protoFile.PetSkillInfo.petSkillName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillLevel', full_name='protoFile.PetSkillInfo.petSkillLevel', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillDes', full_name='protoFile.PetSkillInfo.petSkillDes', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petSkillMaxLevel', full_name='protoFile.PetSkillInfo.petSkillMaxLevel', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=664,
  serialized_end=845,
)

_PETINFO.fields_by_name['petSkillInfo'].message_type = _PETSKILLINFO
DESCRIPTOR.message_types_by_name['PetInfo'] = _PETINFO
DESCRIPTOR.message_types_by_name['PetSkillInfo'] = _PETSKILLINFO

class PetInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PETINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.PetInfo)

class PetSkillInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PETSKILLINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.PetSkillInfo)

# @@protoc_insertion_point(module_scope)
