from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.types.playlist_types import (
    Playlist,
    PlaylistTracks,
    SimplifiedPlaylistObject,
    UserPlaylists,
)
from shrillecho.types.track_types import Track
from shrillecho.utility.general_utility import get_id
from .endpoint_urls import SPOTIFY_URLS


class PlaylistEndpoint(Endpoint):

    async def playlist_tracks_batcher(
        self, playlist_id: str, batch_size=1, **kwargs
    ) -> List[Track]:

        response_type = PlaylistTracks

        url = SPOTIFY_URLS.PLAYLIST.TRACKS.format(playlist_id=playlist_id)

        initial_query_params = {"offset": 0, "limit": 50}

        initial_item: PlaylistTracks = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        playlist_tracks_response: List[Track] = [t.track for t in initial_item.items]

        playlist_tracks_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs
            )
        )

        return playlist_tracks_response

    async def current_user_playlists_batcher(
        self, batch_size=1, **kwargs
    ) -> List[Track]:

        response_type = UserPlaylists

        url = SPOTIFY_URLS.PLAYLIST.MY_PLAYLISTS

        initial_query_params = {"offset": 0, "limit": 50}

        initial_item: UserPlaylists = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        user_playlists_response: List[SimplifiedPlaylistObject] = initial_item.items

        user_playlists_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs
            )
        )

        return user_playlists_response

    async def user_playlists_batcher(
        self, user_id: str, batch_size=1, **kwargs
    ) -> List[Track]:

        response_type = UserPlaylists

        url = SPOTIFY_URLS.PLAYLIST.USER.format(user_id=user_id)

        initial_query_params = {"offset": 0, "limit": 50}

        initial_item: UserPlaylists = await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        user_playlists_response: List[SimplifiedPlaylistObject] = initial_item.items

        user_playlists_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs
            )
        )

        return user_playlists_response

    async def create_playlist(
        self, user_id: str, playlist_name: str, **kwargs
    ) -> Playlist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/create-playlist
        """

        url = SPOTIFY_URLS.PLAYLIST.CREATE.format(user_id=get_id("user", user_id))

        return await self._request_handler.make_request(
            method="POST",
            url=url,
            query_params={},
            response_type=Playlist,
            body={**{"name": playlist_name}, **kwargs},
            ignore_cache=True
        )

    async def get(self, playlist_id: str, **kwargs) -> Playlist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlist
        """

        url = SPOTIFY_URLS.PLAYLIST.ONE.format(
            playlist_id=get_id("playlist", playlist_id)
        )

        return await self._request_handler.make_request(
            method="GET", url=url, query_params=kwargs, response_type=Playlist
        )

    async def tracks_batch(
        self, playlist_id: str, batch_size: int = 50, **kwargs
    ) -> Playlist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        return await self.playlist_tracks_batcher(
            playlist_id=get_id("playlist", playlist_id), batch_size=batch_size, **kwargs
        )

    async def current_user_playlists_batch(
        self, batch_size: int = 1, **kwargs
    ) -> Playlist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        return await self.current_user_playlists_batcher(
            batch_size=batch_size, **kwargs
        )

    async def user_playlists_batch(
        self, user_id: str, batch_size: int = 1, **kwargs
    ) -> Playlist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        return await self.user_playlists_batcher(
            user_id=get_id("user", user_id), batch_size=batch_size, **kwargs
        )

    async def add_tracks(
        self, playlist_id: str, track_uris: List[str], position: int = None
    ) -> str:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.PLAYLIST.TRACKS.format(playlist_id=get_id("playlist", playlist_id))

        body = {"uris": track_uris}
    

        if position is not None:
            body["position"] = position

        return await self._request_handler.make_request(
            method="POST", url=url, query_params={}, body=body, ignore_cache=True
        )
