from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_UNKNOWN: _ClassVar[Client]
    CLIENT_NATIVE_APP: _ClassVar[Client]
    CLIENT_WEB_APP: _ClassVar[Client]
    CLIENT_API: _ClassVar[Client]
CLIENT_UNKNOWN: Client
CLIENT_NATIVE_APP: Client
CLIENT_WEB_APP: Client
CLIENT_API: Client

class InstantMessage(_message.Message):
    __slots__ = ("timestamp", "nested1", "sender_ip", "sender", "recipient", "message", "image_attachments", "metadata")
    class NestedEnum1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN_ZERO: _ClassVar[InstantMessage.NestedEnum1]
        EN_ONE: _ClassVar[InstantMessage.NestedEnum1]
        EN_TWO: _ClassVar[InstantMessage.NestedEnum1]
        EN_THREE: _ClassVar[InstantMessage.NestedEnum1]
    EN_ZERO: InstantMessage.NestedEnum1
    EN_ONE: InstantMessage.NestedEnum1
    EN_TWO: InstantMessage.NestedEnum1
    EN_THREE: InstantMessage.NestedEnum1
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NESTED1_FIELD_NUMBER: _ClassVar[int]
    SENDER_IP_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    nested1: InstantMessage.NestedEnum1
    sender_ip: int
    sender: User
    recipient: User
    message: str
    image_attachments: _containers.RepeatedScalarFieldContainer[bytes]
    metadata: MetaData
    def __init__(self, timestamp: _Optional[int] = ..., nested1: _Optional[_Union[InstantMessage.NestedEnum1, str]] = ..., sender_ip: _Optional[int] = ..., sender: _Optional[_Union[User, _Mapping]] = ..., recipient: _Optional[_Union[User, _Mapping]] = ..., message: _Optional[str] = ..., image_attachments: _Optional[_Iterable[bytes]] = ..., metadata: _Optional[_Union[MetaData, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "screen_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    screen_name: str
    def __init__(self, id: _Optional[int] = ..., screen_name: _Optional[str] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ("nested1", "latency", "inner_data")
    class NestedEnum1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN_ZERO: _ClassVar[MetaData.NestedEnum1]
        EN_ONE: _ClassVar[MetaData.NestedEnum1]
        EN_TWO: _ClassVar[MetaData.NestedEnum1]
        EN_THREE: _ClassVar[MetaData.NestedEnum1]
    EN_ZERO: MetaData.NestedEnum1
    EN_ONE: MetaData.NestedEnum1
    EN_TWO: MetaData.NestedEnum1
    EN_THREE: MetaData.NestedEnum1
    class InnerData(_message.Message):
        __slots__ = ("nested2", "latency", "nested1")
        class NestedEnum2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EN_ZERO: _ClassVar[MetaData.InnerData.NestedEnum2]
            EN_ONE: _ClassVar[MetaData.InnerData.NestedEnum2]
            EN_TWO: _ClassVar[MetaData.InnerData.NestedEnum2]
            EN_THREE: _ClassVar[MetaData.InnerData.NestedEnum2]
        EN_ZERO: MetaData.InnerData.NestedEnum2
        EN_ONE: MetaData.InnerData.NestedEnum2
        EN_TWO: MetaData.InnerData.NestedEnum2
        EN_THREE: MetaData.InnerData.NestedEnum2
        NESTED2_FIELD_NUMBER: _ClassVar[int]
        LATENCY_FIELD_NUMBER: _ClassVar[int]
        NESTED1_FIELD_NUMBER: _ClassVar[int]
        nested2: MetaData.InnerData.NestedEnum2
        latency: float
        nested1: MetaData.NestedEnum1
        def __init__(self, nested2: _Optional[_Union[MetaData.InnerData.NestedEnum2, str]] = ..., latency: _Optional[float] = ..., nested1: _Optional[_Union[MetaData.NestedEnum1, str]] = ...) -> None: ...
    NESTED1_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA_FIELD_NUMBER: _ClassVar[int]
    nested1: MetaData.NestedEnum1
    latency: float
    inner_data: MetaData.InnerData
    def __init__(self, nested1: _Optional[_Union[MetaData.NestedEnum1, str]] = ..., latency: _Optional[float] = ..., inner_data: _Optional[_Union[MetaData.InnerData, _Mapping]] = ...) -> None: ...
