# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensors_to_audio_calculator.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>mediapipe/calculators/tensor/tensors_to_audio_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xbd\x03\n\x1fTensorsToAudioCalculatorOptions\x12\x10\n\x08\x66\x66t_size\x18\x01 \x01(\x03\x12\x13\n\x0bnum_samples\x18\x02 \x01(\x03\x12\"\n\x17num_overlapping_samples\x18\x03 \x01(\x03:\x01\x30\x12\x63\n\x11\x64\x66t_tensor_format\x18\x0b \x01(\x0e\x32:.mediapipe.TensorsToAudioCalculatorOptions.DftTensorFormat:\x0cWITH_NYQUIST\x12\x16\n\x0evolume_gain_db\x18\x0c \x01(\x01\"w\n\x0f\x44\x66tTensorFormat\x12\x1d\n\x19\x44\x46T_TENSOR_FORMAT_UNKNOWN\x10\x00\x12\x1a\n\x16WITHOUT_DC_AND_NYQUIST\x10\x01\x12\x10\n\x0cWITH_NYQUIST\x10\x02\x12\x17\n\x13WITH_DC_AND_NYQUIST\x10\x03\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb0\x93\xf7\xe6\x01 \x01(\x0b\x32*.mediapipe.TensorsToAudioCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.tensor.tensors_to_audio_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TENSORSTOAUDIOCALCULATOROPTIONS']._serialized_start=116
  _globals['_TENSORSTOAUDIOCALCULATOROPTIONS']._serialized_end=561
  _globals['_TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT']._serialized_start=351
  _globals['_TENSORSTOAUDIOCALCULATOROPTIONS_DFTTENSORFORMAT']._serialized_end=470
# @@protoc_insertion_point(module_scope)
