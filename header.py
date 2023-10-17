from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from button import Button


class Header:
    def __init__(self, action_resize=None):
        imageCursorHand = QPixmap("./assets/cursors/hand.cur")
        handCursor = QCursor(imageCursorHand)

        imageCursorMove = QPixmap("./assets/cursors/white_move.cur")
        moveCursor = QCursor(imageCursorMove)

        self.resizeWindow = action_resize
        self.buttonResize = Button("assets/icons/resize_out.png", (50, 50), "blue", self.resizeWindow, handCursor)


    def setupUI(self):
        # layout window
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # header block
        headerWidget = QWidget()
        headerWidget.setStyleSheet(f"background: {self.color};")
        headerWidget.setFixedHeight(50)
        headerWidget.setContentsMargins(0, 0, 0, 0)

        # layout top -> header
        layout.addWidget(headerWidget, alignment=Qt.AlignTop)

        # layoutHeader
        layoutHeader = QHBoxLayout()
        layoutHeader.setSpacing(0)
        layoutHeader.setContentsMargins(0, 0, 0, 0)

        # LayoutHeader -> Resize | coords | Close
        layoutHeader.addWidget(self.buttonResize)
        layoutHeader.addWidget(self.coords)
        layoutHeader.addWidget(self.buttonClose)

        headerWidget.setLayout(layoutHeader)