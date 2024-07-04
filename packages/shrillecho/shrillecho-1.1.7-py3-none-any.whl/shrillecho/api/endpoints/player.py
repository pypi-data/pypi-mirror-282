from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.api.endpoints.endpoint_urls import SPOTIFY_URLS
from shrillecho.types.artist_types import Artist
from shrillecho.types.player_types import PlaybackState, RecentlyPlayedTracks


class PlayerEndpoint(Endpoint):

    async def recently_played(
        self, after: int = None, before: int = None, limit: int = 50
    ) -> RecentlyPlayedTracks:
        """TODO: complete"""

        url = SPOTIFY_URLS.PLAYER.RECENTLY

        query_params = {"limit": limit}

        if after:
            query_params["after"] = after
            print("after")

        elif before:
            query_params["before"] = before
            print("before")

        # else:
        #     raise Exception("invalid call")

        return await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params=query_params,
            response_type=RecentlyPlayedTracks,
        )

    async def playback_state(self, **kwargs) -> PlaybackState:
        """TODO: complete"""

        url = SPOTIFY_URLS.PLAYER.PLAYER

        return await self._request_handler.make_request(
            method="GET", url=url, query_params=kwargs, response_type=PlaybackState
        )
