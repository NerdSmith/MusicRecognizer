import requests
from definitions import HOST, API_LINK


def ping_host():
    r = requests.get(HOST)
    return r.status_code == 200


def get_shazam_data(music_bytes: bytes):
    r = requests.post(API_LINK, files={"b_data": music_bytes})
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f"API status code {r.status_code}")
