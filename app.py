
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListView
from PyQt5.QtWidgets import QMessageBox, QListWidget

class window(QMainWindow):
    """
    This is the main GUI window.
    """
    def __init__(self):
        """
        Title and some other initializations are done here.
        """
        super().__init__()
        self.title = "ChatBot with Speech Recognition"
        self.initialize()

    def initialize(self):
        """
        This method contains all the buttons that are preset on GUI.

        New Case: Whenever a new case has to be registered, this button is used.
        Refresh: This button trains the KNN model. It downloads all the pending cases
                    and trains a KNN model on it.
        Match: This button downloads all the images submitted by the user and
                tries to predict the probability of match. If any match is found then
                it will be printed.
        Confirmed Cases: All cases which have been confirmed will be displayed here.
        """
        self.setWindowTitle(self.title)
        self.setFixedSize(600, 400)

        button_start = QPushButton("Start", self)
        button_start.move(300, 100)
        button_start.clicked.connect(self.speech_recognition)

        self.show()


app = QApplication(sys.argv)
w = window()
sys.exit(App.exec())

