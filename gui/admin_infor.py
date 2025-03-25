# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_infor.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import gui.admin_infor_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(533, 377)
        icon = QIcon()
        icon.addFile(u":/user_in/2557006.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-image: url(:/user_in/Nen.png);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 531, 51))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 0, 91, 81))
        self.label_2.setStyleSheet(u"border-image: url(:/user_in/user.png);")
        self.field_name = QLabel(Form)
        self.field_name.setObjectName(u"field_name")
        self.field_name.setGeometry(QRect(20, 140, 141, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.field_name.setFont(font1)
        self.fiel_pass = QLabel(Form)
        self.fiel_pass.setObjectName(u"fiel_pass")
        self.fiel_pass.setGeometry(QRect(20, 190, 141, 31))
        self.fiel_pass.setFont(font1)
        self.field_role = QLabel(Form)
        self.field_role.setObjectName(u"field_role")
        self.field_role.setGeometry(QRect(20, 240, 141, 31))
        self.field_role.setFont(font1)
        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(170, 140, 361, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.name.setFont(font2)
        self.name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 190, 361, 31))
        self.password.setFont(font2)
        self.password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.role = QLineEdit(Form)
        self.role.setObjectName(u"role")
        self.role.setGeometry(QRect(170, 240, 361, 31))
        self.role.setFont(font2)
        self.role.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.update = QPushButton(Form)
        self.update.setObjectName(u"update")
        self.update.setGeometry(QRect(350, 290, 171, 41))
        self.update.setStyleSheet(u"background-color: rgb(66, 213, 108);")
        self.done = QPushButton(Form)
        self.done.setObjectName(u"done")
        self.done.setGeometry(QRect(180, 290, 161, 41))
        self.done.setStyleSheet(u"background-color: rgb(20, 109, 177);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Admin_infor", None))
        self.label.setText(QCoreApplication.translate("Form", u"Staff Infor App", None))
        self.label_2.setText("")
        self.field_name.setText(QCoreApplication.translate("Form", u"User Name", None))
        self.fiel_pass.setText(QCoreApplication.translate("Form", u"Password", None))
        self.field_role.setText(QCoreApplication.translate("Form", u"Role", None))
        self.name.setText(QCoreApplication.translate("Form", u"sfdb", None))
        self.password.setText(QCoreApplication.translate("Form", u"sfdb", None))
        self.role.setText(QCoreApplication.translate("Form", u"sfdb", None))
        self.update.setText(QCoreApplication.translate("Form", u"C\u1eadp nh\u1eadt", None))
        self.done.setText(QCoreApplication.translate("Form", u"Xong", None))
    # retranslateUi

