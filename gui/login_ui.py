# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logne.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import gui.login_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1002, 620)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 921, 591))
        self.widget.setStyleSheet(u"QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(243, 179, 0, 0.98), stop:1 rgba(0, 102, 204, 1));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(50, 205, 50, 1), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}\n"
"QPushButton#pushButton_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(243, 179, 0, 0.98), stop:1 rgba(0, 102, 204, 1));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 140, 0, 1), stop:1 rg"
                        "ba(255, 200, 0, 1));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 921, 571))
        self.label_2.setStyleSheet(u"\n"
"\n"
"background-image: url(:/newPrefix/Rectangle 175 (1).png);")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Rectangle 175 (1).png"))
        self.exit = QPushButton(self.widget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(880, 0, 41, 28))
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(560, 70, 331, 421))
        self.frame.setMouseTracking(False)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 331, 40))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgba(0, 0, 0, 200);\n"
"")
        self.user_name = QLineEdit(self.frame)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(10, 90, 291, 41))
        self.user_name.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px;")
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(10, 170, 291, 41))
        self.password.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px;")
        self.password.setEchoMode(QLineEdit.Password)
        self.role = QComboBox(self.frame)
        self.role.addItem("")
        self.role.addItem("")
        self.role.setObjectName(u"role")
        self.role.setGeometry(QRect(10, 260, 291, 41))
        self.role.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px;\n"
"")
        self.forgot = QPushButton(parent=self.frame)
        self.forgot.setGeometry(QRect(205, 315, 100, 25))
        self.forgot.setStyleSheet(
            "QPushButton { "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 179, 0, 255), stop:1 rgba(255, 140, 0, 255)); "
            "color: rgba(255, 255, 255, 210); "
            "border-radius: 5px; "
            "font: 9pt 'Arial'; "
            "text-align: center; "
            "} "
            "QPushButton:hover { "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 140, 0, 255), stop:1 rgba(255, 200, 0, 255)); "
            "} "
            "QPushButton:pressed { "
            "padding-left: 5px; "
            "padding-top: 5px; "
            "background-color: rgba(150, 123, 111, 255); "
            "}"
        )
        self.forgot.setObjectName("forgot")
        self.login = QPushButton(parent=self.frame)
        self.login.setGeometry(QRect(70, 350, 201, 41))
        font = QFont()
        font.setFamily("Arial Rounded MT")
        font.setPointSize(11)
        font.setBold(True)
        self.login.setFont(font)
        self.login.setStyleSheet(
            "QPushButton { "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 102, 204, 255), stop:1 rgba(0, 153, 255, 255)); "
            "color: rgba(255, 255, 255, 210); "
            "border-radius: 5px; "
            "} "
            "QPushButton:hover { "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 153, 255, 255), stop:1 rgba(0, 204, 255, 255)); "
            "} "
            "QPushButton:pressed { "
            "padding-left: 5px; "
            "padding-top: 5px; "
            "background-color: rgba(0, 123, 255, 255); "
            "}"
        )
        self.login.setObjectName("login")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 101, 21))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 101, 31))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 230, 49, 21))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 320, 41, 31))
        self.label_10.setPixmap(QPixmap(u":/newPrefix/Frame.png"))
        self.label_10.setScaledContents(True)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 450, 151, 121))
        self.label_6.setPixmap(QPixmap(u":/newPrefix/icon-star-fly 1.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 71, 61))
        self.label_7.setStyleSheet(u"border-image: url(:/newPrefix/image 1.png);")
        self.label_7.setPixmap(QPixmap(u":/newPrefix/image 1.png"))
        self.label_7.setScaledContents(True)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 120, 281, 41))
        self.label_9.setPixmap(QPixmap(u":/newPrefix/Congratulations \ud83c\udf89.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 200, 431, 171))
        self.label_11.setPixmap(QPixmap(u":/newPrefix/Welcome back to our Desktop! This is the login page interface. Please log in to proceed with the next steps. Wishing you a very productive working day !!!.png"))
        self.label_11.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; font-style:italic; color:#0055ff;\">LOGIN</span></p></body></html>", None))
        self.user_name.setText("")
        self.user_name.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your user name", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your password", None))
        self.role.setItemText(0, QCoreApplication.translate("Form", u"User", None))
        self.role.setItemText(1, QCoreApplication.translate("Form", u"Admin", None))

        self.forgot.setText(QCoreApplication.translate("Form", u"Forgot your Log In ", None))
        self.login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">User Name</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Password</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Role</span></p></body></html>", None))
        self.label_10.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_9.setText("")
        self.label_11.setText("")
    # retranslateUi

