# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from gui import Admin_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1431, 759)
        MainWindow.setMinimumSize(QSize(1365, 670))
        icon = QIcon()
        icon.addFile(u":/Logo/2557006.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PanalFrame = QFrame(self.centralwidget)
        self.PanalFrame.setObjectName(u"PanalFrame")
        self.PanalFrame.setGeometry(QRect(20, 100, 221, 521))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PanalFrame.sizePolicy().hasHeightForWidth())
        self.PanalFrame.setSizePolicy(sizePolicy)
        self.PanalFrame.setStyleSheet(u"\n"
"QFrame#PanalFrame{\n"
"background-color: 0;\n"
"}")
        self.PanalFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.widget = QWidget(self.PanalFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 141, 131))
        self.widget.setStyleSheet(u"background-image: url(:/Logo big menu/stock.png);")
        self.Menu_Title = QWidget(self.PanalFrame)
        self.Menu_Title.setObjectName(u"Menu_Title")
        self.Menu_Title.setGeometry(QRect(0, 160, 211, 51))
        self.Menu_Title.setStyleSheet(u"QWidget#Menu_Title{\n"
"background-color: rgb(241, 196, 15);\n"
"border-radius: 5px;\n"
"}")
        self.label_2 = QLabel(self.Menu_Title)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 71, 31))
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.Employee_Button = QPushButton(self.PanalFrame)
        self.Employee_Button.setObjectName(u"Employee_Button")
        self.Employee_Button.setGeometry(QRect(0, 310, 211, 51))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.Employee_Button.setFont(font1)
        self.Employee_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Employee_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon1 = QIcon()
        icon1.addFile(u":/Button/recycle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Employee_Button.setIcon(icon1)
        self.Employee_Button.setIconSize(QSize(24, 24))
        self.Supplier_Button = QPushButton(self.PanalFrame)
        self.Supplier_Button.setObjectName(u"Supplier_Button")
        self.Supplier_Button.setGeometry(QRect(0, 260, 211, 51))
        self.Supplier_Button.setFont(font1)
        self.Supplier_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Supplier_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon2 = QIcon()
        icon2.addFile(u":/Button/invoice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Supplier_Button.setIcon(icon2)
        self.Supplier_Button.setIconSize(QSize(24, 24))
        self.Category_Button = QPushButton(self.PanalFrame)
        self.Category_Button.setObjectName(u"Category_Button")
        self.Category_Button.setGeometry(QRect(0, 360, 211, 51))
        self.Category_Button.setFont(font1)
        self.Category_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Category_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon3 = QIcon()
        icon3.addFile(u":/Button/user (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Category_Button.setIcon(icon3)
        self.Category_Button.setIconSize(QSize(24, 24))
        self.Products_Button = QPushButton(self.PanalFrame)
        self.Products_Button.setObjectName(u"Products_Button")
        self.Products_Button.setGeometry(QRect(0, 460, 211, 51))
        self.Products_Button.setFont(font1)
        self.Products_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Products_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon4 = QIcon()
        icon4.addFile(u":/Button/report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Products_Button.setIcon(icon4)
        self.Products_Button.setIconSize(QSize(24, 24))
        self.Dash_Button = QPushButton(self.PanalFrame)
        self.Dash_Button.setObjectName(u"Dash_Button")
        self.Dash_Button.setGeometry(QRect(0, 210, 211, 51))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.Dash_Button.setFont(font2)
        self.Dash_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Dash_Button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Dash_Button.setAutoFillBackground(False)
        self.Dash_Button.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon5 = QIcon()
        icon5.addFile(u":/Button/_ionicons_svg_md-easel (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Dash_Button.setIcon(icon5)
        self.Dash_Button.setIconSize(QSize(24, 24))
        self.Dash_Button.setAutoDefault(False)
        self.Dash_Button.setFlat(False)
        self.Category_Button_2 = QPushButton(self.PanalFrame)
        self.Category_Button_2.setObjectName(u"Category_Button_2")
        self.Category_Button_2.setGeometry(QRect(0, 410, 211, 51))
        self.Category_Button_2.setFont(font1)
        self.Category_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Category_Button_2.setStyleSheet(u"text-align: left;\n"
"padding-left:20px;")
        icon6 = QIcon()
        icon6.addFile(u":/Button/supplier (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Category_Button_2.setIcon(icon6)
        self.Category_Button_2.setIconSize(QSize(24, 24))
        self.HomeFrame = QFrame(self.centralwidget)
        self.HomeFrame.setObjectName(u"HomeFrame")
        self.HomeFrame.setGeometry(QRect(236, 99, 1141, 541))
        sizePolicy.setHeightForWidth(self.HomeFrame.sizePolicy().hasHeightForWidth())
        self.HomeFrame.setSizePolicy(sizePolicy)
        self.HomeFrame.setMinimumSize(QSize(500, 40))
        self.HomeFrame.setStyleSheet(u"QFrame#HomeFrame{\n"
"background-color: rgb(221, 221, 221);\n"
"}\n"
"background-image: url(:/Background/Nen.png);")
        self.HomeFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.HomeFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TrackingInvoice_2 = QTabWidget(self.HomeFrame)
        self.TrackingInvoice_2.setObjectName(u"TrackingInvoice_2")
        self.TrackingInvoice_2.setMinimumSize(QSize(400, 300))
        self.TrackingInvoice_2.setStyleSheet(u"")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Products_Dash_Frame = QFrame(self.Dashboard)
        self.Products_Dash_Frame.setObjectName(u"Products_Dash_Frame")
        self.Products_Dash_Frame.setGeometry(QRect(230, 320, 211, 81))
        self.Products_Dash_Frame.setStyleSheet(u"background-color: rgb(105, 115, 255);\n"
"border-radius:5px;")
        self.Products_Dash_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.label_57 = QLabel(self.Products_Dash_Frame)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(70, 0, 131, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Products_Label = QLabel(self.Products_Dash_Frame)
        self.Total_Products_Label.setObjectName(u"Total_Products_Label")
        self.Total_Products_Label.setGeometry(QRect(110, 30, 51, 41))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.Total_Products_Label.setFont(font4)
        self.Total_Products_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_6 = QWidget(self.Products_Dash_Frame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 10, 61, 61))
        self.widget_6.setStyleSheet(u"background-image: url(:/Overview item/package.png);")
        self.Sales_Dash_Frame = QFrame(self.Dashboard)
        self.Sales_Dash_Frame.setObjectName(u"Sales_Dash_Frame")
        self.Sales_Dash_Frame.setGeometry(QRect(10, 320, 211, 81))
        self.Sales_Dash_Frame.setStyleSheet(u"background-color: rgb(54, 157, 185);\n"
"border-radius:5px;")
        self.Sales_Dash_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.label_59 = QLabel(self.Sales_Dash_Frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(90, 0, 101, 31))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Sales_Label = QLabel(self.Sales_Dash_Frame)
        self.Total_Sales_Label.setObjectName(u"Total_Sales_Label")
        self.Total_Sales_Label.setGeometry(QRect(110, 30, 71, 41))
        self.Total_Sales_Label.setFont(font4)
        self.Total_Sales_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_7 = QWidget(self.Sales_Dash_Frame)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 10, 71, 61))
        self.widget_7.setStyleSheet(u"background-image: url(:/Overview item/increase.png);")
        self.label_33 = QLabel(self.Sales_Dash_Frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(0, 130, 55, 16))
        self.Category_Dash_Frame = QFrame(self.Dashboard)
        self.Category_Dash_Frame.setObjectName(u"Category_Dash_Frame")
        self.Category_Dash_Frame.setGeometry(QRect(230, 410, 211, 81))
        self.Category_Dash_Frame.setStyleSheet(u"background-color: rgb(52, 73, 94);\n"
"border-radius:5px;")
        self.Category_Dash_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Total_Category_Label = QLabel(self.Category_Dash_Frame)
        self.Total_Category_Label.setObjectName(u"Total_Category_Label")
        self.Total_Category_Label.setGeometry(QRect(120, 30, 31, 41))
        self.Total_Category_Label.setFont(font4)
        self.Total_Category_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64 = QLabel(self.Category_Dash_Frame)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(70, 0, 121, 31))
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.widget_5 = QWidget(self.Category_Dash_Frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 10, 61, 61))
        self.widget_5.setStyleSheet(u"background-image: url(:/Overview item/files_white.png);")
        self.calendar = QCalendarWidget(self.Dashboard)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(0, 10, 441, 300))
        self.calendar.setMinimumSize(QSize(350, 300))
        self.calendar.setAutoFillBackground(False)
        self.calendar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:20px;")
        self.Employee_Dash_Frame = QFrame(self.Dashboard)
        self.Employee_Dash_Frame.setObjectName(u"Employee_Dash_Frame")
        self.Employee_Dash_Frame.setGeometry(QRect(10, 410, 211, 81))
        self.Employee_Dash_Frame.setStyleSheet(u"background-color: rgb(135, 213, 255);\n"
"border-radius:5px;")
        self.Employee_Dash_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.label_12 = QLabel(self.Employee_Dash_Frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 0, 121, 31))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Total_Employee_Label = QLabel(self.Employee_Dash_Frame)
        self.Total_Employee_Label.setObjectName(u"Total_Employee_Label")
        self.Total_Employee_Label.setGeometry(QRect(120, 30, 41, 41))
        self.Total_Employee_Label.setFont(font4)
        self.Total_Employee_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_3 = QWidget(self.Employee_Dash_Frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 71, 61))
        self.widget_3.setStyleSheet(u"background-image: url(:/Overview item/teamwork.png);")
        self.revenue_chart_label = QLabel(self.Dashboard)
        self.revenue_chart_label.setObjectName(u"revenue_chart_label")
        self.revenue_chart_label.setGeometry(QRect(490, 20, 591, 281))
        self.recent_activities_list = QListWidget(self.Dashboard)
        self.recent_activities_list.setObjectName(u"recent_activities_list")
        self.recent_activities_list.setGeometry(QRect(890, 380, 221, 111))
        self.groupBox_7 = QGroupBox(self.Dashboard)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(450, 300, 211, 191))
        font5 = QFont()
        font5.setBold(True)
        self.groupBox_7.setFont(font5)
        self.top_suppliers_table = QTableWidget(self.groupBox_7)
        if (self.top_suppliers_table.columnCount() < 2):
            self.top_suppliers_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.top_suppliers_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.top_suppliers_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.top_suppliers_table.setObjectName(u"top_suppliers_table")
        self.top_suppliers_table.setGeometry(QRect(0, 20, 211, 171))
        self.groupBox_11 = QGroupBox(self.Dashboard)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(670, 300, 211, 191))
        self.groupBox_11.setFont(font5)
        self.top_products_table = QTableWidget(self.groupBox_11)
        if (self.top_products_table.columnCount() < 2):
            self.top_products_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.top_products_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.top_products_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.top_products_table.setObjectName(u"top_products_table")
        self.top_products_table.setGeometry(QRect(0, 20, 211, 171))
        self.groupBox_13 = QGroupBox(self.Dashboard)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(890, 300, 221, 61))
        self.groupBox_13.setFont(font5)
        self.weather_label = QLabel(self.groupBox_13)
        self.weather_label.setObjectName(u"weather_label")
        self.weather_label.setGeometry(QRect(10, 20, 211, 41))
        font6 = QFont()
        font6.setItalic(True)
        self.weather_label.setFont(font6)
        self.weather_label.setStyleSheet(u"color:rgb(0, 0, 127)")
        self.TrackingInvoice_2.addTab(self.Dashboard, "")
        self.InvoiceStatus = QWidget()
        self.InvoiceStatus.setObjectName(u"InvoiceStatus")
        self.label_13 = QLabel(self.InvoiceStatus)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 1111, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_9 = QGroupBox(self.InvoiceStatus)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(210, 80, 741, 61))
        self.groupBox_9.setFont(font5)
        self.groupBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Emp_SearchBy_Comb_2 = QComboBox(self.groupBox_9)
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.addItem("")
        self.Emp_SearchBy_Comb_2.setObjectName(u"Emp_SearchBy_Comb_2")
        self.Emp_SearchBy_Comb_2.setGeometry(QRect(20, 21, 181, 31))
        self.Emp_SearchBy_Comb_2.setFont(font5)
        self.Emp_SearchBy_Comb_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Emp_Search_box_2 = QLineEdit(self.groupBox_9)
        self.Emp_Search_box_2.setObjectName(u"Emp_Search_box_2")
        self.Emp_Search_box_2.setGeometry(QRect(230, 20, 251, 31))
        self.Emp_Search_box_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.search_invoice_btn = QPushButton(self.groupBox_9)
        self.search_invoice_btn.setObjectName(u"search_invoice_btn")
        self.search_invoice_btn.setGeometry(QRect(510, 20, 101, 31))
        self.search_invoice_btn.setMinimumSize(QSize(80, 30))
        self.search_invoice_btn.setMaximumSize(QSize(300, 600))
        self.search_invoice_btn.setFont(font5)
        self.search_invoice_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_invoice_btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/Button/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_invoice_btn.setIcon(icon7)
        self.print_btn = QPushButton(self.groupBox_9)
        self.print_btn.setObjectName(u"print_btn")
        self.print_btn.setGeometry(QRect(620, 20, 91, 31))
        self.print_btn.setFont(font5)
        self.print_btn.setStyleSheet(u"QPushButton{\n"
"  \n"
"	background-color: rgb(229, 153, 0);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.label_14 = QLabel(self.InvoiceStatus)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(-6, 45, 1301, 141))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")
        self.TrackingInvoice_tableWidget = QTableWidget(self.InvoiceStatus)
        if (self.TrackingInvoice_tableWidget.columnCount() < 7):
            self.TrackingInvoice_tableWidget.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.TrackingInvoice_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self.TrackingInvoice_tableWidget.setObjectName(u"TrackingInvoice_tableWidget")
        self.TrackingInvoice_tableWidget.setGeometry(QRect(0, 180, 1121, 301))
        self.TrackingInvoice_tableWidget.setStyleSheet(u"QTableWidget#Category_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.TrackingInvoice_tableWidget.setRowCount(0)
        self.TrackingInvoice_tableWidget.horizontalHeader().setDefaultSectionSize(158)
        self.TrackingInvoice_2.addTab(self.InvoiceStatus, "")
        self.label_14.raise_()
        self.label_13.raise_()
        self.groupBox_9.raise_()
        self.TrackingInvoice_tableWidget.raise_()
        self.InventoryFunction = QWidget()
        self.InventoryFunction.setObjectName(u"InventoryFunction")
        self.groupBox = QGroupBox(self.InventoryFunction)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(200, 6, 711, 61))
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFont(font5)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Emp_SearchBy_Comb = QComboBox(self.groupBox)
        self.Emp_SearchBy_Comb.addItem("")
        self.Emp_SearchBy_Comb.addItem("")
        self.Emp_SearchBy_Comb.addItem("")
        self.Emp_SearchBy_Comb.setObjectName(u"Emp_SearchBy_Comb")
        self.Emp_SearchBy_Comb.setGeometry(QRect(20, 21, 181, 31))
        self.Emp_SearchBy_Comb.setFont(font5)
        self.Emp_SearchBy_Comb.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Emp_Search_box = QLineEdit(self.groupBox)
        self.Emp_Search_box.setObjectName(u"Emp_Search_box")
        self.Emp_Search_box.setGeometry(QRect(230, 20, 251, 31))
        self.Emp_Search_box.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.search = QPushButton(self.groupBox)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(540, 20, 141, 31))
        self.search.setFont(font5)
        self.search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.search.setIcon(icon7)
        self.label_3 = QLabel(self.InventoryFunction)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 80, 1121, 41))
        self.label_3.setFont(font1)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_4 = QLabel(self.InventoryFunction)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 71, 21))
        self.label_4.setFont(font2)
        self.id = QLineEdit(self.InventoryFunction)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(110, 130, 181, 31))
        self.id.setStyleSheet(u"background-color: rgb(255, 255, 215);")
        self.stock = QLineEdit(self.InventoryFunction)
        self.stock.setObjectName(u"stock")
        self.stock.setGeometry(QRect(110, 250, 181, 31))
        self.label_5 = QLabel(self.InventoryFunction)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 180, 81, 21))
        self.label_5.setFont(font2)
        self.label_9 = QLabel(self.InventoryFunction)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 220, 91, 21))
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.InventoryFunction)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 260, 81, 21))
        self.label_10.setFont(font2)
        self.label_16 = QLabel(self.InventoryFunction)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(330, 130, 71, 21))
        self.label_16.setFont(font2)
        self.label_23 = QLabel(self.InventoryFunction)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(330, 170, 61, 21))
        self.label_23.setFont(font2)
        self.label_24 = QLabel(self.InventoryFunction)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(330, 210, 81, 21))
        self.label_24.setFont(font2)
        self.value = QLineEdit(self.InventoryFunction)
        self.value.setObjectName(u"value")
        self.value.setGeometry(QRect(420, 170, 181, 31))
        self.cost = QLineEdit(self.InventoryFunction)
        self.cost.setObjectName(u"cost")
        self.cost.setGeometry(QRect(420, 210, 181, 31))
        self.Category_tableWidget_2 = QTableWidget(self.InventoryFunction)
        if (self.Category_tableWidget_2.columnCount() < 9):
            self.Category_tableWidget_2.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        font7 = QFont()
        font7.setBold(True)
        font7.setUnderline(False)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.Category_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignHCenter|Qt.AlignBottom);
        __qtablewidgetitem16.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.Category_tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.Category_tableWidget_2.setObjectName(u"Category_tableWidget_2")
        self.Category_tableWidget_2.setGeometry(QRect(0, 290, 1121, 211))
        self.Category_tableWidget_2.setStyleSheet(u"QTableWidget#Category_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Category_tableWidget_2.setRowCount(0)
        self.Category_tableWidget_2.horizontalHeader().setDefaultSectionSize(140)
        self.label_25 = QLabel(self.InventoryFunction)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(330, 250, 81, 21))
        self.label_25.setFont(font2)
        self.groupBox_12 = QGroupBox(self.InventoryFunction)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(610, 160, 511, 131))
        self.groupBox_12.setFont(font5)
        self.pushButton_7 = QPushButton(self.groupBox_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(930, 10, 91, 41))
        self.Empl_Update_Btn = QPushButton(self.groupBox_12)
        self.Empl_Update_Btn.setObjectName(u"Empl_Update_Btn")
        self.Empl_Update_Btn.setGeometry(QRect(20, 20, 151, 41))
        self.Empl_Update_Btn.setFont(font5)
        self.Empl_Update_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Update_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(93, 173, 226);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Button/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Empl_Update_Btn.setIcon(icon8)
        self.clear = QPushButton(self.groupBox_12)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(340, 70, 151, 41))
        self.clear.setFont(font5)
        self.clear.setStyleSheet(u"QPushButton{\n"
"  \n"
"	background-color: rgb(231, 231, 231);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.Empl_Save_Btn_4 = QPushButton(self.groupBox_12)
        self.Empl_Save_Btn_4.setObjectName(u"Empl_Save_Btn_4")
        self.Empl_Save_Btn_4.setGeometry(QRect(20, 70, 151, 41))
        self.Empl_Save_Btn_4.setMinimumSize(QSize(80, 30))
        self.Empl_Save_Btn_4.setMaximumSize(QSize(200, 600))
        self.Empl_Save_Btn_4.setFont(font5)
        self.Empl_Save_Btn_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Save_Btn_4.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(46, 204, 113);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(130, 224, 170);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Button/log-in.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Empl_Save_Btn_4.setIcon(icon9)
        self.Empl_Save_Btn_4.setIconSize(QSize(15, 15))
        self.Empl_Save_Btn_3 = QPushButton(self.groupBox_12)
        self.Empl_Save_Btn_3.setObjectName(u"Empl_Save_Btn_3")
        self.Empl_Save_Btn_3.setGeometry(QRect(180, 70, 151, 41))
        self.Empl_Save_Btn_3.setMinimumSize(QSize(80, 30))
        self.Empl_Save_Btn_3.setMaximumSize(QSize(200, 600))
        self.Empl_Save_Btn_3.setFont(font5)
        self.Empl_Save_Btn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Save_Btn_3.setStyleSheet(u"QPushButton{\n"
"  ;\n"
" \n"
"	\n"
"	background-color: rgb(240, 160, 0);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
";\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/Button/log-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Empl_Save_Btn_3.setIcon(icon10)
        self.Empl_Save_Btn_3.setIconSize(QSize(15, 15))
        self.Empl_Delete_Btn = QPushButton(self.groupBox_12)
        self.Empl_Delete_Btn.setObjectName(u"Empl_Delete_Btn")
        self.Empl_Delete_Btn.setGeometry(QRect(180, 20, 151, 41))
        self.Empl_Delete_Btn.setMinimumSize(QSize(80, 30))
        self.Empl_Delete_Btn.setMaximumSize(QSize(200, 600))
        self.Empl_Delete_Btn.setFont(font5)
        self.Empl_Delete_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Delete_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(231, 76, 60);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(236, 112, 99);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Button/bin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Empl_Delete_Btn.setIcon(icon11)
        self.Empl_Delete_Btn.setIconSize(QSize(15, 15))
        self.add = QPushButton(self.groupBox_12)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(340, 20, 151, 41))
        self.add.setMinimumSize(QSize(80, 30))
        self.add.setMaximumSize(QSize(200, 600))
        self.add.setFont(font5)
        self.add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Button/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add.setIcon(icon12)
        self.label_26 = QLabel(self.InventoryFunction)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(-6, 5, 1311, 81))
        self.label_26.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")
        self.name = QLineEdit(self.InventoryFunction)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(110, 170, 181, 31))
        self.category = QComboBox(self.InventoryFunction)
        self.category.addItem("")
        self.category.addItem("")
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(110, 210, 181, 31))
        self.category.setFont(font5)
        self.location = QComboBox(self.InventoryFunction)
        self.location.addItem("")
        self.location.addItem("")
        self.location.addItem("")
        self.location.setObjectName(u"location")
        self.location.setGeometry(QRect(420, 250, 181, 31))
        self.location.setFont(font5)
        self.supplier_inv = QComboBox(self.InventoryFunction)
        self.supplier_inv.setObjectName(u"supplier_inv")
        self.supplier_inv.setGeometry(QRect(420, 130, 181, 31))
        self.supplier_inv.setFont(font5)
        self.TrackingInvoice_2.addTab(self.InventoryFunction, "")
        self.label_26.raise_()
        self.groupBox_12.raise_()
        self.groupBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.id.raise_()
        self.stock.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_16.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.value.raise_()
        self.cost.raise_()
        self.Category_tableWidget_2.raise_()
        self.label_25.raise_()
        self.name.raise_()
        self.category.raise_()
        self.location.raise_()
        self.supplier_inv.raise_()
        self.Account = QWidget()
        self.Account.setObjectName(u"Account")
        self.label_6 = QLabel(self.Account)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-10, 80, 1121, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Supplier_Delete_Btn = QPushButton(self.Account)
        self.Supplier_Delete_Btn.setObjectName(u"Supplier_Delete_Btn")
        self.Supplier_Delete_Btn.setGeometry(QRect(220, 300, 91, 31))
        self.Supplier_Delete_Btn.setFont(font5)
        self.Supplier_Delete_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Delete_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(231, 76, 60);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(236, 112, 99);\n"
