import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    
    for i in range(1, 5):
        for j in range(1, 5):
            button_name = f"B{i}{j}"
            button = QPushButton(button_name)
            grid.addWidget(button, i, j)
            
    win.setLayout(grid)
    win.setGeometry(100, 100, 300, 150)
    win.setWindowTitle("PySide6 Grid Layout")
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    window()
