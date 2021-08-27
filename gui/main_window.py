import sys

import PySide6
from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication
from gui.ui_main_window import Ui_MainWindow
from gui.history_list import HistoryListModel
from definitions import MIN_IMAGE_SIZE, STYLES_FILE_PATH, NO_IMAGE_ICON
from util.qt_utils import get_qt_image_from_url


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open(STYLES_FILE_PATH, mode='r') as qss:
            self.setStyleSheet(qss.read())

        self.MIN_IMAGE_SIZE = MIN_IMAGE_SIZE
        self.pixmap = None

        self.no_image_icon = QImage()
        with open(NO_IMAGE_ICON, 'rb') as i:
            self.no_image_icon.loadFromData(i.read())

        self.ui.image_label.setMinimumSize(1, 1)
        self.ui.image_label.setAlignment(Qt.AlignCenter)
        self.show()

        self.setup_cover()
        self.history_model = HistoryListModel()
        self.ui.history_list_view.setModel(self.history_model)

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        self.repaint_cover()

    def setup_cover(self, path=None):
        if path is not None:
            image = get_qt_image_from_url(path)
        else:
            image = self.no_image_icon
        self.pixmap = QPixmap(image)

        self.repaint_cover()

    def repaint_cover(self):
        new_size = min(self.ui.image_label.width(), self.ui.image_label.height())
        if new_size > self.MIN_IMAGE_SIZE:
            self.ui.image_label.setPixmap(self.pixmap.scaled(new_size,
                                                             new_size,
                                                             Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation))

    def setup_combo(self, names):
        self.ui.input_device_combo.addItems(names)
        self.ui.input_device_combo.repaint()

    def get_listen_btn(self):
        return self.ui.listem_btn

    def get_open_yt_btn(self):
        return self.ui.open_yt

    def get_open_shazam_btn(self):
        return self.ui.open_shazam

    def get_open_spotify_btn(self):
        return self.ui.open_spotify

    def get_result_label(self):
        return self.ui.result_label

    def get_history_list_view(self):
        return self.ui.history_list_view

    def update_history(self, new_history):
        self.history_model.set_history(new_history)
        self.reload_history_view()

    def reload_history_view(self):
        self.history_model.layoutChanged.emit()

    def get_clear_history_btn(self):
        return self.ui.clear_history_btn

    def get_export_history_btn(self):
        return self.ui.export_history_btn

    def get_curr_combo_idx(self):
        return self.ui.input_device_combo.currentIndex()

    def clear_result_label(self):
        self.ui.result_label.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
