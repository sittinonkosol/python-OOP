import sys
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        # Read the image file as binary
        try:
            # Note: The PDF mentions '101_0336.png'
            with open('101_0336.png', 'rb') as f:
                img = f.read()
                # Set content with mime type
                self.setContent(img, "image/png")
        except FileNotFoundError:
            self.setHtml("<h1>Image 101_0336.png not found</h1>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())
