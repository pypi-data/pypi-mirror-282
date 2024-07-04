from typing import List
from shrillecho.api.api_client import SpotifyClient
from shrillecho.types.album_types import Album, SeveralAlbums


class AlbumUtils:

    @staticmethod
    async def fetch_several_albums(
        sp: SpotifyClient, album_ids: List[str], batch_size: int = 20
    ) -> List[Album]:
        albums: List[Album] = []
        for i in range(0, len(album_ids), batch_size):
            chunk = album_ids[i : i + batch_size]
            more_albums: SeveralAlbums = await sp.albums(chunk)
            albums.extend(more_albums.albums)
        return albums
