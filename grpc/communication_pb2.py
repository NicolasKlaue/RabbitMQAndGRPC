# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ommunication.proto\x12\rcommunication\"$\n\x0fJsonDataRequest\x12\x11\n\tjson_data\x18\x01 \x01(\t\"\"\n\x10JsonDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2g\n\x14\x43ommunicationService\x12O\n\x0cSendJsonData\x12\x1e.communication.JsonDataRequest\x1a\x1f.communication.JsonDataResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'communication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_JSONDATAREQUEST']._serialized_start=38
  _globals['_JSONDATAREQUEST']._serialized_end=74
  _globals['_JSONDATARESPONSE']._serialized_start=76
  _globals['_JSONDATARESPONSE']._serialized_end=110
  _globals['_COMMUNICATIONSERVICE']._serialized_start=112
  _globals['_COMMUNICATIONSERVICE']._serialized_end=215
# @@protoc_insertion_point(module_scope)