import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        btn_map = [["Cls","Bck",None, close_button],
                   ["7","8","9","/"],
                   ["4","5","6","*"],
                   ["1","2","3","-"],
                   ["0",".","=","+"]]
        
        for row_i in range(len(btn_map)):
            for col_i, cell_v in enumerate(btn_map[row_i]):
                if isinstance(cell_v, QPushButton):
                    grid.addWidget(cell_v, row_i, col_i)
                elif cell_v is not None:
                    grid.addWidget(QPushButton(cell_v), row_i, col_i)

        self.setLayout(grid)
        self.setWindowTitle("Calculator I")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()