"}")
        self.Supplier_Delete_Btn.setIcon(icon11)
        self.Supplier_Delete_Btn.setIconSize(QSize(15, 15))
        self.Supplier_Save_Btn = QPushButton(self.Account)
        self.Supplier_Save_Btn.setObjectName(u"Supplier_Save_Btn")
        self.Supplier_Save_Btn.setGeometry(QRect(10, 300, 101, 31))
        self.Supplier_Save_Btn.setFont(font5)
        self.Supplier_Save_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Save_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(46, 204, 113);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(130, 224, 170);\n"
"}")
        self.Supplier_Save_Btn.setIcon(icon12)
        self.Supplier_Save_Btn.setIconSize(QSize(15, 15))
        self.Supplier_Update_Btn = QPushButton(self.Account)
        self.Supplier_Update_Btn.setObjectName(u"Supplier_Update_Btn")
        self.Supplier_Update_Btn.setGeometry(QRect(120, 300, 91, 31))
        self.Supplier_Update_Btn.setFont(font5)
        self.Supplier_Update_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Update_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(93, 173, 226);\n"
"}")
        self.Supplier_Update_Btn.setIcon(icon8)
        self.Supplier_Clear_Btn = QPushButton(self.Account)
        self.Supplier_Clear_Btn.setObjectName(u"Supplier_Clear_Btn")
        self.Supplier_Clear_Btn.setGeometry(QRect(320, 300, 91, 31))
        self.Supplier_Clear_Btn.setFont(font5)
        self.Supplier_Clear_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Supplier_Clear_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Button/clean.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Supplier_Clear_Btn.setIcon(icon13)
        self.Supp_tableWidget = QTableWidget(self.Account)
        if (self.Supp_tableWidget.columnCount() < 3):
            self.Supp_tableWidget.setColumnCount(3)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.Supp_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.Supp_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.Supp_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        self.Supp_tableWidget.setObjectName(u"Supp_tableWidget")
        self.Supp_tableWidget.setGeometry(QRect(450, 120, 671, 381))
        self.Supp_tableWidget.setStyleSheet(u"QTableWidget#Supp_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Supp_tableWidget.setRowCount(0)
        self.Supp_tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.groupBox_8 = QGroupBox(self.Account)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(200, 6, 711, 61))
        self.groupBox_8.setFont(font5)
        self.groupBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Supp_SearchBy_Comb = QComboBox(self.groupBox_8)
        self.Supp_SearchBy_Comb.addItem("")
        self.Supp_SearchBy_Comb.addItem("")
        self.Supp_SearchBy_Comb.setObjectName(u"Supp_SearchBy_Comb")
        self.Supp_SearchBy_Comb.setGeometry(QRect(20, 21, 181, 31))
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setItalic(False)
        self.Supp_SearchBy_Comb.setFont(font8)
        self.Supp_SearchBy_Comb.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Supp_Search_box = QLineEdit(self.groupBox_8)
        self.Supp_Search_box.setObjectName(u"Supp_Search_box")
        self.Supp_Search_box.setGeometry(QRect(230, 20, 251, 31))
        self.Supp_Search_box.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Empl_Search_Btn_3 = QPushButton(self.groupBox_8)
        self.Empl_Search_Btn_3.setObjectName(u"Empl_Search_Btn_3")
        self.Empl_Search_Btn_3.setGeometry(QRect(540, 20, 141, 31))
        self.Empl_Search_Btn_3.setFont(font5)
        self.Empl_Search_Btn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Search_Btn_3.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.Empl_Search_Btn_3.setIcon(icon7)
        self.label_27 = QLabel(self.Account)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 1301, 81))
        self.label_27.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")
        self.label_31 = QLabel(self.Account)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(-6, 120, 561, 381))
        font9 = QFont()
        font9.setPointSize(10)
        self.label_31.setFont(font9)
        self.label_31.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")
        self.groupBox_5 = QGroupBox(self.Account)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 140, 421, 141))
        self.groupBox_5.setFont(font5)
        self.groupBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 101, 21))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Supp_Name = QLineEdit(self.groupBox_5)
        self.Supp_Name.setObjectName(u"Supp_Name")
        self.Supp_Name.setGeometry(QRect(130, 60, 261, 31))
        self.Supp_Name.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 60, 121, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Supp_invoice_No = QLineEdit(self.groupBox_5)
        self.Supp_invoice_No.setObjectName(u"Supp_invoice_No")
        self.Supp_invoice_No.setGeometry(QRect(130, 18, 261, 31))
        self.Supp_invoice_No.setStyleSheet(u"background-color: rgb(255, 255, 215);\n"
"color: rgb(0, 0, 0)")
        self.label_29 = QLabel(self.groupBox_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 110, 101, 21))
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.roleComboBox = QComboBox(self.groupBox_5)
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.setObjectName(u"roleComboBox")
        self.roleComboBox.setGeometry(QRect(130, 110, 261, 31))
        self.roleComboBox.setFont(font1)
        self.roleComboBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.roleComboBox.setStyleSheet(u"color: rgb(0, 0, 109);\n"
"\n"
"")
        self.TrackingInvoice_2.addTab(self.Account, "")
        self.label_31.raise_()
        self.label_27.raise_()
        self.label_6.raise_()
        self.Supplier_Delete_Btn.raise_()
        self.Supplier_Save_Btn.raise_()
        self.Supplier_Update_Btn.raise_()
        self.Supplier_Clear_Btn.raise_()
        self.Supp_tableWidget.raise_()
        self.groupBox_8.raise_()
        self.groupBox_5.raise_()
        self.Supplier = QWidget()
        self.Supplier.setObjectName(u"Supplier")
        self.label_15 = QLabel(self.Supplier)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 1101, 41))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2 = QGroupBox(self.Supplier)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(480, 80, 751, 61))
        self.groupBox_2.setFont(font5)
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Product_SearchBy_Comb = QComboBox(self.groupBox_2)
        self.Product_SearchBy_Comb.addItem("")
        self.Product_SearchBy_Comb.addItem("")
        self.Product_SearchBy_Comb.addItem("")
        self.Product_SearchBy_Comb.addItem("")
        self.Product_SearchBy_Comb.setObjectName(u"Product_SearchBy_Comb")
        self.Product_SearchBy_Comb.setGeometry(QRect(10, 21, 181, 31))
        self.Product_SearchBy_Comb.setFont(font5)
        self.Product_SearchBy_Comb.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Product_SearchBox_Comb = QLineEdit(self.groupBox_2)
        self.Product_SearchBox_Comb.setObjectName(u"Product_SearchBox_Comb")
        self.Product_SearchBox_Comb.setGeometry(QRect(210, 20, 251, 31))
        self.Product_SearchBox_Comb.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Empl_Search_Btn_4 = QPushButton(self.groupBox_2)
        self.Empl_Search_Btn_4.setObjectName(u"Empl_Search_Btn_4")
        self.Empl_Search_Btn_4.setGeometry(QRect(470, 20, 131, 31))
        self.Empl_Search_Btn_4.setFont(font5)
        self.Empl_Search_Btn_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Empl_Search_Btn_4.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        self.Empl_Search_Btn_4.setIcon(icon7)
        self.Product_tableWidget = QTableWidget(self.Supplier)
        if (self.Product_tableWidget.columnCount() < 5):
            self.Product_tableWidget.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.Product_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.Product_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font5);
        self.Product_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font5);
        self.Product_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font5);
        self.Product_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.Product_tableWidget.setObjectName(u"Product_tableWidget")
        self.Product_tableWidget.setGeometry(QRect(480, 150, 631, 321))
        self.Product_tableWidget.setStyleSheet(u"QTableWidget#Product_tableWidget{\n"
"background-color: rgb(226, 245, 255);\n"
"}")
        self.Product_tableWidget.setRowCount(0)
        self.groupBox_3 = QGroupBox(self.Supplier)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 80, 451, 391))
        self.groupBox_3.setFont(font5)
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 100, 91, 21))
        self.label_17.setFont(font2)
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 160, 61, 21))
        self.label_19.setFont(font2)
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(30, 220, 101, 21))
        self.label_21.setFont(font2)
        self.Product_Qty = QLineEdit(self.groupBox_3)
        self.Product_Qty.setObjectName(u"Product_Qty")
        self.Product_Qty.setGeometry(QRect(130, 220, 281, 31))
        self.Product_Qty.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"")
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 280, 71, 21))
        self.label_22.setFont(font2)
        self.Product_Status_Comb = QComboBox(self.groupBox_3)
        self.Product_Status_Comb.addItem("")
        self.Product_Status_Comb.addItem("")
        self.Product_Status_Comb.setObjectName(u"Product_Status_Comb")
        self.Product_Status_Comb.setGeometry(QRect(130, 280, 281, 31))
        self.Product_Status_Comb.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Clear_Product_Btn = QPushButton(self.groupBox_3)
        self.Clear_Product_Btn.setObjectName(u"Clear_Product_Btn")
        self.Clear_Product_Btn.setGeometry(QRect(350, 340, 91, 31))
        self.Clear_Product_Btn.setFont(font5)
        self.Clear_Product_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Clear_Product_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        self.Clear_Product_Btn.setIcon(icon13)
        self.Update_Product_Btn = QPushButton(self.groupBox_3)
        self.Update_Product_Btn.setObjectName(u"Update_Product_Btn")
        self.Update_Product_Btn.setGeometry(QRect(150, 340, 91, 31))
        self.Update_Product_Btn.setFont(font5)
        self.Update_Product_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Update_Product_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(93, 173, 226);\n"
