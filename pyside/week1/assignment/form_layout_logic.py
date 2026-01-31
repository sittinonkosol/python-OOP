import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLabel, 
                               QLineEdit, QVBoxLayout, QHBoxLayout, 
                               QRadioButton, QPushButton, QMessageBox)

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QForm with Submit Logic")
        
        fbox = QFormLayout()
        
        self.nm = QLineEdit()
        fbox.addRow(QLabel("Name"), self.nm)
        
        self.add1 = QLineEdit()
        self.add2 = QLineEdit()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.add1)
        vbox.addWidget(self.add2)
        
        fbox.addRow(QLabel("Address"), vbox)
        
        hbox = QHBoxLayout()
        self.r1 = QRadioButton("Male")
        self.r2 = QRadioButton("Female")
        hbox.addWidget(self.r1)
        hbox.addWidget(self.r2)
        hbox.addStretch()
        
        fbox.addRow(QLabel("sex"), hbox)
        
        self.btn_submit = QPushButton("Submit")
        self.btn_cancel = QPushButton("Cancel")
        
        self.btn_submit.clicked.connect(self.on_submit)
        self.btn_cancel.clicked.connect(self.close)
        
        fbox.addRow(self.btn_submit, self.btn_cancel)
        
        self.setLayout(fbox)

    def on_submit(self):
        name = self.nm.text()
        address = f"{self.add1.text()} {self.add2.text()}"
        
        gender = ""
        if self.r1.isChecked():
            gender = "Male"
        elif self.r2.isChecked():
            gender = "Female"
        else:
            gender = "Not selected"
            
        info = f"Name: {name}\nAddress: {address}\nSex: {gender}"
        
        QMessageBox.information(self, "Submission Successful", info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec())
