from song import Song
from dataclass_csv import DataclassReader, DataclassWriter


def get_songs_from_csv(path):
    with open(path, mode="r", encoding='utf-8') as users_csv:
        songs = []
        reader = DataclassReader(users_csv, Song)
        for row in reader:
            songs.append(row)
        return songs


def push_to_csv(path, songs):
    with open(path, "w", encoding='utf-8') as file:
        writer = DataclassWriter(file, songs, Song)
        writer.write()
