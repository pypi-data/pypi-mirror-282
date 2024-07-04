from dataclasses import dataclass
from typing import List
from fastclasses_json import dataclass_json

from shrillecho.types.base_types import ExternalUrls
from shrillecho.types.track_types import Track


@dataclass_json
@dataclass
class Cursors:
    after: str
    before: str


@dataclass_json
@dataclass
class TrackHistoryContext:
    type: str
    href: str
    external_urls: ExternalUrls
    uri: str


@dataclass_json
@dataclass
class PlayHistoryObject:
    track: Track
    played_at: str
    context: TrackHistoryContext


@dataclass_json
@dataclass
class RecentlyPlayedTracks:
    """https://developer.spotify.com/documentation/web-api/reference/get-recently-played"""

    href: str
    limit: int
    next: str
    cursors: Cursors
    total: int
    items: List[PlayHistoryObject]


@dataclass_json
@dataclass
class Device:
    id: str
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    type: str
    volume_percent: int
    supports_volume: bool


@dataclass_json
@dataclass
class Context:
    type: str
    href: str
    external_urls: ExternalUrls
    uri: str


@dataclass_json
@dataclass
class Actions:
    interrupting_playback: bool
    pausing: bool
    resuming: bool
    seeking: bool
    skipping_next: bool
    skipping_prev: bool
    toggling_repeat_context: bool
    toggling_shuffle: bool
    toggling_repeat_track: bool
    transferring_playback: bool


@dataclass_json
@dataclass
class PlaybackState:
    device: Device
    repeat_state: str
    shuffle_state: bool
    context: Context
    timestamp: int
    progress_ms: int
    is_playing: bool
    item: Track
    currently_playing_type: str
    actions: Actions
