from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QPixmap


class Head(QLabel):
    def __init__(self, text):
        super().__init__(text)
        imageCursorMove = QPixmap("./assets/cursors/white_move.cur")
        moveCursor = QCursor(imageCursorMove)
        self.setMouseTracking(True)  # watch mouse
        self.setCursor(moveCursor)

        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 24px;")

