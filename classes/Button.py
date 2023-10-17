from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QCursor, QPixmap


class Button(QPushButton):
    def __init__(self, path, background, event_click):
        super().__init__()
        imageCursorHand = QPixmap("./assets/cursors/hand.cur")
        handCursor = QCursor(imageCursorHand)

        self.icon = QIcon(path)
        self.setFixedSize(50, 50)
        self.setIcon(self.icon)
        self.setStyleSheet(f"background-color: {background};")
        self.clicked.connect(event_click)
        self.setCursor(handCursor)

