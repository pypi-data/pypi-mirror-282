from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.api.endpoints.endpoint_urls import SPOTIFY_URLS
from shrillecho.types.user_types import CurrentUserProfile


class UsersEndpoint(Endpoint):

    async def me(self) -> CurrentUserProfile:

        url = SPOTIFY_URLS.USER.ME

        return await self._request_handler.make_request(
            method="GET", url=url, query_params={}, response_type=CurrentUserProfile
        )
