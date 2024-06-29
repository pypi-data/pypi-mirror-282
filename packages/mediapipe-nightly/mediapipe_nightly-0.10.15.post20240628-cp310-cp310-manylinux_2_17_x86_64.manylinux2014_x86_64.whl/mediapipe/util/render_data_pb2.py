# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/render_data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.util import color_pb2 as mediapipe_dot_util_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n mediapipe/util/render_data.proto\x12\tmediapipe\x1a\x1amediapipe/util/color.proto\"\x8d\x01\n\nRenderData\x12\x37\n\x12render_annotations\x18\x01 \x03(\x0b\x32\x1b.mediapipe.RenderAnnotation\x12\x13\n\x0bscene_class\x18\x02 \x01(\t\x12\x31\n\x0escene_viewport\x18\x03 \x01(\x0b\x32\x19.mediapipe.RenderViewport\"\xf2\x12\n\x10RenderAnnotation\x12:\n\trectangle\x18\x01 \x01(\x0b\x32%.mediapipe.RenderAnnotation.RectangleH\x00\x12G\n\x10\x66illed_rectangle\x18\x02 \x01(\x0b\x32+.mediapipe.RenderAnnotation.FilledRectangleH\x00\x12\x30\n\x04oval\x18\x03 \x01(\x0b\x32 .mediapipe.RenderAnnotation.OvalH\x00\x12=\n\x0b\x66illed_oval\x18\x04 \x01(\x0b\x32&.mediapipe.RenderAnnotation.FilledOvalH\x00\x12\x32\n\x05point\x18\x05 \x01(\x0b\x32!.mediapipe.RenderAnnotation.PointH\x00\x12\x30\n\x04line\x18\x06 \x01(\x0b\x32 .mediapipe.RenderAnnotation.LineH\x00\x12\x32\n\x05\x61rrow\x18\x07 \x01(\x0b\x32!.mediapipe.RenderAnnotation.ArrowH\x00\x12\x30\n\x04text\x18\x08 \x01(\x0b\x32 .mediapipe.RenderAnnotation.TextH\x00\x12I\n\x11rounded_rectangle\x18\t \x01(\x0b\x32,.mediapipe.RenderAnnotation.RoundedRectangleH\x00\x12V\n\x18\x66illed_rounded_rectangle\x18\n \x01(\x0b\x32\x32.mediapipe.RenderAnnotation.FilledRoundedRectangleH\x00\x12\x41\n\rgradient_line\x18\x0e \x01(\x0b\x32(.mediapipe.RenderAnnotation.GradientLineH\x00\x12\x38\n\x08scribble\x18\x0f \x01(\x0b\x32$.mediapipe.RenderAnnotation.ScribbleH\x00\x12\x14\n\tthickness\x18\x0b \x01(\x01:\x01\x31\x12\x1f\n\x05\x63olor\x18\x0c \x01(\x0b\x32\x10.mediapipe.Color\x12\x11\n\tscene_tag\x18\r \x01(\t\x1a\x8e\x01\n\tRectangle\x12\x0c\n\x04left\x18\x01 \x01(\x01\x12\x0b\n\x03top\x18\x02 \x01(\x01\x12\r\n\x05right\x18\x03 \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x04 \x01(\x01\x12\x19\n\nnormalized\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x08rotation\x18\x06 \x01(\x01\x12\x1a\n\x12top_left_thickness\x18\x07 \x01(\x01\x1aq\n\x0f\x46illedRectangle\x12\x38\n\trectangle\x18\x01 \x01(\x0b\x32%.mediapipe.RenderAnnotation.Rectangle\x12$\n\nfill_color\x18\x02 \x01(\x0b\x32\x10.mediapipe.Color\x1a|\n\x10RoundedRectangle\x12\x38\n\trectangle\x18\x01 \x01(\x0b\x32%.mediapipe.RenderAnnotation.Rectangle\x12\x18\n\rcorner_radius\x18\x02 \x01(\x05:\x01\x30\x12\x14\n\tline_type\x18\x03 \x01(\x05:\x01\x34\x1a\x87\x01\n\x16\x46illedRoundedRectangle\x12G\n\x11rounded_rectangle\x18\x01 \x01(\x0b\x32,.mediapipe.RenderAnnotation.RoundedRectangle\x12$\n\nfill_color\x18\x02 \x01(\x0b\x32\x10.mediapipe.Color\x1a@\n\x04Oval\x12\x38\n\trectangle\x18\x01 \x01(\x0b\x32%.mediapipe.RenderAnnotation.Rectangle\x1a\x62\n\nFilledOval\x12.\n\x04oval\x18\x01 \x01(\x0b\x32 .mediapipe.RenderAnnotation.Oval\x12$\n\nfill_color\x18\x02 \x01(\x0b\x32\x10.mediapipe.Color\x1a\x38\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x19\n\nnormalized\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a\xd6\x01\n\x04Line\x12\x0f\n\x07x_start\x18\x01 \x01(\x01\x12\x0f\n\x07y_start\x18\x02 \x01(\x01\x12\r\n\x05x_end\x18\x03 \x01(\x01\x12\r\n\x05y_end\x18\x04 \x01(\x01\x12\x19\n\nnormalized\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x43\n\tline_type\x18\x06 \x01(\x0e\x32).mediapipe.RenderAnnotation.Line.LineType:\x05SOLID\".\n\x08LineType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SOLID\x10\x01\x12\n\n\x06\x44\x41SHED\x10\x02\x1a\xad\x01\n\x0cGradientLine\x12\x0f\n\x07x_start\x18\x01 \x01(\x01\x12\x0f\n\x07y_start\x18\x02 \x01(\x01\x12\r\n\x05x_end\x18\x03 \x01(\x01\x12\r\n\x05y_end\x18\x04 \x01(\x01\x12\x19\n\nnormalized\x18\x05 \x01(\x08:\x05\x66\x61lse\x12 \n\x06\x63olor1\x18\x06 \x01(\x0b\x32\x10.mediapipe.Color\x12 \n\x06\x63olor2\x18\x07 \x01(\x0b\x32\x10.mediapipe.Color\x1a<\n\x08Scribble\x12\x30\n\x05point\x18\x01 \x03(\x0b\x32!.mediapipe.RenderAnnotation.Point\x1a\x62\n\x05\x41rrow\x12\x0f\n\x07x_start\x18\x01 \x01(\x01\x12\x0f\n\x07y_start\x18\x02 \x01(\x01\x12\r\n\x05x_end\x18\x03 \x01(\x01\x12\r\n\x05y_end\x18\x04 \x01(\x01\x12\x19\n\nnormalized\x18\x05 \x01(\x08:\x05\x66\x61lse\x1a\x92\x02\n\x04Text\x12\x14\n\x0c\x64isplay_text\x18\x01 \x01(\t\x12\x0c\n\x04left\x18\x02 \x01(\x01\x12\x10\n\x08\x62\x61seline\x18\x03 \x01(\x01\x12\x16\n\x0b\x66ont_height\x18\x04 \x01(\x01:\x01\x38\x12\x19\n\nnormalized\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x14\n\tfont_face\x18\x06 \x01(\x05:\x01\x30\x12\"\n\x13\x63\x65nter_horizontally\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x63\x65nter_vertically\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x11outline_thickness\x18\x0b \x01(\x01:\x01\x30\x12\'\n\routline_color\x18\x0c \x01(\x0b\x32\x10.mediapipe.ColorB\x06\n\x04\x64\x61ta\"[\n\x0eRenderViewport\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08width_px\x18\x02 \x01(\x05\x12\x11\n\theight_px\x18\x03 \x01(\x05\x12\x18\n\x10\x63ompose_on_video\x18\x04 \x01(\x08\x42\x32\n\x1f\x63om.google.mediapipe.util.protoB\x0fRenderDataProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.util.render_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.google.mediapipe.util.protoB\017RenderDataProto'
  _globals['_RENDERDATA']._serialized_start=76
  _globals['_RENDERDATA']._serialized_end=217
  _globals['_RENDERANNOTATION']._serialized_start=220
  _globals['_RENDERANNOTATION']._serialized_end=2638
  _globals['_RENDERANNOTATION_RECTANGLE']._serialized_start=1053
  _globals['_RENDERANNOTATION_RECTANGLE']._serialized_end=1195
  _globals['_RENDERANNOTATION_FILLEDRECTANGLE']._serialized_start=1197
  _globals['_RENDERANNOTATION_FILLEDRECTANGLE']._serialized_end=1310
  _globals['_RENDERANNOTATION_ROUNDEDRECTANGLE']._serialized_start=1312
  _globals['_RENDERANNOTATION_ROUNDEDRECTANGLE']._serialized_end=1436
  _globals['_RENDERANNOTATION_FILLEDROUNDEDRECTANGLE']._serialized_start=1439
  _globals['_RENDERANNOTATION_FILLEDROUNDEDRECTANGLE']._serialized_end=1574
  _globals['_RENDERANNOTATION_OVAL']._serialized_start=1576
  _globals['_RENDERANNOTATION_OVAL']._serialized_end=1640
  _globals['_RENDERANNOTATION_FILLEDOVAL']._serialized_start=1642
  _globals['_RENDERANNOTATION_FILLEDOVAL']._serialized_end=1740
  _globals['_RENDERANNOTATION_POINT']._serialized_start=1742
  _globals['_RENDERANNOTATION_POINT']._serialized_end=1798
  _globals['_RENDERANNOTATION_LINE']._serialized_start=1801
  _globals['_RENDERANNOTATION_LINE']._serialized_end=2015
  _globals['_RENDERANNOTATION_LINE_LINETYPE']._serialized_start=1969
  _globals['_RENDERANNOTATION_LINE_LINETYPE']._serialized_end=2015
  _globals['_RENDERANNOTATION_GRADIENTLINE']._serialized_start=2018
  _globals['_RENDERANNOTATION_GRADIENTLINE']._serialized_end=2191
  _globals['_RENDERANNOTATION_SCRIBBLE']._serialized_start=2193
  _globals['_RENDERANNOTATION_SCRIBBLE']._serialized_end=2253
  _globals['_RENDERANNOTATION_ARROW']._serialized_start=2255
  _globals['_RENDERANNOTATION_ARROW']._serialized_end=2353
  _globals['_RENDERANNOTATION_TEXT']._serialized_start=2356
  _globals['_RENDERANNOTATION_TEXT']._serialized_end=2630
  _globals['_RENDERVIEWPORT']._serialized_start=2640
  _globals['_RENDERVIEWPORT']._serialized_end=2731
# @@protoc_insertion_point(module_scope)
