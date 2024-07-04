from __future__ import annotations
import json
from typing import List
import requests
from shrillecho.api.api_client import SpotifyClient
from shrillecho.api.task_scheduler import TaskScheduler
from shrillecho.utility.track_utils import TrackUtils
from shrillecho.types.album_types import SimplifiedAlbum, SimplifiedTrack
from shrillecho.types.artist_types import Artist, FollowerCount
from shrillecho.types.track_types import Track
from shrillecho.utility.cache import cached
import logging

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ArtistController:

    def __init__(self, sp: SpotifyClient, artist: Artist):
        self._artist = artist
        self._sp = sp

    @staticmethod
    async def create_from_id(sp: SpotifyClient, artist_id: str = None):
        artist: Artist = await sp.artists.get(artist_id=artist_id)
        return ArtistController(sp=sp, artist=artist)

    async def related(self) -> List[Artist]:
        return await self._sp.artists.related(artist_id=self._artist.id)

    async def albums(self) -> List[SimplifiedAlbum]:
        return await self._sp.artists.artist_albums_batch(artist_id=self._artist.id)

    async def get_all_tracks(self) -> List[SimplifiedTrack]:
        artist_albums: List[SimplifiedAlbum] = await self.albums()
        task_scheduluer = TaskScheduler()
        tasks = [
            (self._sp.albums.album_tracks_batch, (album.id,)) for album in artist_albums
        ]
        task_scheduluer.load_tasks(tasks)
        return await task_scheduluer.execute_tasks(batch_size=1)

    async def get_artist_track_ids(self) -> List[str]:
        """Return all tracks in the form of there ids

        Returns:
            List[str]: all artist tracks in for of ids
        """
        return [item.id for item in await self.get_all_tracks()]

    async def get_artist_tracks(self, unique: bool = True) -> List[Track]:
        all_ids = await self.get_artist_track_ids()
        tracks: List[Track] = await TrackUtils.fetch_several_tracks(
            sp=self._sp, track_ids=all_ids
        )
        if unique:
            return set(tracks)

        return tracks

    """
    TODO: New releaseas
    """
    """
     @staticmethod
    async def get_artist_albums(sp: SpotifyClient, artist_id: str, simple=False) -> List[Album] | List[SimplifiedAlbum]:
        
        artist_albums: List[SimplifiedAlbum] = await sp.artist_albums(artist=artist_id)

        if simple:
            return artist_albums

        album_ids = [album.id for album in artist_albums]
        
        return AlbumUtils.fetch_several_albums(sp, album_ids=album_ids)
    
    @staticmethod
    async def get_artist_new_releases(sp: SpotifyClient, artist_id: str, earliest_date: str ='2024-03-01' ) -> List[SimplifiedAlbum]:
       
        albums: List[SimplifiedAlbum] = []
        artist_albums: ArtistAlbums = await sp.artist_albums_single(artist=artist_id, offset=0)
        albums.extend(artist_albums.items)
        next = artist_albums.next
        
        while next != None:
           

            offset: int = artist_albums.offset + 50
            artist_albums: ArtistAlbums = await sp.artist_albums_single(artist=artist_id, offset=offset)

            if len(artist_albums.items) == 0:
                break

            last_album = artist_albums.items[-1]
            next = artist_albums.next

            if is_earlier(last_album.release_date, earliest_date):
                break

            albums.extend(artist_albums.items)

         
        return albums
    """

    """
    TODO: obscure artists
    
    """


# @staticmethod
# async def most_obscure_artists(sp: SpotifyClient, artist: str, artists: List[Artist], depth: int = 0) -> List[Artist]:

#     if depth == 10:
#         return artists

#     artist_id = get_id("artist", artist)

#     related_artists: List[Artist] = await sp.artist_related(artist=artist_id)

#     most_obscure = math.inf
#     most_obscure_artist = None

#     for artist in related_artists:
#         followers: FollowerCount = await SpotifyArtistUtil.followers(sp, artist=artist.id)
#         follower_count = followers.followers

#         if follower_count < most_obscure and artist not in artists:
#             most_obscure = follower_count
#             most_obscure_artist = artist

#     artists.append(most_obscure_artist)
#     depth += 1

#     return await SpotifyArtistUtil.most_obscure_artists(sp, most_obscure_artist.id, artists, depth)
