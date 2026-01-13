from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Loop(_message.Message):
    __slots__ = ("loop",)
    LOOP_FIELD_NUMBER: _ClassVar[int]
    loop: Loop
    def __init__(self, loop: _Optional[_Union[Loop, _Mapping]] = ...) -> None: ...
