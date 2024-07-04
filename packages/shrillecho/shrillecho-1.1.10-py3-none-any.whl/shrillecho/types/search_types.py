from dataclasses import dataclass
from typing import List
from fastclasses_json import dataclass_json

from shrillecho.types.album_types import Album, SimplifiedAlbum
from shrillecho.types.artist_types import Artist
from shrillecho.types.playlist_types import SimplifiedPlaylistObject
from shrillecho.types.track_types import Track


@dataclass_json
@dataclass
class TrackSearchItems:
    href: str
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items: List[Track]


@dataclass_json
@dataclass
class AlbumSearchItems:
    href: str
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items: List[SimplifiedAlbum]


@dataclass_json
@dataclass
class ArtistSearchItems:
    href: str
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items: List[Artist]


@dataclass_json
@dataclass
class PlaylistSearchItems:
    href: str
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items: List[SimplifiedPlaylistObject]


@dataclass_json
@dataclass
class SearchResult:
    tracks: TrackSearchItems
    artists: ArtistSearchItems
    albums: AlbumSearchItems
    playlists: PlaylistSearchItems
