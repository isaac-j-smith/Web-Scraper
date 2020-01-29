from PyQt5.QtWidgets import QMainWindow

import Layout


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Basic Web Scraper'
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 500

        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        self.setCentralWidget(Layout.Layout(self))
        self.show()
