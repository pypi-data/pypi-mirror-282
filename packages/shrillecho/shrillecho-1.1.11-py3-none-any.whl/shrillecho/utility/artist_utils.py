from typing import List
from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.artist_types import Artist, SeveralArtists
from shrillecho.types.track_types import Track


class ArtistUtils:

    @staticmethod
    async def fetch_several_artists(
        sp: SpotifyClient, artist_ids: List[str], batch_size: int = 20
    ) -> List[Artist]:
        artists: List[Artist] = []
        for i in range(0, len(artist_ids), batch_size):
            chunk = artist_ids[i : i + batch_size]
            more_artists: SeveralArtists = await sp.artists.many(artist_ids=chunk)
            artists.extend(more_artists.artists)
        return artists

    @staticmethod
    async def expand_tracks_list_with_artists(
        sp: SpotifyClient, tracks: List[Track], batch_size: int = 20
    ) -> List[Track]:
        # Collect the artist IDs to expand
        artist_ids = [track.artists[0].id for track in tracks]

        expanded_artists: List[Artist] = []
        for i in range(0, len(artist_ids), batch_size):
            chunk = artist_ids[i : i + batch_size]
            more_artists: SeveralArtists = await sp.artists.many(artist_ids=chunk)
            expanded_artists.extend(more_artists.artists)

        artist_mapping = {artist.id: artist for artist in expanded_artists}

        for track in tracks:
            track.artists[0] = artist_mapping[track.artists[0].id]

        return tracks

    @staticmethod
    def fetch_artists_ids(artists: List[Artist]) -> List[str]:
        """
        Given a list of tracks return a list of the ids only
        """

        ids = []
        for a in artists:
            if a.id:
                ids.append(a.id)
        return ids

    @staticmethod
    def return_top_genres(artists: List[Artist]) -> List[str]:
        """
        Given a list of tracks return a list of the ids only
        """
