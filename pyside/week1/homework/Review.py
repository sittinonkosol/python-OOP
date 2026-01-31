import sys
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Review")
        container = QWidget()
        from_box = QFormLayout(container)

        name_label = QLabel("Name")
        name_from = QLineEdit()
        from_box.addRow(name_label, name_from)

        author_label = QLabel("Author")
        author_from = QLineEdit()
        from_box.addRow(author_label, author_from)

        review_label = QLabel("review")
        review_long_from = QTextEdit()
        from_box.addRow(review_label, review_long_from)

        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