"}")
        self.Update_Product_Btn.setIcon(icon8)
        self.Delete_Product_Btn = QPushButton(self.groupBox_3)
        self.Delete_Product_Btn.setObjectName(u"Delete_Product_Btn")
        self.Delete_Product_Btn.setGeometry(QRect(250, 340, 91, 31))
        self.Delete_Product_Btn.setFont(font5)
        self.Delete_Product_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Delete_Product_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(231, 76, 60);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(236, 112, 99);\n"
"}")
        self.Delete_Product_Btn.setIcon(icon11)
        self.Delete_Product_Btn.setIconSize(QSize(15, 15))
        self.Save_Product_Btn = QPushButton(self.groupBox_3)
        self.Save_Product_Btn.setObjectName(u"Save_Product_Btn")
        self.Save_Product_Btn.setGeometry(QRect(40, 340, 101, 31))
        self.Save_Product_Btn.setFont(font5)
        self.Save_Product_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Save_Product_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(46, 204, 113);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(130, 224, 170);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Button/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_Product_Btn.setIcon(icon14)
        self.Product_Status_Comb_2 = QComboBox(self.groupBox_3)
        self.Product_Status_Comb_2.addItem("")
        self.Product_Status_Comb_2.addItem("")
        self.Product_Status_Comb_2.setObjectName(u"Product_Status_Comb_2")
        self.Product_Status_Comb_2.setGeometry(QRect(130, 100, 281, 31))
        self.Product_Status_Comb_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Product_Name = QLineEdit(self.groupBox_3)
        self.Product_Name.setObjectName(u"Product_Name")
        self.Product_Name.setGeometry(QRect(130, 160, 281, 31))
        self.Product_Name.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 40, 91, 31))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.Supplier_ID_Label = QLabel(self.groupBox_3)
        self.Supplier_ID_Label.setObjectName(u"Supplier_ID_Label")
        self.Supplier_ID_Label.setGeometry(QRect(130, 40, 281, 31))
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setUnderline(True)
        self.Supplier_ID_Label.setFont(font10)
        self.Supplier_ID_Label.setStyleSheet(u"color: rgb(218, 218, 0)")
        self.label_28 = QLabel(self.Supplier)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(4, -25, 1291, 531))
        self.label_28.setStyleSheet(u"background-image: url(:/Overview item/banner_min.png);")
        self.TrackingInvoice_2.addTab(self.Supplier, "")
        self.label_28.raise_()
        self.label_15.raise_()
        self.groupBox_2.raise_()
        self.Product_tableWidget.raise_()
        self.groupBox_3.raise_()
        self.Report = QWidget()
        self.Report.setObjectName(u"Report")
        self.tabWidget_2 = QTabWidget(self.Report)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1301, 511))
        self.ReportExport = QWidget()
        self.ReportExport.setObjectName(u"ReportExport")
        self.label_30 = QLabel(self.ReportExport)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(-10, 0, 1131, 41))
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"background-color: rgb(15, 18, 86);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32 = QLabel(self.ReportExport)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(290, 130, 1001, 41))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"background-color: rgb(52, 152, 219);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.Invoice_plainTextEdit = QPlainTextEdit(self.ReportExport)
        self.Invoice_plainTextEdit.setObjectName(u"Invoice_plainTextEdit")
        self.Invoice_plainTextEdit.setGeometry(QRect(290, 130, 821, 351))
        self.Invoice_plainTextEdit.setStyleSheet(u"")
        self.Invoice_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Invoice_plainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.Invoice_plainTextEdit.setReadOnly(True)
        self.Invoice_listWidget = QListWidget(self.ReportExport)
        self.Invoice_listWidget.setObjectName(u"Invoice_listWidget")
        self.Invoice_listWidget.setGeometry(QRect(-20, 90, 311, 391))
        self.Invoice_listWidget.setStyleSheet(u"background-image: url(:/Overview item/banner_min.png);\n"
"border-radius:10px;")
        self.Invoice_listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Employee_Dash_Frame_6 = QFrame(self.ReportExport)
        self.Employee_Dash_Frame_6.setObjectName(u"Employee_Dash_Frame_6")
        self.Employee_Dash_Frame_6.setGeometry(QRect(40, 100, 221, 101))
        self.Employee_Dash_Frame_6.setStyleSheet(u"background-image: url(:/Background/Nen.png);\n"
"border-radius:30px;")
        self.Employee_Dash_Frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.Total_Sales_Label_3 = QLabel(self.Employee_Dash_Frame_6)
        self.Total_Sales_Label_3.setObjectName(u"Total_Sales_Label_3")
        self.Total_Sales_Label_3.setGeometry(QRect(10, 60, 191, 31))
        self.Total_Sales_Label_3.setFont(font4)
        self.Total_Sales_Label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_11 = QWidget(self.Employee_Dash_Frame_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(70, 0, 61, 61))
        self.widget_11.setStyleSheet(u"background-image: url(:/Overview item/shopping-cart .png);")
        self.Employee_Dash_Frame_7 = QFrame(self.ReportExport)
        self.Employee_Dash_Frame_7.setObjectName(u"Employee_Dash_Frame_7")
        self.Employee_Dash_Frame_7.setGeometry(QRect(40, 230, 221, 101))
        self.Employee_Dash_Frame_7.setStyleSheet(u"background-image: url(:/Background/Nen.png);\n"
"border-radius:30px;")
        self.Employee_Dash_Frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.widget_12 = QWidget(self.Employee_Dash_Frame_7)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(80, 10, 51, 51))
        self.widget_12.setStyleSheet(u"background-image: url(:/New product/Upload-Box-1--Streamline-Core.png (2).png);")
        self.label_65 = QLabel(self.Employee_Dash_Frame_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(68, 130, 131, 31))
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Category_Label_3 = QLabel(self.Employee_Dash_Frame_7)
        self.Total_Category_Label_3.setObjectName(u"Total_Category_Label_3")
        self.Total_Category_Label_3.setGeometry(QRect(218, 130, 31, 31))
        self.Total_Category_Label_3.setFont(font4)
        self.Total_Category_Label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Total_Category_Label_4 = QLabel(self.Employee_Dash_Frame_7)
        self.Total_Category_Label_4.setObjectName(u"Total_Category_Label_4")
        self.Total_Category_Label_4.setGeometry(QRect(10, 60, 191, 31))
        self.Total_Category_Label_4.setFont(font4)
        self.Total_Category_Label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox_10 = QGroupBox(self.ReportExport)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(670, 40, 421, 91))
        self.groupBox_10.setFont(font5)
        self.groupBox_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Clear_Bills_Btn = QPushButton(self.groupBox_10)
        self.Clear_Bills_Btn.setObjectName(u"Clear_Bills_Btn")
        self.Clear_Bills_Btn.setGeometry(QRect(150, 40, 101, 31))
        self.Clear_Bills_Btn.setFont(font5)
        self.Clear_Bills_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Clear_Bills_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(86, 101, 115);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        self.Clear_Bills_Btn.setIcon(icon13)
        self.Search_Bills_Btn = QPushButton(self.groupBox_10)
        self.Search_Bills_Btn.setObjectName(u"Search_Bills_Btn")
        self.Search_Bills_Btn.setGeometry(QRect(10, 40, 111, 31))
        self.Search_Bills_Btn.setFont(font5)
        self.Search_Bills_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Search_Bills_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Button/checking.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Search_Bills_Btn.setIcon(icon15)
        self.Export_Chart_Btn = QPushButton(self.groupBox_10)
        self.Export_Chart_Btn.setObjectName(u"Export_Chart_Btn")
        self.Export_Chart_Btn.setGeometry(QRect(280, 40, 101, 31))
        self.Export_Chart_Btn.setFont(font5)
        self.Export_Chart_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Export_Chart_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(0, 149, 109);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(128, 139, 150);\n"
