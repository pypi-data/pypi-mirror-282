from typing import List, Union
from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.artist_types import Artist, FollowedArtists
from shrillecho.types.playlist_types import SimplifiedPlaylistObject
from shrillecho.types.track_types import Track
from shrillecho.types.user_types import BaseUserProfile, CurrentUserProfile, UserProfile


class UserController:

    def __init__(
        self, sp: SpotifyClient, user: Union[UserProfile | CurrentUserProfile]
    ):
        self._user: Union[UserProfile | CurrentUserProfile] = user
        self._sp = sp

    async def get_followed_artists(self) -> List[Artist]:
        artists: List[Artist] = []
        followed_artist_page: FollowedArtists = (
            await self._sp.follow.get_followed_artists(limit=50, after=None)
        )
        while len(followed_artist_page.artists.items) != 0:
            after = followed_artist_page.artists.items[-1].id
            artists.extend(followed_artist_page.artists.items)
            followed_artist_page: FollowedArtists = (
                await self._sp.follow.get_followed_artists(limit=50, after=after)
            )
        return artists

    async def fetch_all_user_public_tracks(self) -> List[Track]:
        tracks: List[Track] = []
        playlists: List[SimplifiedPlaylistObject] = (
            await self._sp.playlists.user_playlists_batch(user=self._user.id)
        )
        for playlist in playlists:
            tracks.extend(
                await self._sp.playlists.tracks_batch(playlist_id=playlist.id)
            )
        return tracks
