import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addWidget(QPushButton("Cls"), 0, 0)
        grid.addWidget(QPushButton("7"), 1, 0)
        grid.addWidget(QPushButton("4"), 2, 0)
        grid.addWidget(QPushButton("1"), 3, 0)
        grid.addWidget(QPushButton("0"), 4, 0)

        grid.addWidget(QPushButton("Bck"), 0, 1)
        grid.addWidget(QPushButton("8"), 1, 1)
        grid.addWidget(QPushButton("5"), 2, 1)
        grid.addWidget(QPushButton("2"), 3, 1)
        grid.addWidget(QPushButton("."), 4, 1)

        grid.addWidget(QPushButton("9"), 1, 2)
        grid.addWidget(QPushButton("6"), 2, 2)
        grid.addWidget(QPushButton("3"), 3, 2)
        grid.addWidget(QPushButton("="), 4, 2)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        grid.addWidget(close_button, 0, 3)

        grid.addWidget(QPushButton("9"), 1, 3)
        grid.addWidget(QPushButton("6"), 2, 3)
        grid.addWidget(QPushButton("3"), 3, 3)
        grid.addWidget(QPushButton("+"), 4, 3)

        self.setLayout(grid)
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle("Calculator")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()