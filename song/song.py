from dataclasses import dataclass, field


@dataclass
class Song:
    title: str
    author: str
    full_title: str
    thumbnail_url: str = field(default=None)
    shazam_url: str = field(default=None)
