import requests
from definitions import HOST


def ping_host():
    r = requests.get(HOST)
    return r.status_code == 200


def get_shazam_data(music_bytes: bytes):
    r = requests.post("https://nameless-sierra-10297.herokuapp.com/api/v1", files={"b_data": music_bytes})
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f"API status code {r.status_code}")
