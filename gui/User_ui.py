# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userhu.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QComboBox,
    QDateEdit, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)
from gui import User_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1384, 739)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1384, 739))
        icon = QIcon()
        icon.addFile(u":/Background/2557006.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.HomeFrame = QFrame(self.centralwidget)
        self.HomeFrame.setObjectName(u"HomeFrame")
        self.HomeFrame.setGeometry(QRect(190, 69, 1181, 581))
        self.HomeFrame.setStyleSheet(u"QFrame#HomeFrame{\n"
"background-color: rgb(221, 221, 221);\n"
"}\n"
"background-image: url(:/Background/Nen.png);")
        self.HomeFrame.setFrameShape(QFrame.NoFrame)
        self.gridLayout_3 = QGridLayout(self.HomeFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, -1, 0)
        self.tabWidget = QTabWidget(self.HomeFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        sizePolicy.setHeightForWidth(self.Dashboard.sizePolicy().hasHeightForWidth())
        self.Dashboard.setSizePolicy(sizePolicy)
        self.Products_Dash_Frame = QFrame(self.Dashboard)
        self.Products_Dash_Frame.setObjectName(u"Products_Dash_Frame")
        self.Products_Dash_Frame.setGeometry(QRect(860, 30, 281, 141))
        self.Products_Dash_Frame.setStyleSheet(u"background-color: rgb(105, 115, 255);\n"
"border-radius:5px;")
        self.Products_Dash_Frame.setFrameShape(QFrame.NoFrame)
        self.label_57 = QLabel(self.Products_Dash_Frame)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(56, 110, 151, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Products_Label = QLabel(self.Products_Dash_Frame)
        self.Total_Products_Label.setObjectName(u"Total_Products_Label")
        self.Total_Products_Label.setGeometry(QRect(210, 110, 51, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.Total_Products_Label.setFont(font1)
        self.Total_Products_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_6 = QWidget(self.Products_Dash_Frame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(90, 10, 101, 97))
        self.widget_6.setStyleSheet(u"background-image: url(:/Background/package.png);")
        self.Sales_Dash_Frame = QFrame(self.Dashboard)
        self.Sales_Dash_Frame.setObjectName(u"Sales_Dash_Frame")
        self.Sales_Dash_Frame.setGeometry(QRect(550, 30, 301, 141))
        self.Sales_Dash_Frame.setStyleSheet(u"background-color: rgb(54, 157, 185);\n"
"border-radius:5px;")
        self.Sales_Dash_Frame.setFrameShape(QFrame.NoFrame)
        self.label_59 = QLabel(self.Sales_Dash_Frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(90, 110, 101, 31))
        self.label_59.setFont(font)
        self.label_59.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Sales_Label = QLabel(self.Sales_Dash_Frame)
        self.Total_Sales_Label.setObjectName(u"Total_Sales_Label")
        self.Total_Sales_Label.setGeometry(QRect(200, 100, 51, 41))
        self.Total_Sales_Label.setFont(font1)
        self.Total_Sales_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_7 = QWidget(self.Sales_Dash_Frame)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(120, 10, 91, 91))
        self.widget_7.setStyleSheet(u"background-image: url(:/Background/increase.png);")
        self.Category_Dash_Frame = QFrame(self.Dashboard)
        self.Category_Dash_Frame.setObjectName(u"Category_Dash_Frame")
        self.Category_Dash_Frame.setGeometry(QRect(860, 180, 281, 161))
        self.Category_Dash_Frame.setStyleSheet(u"background-color: rgb(52, 73, 94);\n"
"border-radius:5px;")
        self.Category_Dash_Frame.setFrameShape(QFrame.NoFrame)
        self.Total_Category_Label = QLabel(self.Category_Dash_Frame)
        self.Total_Category_Label.setObjectName(u"Total_Category_Label")
        self.Total_Category_Label.setGeometry(QRect(220, 110, 21, 31))
        self.Total_Category_Label.setFont(font1)
        self.Total_Category_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64 = QLabel(self.Category_Dash_Frame)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(64, 110, 151, 31))
        self.label_64.setFont(font)
        self.label_64.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.widget_5 = QWidget(self.Category_Dash_Frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(90, 10, 101, 91))
        self.widget_5.setStyleSheet(u"background-image: url(:/Background/files_white.png);")
        self.calendar = QCalendarWidget(self.Dashboard)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(20, 10, 521, 331))
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setMinimumSize(QSize(350, 300))
        self.calendar.setAutoFillBackground(False)
        self.calendar.setStyleSheet(u"\n"
"border-radius:20px;")
        self.Employee_Dash_Frame = QFrame(self.Dashboard)
        self.Employee_Dash_Frame.setObjectName(u"Employee_Dash_Frame")
        self.Employee_Dash_Frame.setGeometry(QRect(550, 180, 301, 161))
        self.Employee_Dash_Frame.setStyleSheet(u"background-color: rgb(135, 213, 255);\n"
"border-radius:5px;")
        self.Employee_Dash_Frame.setFrameShape(QFrame.NoFrame)
        self.Total_Employee_Label = QLabel(self.Employee_Dash_Frame)
        self.Total_Employee_Label.setObjectName(u"Total_Employee_Label")
        self.Total_Employee_Label.setGeometry(QRect(190, 116, 31, 41))
        self.Total_Employee_Label.setFont(font1)
        self.widget_3 = QWidget(self.Employee_Dash_Frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(110, 0, 111, 101))
        self.widget_3.setStyleSheet(u"background-image: url(:/Background/shopping-cart .png);")
        self.Employee_Dash_Frame_2 = QFrame(self.Employee_Dash_Frame)
        self.Employee_Dash_Frame_2.setObjectName(u"Employee_Dash_Frame_2")
        self.Employee_Dash_Frame_2.setGeometry(QRect(250, 80, 261, 171))
        self.Employee_Dash_Frame_2.setStyleSheet(u"background-color: rgb(135, 213, 255);\n"
"border-radius:5px;")
        self.Employee_Dash_Frame_2.setFrameShape(QFrame.NoFrame)
        self.label_46 = QLabel(self.Employee_Dash_Frame_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(50, 120, 131, 31))
        self.label_46.setFont(font)
        self.Total_Employee_Label_2 = QLabel(self.Employee_Dash_Frame_2)
        self.Total_Employee_Label_2.setObjectName(u"Total_Employee_Label_2")
        self.Total_Employee_Label_2.setGeometry(QRect(190, 116, 31, 41))
        self.Total_Employee_Label_2.setFont(font1)
        self.widget_4 = QWidget(self.Employee_Dash_Frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(90, 10, 91, 91))
        self.widget_4.setStyleSheet(u"background-image: url(:/images/Images/teamwork.png);")
        self.label_60 = QLabel(self.Employee_Dash_Frame)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(90, 120, 121, 31))
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Sales_Label_2 = QLabel(self.Employee_Dash_Frame)
        self.Total_Sales_Label_2.setObjectName(u"Total_Sales_Label_2")
        self.Total_Sales_Label_2.setGeometry(QRect(200, 110, 51, 41))
        self.Total_Sales_Label_2.setFont(font1)
        self.Total_Sales_Label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(self.Dashboard)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_12 = QLabel(self.Dashboard)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Dashboard, "")
        self.label_12.raise_()
        self.Products_Dash_Frame.raise_()
        self.Sales_Dash_Frame.raise_()
        self.Category_Dash_Frame.raise_()
        self.calendar.raise_()
        self.Employee_Dash_Frame.raise_()
        self.Inventory = QWidget()
        self.Inventory.setObjectName(u"Inventory")
        self.label_13 = QLabel(self.Inventory)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 10, 1171, 41))
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setLocale(QLocale(QLocale.Welsh, QLocale.UnitedKingdom))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.Category_tableWidget = QTableWidget(self.Inventory)
        if (self.Category_tableWidget.columnCount() < 8):
            self.Category_tableWidget.setColumnCount(8)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font4 = QFont()
        font4.setBold(True)
        font4.setUnderline(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.Category_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignHCenter|Qt.AlignBottom);
        __qtablewidgetitem3.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.Category_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.Category_tableWidget.setObjectName(u"Category_tableWidget")
        self.Category_tableWidget.setGeometry(QRect(0, 190, 2331, 411))
        self.Category_tableWidget.setStyleSheet(u"QTableWidget#Category_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Category_tableWidget.setRowCount(0)
        self.groupBox_9 = QGroupBox(self.Inventory)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(210, 90, 711, 61))
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setFont(font3)
        self.groupBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Emp_SearchBy_Comb_2 = QComboBox(self.groupBox_9)
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.setObjectName(u"Emp_SearchBy_Comb_2")
        self.Emp_SearchBy_Comb_2.setGeometry(QRect(20, 21, 181, 31))
        self.Emp_SearchBy_Comb_2.setFont(font3)
        self.Emp_SearchBy_Comb_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Emp_Search_box_2 = QLineEdit(self.groupBox_9)
        self.Emp_Search_box_2.setObjectName(u"Emp_Search_box_2")
        self.Emp_Search_box_2.setGeometry(QRect(230, 20, 251, 31))
        self.Emp_Search_box_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.search_track_inventory = QPushButton(self.groupBox_9)
        self.search_track_inventory.setObjectName(u"search_track_inventory")
        self.search_track_inventory.setGeometry(QRect(560, 20, 141, 31))
        self.search_track_inventory.setFont(font3)
        self.search_track_inventory.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_track_inventory.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Background/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_track_inventory.setIcon(icon1)
        self.label_26 = QLabel(self.Inventory)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(-6, -25, 2331, 211))
        self.label_26.setStyleSheet(u"background-image: url(:/Background/banner_min.png);\n"
"")
        self.tabWidget.addTab(self.Inventory, "")
        self.label_26.raise_()
        self.label_13.raise_()
        self.Category_tableWidget.raise_()
        self.groupBox_9.raise_()
        self.Invoice = QWidget()
        self.Invoice.setObjectName(u"Invoice")
        self.tabWidget_2 = QTabWidget(self.Invoice)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 10, 1411, 531))
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.frame_3 = QFrame(self.tab_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 361, 481))
        self.frame_3.setStyleSheet(u"QFrame#frame_3{\n"
"border:1px solid rgb(213, 216, 220);\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 0, 351, 40))
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.groupBox_4 = QGroupBox(self.frame_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 50, 351, 91))
        self.groupBox_4.setFont(font3)
        self.Sales_Search_Product_Input = QLineEdit(self.groupBox_4)
        self.Sales_Search_Product_Input.setObjectName(u"Sales_Search_Product_Input")
        self.Sales_Search_Product_Input.setGeometry(QRect(115, 30, 131, 31))
        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 30, 101, 31))
        self.search_Invoice_btn = QPushButton(self.groupBox_4)
        self.search_Invoice_btn.setObjectName(u"search_Invoice_btn")
        self.search_Invoice_btn.setGeometry(QRect(255, 30, 91, 31))
        self.search_Invoice_btn.setFont(font3)
        self.search_Invoice_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_Invoice_btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.search_Invoice_btn.setIcon(icon1)
        self.Sales_Product_tableWidget = QTableWidget(self.frame_3)
        if (self.Sales_Product_tableWidget.columnCount() < 6):
            self.Sales_Product_tableWidget.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font3);
        self.Sales_Product_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        self.Sales_Product_tableWidget.setObjectName(u"Sales_Product_tableWidget")
        self.Sales_Product_tableWidget.setGeometry(QRect(0, 150, 351, 331))
        self.Sales_Product_tableWidget.setStyleSheet(u"QTableWidget#Sales_Product_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Sales_Product_tableWidget.setRowCount(0)
        self.groupBox_5 = QGroupBox(self.tab_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(380, 10, 441, 91))
        self.label_38 = QLabel(self.groupBox_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 40, 71, 51))
        self.label_38.setFont(font2)
        self.id = QLineEdit(self.groupBox_5)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(70, 50, 341, 31))
        self.Costomer_Bill_Area = QPlainTextEdit(self.tab_8)
        self.Costomer_Bill_Area.setObjectName(u"Costomer_Bill_Area")
        self.Costomer_Bill_Area.setGeometry(QRect(1870, 40, 461, 311))
        self.Costomer_Bill_Area.setFrameShape(QFrame.NoFrame)
        self.Costomer_Bill_Area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Costomer_Bill_Area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Costomer_Bill_Area.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Costomer_Bill_Area.setTabChangesFocus(False)
        self.Costomer_Bill_Area.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.Costomer_Bill_Area.setReadOnly(True)
        self.label_36 = QLabel(self.tab_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(1870, 0, 441, 40))
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_6 = QGroupBox(self.tab_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(380, 110, 441, 265))
        self.Product_Cart_tableWidget = QTableWidget(self.groupBox_6)
        if (self.Product_Cart_tableWidget.columnCount() < 6):
            self.Product_Cart_tableWidget.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font3);
        self.Product_Cart_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.Product_Cart_tableWidget.setObjectName(u"Product_Cart_tableWidget")
        self.Product_Cart_tableWidget.setGeometry(QRect(216, 35, 221, 225))
        self.Product_Cart_tableWidget.setStyleSheet(u"QTableWidget#Product_Cart_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Product_Cart_tableWidget.setRowCount(0)
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(217, 2, 221, 32))
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet(u"background-color: #dddddd;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_41.setTextFormat(Qt.PlainText)
        self.label_41.setMargin(0)
        self.label_41.setIndent(5)
        self.label_41.setOpenExternalLinks(False)
        self.frame_18 = QFrame(self.groupBox_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(2, -2, 206, 263))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.Calc_Input = QLineEdit(self.frame_18)
        self.Calc_Input.setObjectName(u"Calc_Input")
        self.Calc_Input.setGeometry(QRect(3, 6, 199, 51))
        font5 = QFont()
        font5.setPointSize(22)
        font5.setBold(True)
        self.Calc_Input.setFont(font5)
        self.Calc_Input.setLayoutDirection(Qt.LeftToRight)
        self.Calc_Input.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"color: rgb(47, 255, 0);\n"
"border-radius:5px;\n"
"padding-right:10px;\n"
"border:5px solid rgb(128, 139, 150) ;")
        self.Calc_Input.setMaxLength(9)
        self.Calc_Input.setCursorPosition(0)
        self.Calc_Plus_Btn = QPushButton(self.frame_18)
        self.Calc_Plus_Btn.setObjectName(u"Calc_Plus_Btn")
        self.Calc_Plus_Btn.setGeometry(QRect(153, 60, 49, 49))
        self.Calc_Plus_Btn.setFont(font1)
        self.Calc_Plus_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_Plus_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_9_Btn = QPushButton(self.frame_18)
        self.Calc_9_Btn.setObjectName(u"Calc_9_Btn")
        self.Calc_9_Btn.setGeometry(QRect(103, 60, 49, 49))
        self.Calc_9_Btn.setFont(font1)
        self.Calc_9_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_9_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_7_Btn = QPushButton(self.frame_18)
        self.Calc_7_Btn.setObjectName(u"Calc_7_Btn")
        self.Calc_7_Btn.setGeometry(QRect(3, 60, 49, 49))
        self.Calc_7_Btn.setFont(font1)
        self.Calc_7_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_7_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_8_Btn = QPushButton(self.frame_18)
        self.Calc_8_Btn.setObjectName(u"Calc_8_Btn")
        self.Calc_8_Btn.setGeometry(QRect(53, 60, 49, 49))
        self.Calc_8_Btn.setFont(font1)
        self.Calc_8_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_8_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_Minus_Btn = QPushButton(self.frame_18)
        self.Calc_Minus_Btn.setObjectName(u"Calc_Minus_Btn")
        self.Calc_Minus_Btn.setGeometry(QRect(153, 110, 49, 49))
        self.Calc_Minus_Btn.setFont(font1)
        self.Calc_Minus_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_Minus_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_6_Btn = QPushButton(self.frame_18)
        self.Calc_6_Btn.setObjectName(u"Calc_6_Btn")
        self.Calc_6_Btn.setGeometry(QRect(103, 110, 49, 49))
        self.Calc_6_Btn.setFont(font1)
        self.Calc_6_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_6_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_5_Btn = QPushButton(self.frame_18)
        self.Calc_5_Btn.setObjectName(u"Calc_5_Btn")
        self.Calc_5_Btn.setGeometry(QRect(53, 110, 49, 49))
        self.Calc_5_Btn.setFont(font1)
        self.Calc_5_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_5_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_4_Btn = QPushButton(self.frame_18)
        self.Calc_4_Btn.setObjectName(u"Calc_4_Btn")
        self.Calc_4_Btn.setGeometry(QRect(3, 110, 49, 49))
        self.Calc_4_Btn.setFont(font1)
        self.Calc_4_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_4_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_1_Btn = QPushButton(self.frame_18)
        self.Calc_1_Btn.setObjectName(u"Calc_1_Btn")
        self.Calc_1_Btn.setGeometry(QRect(3, 160, 49, 49))
        self.Calc_1_Btn.setFont(font1)
        self.Calc_1_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_1_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_2_Btn = QPushButton(self.frame_18)
        self.Calc_2_Btn.setObjectName(u"Calc_2_Btn")
        self.Calc_2_Btn.setGeometry(QRect(53, 160, 49, 49))
        self.Calc_2_Btn.setFont(font1)
        self.Calc_2_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_2_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_Multiplied_Btn = QPushButton(self.frame_18)
        self.Calc_Multiplied_Btn.setObjectName(u"Calc_Multiplied_Btn")
        self.Calc_Multiplied_Btn.setGeometry(QRect(153, 160, 49, 49))
        self.Calc_Multiplied_Btn.setFont(font1)
        self.Calc_Multiplied_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_Multiplied_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_3_Btn = QPushButton(self.frame_18)
        self.Calc_3_Btn.setObjectName(u"Calc_3_Btn")
        self.Calc_3_Btn.setGeometry(QRect(103, 160, 49, 49))
        self.Calc_3_Btn.setFont(font1)
        self.Calc_3_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_3_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_0_Btn = QPushButton(self.frame_18)
        self.Calc_0_Btn.setObjectName(u"Calc_0_Btn")
        self.Calc_0_Btn.setGeometry(QRect(3, 210, 49, 49))
        self.Calc_0_Btn.setFont(font1)
        self.Calc_0_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_0_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_C_Btn = QPushButton(self.frame_18)
        self.Calc_C_Btn.setObjectName(u"Calc_C_Btn")
        self.Calc_C_Btn.setGeometry(QRect(53, 210, 49, 49))
        self.Calc_C_Btn.setFont(font1)
        self.Calc_C_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_C_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(241, 196, 15);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_Equals_Btn = QPushButton(self.frame_18)
        self.Calc_Equals_Btn.setObjectName(u"Calc_Equals_Btn")
        self.Calc_Equals_Btn.setGeometry(QRect(103, 210, 49, 49))
        self.Calc_Equals_Btn.setFont(font1)
        self.Calc_Equals_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_Equals_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.Calc_Divided_Btn = QPushButton(self.frame_18)
        self.Calc_Divided_Btn.setObjectName(u"Calc_Divided_Btn")
        self.Calc_Divided_Btn.setGeometry(QRect(153, 210, 49, 49))
        self.Calc_Divided_Btn.setFont(font1)
        self.Calc_Divided_Btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Calc_Divided_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(23, 32, 42);\n"
