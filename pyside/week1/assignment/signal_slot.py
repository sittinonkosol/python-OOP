import sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton

def window():
    app = QApplication(sys.argv)
    win = QDialog()
    
    b1 = QPushButton(win)
    b1.setText("Button1")
    b1.move(50, 20)
    b1.clicked.connect(b1_clicked)
    
    b2 = QPushButton(win)
    b2.setText("Button2")
    b2.move(50, 50)
    # The PDF shows old style: QObject.connect(b2, SIGNAL("clicked()"), b2_clicked)
    # We use the modern style for compatibility and best practice in PySide6
    b2.clicked.connect(b2_clicked)
    
    win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle("PyQt") # Title from PDF
    win.show()
    sys.exit(app.exec())

def b1_clicked():
    print("Button 1 clicked")

def b2_clicked():
    print("Button 2 clicked")

if __name__ == '__main__':
    window()
