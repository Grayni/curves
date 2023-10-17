from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton


class Button:
    def __init__(self, icon_path, size, color="transparent", action=None, cursor=Qt.ArrowCursor):
        self.button = QPushButton(self)
        self.icon = QIcon(icon_path)
        self.button.setFixedSize(*size)
        self.button.setIcon(self.icon)
        self.button.setStyleSheet(f"background-color: {color};")
        self.button.clicked.connect(action)
        self.button.setCursor(cursor)


