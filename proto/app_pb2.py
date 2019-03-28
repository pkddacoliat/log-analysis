# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='loganalysis',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tapp.proto\x12\x0bloganalysis\" \n\x11\x41nalyseLogRequest\x12\x0b\n\x03log\x18\x01 \x01(\t\"L\n\x10\x41nalyseLogResult\x12\x15\n\ripBlacklisted\x18\x01 \x01(\x08\x12\x14\n\x0ctimeAnalysed\x18\x02 \x01(\t\x12\x0b\n\x03log\x18\x03 \x01(\t\"E\n\x10StoreAlertResult\x12\x0e\n\x06stored\x18\x01 \x01(\x08\x12\x14\n\x0ctimeAnalysed\x18\x02 \x01(\t\x12\x0b\n\x03log\x18\x03 \x01(\t\"\x1f\n\x0fSendEmailResult\x12\x0c\n\x04sent\x18\x01 \x01(\x08\x32\xf6\x01\n\x0bLogAnalysis\x12M\n\nAnalyseLog\x12\x1e.loganalysis.AnalyseLogRequest\x1a\x1d.loganalysis.AnalyseLogResult\"\x00\x12L\n\nStoreAlert\x12\x1d.loganalysis.AnalyseLogResult\x1a\x1d.loganalysis.StoreAlertResult\"\x00\x12J\n\tSendEmail\x12\x1d.loganalysis.StoreAlertResult\x1a\x1c.loganalysis.SendEmailResult\"\x00\x62\x06proto3')
)




_ANALYSELOGREQUEST = _descriptor.Descriptor(
  name='AnalyseLogRequest',
  full_name='loganalysis.AnalyseLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='loganalysis.AnalyseLogRequest.log', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=58,
)


_ANALYSELOGRESULT = _descriptor.Descriptor(
  name='AnalyseLogResult',
  full_name='loganalysis.AnalyseLogResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipBlacklisted', full_name='loganalysis.AnalyseLogResult.ipBlacklisted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeAnalysed', full_name='loganalysis.AnalyseLogResult.timeAnalysed', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='loganalysis.AnalyseLogResult.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=136,
)


_STOREALERTRESULT = _descriptor.Descriptor(
  name='StoreAlertResult',
  full_name='loganalysis.StoreAlertResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stored', full_name='loganalysis.StoreAlertResult.stored', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeAnalysed', full_name='loganalysis.StoreAlertResult.timeAnalysed', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='loganalysis.StoreAlertResult.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=207,
)


_SENDEMAILRESULT = _descriptor.Descriptor(
  name='SendEmailResult',
  full_name='loganalysis.SendEmailResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sent', full_name='loganalysis.SendEmailResult.sent', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=240,
)

DESCRIPTOR.message_types_by_name['AnalyseLogRequest'] = _ANALYSELOGREQUEST
DESCRIPTOR.message_types_by_name['AnalyseLogResult'] = _ANALYSELOGRESULT
DESCRIPTOR.message_types_by_name['StoreAlertResult'] = _STOREALERTRESULT
DESCRIPTOR.message_types_by_name['SendEmailResult'] = _SENDEMAILRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyseLogRequest = _reflection.GeneratedProtocolMessageType('AnalyseLogRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSELOGREQUEST,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:loganalysis.AnalyseLogRequest)
  ))
_sym_db.RegisterMessage(AnalyseLogRequest)

AnalyseLogResult = _reflection.GeneratedProtocolMessageType('AnalyseLogResult', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSELOGRESULT,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:loganalysis.AnalyseLogResult)
  ))
_sym_db.RegisterMessage(AnalyseLogResult)

StoreAlertResult = _reflection.GeneratedProtocolMessageType('StoreAlertResult', (_message.Message,), dict(
  DESCRIPTOR = _STOREALERTRESULT,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:loganalysis.StoreAlertResult)
  ))
_sym_db.RegisterMessage(StoreAlertResult)

SendEmailResult = _reflection.GeneratedProtocolMessageType('SendEmailResult', (_message.Message,), dict(
  DESCRIPTOR = _SENDEMAILRESULT,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:loganalysis.SendEmailResult)
  ))
_sym_db.RegisterMessage(SendEmailResult)



_LOGANALYSIS = _descriptor.ServiceDescriptor(
  name='LogAnalysis',
  full_name='loganalysis.LogAnalysis',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=243,
  serialized_end=489,
  methods=[
  _descriptor.MethodDescriptor(
    name='AnalyseLog',
    full_name='loganalysis.LogAnalysis.AnalyseLog',
    index=0,
    containing_service=None,
    input_type=_ANALYSELOGREQUEST,
    output_type=_ANALYSELOGRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StoreAlert',
    full_name='loganalysis.LogAnalysis.StoreAlert',
    index=1,
    containing_service=None,
    input_type=_ANALYSELOGRESULT,
    output_type=_STOREALERTRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendEmail',
    full_name='loganalysis.LogAnalysis.SendEmail',
    index=2,
    containing_service=None,
    input_type=_STOREALERTRESULT,
    output_type=_SENDEMAILRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGANALYSIS)

DESCRIPTOR.services_by_name['LogAnalysis'] = _LOGANALYSIS

# @@protoc_insertion_point(module_scope)
