import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QPoint
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, \
     QWidget, QLabel, QDesktopWidget, QPushButton
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Widgets Example")
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 2 window sizes
        self.windowSize = np.array([[430, 480], [600, 650]], dtype=np.uint16)

        self.animationResizeWindow = QPropertyAnimation(self, b"geometry")
        self.animationResizeWindow.setDuration(300)

        curvatureTime = QEasingCurve(QEasingCurve.OutQuad)
        self.animationResizeWindow.setEasingCurve(curvatureTime)

        # window position
        self.screenSize = QDesktopWidget().screenGeometry().size()

        self.setGeometry(
            self.screenSize.width() - self.width() - 200, 140,
            *self.windowSize[0]
        )

        self.coords = QLabel("pass")
        self.coords.setAlignment(Qt.AlignCenter)
        self.coords.setStyleSheet("font-size: 24px;")

        imageCursorHand = QPixmap("./assets/cursors/hand.cur")
        handCursor = QCursor(imageCursorHand)

        # button resize
        self.buttonResize = QPushButton(self)
        self.iconResize = QIcon("assets/icons/resize_out.png")
        self.buttonResize.setFixedSize(50, 50)
        self.buttonResize.setIcon(self.iconResize)
        self.buttonResize.setStyleSheet("background-color: blue;")
        self.buttonResize.clicked.connect(self.resizeWindow)
        self.buttonResize.setCursor(handCursor)

        # button close
        self.buttonClose = QPushButton(self)
        self.buttonClose.setFixedSize(50, 50)
        self.buttonClose.setIcon(QIcon("assets/icons/close.png"))
        self.buttonClose.setStyleSheet("background-color: blue;")
        self.buttonClose.clicked.connect(self.close)
        self.buttonClose.setCursor(handCursor)

        self.setupUI()

    def setupUI(self):
        # layout window
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # header block
        headerWidget = QWidget()
        headerWidget.setStyleSheet("background: red;")
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

        # block 2 (body)
        bodyWidget = QWidget()
        bodyWidget.setStyleSheet("background: green;")
        bodyWidget.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(bodyWidget, stretch=1)

        wrapper = QWidget()
        wrapper.setLayout(layout)
        self.setCentralWidget(wrapper)

    def resizeWindow(self):

        width = self.size().width()
        height = self.size().height()
        resStart = self.geometry()

        if np.array_equal([width, height], self.windowSize[0]):
            self.iconResize = QIcon("assets/icons/resize_in.png")
            resEnd = QRect(resStart.x(), resStart.y(), *self.windowSize[1])
        else:
            self.iconResize = QIcon("assets/icons/resize_out.png")
            resEnd = QRect(resStart.x(), resStart.y(), *self.windowSize[0])

        self.buttonResize.setIcon(self.iconResize)

        self.animationResizeWindow.setStartValue(resStart)
        self.animationResizeWindow.setEndValue(resEnd)

        self.animationResizeWindow.start()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
