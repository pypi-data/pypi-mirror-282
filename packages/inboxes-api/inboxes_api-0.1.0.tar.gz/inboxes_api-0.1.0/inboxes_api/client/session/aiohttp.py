from __future__ import annotations

import ssl
from asyncio import AbstractEventLoop
from http import HTTPMethod
from typing import Any

import certifi
import ujson
from aiohttp import ClientSession, TCPConnector

from ...utils.url_model import URLType
from .base import BaseSession
from .protocols import JsonDumps, JsonLoads


class AiohttpSession(BaseSession):
    def __init__(
        self,
        access_token: str,
        url: URLType | None = None,
        headers: dict[str, Any] | None = None,
        json_loads: JsonLoads = ujson.loads,
        json_dumps: JsonDumps = ujson.dumps,
        loop: AbstractEventLoop | None = None,
    ) -> None:
        super().__init__(
            access_token=access_token,
            url=url,
            headers=headers,
            json_loads=json_loads,
            json_dumps=json_dumps,
        )

        self._client: ClientSession | None = None
        self._connector = TCPConnector
        self._connector_init = {
            "ssl": ssl.create_default_context(cafile=certifi.where())
        }

        self._loop = loop

    @property
    def closed(self) -> bool:
        return self._client is None or self._client.closed

    async def close(self) -> None:
        if not self.closed:
            await self.close()

    def new_session(self) -> ClientSession:
        return ClientSession(
            headers=self._headers.copy(),
            loop=self._loop,
            connector=self._connector(**self._connector_init),
            json_serialize=self._json_dumps,
        )

    def get_session(self) -> ClientSession:
        if self.closed:
            self._client = self.new_session()
        return self._client

    async def request(
        self, method: str, endpoint: str, **kwargs: Any
    ) -> Any:
        session = self.get_session()

        async with session.request(
            method=method, url=self._url.join(endpoint), **kwargs
        ) as resp:
            return await resp.json()

    async def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        return await self.request(
            method=HTTPMethod.GET, endpoint=endpoint, params=params, **kwargs
        )

    async def post(
        self, endpoint: str, data: dict[str, Any] | None = None, **kwargs: Any
    ) -> Any:
        return await self.request(
            method=HTTPMethod.POST, endpoint=endpoint, data=data, **kwargs
        )

    async def delete(self, endpoint: str, **kwargs: Any) -> Any:
        return await self.request(
            method=HTTPMethod.DELETE, endpoint=endpoint, **kwargs
        )
