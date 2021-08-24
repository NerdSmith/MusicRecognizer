from urllib.request import urlopen
from PySide6.QtGui import QImage


def get_qt_image_from_url(url: str):
    data = urlopen(url).read()
    image = QImage()
    image.loadFromData(data)
    return image