"  color: rgb(251, 252, 252);\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(33, 47, 61);\n"
"}")
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(272, 10, 101, 20))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.label_45.setFont(font6)
        self.label_45.setStyleSheet(u"color: rgb(28, 40, 51);")
        self.Label_Total_Products = QLabel(self.groupBox_6)
        self.Label_Total_Products.setObjectName(u"Label_Total_Products")
        self.Label_Total_Products.setGeometry(QRect(378, 6, 31, 21))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.Label_Total_Products.setFont(font7)
        self.Label_Total_Products.setStyleSheet(u"color: #283747;")
        self.pushButton = QPushButton(self.groupBox_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(219, 7, 41, 23))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background: #dddddd;\n"
"color: rgb(255, 255, 255);\n"
"border:0;")
        icon2 = QIcon()
        icon2.addFile(u":/images/Images/cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))
        self.quantity = QGroupBox(self.tab_8)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setGeometry(QRect(380, 370, 441, 121))
        self.Price_PreQty_Bill_Area = QLineEdit(self.quantity)
        self.Price_PreQty_Bill_Area.setObjectName(u"Price_PreQty_Bill_Area")
        self.Price_PreQty_Bill_Area.setGeometry(QRect(180, 40, 131, 31))
        self.Price_PreQty_Bill_Area.setStyleSheet(u"background-color: rgb(255, 255, 206);")
        self.Cuantity_Bill_Area = QLineEdit(self.quantity)
        self.Cuantity_Bill_Area.setObjectName(u"Cuantity_Bill_Area")
        self.Cuantity_Bill_Area.setGeometry(QRect(320, 40, 101, 31))
        self.Cuantity_Bill_Area.setStyleSheet(u"background-color: rgb(255, 255, 206);")
        self.Cart_Clear_Btn = QPushButton(self.quantity)
        self.Cart_Clear_Btn.setObjectName(u"Cart_Clear_Btn")
        self.Cart_Clear_Btn.setGeometry(QRect(190, 80, 91, 31))
        self.Cart_Clear_Btn.setFont(font3)
        self.Cart_Clear_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Cart_Clear_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Background/clean.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Cart_Clear_Btn.setIcon(icon3)
        self.Add_Update_Cart_Btn = QPushButton(self.quantity)
        self.Add_Update_Cart_Btn.setObjectName(u"Add_Update_Cart_Btn")
        self.Add_Update_Cart_Btn.setGeometry(QRect(290, 80, 131, 31))
        self.Add_Update_Cart_Btn.setFont(font3)
        self.Add_Update_Cart_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add_Update_Cart_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#00a8ff;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(93, 173, 226);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Background/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Add_Update_Cart_Btn.setIcon(icon4)
        self.label_42 = QLabel(self.quantity)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(180, 10, 121, 21))
        self.label_42.setFont(font2)
        self.label_43 = QLabel(self.quantity)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 10, 91, 21))
        self.label_43.setFont(font2)
        self.label_44 = QLabel(self.quantity)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(320, 10, 91, 21))
        self.label_44.setFont(font2)
        self.In_Stock_Title = QLabel(self.quantity)
        self.In_Stock_Title.setObjectName(u"In_Stock_Title")
        self.In_Stock_Title.setGeometry(QRect(20, 83, 71, 21))
        self.In_Stock_Title.setFont(font2)
        self.delete_invoice_btn = QPushButton(self.quantity)
        self.delete_invoice_btn.setObjectName(u"delete_invoice_btn")
        self.delete_invoice_btn.setGeometry(QRect(100, 80, 81, 31))
        self.delete_invoice_btn.setFont(font3)
        self.delete_invoice_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_invoice_btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(231, 76, 60);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(236, 112, 99);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Background/bin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_invoice_btn.setIcon(icon5)
        self.delete_invoice_btn.setIconSize(QSize(15, 15))
        self.date = QDateEdit(self.quantity)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(20, 40, 151, 31))
        self.frame_11 = QFrame(self.tab_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(1880, 370, 431, 131))
        self.frame_11.setStyleSheet(u"QFrame#frame_11{\n"
"border:1px solid rgb(213, 216, 220);\n"
"}")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.Print_Bill_Btn = QPushButton(self.frame_11)
        self.Print_Bill_Btn.setObjectName(u"Print_Bill_Btn")
        self.Print_Bill_Btn.setGeometry(QRect(50, 80, 101, 44))
        self.Print_Bill_Btn.setFont(font3)
        self.Print_Bill_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Print_Bill_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: #eb3b5a;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/Images/printing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Print_Bill_Btn.setIcon(icon6)
        self.Clear_All_Btn = QPushButton(self.frame_11)
        self.Clear_All_Btn.setObjectName(u"Clear_All_Btn")
        self.Clear_All_Btn.setGeometry(QRect(180, 80, 101, 44))
        self.Clear_All_Btn.setFont(font3)
        self.Clear_All_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Clear_All_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/Images/clean.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Clear_All_Btn.setIcon(icon7)
        self.Generate_Bill_Btn = QPushButton(self.frame_11)
        self.Generate_Bill_Btn.setObjectName(u"Generate_Bill_Btn")
        self.Generate_Bill_Btn.setGeometry(QRect(320, 80, 101, 44))
        self.Generate_Bill_Btn.setFont(font3)
        self.Generate_Bill_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Generate_Bill_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: #009432;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../../checking.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Generate_Bill_Btn.setIcon(icon8)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(30, 2, 131, 68))
        self.frame_12.setStyleSheet(u"  background-color: #0652DD;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 10, 71, 21))
        self.label_39.setFont(font2)
        self.Label_Bill_Amnt = QLabel(self.frame_12)
        self.Label_Bill_Amnt.setObjectName(u"Label_Bill_Amnt")
        self.Label_Bill_Amnt.setGeometry(QRect(10, 37, 101, 21))
        self.Label_Bill_Amnt.setFont(font2)
        self.Label_Bill_Amnt.setLayoutDirection(Qt.LeftToRight)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(170, 2, 131, 68))
        self.frame_13.setStyleSheet(u"  background-color: rgb(125, 60, 152);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(30, 10, 111, 21))
        self.label_47.setFont(font2)
        self.label_48 = QLabel(self.frame_13)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(60, 36, 51, 21))
        self.label_48.setFont(font2)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(310, 0, 121, 68))
        self.frame_14.setStyleSheet(u"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.Label_Net_Pay = QLabel(self.frame_14)
        self.Label_Net_Pay.setObjectName(u"Label_Net_Pay")
        self.Label_Net_Pay.setGeometry(QRect(0, 35, 111, 21))
        self.Label_Net_Pay.setFont(font2)
        self.label_50 = QLabel(self.frame_14)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(25, 10, 81, 21))
        self.label_50.setFont(font2)
        self.label_35 = QLabel(self.tab_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 500, 1561, 35))
        self.label_35.setFont(font6)
        self.label_35.setStyleSheet(u"background-color: rgb(215, 219, 221);\n"
"color: rgb(23, 32, 42);")
        self.label_35.setTextFormat(Qt.PlainText)
        self.label_35.setMargin(0)
        self.label_35.setIndent(5)
        self.label_35.setOpenExternalLinks(False)
        self.label_37 = QLabel(self.tab_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(380, 0, 441, 40))
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.frame_15 = QFrame(self.tab_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(840, 370, 311, 131))
        self.frame_15.setStyleSheet(u"QFrame#frame_11{\n"
"border:1px solid rgb(213, 216, 220);\n"
"}")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.Print_Bill_Btn_2 = QPushButton(self.frame_15)
        self.Print_Bill_Btn_2.setObjectName(u"Print_Bill_Btn_2")
        self.Print_Bill_Btn_2.setGeometry(QRect(20, 80, 101, 44))
        self.Print_Bill_Btn_2.setFont(font3)
        self.Print_Bill_Btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Print_Bill_Btn_2.setStyleSheet(u"QPushButton{\n"
"  background-color: #eb3b5a;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Background/printing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Print_Bill_Btn_2.setIcon(icon9)
        self.Clear_All_Btn_2 = QPushButton(self.frame_15)
        self.Clear_All_Btn_2.setObjectName(u"Clear_All_Btn_2")
        self.Clear_All_Btn_2.setGeometry(QRect(130, 80, 81, 44))
        self.Clear_All_Btn_2.setFont(font3)
        self.Clear_All_Btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Clear_All_Btn_2.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Background/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Clear_All_Btn_2.setIcon(icon10)
        self.Generate_Bill_Btn_2 = QPushButton(self.frame_15)
        self.Generate_Bill_Btn_2.setObjectName(u"Generate_Bill_Btn_2")
        self.Generate_Bill_Btn_2.setGeometry(QRect(220, 80, 81, 44))
        self.Generate_Bill_Btn_2.setFont(font3)
        self.Generate_Bill_Btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Generate_Bill_Btn_2.setStyleSheet(u"QPushButton{\n"
"  background-color: #009432;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Background/invoice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Generate_Bill_Btn_2.setIcon(icon11)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(20, 2, 91, 68))
        self.frame_16.setStyleSheet(u"  background-color: #0652DD;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.label_51 = QLabel(self.frame_16)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 10, 71, 21))
        self.label_51.setFont(font2)
        self.Label_Bill_Amnt_2 = QLabel(self.frame_16)
        self.Label_Bill_Amnt_2.setObjectName(u"Label_Bill_Amnt_2")
        self.Label_Bill_Amnt_2.setGeometry(QRect(40, 40, 101, 21))
        self.Label_Bill_Amnt_2.setFont(font2)
        self.Label_Bill_Amnt_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(120, 2, 91, 68))
        self.frame_17.setStyleSheet(u"  background-color: rgb(125, 60, 152);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.label_52 = QLabel(self.frame_17)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 10, 111, 21))
        self.label_52.setFont(font2)
        self.label_53 = QLabel(self.frame_17)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(30, 40, 51, 21))
        self.label_53.setFont(font2)
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(220, 0, 81, 68))
        self.frame_19.setStyleSheet(u"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:5px;")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.Label_Net_Pay_2 = QLabel(self.frame_19)
        self.Label_Net_Pay_2.setObjectName(u"Label_Net_Pay_2")
        self.Label_Net_Pay_2.setGeometry(QRect(30, 40, 111, 21))
        self.Label_Net_Pay_2.setFont(font2)
        self.label_54 = QLabel(self.frame_19)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 10, 81, 21))
        self.label_54.setFont(font2)
        self.label_55 = QLabel(self.tab_8)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(830, 0, 331, 40))
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_55.setAlignment(Qt.AlignCenter)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.Costomer_Bill_Area.raise_()
        self.frame_3.raise_()
        self.groupBox_5.raise_()
        self.label_36.raise_()
        self.groupBox_6.raise_()
        self.quantity.raise_()
        self.frame_11.raise_()
        self.label_35.raise_()
        self.label_37.raise_()
        self.frame_15.raise_()
        self.label_55.raise_()
        self.Costomer_Bill_Area_2 = QPlainTextEdit(self.Invoice)
        self.Costomer_Bill_Area_2.setObjectName(u"Costomer_Bill_Area_2")
        self.Costomer_Bill_Area_2.setGeometry(QRect(840, 80, 321, 311))
        self.Costomer_Bill_Area_2.setFrameShape(QFrame.NoFrame)
        self.Costomer_Bill_Area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Costomer_Bill_Area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Costomer_Bill_Area_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Costomer_Bill_Area_2.setTabChangesFocus(False)
        self.Costomer_Bill_Area_2.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.Costomer_Bill_Area_2.setReadOnly(True)
        self.tabWidget.addTab(self.Invoice, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(1363, 641))
        self.frame_4.setStyleSheet(u"\n"
"background-image: url(:/Background/Nen.png);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 650, 1361, 35))
        self.label_49.setFont(font6)
        self.label_49.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_49.setStyleSheet(u"background-color: rgb(215, 219, 221);\n"
"color: rgb(23, 32, 42);")
        self.label_49.setTextFormat(Qt.PlainText)
        self.label_49.setScaledContents(True)
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_49.setMargin(0)
        self.label_49.setIndent(5)
        self.label_49.setOpenExternalLinks(False)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 2601, 61))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-image: url(:/Background/Nen.png);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.logout_Btn = QPushButton(self.frame)
        self.logout_Btn.setObjectName(u"logout_Btn")
        self.logout_Btn.setGeometry(QRect(1230, 0, 131, 61))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.logout_Btn.setFont(font8)
        self.logout_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logout_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Background/power.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_Btn.setIcon(icon12)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -20, 1231, 101))
        font9 = QFont()
        font9.setFamilies([u"PNU Medium"])
        font9.setPointSize(19)
        font9.setBold(True)
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.info = QPushButton(self.frame_4)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(0, 60, 181, 31))
        palette = QPalette()
        brush = QBrush(QColor(0, 26, 104, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 228))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(249, 249, 249, 77))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 92))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.info.setPalette(palette)
        self.info.setFont(font7)
        self.PanalFrame = QFrame(self.frame_4)
        self.PanalFrame.setObjectName(u"PanalFrame")
        self.PanalFrame.setGeometry(QRect(0, 100, 191, 541))
        sizePolicy.setHeightForWidth(self.PanalFrame.sizePolicy().hasHeightForWidth())
        self.PanalFrame.setSizePolicy(sizePolicy)
        self.PanalFrame.setAutoFillBackground(False)
        self.PanalFrame.setStyleSheet(u"QGroupBox {\n"
"    background-color: transparent; \n"
"    border: 1px solid gray;        \n"
"}\n"
"background-image: url(:/Background/Nen.png);")
        self.PanalFrame.setFrameShape(QFrame.NoFrame)
        self.Dash_Button = QPushButton(self.PanalFrame)
        self.Dash_Button.setObjectName(u"Dash_Button")
        self.Dash_Button.setGeometry(QRect(10, 290, 171, 51))
        self.Dash_Button.setFont(font8)
        self.Dash_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Dash_Button.setLayoutDirection(Qt.LeftToRight)
        self.Dash_Button.setAutoFillBackground(False)
        self.Dash_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon13 = QIcon()
        icon13.addFile(u":/Background/_ionicons_svg_md-easel (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Dash_Button.setIcon(icon13)
        self.Dash_Button.setIconSize(QSize(24, 24))
        self.Dash_Button.setAutoDefault(False)
        self.Dash_Button.setFlat(False)
        self.widget = QWidget(self.PanalFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 141, 131))
        self.widget.setStyleSheet(u"border-image: url(:/Background/group(1).png);")
        self.Supplier_Button_2 = QPushButton(self.PanalFrame)
        self.Supplier_Button_2.setObjectName(u"Supplier_Button_2")
        self.Supplier_Button_2.setGeometry(QRect(10, 350, 171, 51))
        self.Supplier_Button_2.setFont(font8)
        self.Supplier_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Button_2.setLayoutDirection(Qt.LeftToRight)
        self.Supplier_Button_2.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        self.Supplier_Button_2.setIcon(icon11)
        self.Supplier_Button_2.setIconSize(QSize(24, 24))
        self.Employee_Button = QPushButton(self.PanalFrame)
        self.Employee_Button.setObjectName(u"Employee_Button")
        self.Employee_Button.setGeometry(QRect(10, 410, 171, 51))
        self.Employee_Button.setFont(font8)
        self.Employee_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Employee_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon14 = QIcon()
        icon14.addFile(u":/Background/recycle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Employee_Button.setIcon(icon14)
        self.Employee_Button.setIconSize(QSize(24, 24))
        self.Supplier_Button = QPushButton(self.PanalFrame)
        self.Supplier_Button.setObjectName(u"Supplier_Button")
        self.Supplier_Button.setGeometry(QRect(10, 470, 171, 51))
        self.Supplier_Button.setFont(font8)
        self.Supplier_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Button.setLayoutDirection(Qt.LeftToRight)
        self.Supplier_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        self.Supplier_Button.setIcon(icon11)
        self.Supplier_Button.setIconSize(QSize(24, 24))
        self.label_2 = QLabel(self.PanalFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 240, 111, 31))
        font10 = QFont()
        font10.setPointSize(20)
        font10.setBold(True)
        self.label_2.setFont(font10)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_4.raise_()
        self.HomeFrame.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.logout_Btn, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.Employee_Button)
        QWidget.setTabOrder(self.Employee_Button, self.Dash_Button)
        QWidget.setTabOrder(self.Dash_Button, self.calendar)
        QWidget.setTabOrder(self.calendar, self.Category_tableWidget)
        QWidget.setTabOrder(self.Category_tableWidget, self.Emp_SearchBy_Comb_2)
        QWidget.setTabOrder(self.Emp_SearchBy_Comb_2, self.Emp_Search_box_2)
        QWidget.setTabOrder(self.Emp_Search_box_2, self.search_track_inventory)
        QWidget.setTabOrder(self.search_track_inventory, self.Supplier_Button)
        QWidget.setTabOrder(self.Supplier_Button, self.Sales_Search_Product_Input)
        QWidget.setTabOrder(self.Sales_Search_Product_Input, self.Sales_Product_tableWidget)
        QWidget.setTabOrder(self.Sales_Product_tableWidget, self.id)
        QWidget.setTabOrder(self.id, self.Costomer_Bill_Area)
        QWidget.setTabOrder(self.Costomer_Bill_Area, self.Product_Cart_tableWidget)
        QWidget.setTabOrder(self.Product_Cart_tableWidget, self.Calc_Input)
        QWidget.setTabOrder(self.Calc_Input, self.Calc_Plus_Btn)
        QWidget.setTabOrder(self.Calc_Plus_Btn, self.Calc_9_Btn)
        QWidget.setTabOrder(self.Calc_9_Btn, self.Calc_7_Btn)
        QWidget.setTabOrder(self.Calc_7_Btn, self.Calc_8_Btn)
        QWidget.setTabOrder(self.Calc_8_Btn, self.Calc_Minus_Btn)
        QWidget.setTabOrder(self.Calc_Minus_Btn, self.Calc_6_Btn)
        QWidget.setTabOrder(self.Calc_6_Btn, self.Calc_5_Btn)
        QWidget.setTabOrder(self.Calc_5_Btn, self.Calc_4_Btn)
        QWidget.setTabOrder(self.Calc_4_Btn, self.Calc_1_Btn)
        QWidget.setTabOrder(self.Calc_1_Btn, self.Calc_2_Btn)
        QWidget.setTabOrder(self.Calc_2_Btn, self.Calc_Multiplied_Btn)
        QWidget.setTabOrder(self.Calc_Multiplied_Btn, self.Calc_3_Btn)
        QWidget.setTabOrder(self.Calc_3_Btn, self.Calc_0_Btn)
        QWidget.setTabOrder(self.Calc_0_Btn, self.Calc_C_Btn)
        QWidget.setTabOrder(self.Calc_C_Btn, self.Calc_Equals_Btn)
        QWidget.setTabOrder(self.Calc_Equals_Btn, self.Calc_Divided_Btn)
        QWidget.setTabOrder(self.Calc_Divided_Btn, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.Price_PreQty_Bill_Area)
        QWidget.setTabOrder(self.Price_PreQty_Bill_Area, self.Cuantity_Bill_Area)
        QWidget.setTabOrder(self.Cuantity_Bill_Area, self.Cart_Clear_Btn)
        QWidget.setTabOrder(self.Cart_Clear_Btn, self.Add_Update_Cart_Btn)
        QWidget.setTabOrder(self.Add_Update_Cart_Btn, self.Print_Bill_Btn)
        QWidget.setTabOrder(self.Print_Bill_Btn, self.Clear_All_Btn)
        QWidget.setTabOrder(self.Clear_All_Btn, self.Generate_Bill_Btn)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inventory and Invoice Management - Enduser", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total Product's", None))
        self.Total_Products_Label.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None))
        self.Total_Sales_Label.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Total_Category_Label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Total Invoice", None))
        self.Total_Employee_Label.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Total Employee", None))
        self.Total_Employee_Label_2.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Total Value", None))
        self.Total_Sales_Label_2.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_12.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dashboard), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tracking Inventory", None))
        ___qtablewidgetitem = self.Category_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product_name", None));
        ___qtablewidgetitem1 = self.Category_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem2 = self.Category_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Current stock", None));
        ___qtablewidgetitem3 = self.Category_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Stock value", None));
        ___qtablewidgetitem4 = self.Category_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stock cost", None));
        ___qtablewidgetitem5 = self.Category_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Reorder level", None));
        ___qtablewidgetitem6 = self.Category_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Reorder-require", None));
        ___qtablewidgetitem7 = self.Category_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Location num", None));
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Search Inventory", None))
        self.Emp_SearchBy_Comb_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Product name", None))
        self.Emp_SearchBy_Comb_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Category", None))
        self.Emp_SearchBy_Comb_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Location number", None))

        self.search_track_inventory.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_26.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory), QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"All Inovice", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Search Invoice Categories", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Invoice_Date", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Price", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Status", None))

        self.search_Invoice_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem8 = self.Sales_Product_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Invoice_ID", None));
        ___qtablewidgetitem9 = self.Sales_Product_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem10 = self.Sales_Product_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Invoice_date", None));
        ___qtablewidgetitem11 = self.Sales_Product_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"QTY", None));
        ___qtablewidgetitem12 = self.Sales_Product_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem13 = self.Sales_Product_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.groupBox_5.setTitle("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Costomer Invoice's Area", None))
        self.groupBox_6.setTitle("")
        ___qtablewidgetitem14 = self.Product_Cart_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Invoice_date", None));
        ___qtablewidgetitem15 = self.Product_Cart_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Product name", None));
        ___qtablewidgetitem16 = self.Product_Cart_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Invocie_date", None));
        ___qtablewidgetitem17 = self.Product_Cart_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"QTY", None));
        ___qtablewidgetitem18 = self.Product_Cart_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem19 = self.Product_Cart_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.label_41.setText("")
        self.Calc_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Calc_Plus_Btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Calc_9_Btn.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Calc_7_Btn.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Calc_8_Btn.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Calc_Minus_Btn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Calc_6_Btn.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Calc_5_Btn.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Calc_4_Btn.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Calc_1_Btn.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Calc_2_Btn.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Calc_Multiplied_Btn.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.Calc_3_Btn.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Calc_0_Btn.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Calc_C_Btn.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Calc_Equals_Btn.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Calc_Divided_Btn.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Total Product's :", None))
        self.Label_Total_Products.setText(QCoreApplication.translate("MainWindow", u" [0]", None))
        self.pushButton.setText("")
        self.quantity.setTitle("")
        self.Cart_Clear_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Add_Update_Cart_Btn.setText(QCoreApplication.translate("MainWindow", u"Add/ Update ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Price Pre QTY", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.In_Stock_Title.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.delete_invoice_btn.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.Print_Bill_Btn.setText(QCoreApplication.translate("MainWindow", u" Print", None))
        self.Clear_All_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.Generate_Bill_Btn.setText(QCoreApplication.translate("MainWindow", u"Generate Bill", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Bill Amount", None))
        self.Label_Bill_Amnt.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"[5%]", None))
        self.Label_Net_Pay.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Net Pay", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u" Note:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Customer Invoice's Area", None))
        self.Print_Bill_Btn_2.setText(QCoreApplication.translate("MainWindow", u" Print", None))
        self.Clear_All_Btn_2.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.Generate_Bill_Btn_2.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Bill Amount", None))
        self.Label_Bill_Amnt_2.setText(QCoreApplication.translate("MainWindow", u"[50]", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"[5%]", None))
        self.Label_Net_Pay_2.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Net Pay", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Customer Invoice's Area", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Billing / Purchase ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Invoice), QCoreApplication.translate("MainWindow", u"Invocie", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"A Desktop App Product Power by Group 11", None))
        self.logout_Btn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Group 11 Inventory Management System", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.Dash_Button.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.Supplier_Button_2.setText(QCoreApplication.translate("MainWindow", u" Report", None))
        self.Employee_Button.setText(QCoreApplication.translate("MainWindow", u" Inventory", None))
        self.Supplier_Button.setText(QCoreApplication.translate("MainWindow", u" Invoice", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
    # retranslateUi

