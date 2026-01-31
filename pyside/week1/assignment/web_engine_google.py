import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl("http://www.google.co.th")) # Load Google Thailand

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())
