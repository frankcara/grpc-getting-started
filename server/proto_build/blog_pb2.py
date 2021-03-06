# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blog.proto',
  package='blog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nblog.proto\x12\x04\x62log\" \n\rGetOneRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\"L\n\x0eGetOneResponse\x12\x1c\n\x04post\x18\x01 \x01(\x0b\x32\x0e.blog.BlogPost\x12\x1c\n\x06\x61uthor\x18\x02 \x01(\x0b\x32\x0c.blog.Author\"M\n\x08\x42logPost\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\"/\n\x06\x41uthor\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t2F\n\x0f\x42logPostService\x12\x33\n\x06GetOne\x12\x13.blog.GetOneRequest\x1a\x14.blog.GetOneResponseb\x06proto3'
)




_GETONEREQUEST = _descriptor.Descriptor(
  name='GetOneRequest',
  full_name='blog.GetOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='post_id', full_name='blog.GetOneRequest.post_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=52,
)


_GETONERESPONSE = _descriptor.Descriptor(
  name='GetOneResponse',
  full_name='blog.GetOneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='post', full_name='blog.GetOneResponse.post', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='blog.GetOneResponse.author', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=130,
)


_BLOGPOST = _descriptor.Descriptor(
  name='BlogPost',
  full_name='blog.BlogPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='blog.BlogPost.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='blog.BlogPost.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='blog.BlogPost.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='blog.BlogPost.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=132,
  serialized_end=209,
)


_AUTHOR = _descriptor.Descriptor(
  name='Author',
  full_name='blog.Author',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='blog.Author.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='blog.Author.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=258,
)

_GETONERESPONSE.fields_by_name['post'].message_type = _BLOGPOST
_GETONERESPONSE.fields_by_name['author'].message_type = _AUTHOR
DESCRIPTOR.message_types_by_name['GetOneRequest'] = _GETONEREQUEST
DESCRIPTOR.message_types_by_name['GetOneResponse'] = _GETONERESPONSE
DESCRIPTOR.message_types_by_name['BlogPost'] = _BLOGPOST
DESCRIPTOR.message_types_by_name['Author'] = _AUTHOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOneRequest = _reflection.GeneratedProtocolMessageType('GetOneRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETONEREQUEST,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetOneRequest)
  })
_sym_db.RegisterMessage(GetOneRequest)

GetOneResponse = _reflection.GeneratedProtocolMessageType('GetOneResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETONERESPONSE,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.GetOneResponse)
  })
_sym_db.RegisterMessage(GetOneResponse)

BlogPost = _reflection.GeneratedProtocolMessageType('BlogPost', (_message.Message,), {
  'DESCRIPTOR' : _BLOGPOST,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.BlogPost)
  })
_sym_db.RegisterMessage(BlogPost)

Author = _reflection.GeneratedProtocolMessageType('Author', (_message.Message,), {
  'DESCRIPTOR' : _AUTHOR,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Author)
  })
_sym_db.RegisterMessage(Author)



_BLOGPOSTSERVICE = _descriptor.ServiceDescriptor(
  name='BlogPostService',
  full_name='blog.BlogPostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=260,
  serialized_end=330,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOne',
    full_name='blog.BlogPostService.GetOne',
    index=0,
    containing_service=None,
    input_type=_GETONEREQUEST,
    output_type=_GETONERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BLOGPOSTSERVICE)

DESCRIPTOR.services_by_name['BlogPostService'] = _BLOGPOSTSERVICE

# @@protoc_insertion_point(module_scope)
