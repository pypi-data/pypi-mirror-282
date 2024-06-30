from abc import (
    abstractmethod,
    ABC,
)
from typing import (
    Callable,
    Any,
)

import grpc
from quick_api_tests.grpc_client.interceptors.logging import LoggerInterceptor

StubType = Callable[[grpc.Channel], object]


class BaseSyncClient(ABC):
    def __init__(self, server_address="5.63.153.31:5055"):
        self.logging_interceptor = [LoggerInterceptor()]
        self.channel = grpc.insecure_channel(
            target=server_address,
            options=self.channel_options,
        )
        self.channel = grpc.intercept_channel(self.channel, *self._interceptors)
        self._stubs: dict = {}

    @property
    def _interceptors(self) -> list:
        return self.logging_interceptor + self.interceptors

    @property
    def interceptors(self) -> list:
        """
        Вы можете переопределить interceptors, если понимаете зачем вы это делаете.

        ```python
        class MyGrpcClient(BaseGrpcClient):
            interceptors = [InterceptorOne, InterceptorTwo]
            ...
        ```
        """
        return []

    @property
    def channel_options(self) -> list:
        """
        Вы можете переопределить channel_options, если понимаете зачем вы это делаете.

        Доступные опции здесь: https://grpc.github.io/grpc/core/group__grpc__arg__keys.html

        ```python
        class MyGrpcClient(BaseGrpcClient):
            channel_options = [
                ("grpc.max_receive_message_length", -1),
                ("grpc.max_send_message_length", -1),
            ]
        ```
        """
        return []

    @property
    @abstractmethod
    def stub_factory(self) -> StubType:
        pass

    def _do_call(self, stub_method: str, **kwargs) -> grpc.Call | Any:  # type: ignore
        return getattr(self._get_stub(), stub_method)(**kwargs)

    def _get_stub(self) -> object:
        stub = self.stub_factory(self.channel)
        return stub
