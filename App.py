from PyQt5.QtWidgets import QMainWindow

import Layout


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Basic Web Scraper'

        self.setMinimumWidth(500)
        self.setWindowTitle(self.title)

        self.setCentralWidget(Layout.Layout(self))
        self.show()
