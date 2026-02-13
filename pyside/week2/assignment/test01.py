# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled01.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_fname = QLabel(self.centralwidget)
        self.lbl_fname.setObjectName(u"lbl_fname")
        self.lbl_fname.setGeometry(QRect(30, 20, 81, 16))
        font = QFont()
        font.setPointSize(13)
        self.lbl_fname.setFont(font)
        self.lbl_lname = QLabel(self.centralwidget)
        self.lbl_lname.setObjectName(u"lbl_lname")
        self.lbl_lname.setGeometry(QRect(30, 50, 81, 16))
        self.lbl_lname.setFont(font)
        self.lineEdit_fname = QLineEdit(self.centralwidget)
        self.lineEdit_fname.setObjectName(u"lineEdit_fname")
        self.lineEdit_fname.setGeometry(QRect(120, 20, 201, 21))
        self.lineEdit_lname = QLineEdit(self.centralwidget)
        self.lineEdit_lname.setObjectName(u"lineEdit_lname")
        self.lineEdit_lname.setGeometry(QRect(120, 50, 201, 21))
        self.radioButton_male = QRadioButton(self.centralwidget)
        self.radioButton_male.setObjectName(u"radioButton_male")
        self.radioButton_male.setGeometry(QRect(120, 80, 98, 24))
        self.radioButton_female = QRadioButton(self.centralwidget)
        self.radioButton_female.setObjectName(u"radioButton_female")
        self.radioButton_female.setGeometry(QRect(220, 80, 98, 24))
        self.submit_btn = QPushButton(self.centralwidget)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(170, 110, 81, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_fname.setText(QCoreApplication.translate("MainWindow", u"FirstName", None))
        self.lbl_lname.setText(QCoreApplication.translate("MainWindow", u"LastName", None))
        self.radioButton_male.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.radioButton_female.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())