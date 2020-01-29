from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget, QMessageBox

import Scraper


class Layout(QWidget):
    def __init__(self, parent):
        super(Layout, self).__init__(parent)
        self.records = QLineEdit(self)
        self.container = QLineEdit(self)
        self.url = QLineEdit(self)
        self.button = QPushButton('< Scrape >', self)
        self.layout = QVBoxLayout(self)
        self.label = QLabel('')
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 50, 20, 20)
        self.build()

    def build(self):
        self.layout.setSpacing(25)
        self.layout.addWidget(QLabel('Enter a url to scrape:'))
        self.layout.addWidget(self.url)
        self.layout.addWidget(QLabel('Enter the container\'s class:'))
        self.layout.addWidget(self.container)
        self.layout.addWidget(QLabel('Enter the category classes:'))
        self.layout.addWidget(self.records)

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        s = Scraper.Scraper(self.url.text(), self.container.text(), self.records.text())
        formatted = ""
        for record in s.run():
            for item in record:
                formatted += item + '; '
            formatted += '\n'

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Data Scrape Complete")
        msg.setInformativeText("Press Show Details to view")
        msg.setWindowTitle("Complete")
        msg.setDetailedText(str(formatted))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)

        msg.exec_()
