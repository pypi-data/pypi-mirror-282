from typing import Any

import ujson

from ...__meta__ import SERVER_SOFTWARE, __package__, __version__
from ...utils.headers import RAPIDAPI_HOST, RAPIDAPI_KEY, USER_AGENT
from ...utils.url_model import URLType, ignore_part, normalize_url
from .protocols import JsonDumps, JsonLoads, SessionProto


class BaseSession(SessionProto):
    def __init__(
        self,
        access_token: str,
        url: URLType | None = None,
        headers: dict[str, Any] | None = None,
        json_loads: JsonLoads = ujson.loads,
        json_dumps: JsonDumps = ujson.dumps,
    ) -> None:
        self._access_token = access_token
        self._url = normalize_url(url)

        if headers is None:
            headers = {}
        self._headers = headers

        self._headers[RAPIDAPI_HOST] = ignore_part(
            part="https://", url=self._url
        )
        self._headers[RAPIDAPI_KEY] = access_token
        self._headers[USER_AGENT] = (
            f"{SERVER_SOFTWARE} {__package__}/{__version__}"
        )

        self._json_loads = json_loads
        self._json_dumps = json_dumps
