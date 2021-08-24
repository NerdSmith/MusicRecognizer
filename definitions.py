import os

import pyaudio

# global
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGFILE_PATH = os.path.join(ROOT_DIR, "app.log")
HISTORY_FILE_PATH = os.path.join(ROOT_DIR, "history.csv")
STYLES_FILE_PATH = os.path.join(ROOT_DIR, 'gui/style.qss')

# resources path
RES_PATH = os.path.join(ROOT_DIR, "resources")
NO_IMAGE_ICON = os.path.join(RES_PATH, "no_image_icon.png")
ICO_PATH = os.path.join(RES_PATH, "app_logo_v2_2.ico")

# gui settings
MIN_IMAGE_SIZE = 250

# recorder settings
DEFAULT_FRAMES = 512
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 48000
RECORD_SECONDS = 9
EXCERPT_PATH = os.path.join(ROOT_DIR, "excerpt.wav")

# update listen btn settings
UPDATE_RATE = 10  # times per second
WAITING_TIME = 25  # seconds
# WAITING_TIME = RECORD_TIMOUT + RECOGNISE_TIMOUT

# timeouts
RECORD_TIMOUT = 10
RECOGNIZE_TIMOUT = 15

# history model
ITEM_SELECTION_CODE = 200

