import asyncio
import json
from typing import Dict, List, Optional, Tuple
import httpx
from .endpoints.endpoint_urls import BASE_API_URL
import redis
from .endpoints.endpoint_urls import *


class SpotifyApiRequestHandler:

    class SpotifyBaseError(Exception):
        """
        The base Error for all spotify exceptions
        """

        def __init__(self, message: dict):
            self.message: dict = message

        def __str__(self):
            return str(self.message)

        def get_json(self) -> Dict[str, Dict[str, str]]:
            """
            Get the the api response which was an error as dict
            {"error":{"status": 400, "message": "The reason"}}
            """
            return self.message

    class RateLimit(SpotifyBaseError):
        def __init__(self, message, retry_after: int = None):
            super().__init__(message)
            self.retry_after = retry_after

    class TokenExpired(SpotifyBaseError):
        """
        Custom token expired message
        """

    class NotFound(SpotifyBaseError):
        """
        Custom token expired message
        """

    class SpotifyApiError(SpotifyBaseError):
        """
        Custom token expired message
        """

    def __init__(self, token: str):
        self.http_client: httpx.AsyncClient = httpx.AsyncClient()
        self.rate_lock = asyncio.Event()
        self._token = token
        self._redis = redis.Redis(host="192.168.0.132", port="6379", db=0)

    @staticmethod
    def _format_query_params(query_params: dict) -> List[Tuple[str, str]]:
        """
        Takes in a dictionary of query params may have a list as the value
        we basically just want to combine that list with commas

        if there is no list then we just pass in the value as an empty list
        """
        return_params: List[Tuple[str, str]] = []
        for key in list(query_params.keys()):
            if not isinstance(query_params[key], List):
                query_params[key] = [str(query_params[key])]
            return_params.append((key, ",".join([str(i) for i in query_params[key]])))

        return return_params

    async def _get_cache_key(self, method: str, url: str, query_params: dict) -> str:
        params_str = json.dumps(self._format_query_params(query_params), sort_keys=True)
        return f"{method}:{url}:{params_str}"

    async def make_request(
        self,
        method: str,
        url: str,
        response_type=None,
        query_params: dict = None,
        body: dict = None,
        ignore_cache: bool = False
    ):

        cache_key = await self._get_cache_key(method, url, query_params)
        cached_response = self._redis.get(cache_key)

        if cached_response and not ignore_cache:
            if response_type:

                return response_type.from_json(cached_response)
            else:
                return json.loads(cached_response)

        while self.rate_lock.is_set():
            await asyncio.sleep(1)

        query_params = self._format_query_params(query_params)

        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        print(method, url, body)

        response = await self.http_client.request(
            method, url, params=query_params, headers=headers, json=body
        )
        print(response.text)

        if response.status_code == 429:
            print("429")
            self.rate_lock.set()
            retry_after = int(response.headers.get("Retry-After"))
            print(response.headers.get("Retry-After"))
            await asyncio.sleep(retry_after)
            self.rate_lock.clear()
            raise SpotifyApiRequestHandler.RateLimit(
                retry_after=retry_after, message=response.text
            )

        if response.status_code == 401:
            raise SpotifyApiRequestHandler.TokenExpired(message=response.text)

        if response.status_code == 404:
            raise SpotifyApiRequestHandler.NotFound(message=response.text)

        if response.status_code > 300:
            raise SpotifyApiRequestHandler.SpotifyApiError(message=response.text)

        self._redis.set(cache_key, json.dumps(response.json()), ex=3600)

        if response_type:

            with open("debug.json", "w") as f:
                json.dump(response.json(), f)
            return response_type.from_json(json.dumps(response.json()))
        else:

            return response.json()

    async def _req_proxy(
        self,
        method: str,
        url: str,
        response_type=None,
        query_params: Optional[dict] = None,
        body: Optional[dict] = None,
    ):

        if True:
            return await self.make_request(
                method, url, response_type, query_params, body
            )

        cache_key = await self._get_cache_key(method, url, query_params)
        cached_response = self._redis.get(cache_key)

        if cached_response:
            if response_type:

                return response_type.from_json(cached_response)
            else:
                return json.loads(cached_response)

        while self.rate_lock.is_set():
            await asyncio.sleep(1)

        data = {"params": query_params, "body": body, "method": method, "endpoint": url}

        response = await self.http_client.post("http://localhost:8002/req", json=data)
        resp_json = response.json()

        data = resp_json["data"]
        status_code = resp_json["status_code"]
        retry_after = resp_json.get("retry_after")

        if status_code == 429:
            print("429 proxied")
            self.rate_lock.set()
            retry_after = int(retry_after)
            print(retry_after)
            await asyncio.sleep(retry_after)
            self.rate_lock.clear()
            raise SpotifyApiRequestHandler.RateLimit(
                retry_after=retry_after, message="Rate limit exceeded"
            )

        if status_code == 401:
            raise SpotifyApiRequestHandler.TokenExpired(message="Unauthorised")

        if status_code == 404:
            raise SpotifyApiRequestHandler.NotFound(message="Not found")

        if status_code > 300:
            raise SpotifyApiRequestHandler.SpotifyApiError(message="API error")

        self._redis.set(cache_key, json.dumps(data), ex=3600)

        if response_type:
            return response_type.from_json(json.dumps(data))
        else:
            return data
