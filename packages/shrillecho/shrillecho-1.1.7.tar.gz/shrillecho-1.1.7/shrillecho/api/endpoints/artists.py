from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.types.album_types import ArtistAlbums, SimplifiedAlbum
from shrillecho.types.artist_types import Artist, SeveralArtists
from shrillecho.types.track_types import SavedTracks
from shrillecho.utility.general_utility import get_id
from .endpoint_urls import SPOTIFY_URLS


class ArtistsEndpoint(Endpoint):

    async def artist_albums_batcher(
        self, artist_id: str, batch_size=1, **kwargs
    ) -> List[SimplifiedAlbum]:

        response_type = ArtistAlbums
        url = SPOTIFY_URLS.ARTIST.ALBUM.format(id=artist_id)

        initial_query_params = {"offset": 0, "limit": 50}

        initial_item: ArtistAlbums = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        artist_albums_response: List[SimplifiedAlbum] = initial_item.items

        artist_albums_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs
            )
        )
        return artist_albums_response

    async def artist_albums_batch(
        self, artist_id: str, batch_size: int = 1, **kwargs
    ) -> List[SimplifiedAlbum]:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        return await self.artist_albums_batcher(
            batch_size=batch_size, artist_id=get_id("artist", artist_id), **kwargs
        )

    async def artist_albums(self, artist_id: str, **kwargs) -> List[SimplifiedAlbum]:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.ARTIST.ALBUM.format(id=artist_id)

        return await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={**kwargs},
            response_type=SimplifiedAlbum,
        )

    async def get(self, artist_id: str) -> Artist:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.ARTIST.ONE.format(id=get_id("artist", artist_id))

        return await self._request_handler._req_proxy(
            method="GET", url=url, query_params={}, response_type=Artist
        )

    async def many(self, artist_ids: List[str], **kwargs) -> List[Artist]:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.ARTIST.SEVERAL

        artists: SeveralArtists = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**{"ids": artist_ids}, **kwargs},
            response_type=SeveralArtists,
        )

        return artists

    async def related(self, artist_id: str) -> List[Artist]:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.ARTIST.SIMILAR_ARTISTS.format(id=get_id("artist", artist_id))

        related_artists: SeveralArtists = await self._request_handler._req_proxy(
            method="GET", url=url, query_params={}, response_type=SeveralArtists
        )
        return related_artists.artists
