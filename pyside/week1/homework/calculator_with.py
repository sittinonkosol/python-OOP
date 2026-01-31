import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator II")

        main_layout = QVBoxLayout()

        display = QLineEdit("0")
        display.setAlignment(Qt.AlignRight)
        display.setReadOnly(True)

        top_btn = QHBoxLayout()
        top_btn_map = ["backspace", "Clear", "Clear All"]

        for row_v in top_btn_map:
            top_btn.addWidget(QPushButton(row_v))

        del row_v

        main_btn = QGridLayout()
        main_btn_map = [["MC", "7", "8", "9", "/", "Sqrt"],
                        ["MR", "4", "5", "6", "*", "x^2"],
                        ["MS", "1", "2", "3", "-", "1/x"],
                        ["M+", "0", ".", "+-", "+", "="]]
        
        for row_i, row_v in enumerate(main_btn_map):
            for col_i, cell_v in enumerate(main_btn_map[row_i]):
                main_btn.addWidget(QPushButton(cell_v), row_i, col_i)

        main_layout.addWidget(display)
        main_layout.addLayout(top_btn)
        main_layout.addLayout(main_btn)
        main_layout.setContentsMargins(5,5,5,5)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()