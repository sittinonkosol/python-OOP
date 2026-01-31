import sys
from PySide6.QtWidgets import *

class myMessageBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')

    def closeEvent(self, event):
        # Override closeEvent to ask for confirmation
        reply = QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = myMessageBox()
    qb.show()
    sys.exit(app.exec())
