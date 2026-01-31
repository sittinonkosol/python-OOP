import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    # Use any class name, but inherit from QWidget
    def __init__(self):
        super().__init__() # or super(myApp, self).__init__()
        self.resize(320, 240) # Set window size
        self.setWindowTitle("Hello, World!") # Set window title

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())