"}")
        self.Export_Chart_Btn.setIcon(icon13)
        self.Employee_Dash_Frame_8 = QFrame(self.ReportExport)
        self.Employee_Dash_Frame_8.setObjectName(u"Employee_Dash_Frame_8")
        self.Employee_Dash_Frame_8.setGeometry(QRect(40, 360, 221, 101))
        self.Employee_Dash_Frame_8.setStyleSheet(u"background-image: url(:/Background/Nen.png);\n"
"border-radius:30px;")
        self.Employee_Dash_Frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.widget_15 = QWidget(self.Employee_Dash_Frame_8)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(80, 10, 51, 51))
        self.widget_15.setStyleSheet(u"background-image: url(:/Background/archive.png);")
        self.label_71 = QLabel(self.Employee_Dash_Frame_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(68, 130, 131, 31))
        self.label_71.setFont(font3)
        self.label_71.setStyleSheet(u"color: rgb(247, 247, 247);")
        self.Total_Category_Label_9 = QLabel(self.Employee_Dash_Frame_8)
        self.Total_Category_Label_9.setObjectName(u"Total_Category_Label_9")
        self.Total_Category_Label_9.setGeometry(QRect(218, 130, 31, 31))
        self.Total_Category_Label_9.setFont(font4)
        self.Total_Category_Label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Total_Category_Label_10 = QLabel(self.Employee_Dash_Frame_8)
        self.Total_Category_Label_10.setObjectName(u"Total_Category_Label_10")
        self.Total_Category_Label_10.setGeometry(QRect(10, 60, 191, 31))
        self.Total_Category_Label_10.setFont(font4)
        self.Total_Category_Label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_5 = QFrame(self.ReportExport)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-10, 40, 301, 51))
        self.frame_5.setStyleSheet(u"background-color: rgb(52, 76, 162);\n"
"border-radius:5px;")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.Date_Time_2 = QLabel(self.frame_5)
        self.Date_Time_2.setObjectName(u"Date_Time_2")
        self.Date_Time_2.setGeometry(QRect(90, 10, 151, 35))
        self.Date_Time_2.setFont(font2)
        self.Date_Time_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_chart = QLabel(self.ReportExport)
        self.lbl_chart.setObjectName(u"lbl_chart")
        self.lbl_chart.setGeometry(QRect(410, 170, 361, 321))
        self.label_34 = QLabel(self.ReportExport)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(1010, 470, 91, 21))
        self.label_34.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.groupBox_4 = QGroupBox(self.ReportExport)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(340, 40, 291, 91))
        self.groupBox_4.setFont(font5)
        self.comboBox_3 = QComboBox(self.groupBox_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(150, 30, 111, 22))
        self.FilterCategory_ComboBox = QComboBox(self.groupBox_4)
        self.FilterCategory_ComboBox.addItem("")
        self.FilterCategory_ComboBox.setObjectName(u"FilterCategory_ComboBox")
        self.FilterCategory_ComboBox.setGeometry(QRect(150, 60, 111, 21))
        self.ChartType_Label = QLabel(self.groupBox_4)
        self.ChartType_Label.setObjectName(u"ChartType_Label")
        self.ChartType_Label.setGeometry(QRect(30, 30, 61, 20))
        font11 = QFont()
        font11.setBold(False)
        self.ChartType_Label.setFont(font11)
        self.FilterCategory_Label = QLabel(self.groupBox_4)
        self.FilterCategory_Label.setObjectName(u"FilterCategory_Label")
        self.FilterCategory_Label.setGeometry(QRect(10, 60, 101, 20))
        self.FilterCategory_Label.setFont(font11)
        self.groupBox_6 = QGroupBox(self.ReportExport)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(870, 180, 221, 91))
        self.groupBox_6.setFont(font5)
        self.ColorScheme_ComboBox = QComboBox(self.groupBox_6)
        self.ColorScheme_ComboBox.addItem("")
        self.ColorScheme_ComboBox.addItem("")
        self.ColorScheme_ComboBox.addItem("")
        self.ColorScheme_ComboBox.setObjectName(u"ColorScheme_ComboBox")
        self.ColorScheme_ComboBox.setGeometry(QRect(140, 30, 71, 21))
        self.StartAngle_SpinBox = QSpinBox(self.groupBox_6)
        self.StartAngle_SpinBox.setObjectName(u"StartAngle_SpinBox")
        self.StartAngle_SpinBox.setGeometry(QRect(140, 60, 88, 21))
        self.StartAngle_SpinBox.setMaximum(360)
        self.ColorScheme_Label = QLabel(self.groupBox_6)
        self.ColorScheme_Label.setObjectName(u"ColorScheme_Label")
        self.ColorScheme_Label.setGeometry(QRect(10, 30, 101, 20))
        self.StartAngle_Label = QLabel(self.groupBox_6)
        self.StartAngle_Label.setObjectName(u"StartAngle_Label")
        self.StartAngle_Label.setGeometry(QRect(10, 60, 111, 16))
        self.Loading_Label = QLabel(self.ReportExport)
        self.Loading_Label.setObjectName(u"Loading_Label")
        self.Loading_Label.setGeometry(QRect(880, 340, 101, 31))
        self.tabWidget_2.addTab(self.ReportExport, "")
        self.Invoice_listWidget.raise_()
        self.Invoice_plainTextEdit.raise_()
        self.groupBox_10.raise_()
        self.label_30.raise_()
        self.label_32.raise_()
        self.Employee_Dash_Frame_6.raise_()
        self.Employee_Dash_Frame_7.raise_()
        self.Employee_Dash_Frame_8.raise_()
        self.frame_5.raise_()
        self.lbl_chart.raise_()
        self.label_34.raise_()
        self.groupBox_4.raise_()
        self.groupBox_6.raise_()
        self.Loading_Label.raise_()
        self.TrackingInvoice_2.addTab(self.Report, "")

        self.verticalLayout_2.addWidget(self.TrackingInvoice_2)

        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(1345, 623))
        self.frame.setStyleSheet(u"background-image: url(:/Background/Nen.png);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 1131, 51))
        font12 = QFont()
        font12.setFamilies([u"PNU Medium"])
        font12.setPointSize(19)
        font12.setBold(True)
        self.label.setFont(font12)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-10, 0, 100, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(100, 50))
        self.widget_2.setMaximumSize(QSize(100, 50))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet(u"border-image: url(:/Logo/c47f36eb-4b82-4936-bec2-af24f431e19e.png);")
        self.Login_Btn = QPushButton(self.frame)
        self.Login_Btn.setObjectName(u"Login_Btn")
        self.Login_Btn.setGeometry(QRect(1220, 0, 141, 51))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Login_Btn.sizePolicy().hasHeightForWidth())
        self.Login_Btn.setSizePolicy(sizePolicy2)
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(True)
        self.Login_Btn.setFont(font13)
        self.Login_Btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Login_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(244, 208, 63);\n"
