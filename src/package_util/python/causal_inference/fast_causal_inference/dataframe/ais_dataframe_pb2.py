# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ais_dataframe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13\x61is_dataframe.proto"3\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t"&\n\x05Limit\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03"8\n\x10\x43lickHouseSource\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t"7\n\x0fStarRocksSource\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t"o\n\x06Source\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.SourceType\x12%\n\nclickhouse\x18\x02 \x01(\x0b\x32\x11.ClickHouseSource\x12#\n\tstarrocks\x18\x03 \x01(\x0b\x32\x10.StarRocksSource".\n\x05Order\x12\x17\n\x06\x63olumn\x18\x01 \x01(\x0b\x32\x07.Column\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08"\xcd\x01\n\tDataFrame\x12\x18\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x07.Column\x12\x0f\n\x07\x66ilters\x18\x02 \x03(\t\x12\x19\n\x08group_by\x18\x03 \x03(\x0b\x32\x07.Column\x12\x18\n\x08order_by\x18\x04 \x03(\x0b\x32\x06.Order\x12\x15\n\x05limit\x18\x05 \x01(\x0b\x32\x06.Limit\x12\x17\n\x06source\x18\x06 \x01(\x0b\x32\x07.Source\x12\x0e\n\x06result\x18\x07 \x01(\t\x12\x13\n\x0b\x65xecute_sql\x18\x08 \x01(\t\x12\x0b\n\x03\x63te\x18\t \x01(\t"z\n\x10\x44\x61taFrameRequest\x12\x16\n\x02\x64\x66\x18\x01 \x01(\x0b\x32\n.DataFrame\x12\x1c\n\ttask_type\x18\x02 \x01(\x0e\x32\t.TaskType\x12\x0b\n\x03rtx\x18\x03 \x01(\t\x12\x11\n\tdevice_id\x18\x04 \x01(\x05\x12\x10\n\x08\x64\x61tabase\x18\x05 \x01(\t"T\n\x11\x44\x61taFrameResponse\x12\x16\n\x02\x64\x66\x18\x01 \x01(\x0b\x32\n.DataFrame\x12\x1a\n\x06status\x18\x02 \x01(\x0e\x32\n.RetStatus\x12\x0b\n\x03msg\x18\x03 \x01(\t*z\n\nColumnType\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06String\x10\x01\x12\x07\n\x03Int\x10\x02\x12\t\n\x05\x46loat\x10\x03\x12\x08\n\x04\x42ool\x10\x04\x12\x08\n\x04\x44\x61te\x10\x05\x12\x0c\n\x08\x44\x61teTime\x10\x06\x12\x08\n\x04Time\x10\x07\x12\x08\n\x04UUID\x10\x08\x12\t\n\x05\x41rray\x10\t*2\n\x08TaskType\x12\x08\n\x04None\x10\x00\x12\x0f\n\x0b\x46ILL_SCHEMA\x10\x01\x12\x0b\n\x07\x45XECUTE\x10\x02*+\n\nSourceType\x12\x0e\n\nClickHouse\x10\x00\x12\r\n\tStarRocks\x10\x01*\x1f\n\tRetStatus\x12\x08\n\x04SUCC\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "ais_dataframe_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _COLUMNTYPE._serialized_start = 810
    _COLUMNTYPE._serialized_end = 932
    _TASKTYPE._serialized_start = 934
    _TASKTYPE._serialized_end = 984
    _SOURCETYPE._serialized_start = 986
    _SOURCETYPE._serialized_end = 1029
    _RETSTATUS._serialized_start = 1031
    _RETSTATUS._serialized_end = 1062
    _COLUMN._serialized_start = 23
    _COLUMN._serialized_end = 74
    _LIMIT._serialized_start = 76
    _LIMIT._serialized_end = 114
    _CLICKHOUSESOURCE._serialized_start = 116
    _CLICKHOUSESOURCE._serialized_end = 172
    _STARROCKSSOURCE._serialized_start = 174
    _STARROCKSSOURCE._serialized_end = 229
    _SOURCE._serialized_start = 231
    _SOURCE._serialized_end = 342
    _ORDER._serialized_start = 344
    _ORDER._serialized_end = 390
    _DATAFRAME._serialized_start = 393
    _DATAFRAME._serialized_end = 598
    _DATAFRAMEREQUEST._serialized_start = 600
    _DATAFRAMEREQUEST._serialized_end = 722
    _DATAFRAMERESPONSE._serialized_start = 724
    _DATAFRAMERESPONSE._serialized_end = 808
# @@protoc_insertion_point(module_scope)