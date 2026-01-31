import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nesting Demo")
        
        layout_main = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()
        
        layout_left.addWidget(Color("red"))
        layout_left.addWidget(Color("yellow"))
        layout_left.addWidget(Color("purple"))
        
        layout_main.addLayout(layout_left)
        layout_main.addWidget(Color("green"))
        
        layout_right.addWidget(Color("red"))
        layout_right.addWidget(Color("purple"))
        
        layout_main.addLayout(layout_right)
        
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(20)
        
        container = QWidget()
        container.setLayout(layout_main)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
