from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraMeta_(_message.Message):
    __slots__ = ("serialNumber", "modelName", "manufactureName", "deviceVersion", "userDefinedName", "cameraType", "info")
    class InfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURENAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEVERSION_FIELD_NUMBER: _ClassVar[int]
    USERDEFINEDNAME_FIELD_NUMBER: _ClassVar[int]
    CAMERATYPE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    serialNumber: str
    modelName: str
    manufactureName: str
    deviceVersion: str
    userDefinedName: str
    cameraType: str
    info: _containers.ScalarMap[str, str]
    def __init__(self, serialNumber: _Optional[str] = ..., modelName: _Optional[str] = ..., manufactureName: _Optional[str] = ..., deviceVersion: _Optional[str] = ..., userDefinedName: _Optional[str] = ..., cameraType: _Optional[str] = ..., info: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CameraMetas(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CameraMeta_]
    def __init__(self, data: _Optional[_Iterable[_Union[CameraMeta_, _Mapping]]] = ...) -> None: ...

class BytesBody(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class InputString(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...
