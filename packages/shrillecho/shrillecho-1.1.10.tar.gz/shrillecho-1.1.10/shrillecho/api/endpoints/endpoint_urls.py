BASE_API_URL = "https://api.spotify.com/v1"


class SPOTIFY_URLS:

    class TRACKS:
        """
        URLs concerning tracks
        """

        ANALYZE: str = BASE_API_URL + "/audio-analysis/{id}"
        FEATURES: str = BASE_API_URL + "/audio-features/{id}"
        MULTI_FEATURES: str = BASE_API_URL + "/audio-features"
        SEVERAL: str = BASE_API_URL + "/tracks"
        ONE: str = BASE_API_URL + "/tracks/{id}"
        RECOMMENDATIONS: str = BASE_API_URL + "/recommendations"

    class PLAYLIST:
        """
        URLs concerning the playlists
        """

        ONE: str = BASE_API_URL + "/playlists/{playlist_id}"
        CREATE: str = BASE_API_URL + "/users/{user_id}/playlists"
        MY_PLAYLISTS: str = BASE_API_URL + "/me/playlists"
        USER: str = BASE_API_URL + "/users/{user_id}/playlists"
        COVER: str = BASE_API_URL + "/playlists/{playlist_id}/images"
        TRACKS: str = BASE_API_URL + "/playlists/{playlist_id}/tracks"

    class SEARCH:
        """
        URLs concerning the playlists
        """

        ITEM: str = BASE_API_URL + "/search"

    class LIBRARY:
        """
        URLs concerning the user library
        """

        CONTAINS_ALBUM: str = BASE_API_URL + "/me/albums/contains"
        CONTAINS_TRACK: str = BASE_API_URL + "/me/tracks/contains"
        CONTAINS_SHOWS: str = BASE_API_URL + "/me/shows/contains"

        ALBUMS: str = BASE_API_URL + "/me/albums"
        TRACKS: str = BASE_API_URL + "/me/tracks"
        SHOWS: str = BASE_API_URL + "/me/shows"

    class ALBUM:
        """
        URLs concerning the album
        """

        ONE: str = BASE_API_URL + "/albums/{id}"
        TRACKS: str = BASE_API_URL + "/albums/{id}/tracks"
        MULTIPLE: str = BASE_API_URL + "/albums"

    class ARTIST:
        """
        URLs concerning the artist
        """

        ONE: str = BASE_API_URL + "/artists/{id}"
        ALBUM: str = BASE_API_URL + "/artists/{id}/albums"
        TOP_TRACKS: str = BASE_API_URL + "/artists/{id}/top-tracks"
        SIMILAR_ARTISTS: str = BASE_API_URL + "/artists/{id}/related-artists"
        SEVERAL: str = BASE_API_URL + "/artists/"

    class USER:
        """
        URLs concerning a spotify user profile
        """

        ME: str = BASE_API_URL + "/me"
        USER: str = BASE_API_URL + "/users/{user_id}"

    class FOLLOW:
        """
        URLs concerning the follow endpoint
        """

        CONTAINS: str = BASE_API_URL + "/me/following/contains"
        CONTAINS_PLAYLIST: str = (
            BASE_API_URL + "/playlists/{playlist_id}/followers/contains"
        )
        HUMAN: str = BASE_API_URL + "/me/following"
        PLAYLIST: str = BASE_API_URL + "/playlists/{playlist_id}/followers"
        FOLLOWING_ARTISTS: str = BASE_API_URL + "/me/following?type=artist"

    class PLAYER:
        """
        URLs concerning the player
        """

        PLAYER: str = BASE_API_URL + "/me/player"
        QUEUE: str = BASE_API_URL + "/me/player/queue"
        DEVICES: str = BASE_API_URL + "/me/player/devices"
        RECENTLY: str = BASE_API_URL + "/me/player/recently-played"
        PLAYING: str = BASE_API_URL + "/me/player/currently-playing"

        PAUSE: str = BASE_API_URL + "/me/player/pause"
        SEEK: str = BASE_API_URL + "/me/player/seek"
        REPEAT: str = BASE_API_URL + "/me/player/repeat"
        VOLUME: str = BASE_API_URL + "/me/player/volume"
        NEXT: str = BASE_API_URL + "/me/player/next"
        PREVIOUS: str = BASE_API_URL + "/me/player/previous"
        PLAY: str = BASE_API_URL + "/me/player/play"
        SHUFFLE: str = BASE_API_URL + "/me/player/shuffle"
