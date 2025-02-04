import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QStatusBar, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import directoryCheck
import friends
import addfriends
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Customer Experience')
        
        label = QLabel('Welcome!')
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar('Nav bar')
        self.addToolBar(toolbar)
        
        # Create a button and connect it to the directory check function
        button = QPushButton('Check Directory')
        button.clicked.connect(self.onButtonClick)

        viewlist = QPushButton('Friends List')
        viewlist.clicked.connect(self.onFriendsListButtonClick)
        addfriend = QPushButton('Add Friends')
        addfriend.clicked.connect(self.onAddFriendButtonClick)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(viewlist)
        layout.addWidget(button)
        layout.addWidget(addfriend)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def onButtonClick(self):
        reply = QMessageBox.question(self, 'Create Directory', 
                                     "Do you want to create the 'Shotgun' directory?", 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            result = directoryCheck.check_and_create_directory()
            QMessageBox.information(self, 'Result', result)
        else:
            QMessageBox.information(self, 'Result', "Directory creation canceled.")
    def onFriendsListButtonClick(self):
        friends.read_file()
    def onAddFriendButtonClick(self):
        addfriends.write_file()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()