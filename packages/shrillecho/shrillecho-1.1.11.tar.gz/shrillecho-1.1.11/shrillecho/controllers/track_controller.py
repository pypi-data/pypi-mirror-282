from typing import List, Set
from shrillecho.api.api_client import SpotifyClient
from shrillecho.controllers.tracks_controller import TracksController
from shrillecho.types.track_types import Track
from shrillecho.utility.general_utility import get_id


class TrackController:

    def __init__(self, sp: SpotifyClient, track: Track = None):
        self._sp = sp
        self._track = track
        self._liked_tracks: Set[Track] = None
        self._loaded_likes = False

    @classmethod
    def create(cls, track_uri: str):
        return cls(track=get_id("track", track_uri))

    async def _load_likes(self):
        saved_tracks: List[Track] = await self._sp.tracks.saved_tracks_batch()
        self._liked_tracks = set(saved_tracks)
        self._loaded_likes = True

    async def is_liked(self) -> bool:
        if not self._loaded_likes:
            await self._load_likes()
        return self._track in self._liked_tracks
