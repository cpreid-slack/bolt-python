from abc import abstractmethod, ABCMeta
from logging import Logger
from typing import Callable, Awaitable, Any, Coroutine

from slack_bolt.lazy_listener.async_internals import to_runnable_function
from slack_bolt.request.async_request import AsyncBoltRequest


class AsyncLazyListenerRunner(metaclass=ABCMeta):
    logger: Logger

    @abstractmethod
    def start(
        self, function: Callable[..., Awaitable[None]], request: AsyncBoltRequest
    ) -> None:
        raise NotImplementedError()

    async def run(
        self, function: Callable[..., Awaitable[None]], request: AsyncBoltRequest
    ) -> None:
        func = to_runnable_function(
            internal_func=function, logger=self.logger, request=request,
        )
        return await func()  # type: ignore
