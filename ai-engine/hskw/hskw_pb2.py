# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hskw/hskw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fhskw/hskw.proto";\n\x0fGenerateCaption\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t"?\n\x16GenerateQuestionAnswer\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t">\n\x15\x43reatedCaptionRequest\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t"\x18\n\x16\x43reatedCaptionResponse"\'\n\x03QNA\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\t"B\n\x16\x43reatedQuestionRequest\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\x05\x12\x12\n\x04qnas\x18\x02 \x03(\x0b\x32\x04.QNA"\x19\n\x17\x43reatedQuestionResponse2\x95\x01\n\x06Snappy\x12\x43\n\x0e\x43reatedCaption\x12\x16.CreatedCaptionRequest\x1a\x17.CreatedCaptionResponse"\x00\x12\x46\n\x0f\x43reatedQuestion\x12\x17.CreatedQuestionRequest\x1a\x18.CreatedQuestionResponse"\x00\x42\x1bZ\x19senkawa.moe/haa-chan/hskwb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "hskw.hskw_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\031senkawa.moe/haa-chan/hskw"
    _GENERATECAPTION._serialized_start = 19
    _GENERATECAPTION._serialized_end = 78
    _GENERATEQUESTIONANSWER._serialized_start = 80
    _GENERATEQUESTIONANSWER._serialized_end = 143
    _CREATEDCAPTIONREQUEST._serialized_start = 145
    _CREATEDCAPTIONREQUEST._serialized_end = 207
    _CREATEDCAPTIONRESPONSE._serialized_start = 209
    _CREATEDCAPTIONRESPONSE._serialized_end = 233
    _QNA._serialized_start = 235
    _QNA._serialized_end = 274
    _CREATEDQUESTIONREQUEST._serialized_start = 276
    _CREATEDQUESTIONREQUEST._serialized_end = 342
    _CREATEDQUESTIONRESPONSE._serialized_start = 344
    _CREATEDQUESTIONRESPONSE._serialized_end = 369
    _SNAPPY._serialized_start = 372
    _SNAPPY._serialized_end = 521
# @@protoc_insertion_point(module_scope)
