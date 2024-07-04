from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.api.endpoints.endpoint_urls import SPOTIFY_URLS
from shrillecho.types.artist_types import Artist
from shrillecho.types.user_types import CurrentUserProfile
from shrillecho.utility.general_utility import get_id


class FollowEndpoint(Endpoint):

    async def get_followed_artists(self, after: str, limit: int) -> List[Artist]:

        url = SPOTIFY_URLS.FOLLOW.FOLLOWING_ARTISTS

        return await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={"after": after, "limit": limit},
            response_type=CurrentUserProfile,
        )

    async def current_user_unfollow_playlist(self, playlist_id: str):

        url = SPOTIFY_URLS.FOLLOW.PLAYLIST.format(
            playlist_id=get_id("playlist", playlist_id)
        )

        await self._request_handler.make_request(
            method="DELETE", url=url, query_params={}
        )
