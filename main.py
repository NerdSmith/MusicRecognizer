from definitions import LOGFILE_PATH, HISTORY_FILE_PATH, ITEM_SELECTION_CODE, ICO_PATH
import logging

logging.basicConfig(filename=LOGFILE_PATH, filemode='w', level=logging.DEBUG)

import sys
import os
import time
from functools import partial
from threading import Thread
import shutil

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog
from PySide6.QtGui import QCloseEvent, QMouseEvent

from definitions import UPDATE_RATE, WAITING_TIME, EXCERPT_PATH, RECORD_TIMEOUT, RECOGNIZE_TIMEOUT
from gui import MainWindow
from recorder import Recorder
from recognizer import Recognizer
from song import Song
from util.web_utils import get_spotify_search_link, get_yt_search_link, open_in_browser
from util.csv_utils import get_songs_from_csv, push_to_csv


class MainWindowWrapper(MainWindow):
    def __init__(self):
        super().__init__()
        self.curr_song: Song = None
        self.history = []
        self.recorder = Recorder()
        self.init_devices_combo()

        self.thread_manager = ThreadManager(self.recorder, self)

        self.connect(self.get_listen_btn(), QtCore.SIGNAL('clicked()'), self.start_listen)
        self.connect(self.get_open_yt_btn(), QtCore.SIGNAL('clicked()'), partial(self.open_browser_search, "yt_url"))
        self.connect(self.get_open_shazam_btn(), QtCore.SIGNAL('clicked()'),
                     partial(self.open_browser_search, "shazam_url"))
        self.connect(self.get_open_spotify_btn(), QtCore.SIGNAL('clicked()'),
                     partial(self.open_browser_search, "spot_url"))
        self.connect(self.get_clear_history_btn(), QtCore.SIGNAL('clicked()'), self.drop_history)
        self.connect(self.get_export_history_btn(), QtCore.SIGNAL('clicked()'), self.export_history_to_csv)

        self.load_history()

        self.get_history_list_view().mouseReleaseEvent = lambda event: self.click_on_history_item(event)

    def init_devices_combo(self):
        names = []

        for item in self.recorder.get_devices():
            names.append(item["name"])

        self.setup_combo(names)

    def drop_history(self):
        self.history = []
        self.update_history(self.history)

    def start_listen(self):
        if not self.thread_manager.block:
            listen_rec_th = Thread(target=self.thread_manager.run_listen_th,
                                   args=(self.get_listen_btn(), self.get_curr_combo_idx()),
                                   daemon=True,
                                   name="listen_rec_th")
            listen_rec_th.start()

    def set_song(self, song: Song = None):
        self.curr_song = song
        if song is not None:
            self.get_result_label().setText(song.full_title)
            self.setup_cover(song.thumbnail_url)
        else:
            self.clear_song_view()

    def push_to_history(self, song):
        self.history.insert(0, song)
        self.reload_history_view()

    def click_on_history_item(self, event: QMouseEvent):
        selected_indexes = self.get_history_list_view().selectedIndexes()
        if self.history and selected_indexes:
            song = selected_indexes[0].data(role=ITEM_SELECTION_CODE)
            self.set_song(song)

    def open_browser_search(self, url_type):
        if self.curr_song is not None:
            link = ""
            if url_type == "shazam_url":
                link = getattr(self.curr_song, url_type)
            elif url_type == "yt_url":
                link = get_yt_search_link(self.curr_song.full_title)
            elif url_type == "spot_url":
                link = get_spotify_search_link(self.curr_song.full_title)
            open_in_browser(link)

    def load_history(self):
        if os.path.exists(HISTORY_FILE_PATH):
            try:
                self.history = get_songs_from_csv(HISTORY_FILE_PATH)
                self.update_history(self.history)
            except Exception as e:
                logging.error(f"Failed to load history {e}")

    def export_history_to_csv(self):
        path = QFileDialog.getSaveFileName(self, "Export", "hst.csv", "*.csv")[0]
        if path:
            shutil.copyfile(HISTORY_FILE_PATH, path)

    def closeEvent(self, event: QCloseEvent) -> None:
        push_to_csv(HISTORY_FILE_PATH, self.history)

    def clear_song_view(self):
        self.setup_cover()
        self.clear_result_label()


class ThreadManager:
    def __init__(self, recorder, main_window):
        self.recorder = recorder
        self.main_window = main_window
        self.block = False

    def run_listen_th(self, listen_btn, curr_combo_idx):
        self.block = True
        listen_btn_th_wrapper = UpdateListenBtnThWrapper()
        listen_btn_th = Thread(target=listen_btn_th_wrapper.update,
                               args=(listen_btn,),
                               daemon=True,
                               name="listen_btn_th")
        listen_btn_th.start()

        record_th_wrapper = RecorderThWrapper(self.recorder)
        record_th = Thread(target=record_th_wrapper.run,
                           args=(curr_combo_idx,),
                           daemon=True,
                           name="record_th")
        record_th.start()

        record_th.join(timeout=RECORD_TIMEOUT)
        if record_th_wrapper.is_success and not record_th_wrapper.is_running:
            listen_btn_th_wrapper.btn_state = "Recognition"
        else:
            record_th_wrapper.terminate()
            listen_btn_th_wrapper.terminate()
            self.main_window.clear_song_view()
            self.block = False
            return

        recognize_th_wrapper = RecognizerThWrapper()
        recognize_th = Thread(target=recognize_th_wrapper.run,
                              args=(),
                              daemon=True,
                              name="recognize_th")
        recognize_th.start()
        recognize_th.join(RECOGNIZE_TIMEOUT)
        listen_btn_th_wrapper.terminate()
        if recognize_th_wrapper.is_success:
            song = recognize_th_wrapper.song
        else:
            self.main_window.set_song()
            self.block = False
            return

        song.yt_url = get_yt_search_link(song.full_title)
        song.spot_url = get_spotify_search_link(song.full_title)

        self.main_window.set_song(song)
        self.main_window.push_to_history(song)
        self.block = False


class RecognizerThWrapper:
    def __init__(self):
        self.song = None
        self.is_success = False

    def run(self):
        try:
            with open(EXCERPT_PATH, mode='rb') as excerpt_data:
                self.song = Recognizer.recognize_API(excerpt_data.read())
                if self.song is not None:
                    self.is_success = True
                else:
                    self.is_success = False
        except Exception as e:
            logging.error(e)


class RecorderThWrapper:
    def __init__(self, recorder):
        self.recorder = recorder
        self.is_success = False
        self.is_running = False

    def run(self, device_idx):
        self.is_running = True
        sys_device_idx = self.recorder.get_devices()[device_idx].get("index")
        self.recorder.set_default_device(sys_device_idx)
        self.is_success = self.recorder.record()
        self.is_running = False

    def terminate(self):
        self.recorder.close_channels()


class UpdateListenBtnThWrapper:
    def __init__(self):
        self.flag = True
        self.symbols = ["|", "/", "-", "\\"]
        self.btn_state = "Listening"

    def update(self, btn: QPushButton):
        btn.setEnabled(False)
        counter = int(UPDATE_RATE * WAITING_TIME)
        while self.flag and counter > 0:
            btn.setText(
                f"""{self.symbols[counter % len(self.symbols)]} {self.btn_state} {self.symbols[counter % len(self.symbols)]}\n{counter / UPDATE_RATE}""")
            time.sleep(1 / UPDATE_RATE)
            counter -= 1
        btn.setEnabled(True)
        btn.setText("Listen!")

    def terminate(self):
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowWrapper()
    window.setWindowIcon(QtGui.QIcon(ICO_PATH))
    sys.exit(app.exec())
