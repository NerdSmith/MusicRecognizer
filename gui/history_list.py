from typing import Union, Any

from PySide6 import QtCore

import PySide6
from PySide6.QtCore import QAbstractListModel
from PySide6.QtGui import Qt

from definitions import ITEM_SELECTION_CODE


class HistoryListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.history = []

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.history)

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        if index.isValid():
            if role == Qt.DisplayRole:
                value = self.history[index.row()].full_title
                return str(value)
            if role == ITEM_SELECTION_CODE and self.history:
                return self.history[index.row()]

    def set_history(self, new_history):
        self.history = new_history

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
