import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)
        self.setWindowTitle("Hello, World!")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        hello = QPushButton("Hello world!")
        hello.resize(100, 30)
        layout.addWidget(hello)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())
