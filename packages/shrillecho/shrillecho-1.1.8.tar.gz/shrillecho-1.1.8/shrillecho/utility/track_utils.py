from typing import List
from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.artist_types import Artist
from shrillecho.types.track_types import Track


class TrackUtils:

    @staticmethod
    async def fetch_several_tracks(
        sp: SpotifyClient, track_ids: List[str], batch_size: int = 50
    ) -> List[Track]:

        tracks: List[Track] = []
        for i in range(0, len(track_ids), batch_size):
            chunk = track_ids[i : i + batch_size]
            more_tracks: List[Track] = await sp.tracks.many(chunk)
            tracks.extend(more_tracks)

        return tracks

    @staticmethod
    def determine_main_artist(track: Track) -> Artist:
        """The main artist is the artist who actually made the track,
        so if its a remix , they are the creators of the remix but may not be listed
        as the first artist. The main artist does not include the feats just the core artist,
        may extend to be feats..

        Args:
            track (Track): the track to determine the main artist of

        Returns:
            List[Artist]: list of artists in the playlist
        """
        main_artist = None
        if "Remix" in track.name:
            for artist in track.artists:
                if artist.name in track.name:
                    main_artist = artist
            if not main_artist:
                main_artist = track.artists[0]
        else:
            main_artist = track.artists[0]

        return main_artist

    @staticmethod
    def fetch_track_ids(tracks: List[Track]) -> List[str]:
        """
        Given a list of tracks return a list of the ids only
        """

        ids = []
        for track in tracks:
            if track.id:
                ids.append(track.id)

        print(f"ids: {len(ids)}")
        return ids

    @staticmethod
    def clean_tracks(tracks: List[Track]):

        cleaned_tracks: List[Track] = []
        for track in tracks:
            if track.external_ids.isrc:
                cleaned_tracks.append(track)
        return cleaned_tracks