"  color: rgb(33, 47, 61);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(248, 196, 113);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/Button/power.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Login_Btn.setIcon(icon16)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-20, 50, 1381, 31))
        self.frame_2.setStyleSheet(u"background-image: url(:/Background/banner_min.png);")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.Date_Time = QLabel(self.frame_2)
        self.Date_Time.setObjectName(u"Date_Time")
        self.Date_Time.setGeometry(QRect(1280, 10, 81, 20))
        font14 = QFont()
        font14.setPointSize(11)
        font14.setBold(False)
        self.Date_Time.setFont(font14)
        self.Date_Time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.show_infor = QPushButton(self.frame_2)
        self.show_infor.setObjectName(u"show_infor")
        self.show_infor.setGeometry(QRect(60, 0, 141, 28))
        self.show_infor.setFont(font13)
        self.show_infor.setStyleSheet(u"background-color: rgb(231, 172, 34);")
        self.Date_Time_3 = QLabel(self.frame)
        self.Date_Time_3.setObjectName(u"Date_Time_3")
        self.Date_Time_3.setGeometry(QRect(0, 630, 1441, 41))
        sizePolicy.setHeightForWidth(self.Date_Time_3.sizePolicy().hasHeightForWidth())
        self.Date_Time_3.setSizePolicy(sizePolicy)
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(9)
        font15.setBold(True)
        font15.setItalic(False)
        self.Date_Time_3.setFont(font15)
        self.Date_Time_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.Date_Time_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.HomeFrame.raise_()
        self.PanalFrame.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.TrackingInvoice_2.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Group 11 Inventory and Invoice Management app - Admin ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.Employee_Button.setText(QCoreApplication.translate("MainWindow", u" Inventory", None))
        self.Supplier_Button.setText(QCoreApplication.translate("MainWindow", u" Invoice status", None))
        self.Category_Button.setText(QCoreApplication.translate("MainWindow", u" Account", None))
        self.Products_Button.setText(QCoreApplication.translate("MainWindow", u" Report", None))
        self.Dash_Button.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.Category_Button_2.setText(QCoreApplication.translate("MainWindow", u" Supplier", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total Product's", None))
        self.Total_Products_Label.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.Total_Sales_Label.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_33.setText("")
        self.Total_Category_Label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Total Category", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total Supplier", None))
        self.Total_Employee_Label.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.revenue_chart_label.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Top Suppliers", None))
        ___qtablewidgetitem = self.top_suppliers_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Top Suppliers", None));
        ___qtablewidgetitem1 = self.top_suppliers_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Product Count", None));
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Top Products", None))
        ___qtablewidgetitem2 = self.top_products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Top Products", None));
        ___qtablewidgetitem3 = self.top_products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sold Quantity", None));
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Weather Forecast", None))
        self.weather_label.setText(QCoreApplication.translate("MainWindow", u"Weather: Loading...", None))
        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.Dashboard), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tracking Inovice", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Search Invoices", None))
        self.Emp_SearchBy_Comb_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Invoice ID", None))
        self.Emp_SearchBy_Comb_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.Emp_SearchBy_Comb_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Invoice Date", None))
        self.Emp_SearchBy_Comb_2.setItemText(3, QCoreApplication.translate("MainWindow", u"QTY", None))
        self.Emp_SearchBy_Comb_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Price", None))
        self.Emp_SearchBy_Comb_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Status", None))

        self.search_invoice_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_14.setText("")
        ___qtablewidgetitem4 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem5 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Invoice ID", None));
        ___qtablewidgetitem6 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Invoice Date", None));
        ___qtablewidgetitem7 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"QTY", None));
        ___qtablewidgetitem8 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Total Price", None));
        ___qtablewidgetitem9 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem10 = self.TrackingInvoice_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Confirm", None));
        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.InvoiceStatus), QCoreApplication.translate("MainWindow", u"Invoice Status", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search Inventory", None))
        self.Emp_SearchBy_Comb.setItemText(0, QCoreApplication.translate("MainWindow", u"Product_name", None))
        self.Emp_SearchBy_Comb.setItemText(1, QCoreApplication.translate("MainWindow", u"Category", None))
        self.Emp_SearchBy_Comb.setItemText(2, QCoreApplication.translate("MainWindow", u"Location number", None))

        self.Emp_Search_box.setText("")
        self.search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Inventory function", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
        ___qtablewidgetitem11 = self.Category_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem12 = self.Category_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Product name", None));
        ___qtablewidgetitem13 = self.Category_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem14 = self.Category_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Current stock", None));
        ___qtablewidgetitem15 = self.Category_tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Supplier", None));
        ___qtablewidgetitem16 = self.Category_tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Stock value", None));
        ___qtablewidgetitem17 = self.Category_tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Stock cost", None));
        ___qtablewidgetitem18 = self.Category_tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem19 = self.Category_tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Reorder-require", None));
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng kho", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"New Product", None))
        self.Empl_Update_Btn.setText(QCoreApplication.translate("MainWindow", u" Update", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Empl_Save_Btn_4.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.Empl_Save_Btn_3.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.Empl_Delete_Btn.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_26.setText("")
        self.category.setItemText(0, QCoreApplication.translate("MainWindow", u"Electronics", None))
        self.category.setItemText(1, QCoreApplication.translate("MainWindow", u"Accessories", None))

        self.location.setItemText(0, QCoreApplication.translate("MainWindow", u"O", None))
        self.location.setItemText(1, QCoreApplication.translate("MainWindow", u"T", None))
        self.location.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))

        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.InventoryFunction), QCoreApplication.translate("MainWindow", u"Inventory Function", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Manage Account", None))
        self.Supplier_Delete_Btn.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.Supplier_Save_Btn.setText(QCoreApplication.translate("MainWindow", u" Add ", None))
        self.Supplier_Update_Btn.setText(QCoreApplication.translate("MainWindow", u" Update", None))
        self.Supplier_Clear_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        ___qtablewidgetitem20 = self.Supp_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"User Name", None));
        ___qtablewidgetitem21 = self.Supp_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem22 = self.Supp_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Search Account", None))
        self.Supp_SearchBy_Comb.setItemText(0, QCoreApplication.translate("MainWindow", u"UserName", None))
        self.Supp_SearchBy_Comb.setItemText(1, QCoreApplication.translate("MainWindow", u"Role", None))

        self.Supp_Search_box.setText("")
        self.Supp_Search_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u1eeb kh\u00f3a t\u00ecm ki\u1ebfm....", None))
        self.Empl_Search_Btn_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_27.setText("")
        self.label_31.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Account Function", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.Supp_Name.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Supp_invoice_No.setText("")
        self.Supp_invoice_No.setPlaceholderText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.roleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))
        self.roleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"user", None))

        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.Account), QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Manage Supplier", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Search Supplier", None))
        self.Product_SearchBy_Comb.setItemText(0, QCoreApplication.translate("MainWindow", u"Search by ...", None))
        self.Product_SearchBy_Comb.setItemText(1, QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.Product_SearchBy_Comb.setItemText(2, QCoreApplication.translate("MainWindow", u"Category", None))
        self.Product_SearchBy_Comb.setItemText(3, QCoreApplication.translate("MainWindow", u"Name", None))

        self.Product_SearchBox_Comb.setText("")
        self.Product_SearchBox_Comb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u1eeb kh\u00f3a t\u00ecm ki\u1ebfm....", None))
        self.Empl_Search_Btn_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem23 = self.Product_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Supplier_ID", None));
        ___qtablewidgetitem24 = self.Product_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem25 = self.Product_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem26 = self.Product_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem27 = self.Product_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Supplier Detail", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.Product_Qty.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.Product_Status_Comb.setItemText(0, QCoreApplication.translate("MainWindow", u"active", None))
        self.Product_Status_Comb.setItemText(1, QCoreApplication.translate("MainWindow", u"inactive", None))

        self.Clear_Product_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Update_Product_Btn.setText(QCoreApplication.translate("MainWindow", u" Update", None))
        self.Delete_Product_Btn.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.Save_Product_Btn.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.Product_Status_Comb_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Accessories", None))
        self.Product_Status_Comb_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Electronics", None))

        self.Product_Name.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Supplier_ID", None))
        self.Supplier_ID_Label.setText("")
        self.label_28.setText("")
        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.Supplier), QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Inventory Report", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Chart/Graph Area", None))
        self.Total_Sales_Label_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Out of Stock", None))
        self.Total_Category_Label_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Total_Category_Label_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
