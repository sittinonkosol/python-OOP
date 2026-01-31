import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLabel, 
                               QLineEdit, QVBoxLayout, QHBoxLayout, 
                               QRadioButton, QPushButton)

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QForm")
        
        fbox = QFormLayout()
        
        l1 = QLabel("Name")
        nm = QLineEdit()
        fbox.addRow(l1, nm)
        
        l2 = QLabel("Address")
        add1 = QLineEdit()
        add2 = QLineEdit()
        
        vbox = QVBoxLayout()
        vbox.addWidget(add1)
        vbox.addWidget(add2)
        
        fbox.addRow(l2, vbox)
        
        hbox = QHBoxLayout()
        r1 = QRadioButton("Male")
        r2 = QRadioButton("Female")
        hbox.addWidget(r1)
        hbox.addWidget(r2)
        hbox.addStretch()
        
        fbox.addRow(QLabel("sex"), hbox)
        
        fbox.addRow(QPushButton("Submit"), QPushButton("Cancel"))
        
        self.setLayout(fbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec())
