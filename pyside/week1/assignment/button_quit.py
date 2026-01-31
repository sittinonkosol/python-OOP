import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)
        self.setWindowTitle("Hello, World!")
        
        btn = QPushButton("Quit", self)
        btn.resize(75, 30)
        # Using QFont needs QtGui import
        btn.setFont(QFont("Times", 16, QFont.Bold))
        btn.move(80, 50)
        
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())