#if QT_CONFIG(tooltip)
        self.Clear_Bills_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the chart", None))
#endif // QT_CONFIG(tooltip)
        self.Clear_Bills_Btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.Search_Bills_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Generate the chart", None))
#endif // QT_CONFIG(tooltip)
        self.Search_Bills_Btn.setText(QCoreApplication.translate("MainWindow", u"Excute", None))
#if QT_CONFIG(tooltip)
        self.Export_Chart_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Export the chart as a PNG file", None))
#endif // QT_CONFIG(tooltip)
        self.Export_Chart_Btn.setText(QCoreApplication.translate("MainWindow", u"Export Chart", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Out of Stock", None))
        self.Total_Category_Label_9.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Total_Category_Label_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Date_Time_2.setText(QCoreApplication.translate("MainWindow", u"Figure Analysis", None))
        self.lbl_chart.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u ch\u1ec9nh g\u00f3c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Chart Selection", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 t\u1ed3n kho ", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 Supplier", None))

#if QT_CONFIG(tooltip)
        self.comboBox_3.setToolTip(QCoreApplication.translate("MainWindow", u"Select the type of chart to display", None))
#endif // QT_CONFIG(tooltip)
        self.FilterCategory_ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))

#if QT_CONFIG(tooltip)
        self.FilterCategory_ComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Filter data by category", None))
