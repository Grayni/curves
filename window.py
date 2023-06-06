import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QDesktopWidget, QPushButton
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Widgets Example")

        # 2 window sizes
        self.windowSize = np.array([[600, 650], [430, 480]], dtype=np.uint16)
        self.setFixedSize(self.windowSize[0, 0], self.windowSize[0, 1])

        # window position
        self.screenSize = QDesktopWidget().screenGeometry().size()
        self.move(self.screenSize.width() - self.width() - 200, 10)

        # button resize
        self.buttonResize = QPushButton(self)
        self.iconResize = QIcon("assets/icons/resize.png")
        self.buttonResize.setFixedSize(50, 50)
        self.buttonResize.setIcon(self.iconResize)
        self.buttonResize.setStyleSheet("background-color: blue; height: 20px; width: 20px;")
        self.buttonResize.clicked.connect(self.resizeWindow)

        self.setupUI()

    def setupUI(self):
        # layout
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # block 1 (header)
        headerWidget = QWidget()
        headerWidget.setStyleSheet("background: red;")
        headerWidget.setFixedHeight(50)
        headerWidget.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(headerWidget, alignment=Qt.AlignTop)

        # in body
        layoutHeader = QVBoxLayout()
        layoutHeader.setSpacing(0)
        layoutHeader.setContentsMargins(0, 0, 0, 0)
        layoutHeader.addWidget(self.buttonResize)
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

        if [width, height] == self.windowSize[0].tolist():
            self.setFixedSize(self.windowSize[1, 0], self.windowSize[1, 1])
        else:
            self.setFixedSize(self.windowSize[0, 0], self.windowSize[0, 1])



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


# from PyQt5.QtCore import Qt, QEvent
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Window Event Example")
#
#         self.setupUI()
#
#     def setupUI(self):
#         # Остальной код вашего интерфейса
#         ...
#
#     def changeEvent(self, event):
#         if event.type() == QEvent.WindowStateChange:
#             if self.isMaximized():
#                 print("Окно развернуто на весь экран")
#             else:
#                 print("Окно не развернуто на весь экран")
#
#         super().changeEvent(event)
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()
