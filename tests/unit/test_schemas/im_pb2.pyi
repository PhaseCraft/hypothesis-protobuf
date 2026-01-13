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

class User(_message.Message):
    __slots__ = ("id", "screen_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    screen_name: str
    def __init__(self, id: _Optional[int] = ..., screen_name: _Optional[str] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ("latency", "inner")
    class Inner(_message.Message):
        __slots__ = ("a", "b", "layer")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEAD: _ClassVar[MetaData.Inner.Status]
            ALIVE: _ClassVar[MetaData.Inner.Status]
            UNKNOWN: _ClassVar[MetaData.Inner.Status]
        DEAD: MetaData.Inner.Status
        ALIVE: MetaData.Inner.Status
        UNKNOWN: MetaData.Inner.Status
        class Client(_message.Message):
            __slots__ = ("name", "id")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            name: str
            id: int
            def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...
        class LimboDreamLayer(_message.Message):
            __slots__ = ("client", "status")
            CLIENT_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            client: MetaData.Inner.Client
            status: MetaData.Inner.Status
            def __init__(self, client: _Optional[_Union[MetaData.Inner.Client, _Mapping]] = ..., status: _Optional[_Union[MetaData.Inner.Status, str]] = ...) -> None: ...
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        LAYER_FIELD_NUMBER: _ClassVar[int]
        a: float
        b: float
        layer: MetaData.Inner.LimboDreamLayer
        def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ..., layer: _Optional[_Union[MetaData.Inner.LimboDreamLayer, _Mapping]] = ...) -> None: ...
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    INNER_FIELD_NUMBER: _ClassVar[int]
    latency: float
    inner: MetaData.Inner
    def __init__(self, latency: _Optional[float] = ..., inner: _Optional[_Union[MetaData.Inner, _Mapping]] = ...) -> None: ...

class InstantMessage(_message.Message):
    __slots__ = ("timestamp", "client", "sender_ip", "sender", "recipient", "message", "image_attachments", "metadata")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    SENDER_IP_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    client: Client
    sender_ip: int
    sender: User
    recipient: User
    message: str
    image_attachments: _containers.RepeatedScalarFieldContainer[bytes]
    metadata: MetaData
    def __init__(self, timestamp: _Optional[int] = ..., client: _Optional[_Union[Client, str]] = ..., sender_ip: _Optional[int] = ..., sender: _Optional[_Union[User, _Mapping]] = ..., recipient: _Optional[_Union[User, _Mapping]] = ..., message: _Optional[str] = ..., image_attachments: _Optional[_Iterable[bytes]] = ..., metadata: _Optional[_Union[MetaData, _Mapping]] = ...) -> None: ...
