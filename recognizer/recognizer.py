import json
import logging

from song import Song
from util.api_utils import get_shazam_data


class Recognizer:
    @staticmethod
    def recognize_API(music_bytes: bytes):
        try:
            shazam_data = get_shazam_data(music_bytes)
            song_data = json.loads(shazam_data)["data"]
            song = Song(song_data[1]["track"]["title"],
                        song_data[1]["track"]["subtitle"],
                        f"{song_data[1]['track']['title']} - {song_data[1]['track']['subtitle']}",
                        song_data[1]["track"]["share"].get("image"),
                        song_data[1]["track"]["url"])
            return song
        except Exception as e:
            logging.error(f"recognizer error {e}")
            return None


    """Old version of recognize method"""
    """@staticmethod
    def recognize(music_bytes: bytes):
        try:
            shazam = Shazam(music_bytes)
            recognize_generator = shazam.recognizeSong()
            song_data = next(recognize_generator)
            song = Song(song_data[1]["track"]["title"],
                        song_data[1]["track"]["subtitle"],
                        f"{song_data[1]['track']['title']} - {song_data[1]['track']['subtitle']}",
                        song_data[1]["track"]["share"].get("image"),
                        song_data[1]["track"]["url"])
            return song
        except Exception as e:
            logging.error(f"recognizer error {e}")
            return None"""