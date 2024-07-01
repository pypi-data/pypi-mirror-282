import json
import typing
from collections import defaultdict

from pykour.url import URL


class Request(typing.Mapping[str, typing.Any]):
    def __init__(self, scope, receive):
        print(f"Request: {scope}")
        self.scope = scope
        self.receive = receive
        self._headers = defaultdict(list)
        self.content_type = None
        self.charset = "utf-8"

        # ヘッダーを解析し、Content-Typeヘッダーを先に解析する
        for key, value in self.scope["headers"]:
            decoded_key = key.decode("latin1").lower()
            decoded_value = value.decode("latin1")
            self._headers[decoded_key].append(decoded_value)

            if decoded_key == "content-type":
                self.content_type = decoded_value
                if "charset=" in decoded_value:
                    self.charset = decoded_value.split("charset=")[-1]

        self._stream_consumed = False

    def __getitem__(self, key: str) -> typing.Any:
        return self.scope[key]

    def __iter__(self) -> typing.Iterator[typing.Any]:
        return iter(self.scope)

    def __len__(self) -> int:
        return len(self.scope)

    __eq__ = object.__eq__
    __hash__ = object.__hash__

    @property
    def app(self) -> str:
        return self.scope["app"]

    @property
    def url(self) -> URL:
        return URL(scope=self.scope)

    @property
    def headers(self) -> dict[str, list[str]]:
        return self._headers

    def get_header(self, name: str) -> list[str]:
        return self._headers.get(name)

    @property
    def method(self) -> str:
        return typing.cast(str, self.scope["method"])

    @property
    def version(self) -> str:
        return self.scope["http_version"]

    @property
    def query_string(self) -> bytes:
        return self.scope["query_string"]

    async def body(self) -> bytes:
        try:
            body = b""
            more_body = True

            while more_body:
                message = await self.receive()
                body += message.get("body", b"")
                more_body = message.get("more_body", False)

            return body
        except Exception as e:
            print(f"Error occurred while receiving body: {e}")
            raise e

    async def json(self) -> typing.Any:
        try:
            body = await self.body()
            return json.loads(body)
        except Exception as e:
            print(f"Error occurred while parsing JSON: {e}")
            raise e
