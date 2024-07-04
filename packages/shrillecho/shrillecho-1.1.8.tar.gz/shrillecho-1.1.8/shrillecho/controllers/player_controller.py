from typing import List
import spotipy

from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.track_types import Track


class SpotifyPlayer:

    @staticmethod
    def play_track(sp: spotipy.Spotify, uri: str):
        """
        Play a specific uri on the first device ID listed.
        """

        uri = f"spotify:track:{uri}"

        device_id = sp.devices()["devices"][0]["id"]
        sp.start_playback(device_id=device_id, uris=[uri])

    @staticmethod
    async def get_recently_played(sp: SpotifyClient) -> List[Track]:
        sp.player.current_user_recently_played()
