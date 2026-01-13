from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sfixed(_message.Message):
    __slots__ = ("sfixed32", "sfixed64")
    SFIXED32_FIELD_NUMBER: _ClassVar[int]
    SFIXED64_FIELD_NUMBER: _ClassVar[int]
    sfixed32: int
    sfixed64: int
    def __init__(self, sfixed32: _Optional[int] = ..., sfixed64: _Optional[int] = ...) -> None: ...