#endif // QT_CONFIG(tooltip)
        self.ChartType_Label.setText(QCoreApplication.translate("MainWindow", u"Chart Type", None))
        self.FilterCategory_Label.setText(QCoreApplication.translate("MainWindow", u"Filter by Category", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Chart Customization", None))
        self.ColorScheme_ComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.ColorScheme_ComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pastel", None))
        self.ColorScheme_ComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Bright", None))

#if QT_CONFIG(tooltip)
        self.ColorScheme_ComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a color scheme for the chart", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.StartAngle_SpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"Set the starting angle of the chart (0-360 degrees)", None))
#endif // QT_CONFIG(tooltip)
        self.ColorScheme_Label.setText(QCoreApplication.translate("MainWindow", u"Color Scheme", None))
        self.StartAngle_Label.setText(QCoreApplication.translate("MainWindow", u"Start Angle (degrees)", None))
        self.Loading_Label.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.ReportExport), QCoreApplication.translate("MainWindow", u"Report  Export", None))
        self.TrackingInvoice_2.setTabText(self.TrackingInvoice_2.indexOf(self.Report), QCoreApplication.translate("MainWindow", u"Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Group 11 Inventory Management System-Admin", None))
        self.Login_Btn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.Date_Time.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.show_infor.setText(QCoreApplication.translate("MainWindow", u"Infor", None))
        self.Date_Time_3.setText(QCoreApplication.translate("MainWindow", u"A Desktop App Product Power By Group 11", None))
    # retranslateUi

