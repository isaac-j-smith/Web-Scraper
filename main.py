import sys

from PyQt5.QtWidgets import QApplication

import App
import Scraper

if __name__ == "__main__":

    app = QApplication([])
    app.setStyle('Fusion')
    win = App.App()
    sys.exit(app.exec())
