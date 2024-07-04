from typing import List
from shrillecho.controllers.tracks_controller import TracksController
from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.playlist_types import Playlist
from shrillecho.types.track_types import Track


class PlaylistController:

    def __init__(
        self,
        sp: SpotifyClient,
        playlist: Playlist = None,
        tracks: TracksController = None,
    ):

        if not playlist or not tracks:
            raise Exception(
                "Use `create` methods or pass track controller and playlist"
            )

        self._sp: SpotifyClient = sp
        self.playlist: Playlist = playlist
        self.playlist_tracks: TracksController = tracks

    @classmethod
    async def create(
        cls, sp: SpotifyClient, playlist_id: str = None, playlist: Playlist = None
    ):

        if not playlist:
            playlist = await sp.playlist(playlist_id=playlist_id)

        if not playlist_id:
            playlist_id = playlist.id

        tracks = await TracksController.create_from_playlist(sp, playlist=playlist_id)

        return cls(sp=sp, playlist=playlist, tracks=tracks)

    def internal_tracks(self) -> List[Track]:
        return self.playlist_tracks.tracks
