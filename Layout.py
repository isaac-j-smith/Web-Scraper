from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget, QMessageBox, QFormLayout

import Scraper


class Layout(QWidget):
    def __init__(self, parent):
        super(Layout, self).__init__(parent)
        self.records = QLineEdit(self)
        self.container = QLineEdit(self)
        self.url = QLineEdit(self)
        self.button = QPushButton('< Scrape >', self)
        self.layout = QFormLayout(self)
        self.label = QLabel('')
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.build()

    def build(self):
        self.setTabOrder(self.url, self.container)
        self.setTabOrder(self.container, self.records)
        self.setTabOrder(self.records, self.button)

        self.layout.setSpacing(25)
        self.layout.addRow(QLabel('URL:'), self.url)

        self.layout.addRow(QLabel('Container class name:'), self.container)

        self.layout.addRow(QLabel('Category class names \n(comma separated):'), self.records)

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
