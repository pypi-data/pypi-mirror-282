from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.types.album_types import (
    Album,
    AlbumTracks,
    SeveralAlbums,
    SimplifiedTrack,
)
from shrillecho.utility.general_utility import get_id
from .endpoint_urls import SPOTIFY_URLS


class AlbumsEndpoint(Endpoint):

    async def album_tracks_batcher(
        self, album_id: str, batch_size=1, **kwargs
    ) -> List[SimplifiedTrack]:

        response_type = AlbumTracks
        url = SPOTIFY_URLS.ALBUM.TRACKS.format(id=album_id)

        initial_query_params = {"offset": 0, "limit": 50}

        initial_item: AlbumTracks = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        album_tracks_response: List[SimplifiedTrack] = [t for t in initial_item.items]

        album_tracks_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs
            )
        )
        return album_tracks_response

    async def album_tracks_batch(
        self, album_id: str, batch_size: int = 1, **kwargs
    ) -> List[SimplifiedTrack]:
        return await self.album_tracks_batcher(
            batch_size=batch_size, album_id=get_id("album", album_id), **kwargs
        )

    async def one(self, album_id: str, **kwargs) -> Album:

        url = SPOTIFY_URLS.ALBUM.ONE.format(id=get_id("album", album_id))

        return await self._request_handler._req_proxy(
            method="GET", url=url, query_params={**kwargs}, response_type=Album
        )

    async def many(self, album_uris: List[str], **kwargs) -> List[Album]:

        url = SPOTIFY_URLS.ALBUM.MULTIPLE

        multiple_albums: SeveralAlbums = await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={"ids": album_uris, **kwargs},
            response_type=SeveralAlbums,
        )
        return multiple_albums.albums
