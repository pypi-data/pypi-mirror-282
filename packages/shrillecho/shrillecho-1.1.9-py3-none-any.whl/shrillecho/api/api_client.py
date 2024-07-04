from typing import Union

from shrillecho.api.endpoints.search import SearchEndpoint

from .endpoints.albums import AlbumsEndpoint
from .endpoints.artists import ArtistsEndpoint
from .endpoints.follow import FollowEndpoint
from .endpoints.player import PlayerEndpoint
from .endpoints.playlists import PlaylistEndpoint
from .endpoints.tracks import TracksEndpoint
from .endpoints.users import UsersEndpoint
from .auth.oauth import ClientCredentials, OAuthCredentials
from .api_request_handler import SpotifyApiRequestHandler


class SpotifyClient:

    def __init__(
        self, token=None, auth_flow: Union[OAuthCredentials | ClientCredentials] = None
    ):

        if auth_flow:
            self.access_token = auth_flow.get_access_token()
        else:
            self.access_token = token

        self._request_handler = SpotifyApiRequestHandler(token=self.access_token)

        self.playlists: PlaylistEndpoint = PlaylistEndpoint(self._request_handler)
        self.tracks: TracksEndpoint = TracksEndpoint(self._request_handler)
        self.albums: AlbumsEndpoint = AlbumsEndpoint(self._request_handler)
        self.artists: ArtistsEndpoint = ArtistsEndpoint(self._request_handler)
        self.users: UsersEndpoint = UsersEndpoint(self._request_handler)
        self.follow: FollowEndpoint = FollowEndpoint(self._request_handler)
        self.player: PlayerEndpoint = PlayerEndpoint(self._request_handler)
        self.search: SearchEndpoint = SearchEndpoint(self._request_handler)
