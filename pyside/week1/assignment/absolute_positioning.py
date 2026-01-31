import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide") # Title from PDF
        lbl = QLabel('Hello World', self) # self is the container window
        lbl.move(10, 10)
        
        btn = QPushButton('OK', self)
        btn.move(80, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())
