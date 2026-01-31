import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout
)
from PySide6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stacked + Buttons")
        self.resize(400, 300)
        
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack = QStackedLayout()
        
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack)
        
        btn_red = QPushButton("Red")
        btn_red.pressed.connect(lambda: self.stack.setCurrentIndex(0))
        button_layout.addWidget(btn_red)
        self.stack.addWidget(Color("red"))
        
        btn_green = QPushButton("Green")
        btn_green.pressed.connect(lambda: self.stack.setCurrentIndex(1))
        button_layout.addWidget(btn_green)
        self.stack.addWidget(Color("green"))
        
        btn_yellow = QPushButton("Yellow")
        btn_yellow.pressed.connect(lambda: self.stack.setCurrentIndex(2))
        button_layout.addWidget(btn_yellow)
        self.stack.addWidget(Color("yellow"))
        
        container = QWidget()
        container.setLayout(page_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
