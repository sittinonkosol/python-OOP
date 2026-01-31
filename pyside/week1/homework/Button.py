import sys
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        VBox = QVBoxLayout()
        HBox = QHBoxLayout()

        self.ok_btn = QPushButton("OK")
        self.ok_btn.pressed.connect(self.show_msg_box)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.pressed.connect(self.exit_app)
        HBox.addWidget(self.ok_btn)
        HBox.addWidget(self.cancel_btn)

        VBox.addLayout(HBox)

        container = QWidget()
        container.setLayout(VBox)
        self.setCentralWidget(container)

    def show_msg_box(self):
        info = f"กดปุ่ม OK แล้วข้อความจะปรากฎ MessageBox\nQMessageBox()"
        QMessageBox.information(self, "Information", info)

    def exit_app(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()