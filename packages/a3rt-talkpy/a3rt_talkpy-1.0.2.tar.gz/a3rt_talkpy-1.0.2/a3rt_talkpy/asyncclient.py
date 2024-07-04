import aiohttp

from .response import Response
from .exception import *

class AsyncTalkClient:
    """
    A3RT Talk APIを非同期で利用するためのクライアントクラスです。
    """

    def __init__(self, apikey: str, session: aiohttp.ClientSession | None = None) -> None:
        """
        A3RT Talk APIを非同期で利用するためのクライアントクラスです。

        Args:
            apikey (str): A3RT Talk APIのAPIキー
            session (aiohttp.ClientSession, optional): セッションを指定します。指定しない場合は新しいセッションが作成されます。
        """
        self.apikey: str = apikey
        self.base_url: str = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
        self._session = session

    async def session(self) -> aiohttp.ClientSession:
        """
        セッションを取得します。
        通常はこれを直接呼び出す必要はありません。
        """
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def talk(self, query: str) -> Response:
        """
        A3RT Talk APIを非同期で利用します。

        Args:
            query (str): 送信するクエリ

        Returns:
            Response: A3RT Talk APIのレスポンス
        """
        async with (await self.session()).post(self.base_url, data={'apikey': self.apikey, 'query': query}) as res:
            response = await res.json()
            match response['status']:
                case 0:
                    return Response(response=response)
                case 1000:
                    raise ApiKeyIsNull
                case 1001:
                    raise ApiKeyNotFound
                case 1002:
                    raise DeletedAccount
                case 1003:
                    raise TemporaryAccount
                case 1010:
                    raise ServerNotFound
                case 1011:
                    raise ServerParameterError
                case 1030:
                    raise AccessDeny
                case 1400:
                    raise BadRequest
                case 1404:
                    raise NotFound
                case 1405:
                    raise MethodNotAllowed
                case 1413:
                    raise RequestEntityTooLong
                case 1500:
                    raise InternalServerError
                case 2000:
                    return Response(response=response)
                case _:
                    raise UnknownError
