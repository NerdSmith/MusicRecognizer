from urllib.parse import quote
import webbrowser


def get_yt_search_link(song_title: str):
    return f"https://www.youtube.com/results?search_query={quote(song_title)}"


def get_spotify_search_link(song_title: str):
    return f"https://open.spotify.com/search/{quote(song_title)}?si=jX_LAAaeSfyg0rhLZPgIIw"


def open_in_browser(url):
    webbrowser.open(url, new=2)
