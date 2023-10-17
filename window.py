import numpy as np
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QIcon, QCursor, QPixmap, QGuiApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from classes.Button import Button
from classes.Head import Head


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # hide frame
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.dragPosition = None

        # 2 window sizes
        self.windowSize = np.array([[430, 480], [600, 650]], dtype=np.uint16)

        # window sizes -> animation
        self.animationResizeWindow = QPropertyAnimation(self, b"geometry")
        self.animationResizeWindow.setDuration(500)

        curvatureTime = QEasingCurve(QEasingCurve.OutQuad)
        self.animationResizeWindow.setEasingCurve(curvatureTime)

        # window position
        self.screenSize = QGuiApplication.primaryScreen().size()

        self.setGeometry(
            self.screenSize.width() - self.width() - 200, 140,
            *self.windowSize[0]
        )

        # window Header
        # H-center
        self.coords = Head("^__________________^")

        # H-button_resize
        self.buttonResize = Button("assets/icons/resize_out.png", "blue", self.resizeWindow)

        # H-button_close
        self.buttonClose = Button("assets/icons/close.png", "blue", self.close)


        self.setupUI()

    def setupUI(self):
        # layout window
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # header block (H)
        headerWidget = QWidget()
        headerWidget.setStyleSheet("background: #222; color: #666;")

        # layout top -> header (H)
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

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.coords.underMouse():
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.coords.underMouse():
            self.move(event.globalPos() - self.dragPosition)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
