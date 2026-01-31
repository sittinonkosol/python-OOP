import sys
from PySide6.QtWidgets import *

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)
        self.setWindowTitle("Hello, World!")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Hello World")
        layout.addWidget(label)
        
        # In PDF Example 4, there are multiple labels added in subsequent steps or variations
        # references Example 3 converted to class.
        # Example 4 in PDF (page 61) shows just one label initially. 
        # But later text says "we can add more components".

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())
