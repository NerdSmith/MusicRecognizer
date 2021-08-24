# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SongRecognisergNBZhy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1118, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.song_groupbox = QGroupBox(self.frame)
        self.song_groupbox.setObjectName(u"song_groupbox")
        sizePolicy.setHeightForWidth(self.song_groupbox.sizePolicy().hasHeightForWidth())
        self.song_groupbox.setSizePolicy(sizePolicy)
        self.song_groupbox.setMinimumSize(QSize(350, 450))
        self.song_groupbox.setContextMenuPolicy(Qt.NoContextMenu)
        self.song_groupbox.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.song_groupbox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.image_label = QLabel(self.song_groupbox)
        self.image_label.setObjectName(u"image_label")
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.image_label)

        self.frame_2 = QFrame(self.song_groupbox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(320, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.result_label = QLabel(self.frame_2)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setText(u"")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.result_label)

        self.open_yt = QPushButton(self.frame_2)
        self.open_yt.setObjectName(u"open_yt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_yt.sizePolicy().hasHeightForWidth())
        self.open_yt.setSizePolicy(sizePolicy2)
        self.open_yt.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.open_yt)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(320, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.open_shazam = QPushButton(self.frame_3)
        self.open_shazam.setObjectName(u"open_shazam")
        sizePolicy2.setHeightForWidth(self.open_shazam.sizePolicy().hasHeightForWidth())
        self.open_shazam.setSizePolicy(sizePolicy2)
        self.open_shazam.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.open_shazam)

        self.open_spotify = QPushButton(self.frame_3)
        self.open_spotify.setObjectName(u"open_spotify")
        sizePolicy2.setHeightForWidth(self.open_spotify.sizePolicy().hasHeightForWidth())
        self.open_spotify.setSizePolicy(sizePolicy2)
        self.open_spotify.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.open_spotify)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.song_groupbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.device_listen_frame = QFrame(self.frame)
        self.device_listen_frame.setObjectName(u"device_listen_frame")
        self.device_listen_frame.setFrameShape(QFrame.StyledPanel)
        self.device_listen_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.device_listen_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.device_listen_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.input_device_combo = QComboBox(self.frame_4)
        self.input_device_combo.setObjectName(u"input_device_combo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.input_device_combo.sizePolicy().hasHeightForWidth())
        self.input_device_combo.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.input_device_combo)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.listem_btn = QPushButton(self.device_listen_frame)
        self.listem_btn.setObjectName(u"listem_btn")
        self.listem_btn.setMinimumSize(QSize(0, 65))
        font = QFont()
        font.setPointSize(9)
        self.listem_btn.setFont(font)

        self.verticalLayout_5.addWidget(self.listem_btn)


        self.verticalLayout.addWidget(self.device_listen_frame)


        self.horizontalLayout.addWidget(self.frame)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(400, 0))
        self.groupBox.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.history_list_view = QListView(self.groupBox)
        self.history_list_view.setObjectName(u"history_list_view")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.history_list_view.setFont(font1)

        self.verticalLayout_4.addWidget(self.history_list_view)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.clear_history_btn = QPushButton(self.frame_5)
        self.clear_history_btn.setObjectName(u"clear_history_btn")

        self.horizontalLayout_3.addWidget(self.clear_history_btn)

        self.export_history_btn = QPushButton(self.frame_5)
        self.export_history_btn.setObjectName(u"export_history_btn")

        self.horizontalLayout_3.addWidget(self.export_history_btn)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Recognizer ", None))
        self.song_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Song", None))
        self.image_label.setText("")
        self.open_yt.setText(QCoreApplication.translate("MainWindow", u"Open on YouTube", None))
        self.open_shazam.setText(QCoreApplication.translate("MainWindow", u"Open on Shazam", None))
        self.open_spotify.setText(QCoreApplication.translate("MainWindow", u"Open on Spotify", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input device:", None))
        self.listem_btn.setText(QCoreApplication.translate("MainWindow", u"Listen!", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"History", None))
        self.clear_history_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.export_history_btn.setText(QCoreApplication.translate("MainWindow", u"CSV export", None))
    # retranslateUi

