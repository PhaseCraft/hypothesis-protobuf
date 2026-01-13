from . import im_pb2 as _im_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DepEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZERO: _ClassVar[DepEnum]
    ONE: _ClassVar[DepEnum]
    TWO: _ClassVar[DepEnum]
ZERO: DepEnum
ONE: DepEnum
TWO: DepEnum

class DepMessage(_message.Message):
    __slots__ = ("en", "user")
    EN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    en: DepEnum
    user: _im_pb2.User
    def __init__(self, en: _Optional[_Union[DepEnum, str]] = ..., user: _Optional[_Union[_im_pb2.User, _Mapping]] = ...) -> None: ...
