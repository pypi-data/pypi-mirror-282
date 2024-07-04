from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.types.playlist_types import Playlist, PlaylistTracks
from shrillecho.types.track_types import (
    AudioFeatures,
    Recc,
    SavedTracks,
    SeveralTracks,
    Track,
)
from shrillecho.utility.general_utility import get_id
from .endpoint_urls import SPOTIFY_URLS


class TracksEndpoint(Endpoint):

    async def _saved_tracks_batcher(self, batch_size=1, **kwargs) -> List[Track]:

        response_type = SavedTracks
        url = SPOTIFY_URLS.LIBRARY.TRACKS

        initial_query_params = {"offset": 0, "limit": 50}

        # We need to know the total number of tracks to collect all URLs, so we do this initial call
        initial_item: SavedTracks = await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={**initial_query_params, **kwargs},
            response_type=response_type,
        )

        # unpack the initial response to our base response
        saved_tracks_response: List[Track] = [t.track for t in initial_item.items]

        # extend the base response with a batched get of all other urls
        saved_tracks_response.extend(
            await self.batch_get(
                url=url,
                response_type=response_type,
                initial_item=initial_item,
                batch_size=batch_size,
                **kwargs,
            )
        )
        return saved_tracks_response

    async def saved_tracks_batch(self, batch_size: int = 1, **kwargs) -> List[Track]:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        return await self._saved_tracks_batcher(batch_size=batch_size, **kwargs)

    async def audio_features(self, track_id: str) -> AudioFeatures:
        """
        docs: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """

        url = SPOTIFY_URLS.TRACKS.FEATURES.format(id=get_id("track", track_id))

        return await self._request_handler._req_proxy(
            method="GET", endpoint=url, response_type=AudioFeatures
        )

    async def one(self, track_id: str, **kwargs) -> Track:

        url = SPOTIFY_URLS.TRACKS.ONE.format(id=get_id("track", track_id))

        return await self._request_handler._req_proxy(
            method="GET", url=url, query_params={**kwargs}, response_type=Track
        )

    async def many(self, track_ids: List[str], **kwargs) -> List[Track]:

        url = SPOTIFY_URLS.TRACKS.SEVERAL

        several_tracks: SeveralTracks = await self._request_handler._req_proxy(
            method="GET",
            url=url,
            query_params={**{"ids": track_ids}, **kwargs},
            response_type=SeveralTracks,
        )
        print(f"many: {len(several_tracks.tracks)}")
        return several_tracks.tracks

    async def reccomendation(self, **kwargs) -> Recc:

        url = SPOTIFY_URLS.TRACKS.RECOMMENDATIONS

        return await self._request_handler.make_request(
            method="GET", url=url, query_params={**kwargs}, response_type=Recc
        )
