import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QStatusBar, QLabel, QComboBox)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Customer Experience')

        label = QLabel('Welcome!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('Nav bar')
        self.addToolBar(toolbar)

    def onNavBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()