from __future__ import annotations
from collections import defaultdict
from typing import List
from shrillecho.api.api_client import SpotifyClient
from shrillecho.utility.track_utils import TrackUtils
from shrillecho.types.album_types import Album
from shrillecho.types.artist_types import Artist
from shrillecho.types.playlist_types import Playlist
from shrillecho.types.soundcloud_types import User
from shrillecho.types.track_types import Track
from shrillecho.utility.artist_utils import ArtistUtils


class TracksController:
    """
    A class to encapsulate any collection of tracks
    """

    def __init__(self, sp: SpotifyClient, tracks: List[Track] = []):
        self.tracks: List[Track] = tracks
        self.liked_tracks: List[Track] = []
        self.unliked_tracks: List[Track] = []
        self.loaded_likes = False
        self._sp = sp

    @classmethod
    async def create_from_playlist(cls, sp: SpotifyClient, playlist: str):
        return cls(
            sp,
            tracks=await sp.playlists.tracks_batch(playlist_id=playlist, batch_size=5),
        )

    @classmethod
    async def create_from_album(cls, sp: SpotifyClient, album: str):
        return cls(sp, tracks=await sp.albums.album_tracks_batch(album_id=album))

    async def get_likes(self) -> TracksController:
        if not self.loaded_likes:
            await self.load_likes()
        return TracksController(sp=self._sp, tracks=self.liked_tracks)

    async def get_unliked(self) -> TracksController:
        if not self.loaded_likes:
            await self.load_likes()
        return TracksController(sp=self._sp, tracks=self.unliked_tracks)

    async def load_playlist(self, playlist_id: str):
        self.tracks = await self._sp.playlists.tracks_batch(playlist_id=playlist_id)

    async def load_album(self, album_id: str):
        self.tracks = await self._sp.albums.album_tracks_batch(album=album_id)

    async def load_likes(self):
        saved_tracks: List[Track] = await self._sp.tracks.saved_tracks_batch()

        saved_track_map = set(saved_tracks)

        for track in self.tracks:
            if not track:
                print(track)

            if track in saved_track_map:
                track.liked = True
                self.liked_tracks.append(track)
            else:
                track.liked = False
                self.unliked_tracks.append(track)

        self.loaded_likes = True

    async def clean_tracks(self):
        """
        If a track has no ISRC then we presume its an invalid track
        """
        local_removed_copyright = 0
        cleaned_tracks: List[Track] = []
        for track in self.tracks:
            if track.external_ids.isrc:
                cleaned_tracks.append(track)
            else:
                local_removed_copyright += 1
        self.tracks = cleaned_tracks

    async def write_tracks(self, name: str, user: str = "me") -> Playlist:

        if user == "me":
            me: User = await self._sp.users.me()
            user = me.id

        track_ids = TrackUtils.fetch_track_ids(self.tracks)

        track_uris = [f'spotify:track:{id}' for id in track_ids]

        playlist = await self._sp.playlists.create_playlist(
            user_id=user, playlist_name=name, public=False
        )
        limit = 50
        for i in range(0, len(track_uris), limit):
            await self._sp.playlists.add_tracks(
                playlist_id=playlist.id, track_uris=track_uris[i : i + limit]
            )
        return playlist

    async def artists(self, all_artists=False) -> List[Artist]:
        artist_ids_to_fetch = set()
        for track in self.tracks:
            if all_artists:
                for artist in track.artists:
                    artist_ids_to_fetch.add(artist.id)
            else:
                main_artist: Artist = TrackUtils.determine_main_artist(track)
                if main_artist.id:
                    artist_ids_to_fetch.add(track.artists[0].id)

        playlist_artists: list[Artist] = await ArtistUtils.fetch_several_artists(
            self._sp, artist_ids=list(artist_ids_to_fetch)
        )
        return playlist_artists

    async def genres(self) -> List[bool]:
        """
        From our list of tracks, obtain all the genres in a dictionary form

        genres = {
            'future_bass': 5,
            'hyperpop': 2,
            ...
        }
        """
        playlist_artists: List[Artist] = await self.artists()

        genre_counts = defaultdict(int)

        for artist in playlist_artists:
            for genre in artist.genres:
                genre_counts[genre] += 1

        sorted_genres: List[int] = sorted(
            genre_counts.items(), key=lambda x: x[1], reverse=True
        )

        return sorted_genres

    def __sub__(self, other: TracksController):
        other_track_sets = set(other.tracks)
        return TracksController(
            sp=self._sp,
            tracks=[track for track in self.tracks if track not in other_track_sets],
        )

    def __repr__(self):
        return f"{self.tracks}"

    def __and__(self, other):
        if isinstance(other, TracksController):
            self_set = set(self.tracks)
            other_set = set(other.tracks)
            return TracksController(sp=self._sp, tracks=self_set & other_set)
        return NotImplemented

    def __getitem__(self, index) -> Track:
        return self.tracks[index]

    def __len__(self):
        return len(self.tracks)
