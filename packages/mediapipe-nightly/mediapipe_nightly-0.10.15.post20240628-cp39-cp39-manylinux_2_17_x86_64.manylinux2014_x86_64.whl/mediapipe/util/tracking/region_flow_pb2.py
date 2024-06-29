# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/region_flow.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)mediapipe/util/tracking/region_flow.proto\x12\tmediapipe\"\x1f\n\x0fPatchDescriptor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\'\n\x17\x42inaryFeatureDescriptor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"D\n\x15TemporalIRLSSmoothing\x12\x15\n\nweight_sum\x18\x01 \x01(\x02:\x01\x30\x12\x14\n\tvalue_sum\x18\x02 \x01(\x02:\x01\x30\"\x99\x04\n\x11RegionFlowFeature\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\r\n\x02\x64x\x18\x03 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x04 \x01(\x02:\x01\x30\x12\x14\n\x08track_id\x18\r \x01(\x05:\x02-1\x12\x19\n\x0etracking_error\x18\x05 \x01(\x02:\x01\x30\x12\x16\n\x0birls_weight\x18\x06 \x01(\x02:\x01\x31\x12\x1a\n\x0f\x63orner_response\x18\x0b \x01(\x02:\x01\x30\x12\x36\n\x12\x66\x65\x61ture_descriptor\x18\x07 \x01(\x0b\x32\x1a.mediapipe.PatchDescriptor\x12<\n\x18\x66\x65\x61ture_match_descriptor\x18\x08 \x01(\x0b\x32\x1a.mediapipe.PatchDescriptor\x12\x37\n\rinternal_irls\x18\n \x01(\x0b\x32 .mediapipe.TemporalIRLSSmoothing\x12\r\n\x05label\x18\x0e \x01(\t\x12\r\n\x05\x66lags\x18\x0f \x01(\x05\x12\x12\n\nfeature_id\x18\x10 \x01(\x05\x12\x11\n\x06octave\x18\x11 \x01(\x05:\x01\x30\x12\x45\n\x19\x62inary_feature_descriptor\x18\x12 \x01(\x0b\x32\".mediapipe.BinaryFeatureDescriptor\"\x1e\n\x05\x46lags\x12\x15\n\x11\x46LAG_BROKEN_TRACK\x10\x01*\x04\x08\t\x10\n*\x04\x08\x0c\x10\r\"\xbd\x04\n\x0fRegionFlowFrame\x12:\n\x0bregion_flow\x18\x01 \x03(\x0b\x32%.mediapipe.RegionFlowFrame.RegionFlow\x12\x1d\n\x12num_total_features\x18\x02 \x01(\x05:\x01\x30\x12\x1d\n\x0eunstable_frame\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x12\n\nblur_score\x18\x07 \x01(\x02\x12\x13\n\x0b\x66rame_width\x18\x08 \x01(\x05\x12\x14\n\x0c\x66rame_height\x18\t \x01(\x05\x12\x44\n\x10\x62lock_descriptor\x18\n \x01(\x0b\x32*.mediapipe.RegionFlowFrame.BlockDescriptor\x1a\xa8\x01\n\nRegionFlow\x12\x11\n\tregion_id\x18\x01 \x02(\x05\x12\x15\n\ncentroid_x\x18\x02 \x01(\x02:\x01\x30\x12\x15\n\ncentroid_y\x18\x03 \x01(\x02:\x01\x30\x12\x11\n\x06\x66low_x\x18\x04 \x01(\x02:\x01\x30\x12\x11\n\x06\x66low_y\x18\x05 \x01(\x02:\x01\x30\x12-\n\x07\x66\x65\x61ture\x18\x07 \x03(\x0b\x32\x1c.mediapipe.RegionFlowFeature*\x04\x08\x06\x10\x07\x1an\n\x0f\x42lockDescriptor\x12\x13\n\x0b\x62lock_width\x18\x01 \x01(\x05\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x05\x12\x17\n\x0cnum_blocks_x\x18\x03 \x01(\x05:\x01\x30\x12\x17\n\x0cnum_blocks_y\x18\x04 \x01(\x05:\x01\x30*\x04\x08\x03\x10\x04*\x04\x08\x05\x10\x06*\x04\x08\x06\x10\x07\"\x9c\x03\n\x15RegionFlowFeatureList\x12-\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x1c.mediapipe.RegionFlowFeature\x12\x13\n\x0b\x66rame_width\x18\x02 \x01(\x05\x12\x14\n\x0c\x66rame_height\x18\x03 \x01(\x05\x12\x17\n\x08unstable\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x14\x64istance_from_border\x18\x05 \x01(\x05:\x01\x30\x12\x12\n\nblur_score\x18\x06 \x01(\x02\x12\x1a\n\x0blong_tracks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12&\n\x1b\x66rac_long_features_rejected\x18\x08 \x01(\x02:\x01\x30\x12\x1e\n\x12visual_consistency\x18\t \x01(\x02:\x02-1\x12\x19\n\x0etimestamp_usec\x18\n \x01(\x03:\x01\x30\x12\x16\n\x0bmatch_frame\x18\x0b \x01(\x05:\x01\x30\x12\x1c\n\ris_duplicated\x18\x0c \x01(\x08:\x05\x66\x61lse\x12&\n\x1e\x61\x63tively_discarded_tracked_ids\x18\r \x03(\x05\"\x80\x03\n\x0cSalientPoint\x12\x17\n\x0cnorm_point_x\x18\x01 \x01(\x02:\x01\x30\x12\x17\n\x0cnorm_point_y\x18\x02 \x01(\x02:\x01\x30\x12\x44\n\x04type\x18\x0b \x01(\x0e\x32(.mediapipe.SalientPoint.SalientPointType:\x0cTYPE_INCLUDE\x12\x11\n\x04left\x18\x03 \x01(\x02:\x03\x30.3\x12\x13\n\x06\x62ottom\x18\x04 \x01(\x02:\x03\x30.3\x12\x12\n\x05right\x18\t \x01(\x02:\x03\x30.3\x12\x10\n\x03top\x18\n \x01(\x02:\x03\x30.3\x12\x12\n\x06weight\x18\x05 \x01(\x02:\x02\x31\x35\x12\x12\n\nnorm_major\x18\x06 \x01(\x02\x12\x12\n\nnorm_minor\x18\x07 \x01(\x02\x12\r\n\x05\x61ngle\x18\x08 \x01(\x02\"S\n\x10SalientPointType\x12\x10\n\x0cTYPE_INCLUDE\x10\x01\x12\x15\n\x11TYPE_EXCLUDE_LEFT\x10\x02\x12\x16\n\x12TYPE_EXCLUDE_RIGHT\x10\x03*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"G\n\x11SalientPointFrame\x12&\n\x05point\x18\x01 \x03(\x0b\x32\x17.mediapipe.SalientPoint*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\x42!\n\x1d\x63om.google.mediapipe.trackingP\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.util.tracking.region_flow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.google.mediapipe.trackingP\001'
  _globals['_PATCHDESCRIPTOR']._serialized_start=56
  _globals['_PATCHDESCRIPTOR']._serialized_end=87
  _globals['_BINARYFEATUREDESCRIPTOR']._serialized_start=89
  _globals['_BINARYFEATUREDESCRIPTOR']._serialized_end=128
  _globals['_TEMPORALIRLSSMOOTHING']._serialized_start=130
  _globals['_TEMPORALIRLSSMOOTHING']._serialized_end=198
  _globals['_REGIONFLOWFEATURE']._serialized_start=201
  _globals['_REGIONFLOWFEATURE']._serialized_end=738
  _globals['_REGIONFLOWFEATURE_FLAGS']._serialized_start=696
  _globals['_REGIONFLOWFEATURE_FLAGS']._serialized_end=726
  _globals['_REGIONFLOWFRAME']._serialized_start=741
  _globals['_REGIONFLOWFRAME']._serialized_end=1314
  _globals['_REGIONFLOWFRAME_REGIONFLOW']._serialized_start=1016
  _globals['_REGIONFLOWFRAME_REGIONFLOW']._serialized_end=1184
  _globals['_REGIONFLOWFRAME_BLOCKDESCRIPTOR']._serialized_start=1186
  _globals['_REGIONFLOWFRAME_BLOCKDESCRIPTOR']._serialized_end=1296
  _globals['_REGIONFLOWFEATURELIST']._serialized_start=1317
  _globals['_REGIONFLOWFEATURELIST']._serialized_end=1729
  _globals['_SALIENTPOINT']._serialized_start=1732
  _globals['_SALIENTPOINT']._serialized_end=2116
  _globals['_SALIENTPOINT_SALIENTPOINTTYPE']._serialized_start=2021
  _globals['_SALIENTPOINT_SALIENTPOINTTYPE']._serialized_end=2104
  _globals['_SALIENTPOINTFRAME']._serialized_start=2118
  _globals['_SALIENTPOINTFRAME']._serialized_end=2189
# @@protoc_insertion_point(module_scope)
