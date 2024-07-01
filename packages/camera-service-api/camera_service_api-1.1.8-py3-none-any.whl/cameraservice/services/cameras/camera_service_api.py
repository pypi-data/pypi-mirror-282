from typing import List
import grpc
from google.protobuf import empty_pb2
from grpc._cython.cygrpc import ChannelArgKey

from cameraservice.services.cameras.camera_provider import CameraMeta
from cameraservice.services.cameras.constants import DEFAULT_GRPC_PACKAGE_SIZE
from cameraservice.services.grpc import camera_service_pb2 as service_pb2
from cameraservice.services.grpc.camera_service_pb2_grpc import CameraServiceStub
from cameraservice.services.grpc.grpcutilsc import pb2_to_local
from cameraservice.services.grpc.pb2utils import RemoveError, wrapper_rpc_error
from cameraservice.util.utils import M1

_EMPTY = empty_pb2.Empty()


class GrpcChannel:
    def __init__(self, host='localhost', port=49001, default_size:int = DEFAULT_GRPC_PACKAGE_SIZE ):
        addr = f'{host}:{port}'
        package_size = default_size * M1
        params = [
            (ChannelArgKey.max_send_message_length  ,package_size ),
            (ChannelArgKey.max_receive_message_length, package_size)

        ]
        self.channel = grpc.insecure_channel(addr,params)


class CameraServiceClient:

    def __init__(self, channel: GrpcChannel):
        self._stub = CameraServiceStub(channel.channel)
        pass

    @wrapper_rpc_error
    def get_camera_metas(self) -> List[CameraMeta]:
        response = self._stub.GetCameraMetas(_EMPTY)
        metas = pb2_to_local.to_CameraMetas(response)
        return metas

    @wrapper_rpc_error
    def get_image(self, sn: str) -> bytes:
        response = self._stub.GetImage(service_pb2.InputString(value=sn))
        output = pb2_to_local.to_Bytes(response)
        return output;

    @wrapper_rpc_error
    def reset(self):
        self._stub.Reset(_EMPTY)


def create_camera_service_api(host, port, package_size : int = DEFAULT_GRPC_PACKAGE_SIZE ) -> CameraServiceClient:
    c = GrpcChannel(host, port, package_size)
    return CameraServiceClient(c)
