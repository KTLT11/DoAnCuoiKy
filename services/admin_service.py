

from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView, QDialog, QVBoxLayout, QLabel, QLineEdit, \
    QHBoxLayout, QPushButton, QComboBox, QTableWidget, QWidget, QFileDialog, QListWidget
from PySide6.QtCore import QTimer, Slot, Qt
from PySide6.QtGui import QPixmap
from database.API_Admin import AdminExFnct_Api
from database.API_Login import logger
from gui.Admin_ui import Ui_MainWindow
from services.admin_infor_dialog import AdminInforDialog
from reportlab.lib.pagesizes import A5
from reportlab.lib import colors

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import matplotlib.pyplot as plt
import pandas as pd
import io
import os
import logging
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

# Thiết lập logging
logger = logging.getLogger(__name__)

class ChartDialog(QDialog):
    def __init__(self, pixmap, parent=None, on_resize_callback=None):
        super().__init__(parent)
        self.setWindowTitle("Chart Preview")
        self.setMinimumSize(600, 400)  # Kích thước tối thiểu
        self.setGeometry(100, 100, 800, 600)  # Kích thước mặc định
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)  # Cho phép phóng to
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(600, 400)
        self.on_resize_callback = on_resize_callback

    def resizeEvent(self, event):
        """Gọi callback khi dialog được thay đổi kích thước"""
        super().resizeEvent(event)
        if self.on_resize_callback:
            self.on_resize_callback(self.size().width(), self.size().height())

class AdminExFnct_Process(QMainWindow):
    def __init__(self, login_window=None, user_data=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.api = AdminExFnct_Api()
        self.login_window = login_window
        self.current_user = user_data
        self.chart_buffer = None
        self.chart_size = (5, 3)  # Kích thước mặc định của biểu đồ (inch)
        logger.debug(f"AdminExFnct_Process.__init__: login_window = {self.login_window}, current_user = {self.current_user}")

        # Load API key for weather
        load_dotenv()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")
        self.city = "Ho Chi Minh City"  # Thay bằng thành phố của kho

        # Khởi tạo các thiết lập
        self._setup_ui_properties()
        self._setup_search_timers()
        self._load_initial_data()
        self.setup_connection()

        # Khởi tạo QTimer để cập nhật số liệu Dashboard
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_dashboard_stats)
        self.update_timer.start(60000)  # Cập nhật mỗi 60 giây

        # Load Dashboard data
        self.update_dashboard_stats()
        self.show_revenue_chart()
        self.load_top_suppliers()
        self.load_top_products()
        self.load_recent_activities()
        self.load_weather()
        # không tự động chọn hàng trong bảng tracking invoice
        self.ui.TrackingInvoice_tableWidget.clearSelection()
        self.ui.TrackingInvoice_tableWidget.setCurrentCell(-1, -1)

    def _setup_ui_properties(self):
        """Cấu hình các thuộc tính UI"""
        for combo in [self.ui.category, self.ui.location, self.ui.supplier_inv]:
            combo.setEditable(False)
            combo.setInsertPolicy(QComboBox.InsertAtTop)

        for table in [self.ui.Supp_tableWidget, self.ui.Product_tableWidget,
                      self.ui.Category_tableWidget_2, self.ui.TrackingInvoice_tableWidget]:
            table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Đặt kích thước cố định cho revenue_chart_label
        if hasattr(self.ui, "revenue_chart_label"):
            self.ui.revenue_chart_label.setMinimumSize(500, 300)
            self.ui.revenue_chart_label.setMaximumSize(600, 350)

        self.apply_tab_stylesheet()
        self.ui.TrackingInvoice_2.tabBar().setExpanding(False)
        self.ui.TrackingInvoice_2.tabBar().setEnabled(False)
        self.ui.TrackingInvoice_2.setCurrentIndex(0)  # Dashboard mặc định

    def _setup_search_timers(self):
        """Khởi tạo timer debounce cho tìm kiếm"""
        self.search_timer_account = QTimer()
        self.search_timer_account.setInterval(300)
        self.search_timer_account.setSingleShot(True)

        self.search_timer_supplier = QTimer()
        self.search_timer_supplier.setInterval(300)
        self.search_timer_supplier.setSingleShot(True)

    def _load_initial_data(self):
        """Tải tất cả dữ liệu ban đầu"""
        self.load_suppliers()
        self.load_users()
        self.load_data()
        self.load_product_data()
        self.load_invoice_data()
        self.load_categories_for_filter()
        self.check_data_availability()

    def setup_connection(self):
        """Kết nối các thành phần UI với các hàm xử lý"""
        # Tracking Invoice
        self.ui.search_invoice_btn.clicked.connect(self.search_invoice)
        self.ui.print_btn.clicked.connect(self.print_invoices)
        self.ui.category.currentTextChanged.connect(self.on_category_changed)
        self.ui.location.currentTextChanged.connect(self.on_location_changed)

        # Inventory Functions
        self.ui.add.clicked.connect(self.add_inventory)
        self.ui.Empl_Update_Btn.clicked.connect(self.update_inventory)
        self.ui.Empl_Delete_Btn.clicked.connect(self.delete_inventory)
        self.ui.search.clicked.connect(self.search_inventory)
        self.ui.Empl_Save_Btn_4.clicked.connect(self.import_inventory)
        self.ui.Empl_Save_Btn_3.clicked.connect(self.export_inventory)
        self.ui.clear.clicked.connect(self.clear_inventory)
        self.ui.Category_tableWidget_2.cellClicked.connect(self.load_selected_inventory)

        # Navigation
        self.ui.Dash_Button.clicked.connect(self.show_Dashboard)
        self.ui.Employee_Button.clicked.connect(self.show_InventoryFunction)
        self.ui.Supplier_Button.clicked.connect(self.show_InvoiceStatus)
        self.ui.Category_Button_2.clicked.connect(self.show_Supplier)
        self.ui.Category_Button.clicked.connect(self.show_Account)
        self.ui.Products_Button.clicked.connect(self.show_Report)

        # User Management
        self.ui.Supplier_Save_Btn.clicked.connect(self.add_user)
        self.ui.Supplier_Update_Btn.clicked.connect(self.update_user)
        self.ui.Supplier_Delete_Btn.clicked.connect(self.delete_user)
        self.ui.Supplier_Clear_Btn.clicked.connect(self.clear_fields_user)
        self.ui.Supp_tableWidget.cellClicked.connect(self.load_selected_user)
        self.ui.Empl_Search_Btn_3.clicked.connect(self.search_user)
        self.ui.Supp_Search_box.textChanged.connect(self.search_timer_account.start)
        self.search_timer_account.timeout.connect(self.search_user)

        # Supplier Management
        self.ui.Save_Product_Btn.clicked.connect(self.add_supplier)
        self.ui.Update_Product_Btn.clicked.connect(self.update_supplier)
        self.ui.Delete_Product_Btn.clicked.connect(self.delete_supplier)
        self.ui.Clear_Product_Btn.clicked.connect(self.clear_fields_supplier)
        self.ui.Product_tableWidget.cellClicked.connect(self.load_selected_supplier)
        self.ui.Empl_Search_Btn_4.clicked.connect(self.search_supplier)
        self.ui.Product_SearchBox_Comb.textChanged.connect(self.search_timer_supplier.start)
        self.search_timer_supplier.timeout.connect(self.search_supplier)

        # Reports
        self.ui.comboBox_3.currentIndexChanged.connect(self.update_chart)
        self.ui.Search_Bills_Btn.clicked.connect(self.show_pie_chart)
        self.ui.Clear_Bills_Btn.clicked.connect(self.clear_pie_chart)
        if hasattr(self.ui, "FilterCategory_ComboBox"):
            self.ui.FilterCategory_ComboBox.currentTextChanged.connect(self.update_chart)
        if hasattr(self.ui, "Export_Chart_Btn"):
            self.ui.Export_Chart_Btn.clicked.connect(self.export_chart)
        if hasattr(self.ui, "revenue_chart_label"):
            self.ui.revenue_chart_label.mousePressEvent = self.show_revenue_chart_dialog

        # Show Infor
        self.ui.show_infor.clicked.connect(self.show_user_info_dialog)

        # Logout
        self.ui.Login_Btn.clicked.connect(self.logout)

    def apply_tab_stylesheet(self):
        """Áp dụng stylesheet để làm nổi bật tab hiện tại bằng màu xám"""
        tab_stylesheet = """
            QTabBar::tab {
                padding: 8px;
                border: 1px solid #C4C4C3;
                border-bottom: none;
                background: #E0E0E0;
            }
            QTabBar::tab:selected {
                background: #A9A9A9;
                font-weight: bold;
            }
            QTabBar::tab:!selected {
                background: #E0E0E0;
            }
            QTabBar::tab:hover {
                background: #D0D0D0;
            }
        """
        self.ui.TrackingInvoice_2.setStyleSheet(tab_stylesheet)
        logger.debug("Đã áp dụng stylesheet cho tabWidget.")

    def login(self, username, password):
        """Xử lý đăng nhập"""
        try:
            user = self.api.users.find_one({"username": username, "password": password}, {"_id": 0})
            if user:
                self.current_user = user
                self.show()
                return True
            else:
                QMessageBox.critical(self, "Error", "Invalid username or password!")
                return False
        except Exception as e:
            logger.error(f"Error during login: {e}")
            QMessageBox.critical(self, "Error", f"Login failed: {e}")
            return False

    def show_user_info_dialog(self):
        """Hiển thị hộp thoại thông tin tài khoản"""
        if not self.current_user:
            QMessageBox.critical(self, "Error", "No user is currently logged in!")
            return
        dialog = AdminInforDialog(self.current_user, self.api, self)
        dialog.exec()

    def logout(self):
        """Xử lý đăng xuất"""
        if QMessageBox.question(self, "Log Out", "Are you sure you want to log out?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.current_user = None
            self.close()
            logger.debug(f"AdminExFnct_Process.logout: self.login_window = {self.login_window}")
            if isinstance(self.login_window, QWidget):
                self.login_window.show()
            else:
                logger.error(f"self.login_window is not a QWidget: {self.login_window}")
                QMessageBox.critical(self, "Error", "Cannot return to login screen. Please restart the application.")

    # --- Account Functions ---
    def load_users(self):
        """Tải danh sách người dùng vào bảng"""
        try:
            users = self.api.get_users() or []
            self.ui.Supp_tableWidget.setRowCount(len(users))
            for row, user in enumerate(users):
                for col, value in enumerate([user.get("username", ""), user.get("password", ""), user.get("role", "")]):
                    self.ui.Supp_tableWidget.setItem(row, col, QTableWidgetItem(value))
        except Exception as e:
            logger.error(f"Error loading users: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load users: {e}")

    def add_user(self):
        """Thêm người dùng mới"""
        username = self.ui.Supp_invoice_No.text().strip()
        password = self.ui.Supp_Name.text().strip()
        role = self.ui.roleComboBox.currentText().strip()

        if not username or not password or not role:
            QMessageBox.warning(self, "Warning", "Please fill all fields!")
            return

        existing_user = self.api.users.find_one({"username": username})
        if existing_user:
            QMessageBox.warning(self, "Error", "Username already exists! Please choose a different username.")
            return

        new_user = {"username": username, "password": password, "role": role}
        self.api.add_user(new_user)
        self.load_users()
        self.clear_fields_user()
        QMessageBox.information(self, "Success", "User added successfully!")

    def update_user(self):
        """Cập nhật người dùng được chọn"""
        selected_row = self._validate_selection(self.ui.Supp_tableWidget, "user")
        if selected_row is None:
            return
        old_username = self.ui.Supp_tableWidget.item(selected_row, 0).text()
        new_data = {
            "username": self.ui.Supp_invoice_No.text().strip(),
            "password": self.ui.Supp_Name.text().strip(),
            "role": self.ui.roleComboBox.currentText().strip()
        }
        if not all(new_data.values()):
            QMessageBox.warning(self, "Warning", "Please fill all fields!")
            return
        if new_data["username"] != old_username:
            existing_user = self.api.users.find_one({"username": new_data["username"]})
            if existing_user:
                QMessageBox.warning(self, "Error", "Username already exists! Please choose a different username.")
                return
        self.api.update_user(old_username, new_data)
        self.load_users()
        self.clear_fields_user()
        self.ui.Supp_tableWidget.clearSelection()
        QMessageBox.information(self, "Success", f"User '{new_data['username']}' updated!")

    def delete_user(self):
        """Xóa người dùng được chọn"""
        selected_row = self._validate_selection(self.ui.Supp_tableWidget, "user")
        if selected_row is None:
            return
        username = self.ui.Supp_tableWidget.item(selected_row, 0).text()
        if QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete user '{username}'?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return
        self.api.delete_user(username)
        self.load_users()
        self.clear_fields_user()
        self.ui.Supp_tableWidget.clearSelection()
        QMessageBox.information(self, "Success", f"User '{username}' deleted!")

    def clear_fields_user(self):
        """Xóa các trường nhập liệu người dùng"""
        self.ui.Supp_invoice_No.clear()
        self.ui.Supp_Name.clear()
        self.ui.roleComboBox.setCurrentIndex(0)
        self.ui.Supp_tableWidget.clearSelection()
        self.ui.Supp_invoice_No.setFocus()

    def load_selected_user(self, row, _):
        """Tải dữ liệu người dùng được chọn"""
        if row >= 0:
            self.ui.Supp_invoice_No.setText(self.ui.Supp_tableWidget.item(row, 0).text())
            self.ui.Supp_Name.setText(self.ui.Supp_tableWidget.item(row, 1).text())
            role = self.ui.Supp_tableWidget.item(row, 2).text()
            index = self.ui.roleComboBox.findText(role)
            self.ui.roleComboBox.setCurrentIndex(index if index != -1 else 0)

    def search_user(self):
        """Tìm kiếm người dùng và cập nhật bảng"""
        search_text = self.ui.Supp_Search_box.text().strip()
        search_type = self.ui.Supp_SearchBy_Comb.currentText()
        if not search_text:
            self.load_users()
            return
        field = "username" if search_type == "UserName" else "role"
        try:
            users = self.api.search_users(field, search_text) or []
            self.ui.Supp_tableWidget.setRowCount(len(users))
            for row, user in enumerate(users):
                for col, value in enumerate([user.get("username", ""), user.get("password", ""), user.get("role", "")]):
                    self.ui.Supp_tableWidget.setItem(row, col, QTableWidgetItem(value))
        except Exception as e:
            logger.error(f"Error searching users: {e}")
            QMessageBox.critical(self, "Error", f"Failed to search users: {e}")

    # --- Supplier Functions ---
    def load_suppliers(self):
        """Tải danh sách nhà cung cấp vào bảng và combo box"""
        try:
            suppliers = self.api.get_suppliers() or []
            self.ui.Product_tableWidget.setRowCount(len(suppliers))
            for row, supplier in enumerate(suppliers):
                items = [
                    supplier.get("supplier_id", ""),
                    supplier.get("category", ""),
                    supplier.get("supplier_name", ""),
                    str(supplier.get("contact_number", "")),
                    supplier.get("status", "")
                ]
                for col, value in enumerate(items):
                    self.ui.Product_tableWidget.setItem(row, col, QTableWidgetItem(value))

            supplier_ids = [s.get("supplier_id", "") for s in suppliers]
            self.ui.supplier_inv.clear()
            if supplier_ids:
                self.ui.supplier_inv.addItems(supplier_ids)
                self.ui.supplier_inv.setCurrentIndex(0)
            else:
                self.ui.supplier_inv.addItem("Không có supplier")
                self.ui.supplier_inv.setEnabled(False)
        except Exception as e:
            logger.error(f"Error loading suppliers: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load suppliers: {e}")

    def generate_supplier_id(self):
        """Tạo supplier_id mới"""
        suppliers = self.api.get_suppliers()
        if not suppliers:
            return "S001"

        supplier_ids = [supplier["supplier_id"] for supplier in suppliers]
        valid_ids = [sid for sid in supplier_ids if sid.startswith("S") and sid[1:].isdigit()]
        if not valid_ids:
            return "S001"
        max_id = max(int(sid[1:]) for sid in valid_ids)
        new_id = max_id + 1
        return f"S{new_id:03d}"

    def add_supplier(self):
        """Thêm nhà cung cấp mới"""
        category = self.ui.Product_Status_Comb_2.currentText().strip()
        name = self.ui.Product_Name.text().strip()
        contact_str = self.ui.Product_Qty.text().strip()
        status = self.ui.Product_Status_Comb.currentText().strip()

        if not category or not name or not contact_str or not status:
            QMessageBox.warning(self, "Warning", "Please fill all fields!")
            return

        existing_supplier_name = self.api.suppliers.find_one({"supplier_name": name})
        if existing_supplier_name:
            QMessageBox.warning(self, "Error", "Supplier Name already exists! Please choose a different Supplier Name.")
            return

        if not contact_str.isdigit():
            QMessageBox.warning(self, "Warning", "Contact must be a valid number!")
            return
        if not contact_str.startswith("0"):
            QMessageBox.warning(self, "Warning", "Contact must start with 0!")
            return
        if len(contact_str) != 10:
            QMessageBox.warning(self, "Warning", "Contact must be exactly 10 digits!")
            return
        if contact_str[1] == "0":
            QMessageBox.warning(self, "Warning", "The second digit of Contact must not be 0!")
            return

        supplier_id = self.generate_supplier_id()
        contact = contact_str

        new_supplier = {
            "supplier_id": supplier_id,
            "category": category,
            "supplier_name": name,
            "contact_number": contact,
            "status": status
        }
        self.api.add_supplier(new_supplier)
        self.load_suppliers()
        self.clear_fields_supplier()
        QMessageBox.information(self, "Success", "Supplier added successfully!")

    def update_supplier(self):
        """Cập nhật nhà cung cấp được chọn"""
        selected_row = self._validate_selection(self.ui.Product_tableWidget, "supplier")
        if selected_row is None:
            return

        old_supplier_id = self.ui.Product_tableWidget.item(selected_row, 0).text()
        contact_str = self.ui.Product_Qty.text().strip()

        old_contact = self.ui.Product_tableWidget.item(selected_row, 3).text()
        contact_str = old_contact if not contact_str or contact_str.strip() == "" else contact_str

        if not contact_str.isdigit():
            QMessageBox.warning(self, "Warning", "Contact must be a valid number!")
            return
        if not contact_str.startswith("0"):
            QMessageBox.warning(self, "Warning", "Contact must start with 0!")
            return
        if len(contact_str) != 10:
            QMessageBox.warning(self, "Warning", "Contact must be exactly 10 digits!")
            return
        if contact_str[1] == "0":
            QMessageBox.warning(self, "Warning", "The second digit of Contact must not be 0!")
            return

        contact = contact_str

        new_data = {
            "supplier_id": old_supplier_id,
            "category": self.ui.Product_Status_Comb_2.currentText().strip(),
            "supplier_name": self.ui.Product_Name.text().strip(),
            "contact_number": contact,
            "status": self.ui.Product_Status_Comb.currentText().strip()
        }
        if not all(new_data.values()):
            QMessageBox.warning(self, "Warning", "Please fill all fields!")
            return

        self.api.update_supplier(old_supplier_id, new_data)
        self.load_suppliers()
        self.clear_fields_supplier()
        self.ui.Product_tableWidget.clearSelection()
        QMessageBox.information(self, "Success", "Supplier updated successfully!")

    def delete_supplier(self):
        """Xóa nhà cung cấp được chọn"""
        selected_row = self._validate_selection(self.ui.Product_tableWidget, "supplier")
        if selected_row is None:
            return
        supplier_id = self.ui.Product_tableWidget.item(selected_row, 0).text()
        if QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete supplier '{supplier_id}'?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return
        self.api.delete_supplier(supplier_id)
        self.load_suppliers()
        self.clear_fields_supplier()
        self.ui.Product_tableWidget.clearSelection()
        QMessageBox.information(self, "Success", f"Supplier '{supplier_id}' deleted!")

    def clear_fields_supplier(self):
        """Xóa các trường nhập liệu nhà cung cấp"""
        self.ui.Supplier_ID_Label.clear()
        self.ui.Product_Status_Comb_2.setCurrentIndex(0)
        self.ui.Product_Name.clear()
        self.ui.Product_Qty.clear()
        self.ui.Product_Status_Comb.setCurrentIndex(0)
        self.ui.Product_tableWidget.clearSelection()
        self.ui.Product_Name.setFocus()

    def load_selected_supplier(self, row, _):
        """Tải dữ liệu nhà cung cấp được chọn"""
        if row >= 0:
            self.ui.Supplier_ID_Label.setText(self.ui.Product_tableWidget.item(row, 0).text())
            self.ui.Product_Status_Comb_2.setCurrentText(self.ui.Product_tableWidget.item(row, 1).text())
            self.ui.Product_Name.setText(self.ui.Product_tableWidget.item(row, 2).text())
            self.ui.Product_Qty.setText(self.ui.Product_tableWidget.item(row, 3).text())
            self.ui.Product_Status_Comb.setCurrentText(self.ui.Product_tableWidget.item(row, 4).text())

    def search_supplier(self):
        """Tìm kiếm nhà cung cấp và cập nhật bảng"""
        search_by = self.ui.Product_SearchBy_Comb.currentText().strip()
        search_text = self.ui.Product_SearchBox_Comb.text().strip()
        if not search_text:
            self.load_suppliers()
            return
        field_map = {"Supplier": "supplier_id", "Category": "category", "Name": "supplier_name"}
        field = field_map.get(search_by)
        if not field:
            return
        try:
            suppliers = self.api.search_suppliers(field, search_text) or []
            self.ui.Product_tableWidget.setRowCount(len(suppliers))
            for row, supplier in enumerate(suppliers):
                items = [
                    supplier.get("supplier_id", ""),
                    supplier.get("category", ""),
                    supplier.get("supplier_name", ""),
                    str(supplier.get("contact_number", "")),
                    supplier.get("status", "")
                ]
                for col, value in enumerate(items):
                    self.ui.Product_tableWidget.setItem(row, col, QTableWidgetItem(value))
        except Exception as e:
            logger.error(f"Error searching suppliers: {e}")
            QMessageBox.critical(self, "Error", f"Failed to search suppliers: {e}")

    # --- Report Functions ---
    def load_categories_for_filter(self):
        """Tải danh mục để lọc trong tab Report"""
        supplier_categories = self.api.suppliers.distinct("category")
        product_categories = self.api.products.distinct("category")
        categories = sorted(set(supplier_categories + product_categories))
        if hasattr(self.ui, "FilterCategory_ComboBox"):
            self.ui.FilterCategory_ComboBox.clear()
            self.ui.FilterCategory_ComboBox.addItem("All")
            self.ui.FilterCategory_ComboBox.addItems(categories)

    def check_data_availability(self):
        """Kiểm tra dữ liệu để kích hoạt nút Search trong tab Report"""
        has_supplier_data = bool(self.api.get_suppliers())
        has_inventory_data = bool(self.api.get_products())
        if not (has_supplier_data or has_inventory_data):
            self.ui.Search_Bills_Btn.setEnabled(False)
        else:
            self.ui.Search_Bills_Btn.setEnabled(True)

    def update_chart(self):
        """Cập nhật biểu đồ khi thay đổi bộ lọc"""
        self.show_pie_chart()

    @Slot()
    def show_pie_chart(self):
        """Tạo và hiển thị biểu đồ tròn"""
        if hasattr(self.ui, "Loading_Label"):
            self.ui.Loading_Label.setText("Loading...")
            self.ui.Loading_Label.repaint()

        chart_type = self.ui.comboBox_3.currentText().strip()
        filter_category = self.ui.FilterCategory_ComboBox.currentText().strip() if hasattr(self.ui, "FilterCategory_ComboBox") else "All"
        color_scheme = self.ui.ColorScheme_ComboBox.currentText().strip() if hasattr(self.ui, "ColorScheme_ComboBox") else "Default"
        start_angle = self.ui.StartAngle_SpinBox.value() if hasattr(self.ui, "StartAngle_SpinBox") else 140

        colors = {
            "Default": None,
            "Pastel": plt.cm.Pastel1.colors,
            "Bright": plt.cm.Set1.colors
        }.get(color_scheme, None)

        match_filter = {"category": {"$ne": ""}}
        if filter_category and filter_category != "All":
            match_filter["category"] = filter_category

        if chart_type == "Biểu đồ Supplier":
            pipeline = [
                {"$match": match_filter},
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$project": {"category": "$_id", "count": 1, "_id": 0}}
            ]
            data = list(self.api.suppliers.aggregate(pipeline))
            if not data:
                if hasattr(self.ui, "Loading_Label"):
                    self.ui.Loading_Label.setText("")
                QMessageBox.warning(self, "Warning", "No supplier data available!")
                return
            categories = [item["category"] for item in data]
            counts = [item["count"] for item in data]
            title = "Supplier Distribution by Category"
        elif chart_type == "Biểu đồ tồn kho":
            products = self.api.get_products()
            invalid_data = [p for p in products if not isinstance(p.get("current_stock", 0), (int, float)) or p.get("current_stock", 0) < 0]
            if invalid_data:
                if hasattr(self.ui, "Loading_Label"):
                    self.ui.Loading_Label.setText("")
                QMessageBox.warning(self, "Warning", f"Found {len(invalid_data)} invalid stock values. They will be ignored.")

            pipeline = [
                {"$match": match_filter},
                {"$group": {"_id": "$category", "total_stock": {"$sum": "$current_stock"}}},
                {"$project": {"category": "$_id", "total_stock": 1, "_id": 0}}
            ]
            data = list(self.api.products.aggregate(pipeline))
            if not data:
                if hasattr(self.ui, "Loading_Label"):
                    self.ui.Loading_Label.setText("")
                QMessageBox.warning(self, "Warning", "No inventory data available!")
                return
            categories = [item["category"] for item in data]
            counts = [item["total_stock"] for item in data]
            title = "Current Stock Distribution by Category"
        else:
            if hasattr(self.ui, "Loading_Label"):
                self.ui.Loading_Label.setText("")
            return

        plt.clf()
        fig, ax = plt.subplots(figsize=(6, 6))

        def autopct_format(values):
            def my_format(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return f'{pct:.1f}%\n({val})'
            return my_format

        ax.pie(counts, labels=categories, autopct=autopct_format(counts), startangle=start_angle, colors=colors)
        ax.set_title(title)
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.read())
        self.ui.lbl_chart.setPixmap(pixmap)
        self.ui.lbl_chart.setScaledContents(True)
        self.chart_buffer = buf
        plt.close(fig)
        if hasattr(self.ui, "Loading_Label"):
            self.ui.Loading_Label.setText("")
        QMessageBox.information(self, "Success", "Chart generated successfully!")

    @Slot()
    def export_chart(self):
        """Xuất biểu đồ dưới dạng PNG"""
        if not hasattr(self, 'chart_buffer') or self.chart_buffer is None:
            QMessageBox.warning(self, "Warning", "No chart available to export!")
            return
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Chart", "", "PNG Files (*.png)")
        if file_name:
            with open(file_name, 'wb') as f:
                self.chart_buffer.seek(0)
                f.write(self.chart_buffer.read())
            QMessageBox.information(self, "Success", "Chart exported successfully!")

    @Slot()
    def clear_pie_chart(self):
        """Xóa biểu đồ tròn"""
        self.ui.lbl_chart.clear()
        self.chart_buffer = None
        if hasattr(self.ui, "Loading_Label"):
            self.ui.Loading_Label.setText("")

    def show_chart_dialog(self, event):
        """Hiển thị biểu đồ trong dialog có thể thay đổi kích thước"""
        if self.ui.lbl_chart.pixmap() and not self.ui.lbl_chart.pixmap().isNull():
            dialog = ChartDialog(self.ui.lbl_chart.pixmap(), self)
            dialog.exec_()

    # --- Dashboard Functions ---
    def update_chart_size(self, width, height):
        """Cập nhật kích thước biểu đồ dựa trên kích thước dialog"""
        new_width = width / 100
        new_height = height / 100
        self.chart_size = (new_width, new_height)
        logger.debug(f"Updated chart size to: {self.chart_size}")
        self.show_revenue_chart()

    def show_revenue_chart(self):
        """Hiển thị biểu đồ đường doanh thu theo tuần"""
        if not hasattr(self.ui, "revenue_chart_label"):
            return
        revenue_data = self.api.get_revenue_by_week()
        if not revenue_data:
            self.ui.revenue_chart_label.setText("No revenue data available for the past 4 weeks.")
            return

        weeks = [item["week"] for item in revenue_data]
        values = [item["total_value"] for item in revenue_data]

        plt.clf()
        fig, ax = plt.subplots(figsize=self.chart_size)

        plt.rc('font', size=11)
        plt.rc('axes', titlesize=11)
        plt.rc('axes', labelsize=9)
        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.rc('legend', fontsize=9)

        ax.plot(weeks, values, marker='o', linestyle='-', color='b', label='Revenue')
        ax.set_title("Weekly Revenue")
        ax.set_xlabel("Week (YYYY-WW)")
        ax.set_ylabel("Total Value")
        ax.grid(True)
        ax.legend()

        plt.xticks(rotation=30, ha='right')
        plt.subplots_adjust(bottom=0.25)
        plt.tight_layout()

        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buf.read())
        self.ui.revenue_chart_label.setPixmap(pixmap)
        self.ui.revenue_chart_label.setScaledContents(True)

        self.chart_buffer = buf
        plt.close(fig)

    def show_revenue_chart_dialog(self, event):
        """Hiển thị biểu đồ doanh thu trong dialog có thể thay đổi kích thước"""
        if hasattr(self.ui, "revenue_chart_label") and self.ui.revenue_chart_label.pixmap() and not self.ui.revenue_chart_label.pixmap().isNull():
            dialog = ChartDialog(self.ui.revenue_chart_label.pixmap(), self, self.update_chart_size)
            dialog.exec_()

    def load_top_suppliers(self):
        """Hiển thị top nhà cung cấp"""
        if not hasattr(self.ui, "top_suppliers_table"):
            return
        top_suppliers = self.api.get_top_suppliers(limit=5)
        self.ui.top_suppliers_table.setRowCount(len(top_suppliers))
        for row, supplier in enumerate(top_suppliers):
            self.ui.top_suppliers_table.setItem(row, 0, QTableWidgetItem(supplier["supplier_name"]))
            self.ui.top_suppliers_table.setItem(row, 1, QTableWidgetItem(str(supplier["product_count"])))

    def load_top_products(self):
        """Hiển thị top sản phẩm bán chạy"""
        if not hasattr(self.ui, "top_products_table"):
            return
        top_products = self.api.get_top_products_sold(limit=5)
        if not top_products:
            self.ui.top_products_table.setRowCount(1)
            self.ui.top_products_table.setItem(0, 0, QTableWidgetItem("No data available"))
            self.ui.top_products_table.setItem(0, 1, QTableWidgetItem(""))
            return
        self.ui.top_products_table.setRowCount(len(top_products))
        for row, product in enumerate(top_products):
            self.ui.top_products_table.setItem(row, 0, QTableWidgetItem(product["product_name"]))
            self.ui.top_products_table.setItem(row, 1, QTableWidgetItem(str(product["total_sold"])))

    def update_dashboard_stats(self):
        """Cập nhật số liệu trên Dashboard"""
        total_cost = sum(invoice["total_price"] for invoice in self.api.invoices.find({}, {"total_price": 1}))
        total_products = self.api.products.count_documents({})
        total_suppliers = self.api.suppliers.count_documents({})
        total_categories = len(self.api.products.distinct("category"))

        if hasattr(self.ui, "Total_Sales_Label"):
            self.ui.Total_Sales_Label.setText(f"{total_cost}")
        if hasattr(self.ui, "Total_Products_Label"):
            self.ui.Total_Products_Label.setText(f"{total_products}")
        if hasattr(self.ui, "Total_Employee_Label"):
            self.ui.Total_Employee_Label.setText(f"{total_suppliers}")
        if hasattr(self.ui, "Total_Category_Label"):
            self.ui.Total_Category_Label.setText(f"{total_categories}")

        self.load_data()

    def load_recent_activities(self):
        """Hiển thị các hoạt động gần đây"""
        if not hasattr(self.ui, "recent_activities_list"):
            return
        activities = self.api.get_recent_activities()
        self.ui.recent_activities_list.clear()
        for activity in activities:
            self.ui.recent_activities_list.addItem(activity["message"])

    def load_weather(self):
        """Lấy thông tin thời tiết từ OpenWeatherMap"""
        if not hasattr(self.ui, "weather_label"):
            return
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                self.ui.weather_label.setText(f"Weather: {temp}°C, {description}")
            else:
                self.ui.weather_label.setText("Weather: Failed to load")
        except Exception as e:
            self.ui.weather_label.setText("Weather: Error")
            logger.error(f"Error loading weather: {e}")

    # --- Data Loading Methods ---
    def load_data(self):
        """Tải thống kê kho vào Dashboard"""
        try:
            reorder_count, out_of_stock_count, current_stock_count = self.api.get_reorder_stats() or (0, 0, 0)
            self.ui.Total_Sales_Label_3.setText(f"Reorder: {reorder_count}")
            self.ui.Total_Category_Label_4.setText(f"Out of Stock: {out_of_stock_count}")
            self.ui.Total_Category_Label_10.setText(f"Current Stock: {current_stock_count}")
        except Exception as e:
            logger.error(f"Error loading stats: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load stats: {e}")

    def load_product_data(self):
        """Tải dữ liệu sản phẩm vào bảng và cập nhật combo boxes"""
        try:
            data = self.api.get_all_products_with_categories() or {"products": [], "categories": [], "locations": []}
            products = data["products"]
            self.ui.Category_tableWidget_2.setRowCount(len(products))
            for row, product in enumerate(products):
                items = [
                    product.get("product_id", ""),
                    product.get("product_name", ""),
                    product.get("category", ""),
                    str(product.get("current_stock", 0)),
                    product.get("supplier_id", ""),
                    str(product.get("price_per_unit", 0.0)),
                    str(product.get("cost_per_unit", 0.0)),
                    product.get("location_number", ""),
                    "Yes" if product.get("current_stock", 0) <= 10 else "No"
                ]
                for col, value in enumerate(items):
                    self.ui.Category_tableWidget_2.setItem(row, col, QTableWidgetItem(value))

            self.ui.category.clear()
            self.ui.category.addItems(data["categories"] or ["Không có danh mục"])
            self.ui.location.clear()
            self.ui.location.addItems(data["locations"] or ["Không có vị trí"])
            self._generate_product_id()

            # Đảm bảo không có hàng nào được chọn khi tải dữ liệu
            self.ui.Category_tableWidget_2.clearSelection()
            self.ui.Category_tableWidget_2.setCurrentCell(-1, -1)

        except Exception as e:
            logger.error(f"Error loading product data: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load product data: {e}")

    def update_invoice_status(self, row, invoice_id, new_status, dialog):
        """Cập nhật trạng thái hóa đơn và tải lại bảng"""
        if not invoice_id or not new_status:
            QMessageBox.warning(self, "Cảnh báo", "Mã hóa đơn hoặc trạng thái mới không hợp lệ!")
            return

        try:
            success = self.api.update_invoice_status(invoice_id, new_status)
            if success:
                QMessageBox.information(self, "Thành công",
                                        f"Trạng thái hóa đơn {invoice_id} đã được cập nhật thành {new_status}!")
                dialog.accept()
                self.load_invoice_data()  # Tải lại bảng để phản ánh thay đổi
            else:
                QMessageBox.warning(self, "Cảnh báo",
                                    f"Không thể cập nhật trạng thái hóa đơn {invoice_id}. Hóa đơn không tồn tại hoặc không có thay đổi!")
        except Exception as e:
            logger.error(f"Lỗi khi cập nhật trạng thái hóa đơn {invoice_id}: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật trạng thái hóa đơn: {str(e)}")

    def load_invoice_data(self):
        """Tải dữ liệu hóa đơn vào bảng và thêm nút Confirm"""
        try:
            invoices = self.api.get_all_invoices() or []
            if not invoices:
                QMessageBox.information(self, "Thông báo", "Không có hóa đơn nào để hiển thị!")
                self.ui.TrackingInvoice_tableWidget.setRowCount(0)
                return

            self.ui.TrackingInvoice_tableWidget.setRowCount(len(invoices))
            for row, invoice in enumerate(invoices):
                cart = invoice.get("cart", [{}])[0] if invoice.get("cart") else {}
                items = [
                    invoice.get("invoice_id", "N/A"),
                    cart.get("product_name", "Không có sản phẩm"),
                    invoice.get("invoice_date", "N/A"),
                    str(cart.get("quantity", 0)),
                    str(invoice.get("total_price", 0.0)),
                    invoice.get("status", "Unknown"),
                ]
                for col, value in enumerate(items):
                    item = QTableWidgetItem(value)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Không cho chỉnh sửa trực tiếp trên bảng
                    self.ui.TrackingInvoice_tableWidget.setItem(row, col, item)

                confirm_btn = QPushButton("Confirm")
                confirm_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #2196F3;
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #42A5F5;
                    }
                """)
                confirm_btn.clicked.connect(
                    lambda checked, r=row, inv_id=invoice.get("invoice_id", ""): self.show_confirm_dialog(r, inv_id)
                )
                self.ui.TrackingInvoice_tableWidget.setCellWidget(row, 6, confirm_btn)

            # Reset lựa chọn để tránh lỗi
            self.ui.TrackingInvoice_tableWidget.clearSelection()
            self.ui.TrackingInvoice_tableWidget.setCurrentCell(-1, -1)

        except Exception as e:
            logger.error(f"Lỗi khi tải dữ liệu hóa đơn: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu hóa đơn: {str(e)}")
            self.ui.TrackingInvoice_tableWidget.setRowCount(0)
            # Điều chỉnh bảng tự động co giãn theo nội dung
            self.ui.TrackingInvoice_tableWidget.resizeColumnsToContents()
            self.ui.TrackingInvoice_tableWidget.horizontalHeader().setStretchLastSection(True)
            self.ui.TrackingInvoice_tableWidget.setRowCount(0)  # Xóa toàn bộ hàng trước khi thêm mới


    def search_invoice(self):
        """Tìm kiếm hóa đơn và cập nhật bảng"""
        try:
            search_value = self.ui.Emp_Search_box_2.text().strip()
            if not hasattr(self.ui, 'Emp_SearchBy_Comb_2'):
                search_field = "invoice_id"
            else:
                # Lấy giá trị từ combobox và ánh xạ sang tên trường trong cơ sở dữ liệu
                search_option = self.ui.Emp_SearchBy_Comb_2.currentText()
                field_mapping = {
                    "Invoice ID": "invoice_id",
                    "Product Name": "product_name",  # Sẽ xử lý cart.product_name trong API
                    "Invoice Date": "invoice_date",
                    "QTY": "quantity",  # Sẽ xử lý cart.quantity trong API
                    "Price": "total_price",  # Đúng: Ánh xạ "Price" sang "total_price"
                    "Status": "status"
                }
                search_field = field_mapping.get(search_option, "invoice_id")

            if not search_value:
                self.load_invoice_data()
                return

            invoices = self.api.search_invoice(search_field, search_value)
            if not invoices:
                QMessageBox.information(self, "Thông báo", "Không tìm thấy hóa đơn nào phù hợp!")
                self.ui.TrackingInvoice_tableWidget.setRowCount(0)
                return

            self.ui.TrackingInvoice_tableWidget.setRowCount(len(invoices))
            for row, invoice in enumerate(invoices):
                cart = invoice.get("cart", [{}])[0] if invoice.get("cart") else {}
                items = [
                    invoice.get("invoice_id", "N/A"),
                    cart.get("product_name", "Không có sản phẩm"),
                    invoice.get("invoice_date", "N/A"),
                    str(cart.get("quantity", 0)),
                    str(invoice.get("total_price", 0.0)),
                    invoice.get("status", "Unknown"),
                    "Có" if invoice.get("status") == "Done" else "Không"
                ]
                for col, value in enumerate(items):
                    item = QTableWidgetItem(value)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Không cho chỉnh sửa trực tiếp trên bảng
                    self.ui.TrackingInvoice_tableWidget.setItem(row, col, item)

                # Thêm nút Confirm vào cột cuối cùng (cột 6)
                confirm_btn = QPushButton("Confirm")
                confirm_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #2196F3;
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #42A5F5;
                    }
                """)
                confirm_btn.clicked.connect(
                    lambda checked, r=row, inv_id=invoice.get("invoice_id", ""): self.show_confirm_dialog(r, inv_id)
                )
                self.ui.TrackingInvoice_tableWidget.setCellWidget(row, 6, confirm_btn)

            # Reset lựa chọn để tránh lỗi
            self.ui.TrackingInvoice_tableWidget.clearSelection()
            self.ui.TrackingInvoice_tableWidget.setCurrentCell(-1, -1)

        except Exception as e:
            logger.error(f"Lỗi khi tìm kiếm hóa đơn: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể tìm kiếm hóa đơn: {str(e)}")
            self.ui.TrackingInvoice_tableWidget.setRowCount(0)
            # Điều chỉnh bảng tự động co giãn theo nội dung
            self.ui.TrackingInvoice_tableWidget.resizeColumnsToContents()
            self.ui.TrackingInvoice_tableWidget.horizontalHeader().setStretchLastSection(True)
            self.ui.TrackingInvoice_tableWidget.setRowCount(0)  # Xóa toàn bộ hàng trước khi thêm mới


    def show_confirm_dialog(self, row, invoice_id):
        """Hiển thị hộp thoại để xác nhận trạng thái hóa đơn"""
        if not invoice_id:
            QMessageBox.warning(self, "Cảnh báo", "Mã hóa đơn không hợp lệ!")
            return

        try:
            current_status = self.ui.TrackingInvoice_tableWidget.item(row,
                                                                      5).text() if self.ui.TrackingInvoice_tableWidget.item(
                row, 5) else "Unknown"
        except Exception as e:
            logger.error(f"Lỗi khi lấy trạng thái hiện tại tại hàng {row}: {e}")
            current_status = "Unknown"

        dialog = QDialog(self)
        dialog.setWindowTitle("Xác nhận trạng thái hóa đơn")
        dialog.setFixedSize(300, 200)

        layout = QVBoxLayout()
        current_status_label = QLabel(f"Trạng thái hiện tại: {current_status}")
        current_status_label.setStyleSheet("font-weight: bold; color: #333333;")
        layout.addWidget(current_status_label)

        label = QLabel("Chọn trạng thái mới cho hóa đơn:")
        layout.addWidget(label)

        status_combo = QComboBox()
        status_options = ["Prepare", "Transportation", "Done"]
        status_combo.addItems(status_options)

        if current_status in status_options:
            status_combo.setCurrentText(current_status)
        else:
            status_combo.setCurrentIndex(0)

        layout.addWidget(status_combo)

        button_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Hủy")

        ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #66BB6A;
            }
        """)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #EF5350;
            }
        """)

        ok_btn.clicked.connect(lambda: self.update_invoice_status(row, invoice_id, status_combo.currentText(), dialog))
        cancel_btn.clicked.connect(dialog.reject)

        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)

        dialog.setLayout(layout)
        dialog.exec()

    def _generate_product_id(self):
        """Tạo product_id mới"""
        try:
            new_id = self.api.get_max_product_id() or "P001"
            self.ui.id.setText(new_id)
            self.ui.id.setReadOnly(True)
        except Exception as e:
            logger.error(f"Error generating product ID: {e}")
            self.ui.id.setText("P001")

    # --- Inventory Management ---
    def search_inventory(self):
        """Tìm kiếm sản phẩm và cập nhật bảng"""
        search_input = self.ui.Emp_Search_box.text().strip().lower()
        search_field = self.ui.Emp_SearchBy_Comb.currentText().lower().replace(" ", "_")
        try:
            if not search_input:
                self.load_product_data()
                return
            results = self.api.search_product(search_field, search_input) or []
            self.ui.Category_tableWidget_2.setRowCount(len(results))
            for row, product in enumerate(results):
                items = [
                    product.get("product_id", ""),
                    product.get("product_name", ""),
                    product.get("category", ""),
                    str(product.get("current_stock", 0)),
                    product.get("supplier_id", ""),
                    str(product.get("price_per_unit", 0.0)),
                    str(product.get("cost_per_unit", 0.0)),
                    product.get("location_number", ""),
                    "Yes" if product.get("current_stock", 0) <= 10 else "No"
                ]
                for col, value in enumerate(items):
                    self.ui.Category_tableWidget_2.setItem(row, col, QTableWidgetItem(value))

            # Đảm bảo không có hàng nào được chọn sau khi tìm kiếm
            self.ui.Category_tableWidget_2.clearSelection()
            self.ui.Category_tableWidget_2.setCurrentCell(-1, -1)

        except Exception as e:
            logger.error(f"Error searching inventory: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể tìm kiếm kho: {e}")

    def add_inventory(self):
        """Thêm sản phẩm mới"""
        product_data = self._get_inventory_input()
        if not product_data:
            return
        try:
            result = self.api.add_product(product_data)
            if result == 0:
                self._update_combo_boxes(product_data["category"], product_data["location_number"], product_data["supplier_id"])
                self.clear_inventory()
                QMessageBox.information(self, "Thành công", "Thêm sản phẩm thành công!")
                self.load_product_data()  # Reset lựa chọn sau khi thêm
            else:
                QMessageBox.critical(self, "Lỗi", "Mã sản phẩm đã tồn tại!")
        except Exception as e:
            logger.error(f"Error adding product: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể thêm sản phẩm: {e}")

    def _get_inventory_input(self):
        """Lấy và kiểm tra dữ liệu đầu vào của kho"""
        fields = {
            "product_id": self.ui.id.text().strip(),
            "product_name": self.ui.name.text().strip(),
            "category": self.ui.category.currentText().strip(),
            "current_stock": self.ui.stock.text().strip(),
            "supplier_id": self.ui.supplier_inv.currentText().strip(),
            "price_per_unit": self.ui.value.text().strip(),
            "cost_per_unit": self.ui.cost.text().strip(),
            "location_number": self.ui.location.currentText().strip()
        }

        if not all(fields.values()):
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng điền đầy đủ các trường!")
            return None

        try:
            stock = int(fields["current_stock"])
            price = float(fields["price_per_unit"])
            cost = float(fields["cost_per_unit"])
            if stock < 0:
                raise ValueError("Số lượng tồn kho không thể âm!")
            if price <= cost:
                raise ValueError("Giá bán phải lớn hơn giá vốn!")
            supplier_ids = [self.ui.supplier_inv.itemText(i) for i in range(self.ui.supplier_inv.count())]
            if fields["supplier_id"] not in supplier_ids or fields["supplier_id"] == "Không có supplier":
                raise ValueError("Nhà cung cấp không hợp lệ!")
            return {
                "product_id": fields["product_id"],
                "product_name": fields["product_name"],
                "category": fields["category"],
                "current_stock": stock,
                "supplier_id": fields["supplier_id"],
                "price_per_unit": price,
                "cost_per_unit": cost,
                "location_number": fields["location_number"]
            }
        except ValueError as e:
            QMessageBox.critical(self, "Lỗi", f"Dữ liệu không hợp lệ: {e}")
            return None

    def update_inventory(self):
        """Cập nhật sản phẩm được chọn"""
        selected_row = self.ui.Category_tableWidget_2.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa chọn sản phẩm nào!")
            return
        product_id = self.ui.Category_tableWidget_2.item(selected_row, 0).text()
        updated_data = self._get_inventory_input()
        if not updated_data:
            return
        try:
            if self.api.update_product(product_id, updated_data):
                self._update_combo_boxes(updated_data["category"], updated_data["location_number"], updated_data["supplier_id"])
                self.clear_inventory()
                QMessageBox.information(self, "Thành công", "Cập nhật sản phẩm thành công!")
                self.load_product_data()  # Reset lựa chọn sau khi cập nhật
            else:
                QMessageBox.critical(self, "Lỗi", "Cập nhật thất bại!")
        except Exception as e:
            logger.error(f"Error updating product: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật sản phẩm: {e}")

    def delete_inventory(self):
        """Xóa sản phẩm được chọn"""
        selected_row = self.ui.Category_tableWidget_2.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa chọn sản phẩm nào!")
            return

        product_id = self.ui.Category_tableWidget_2.item(selected_row, 0).text()
        if QMessageBox.question(self, "Xác nhận xóa", f"Bạn có chắc chắn muốn xóa sản phẩm '{product_id}' không?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return

        try:
            if self.api.delete_product(product_id):
                self.ui.Category_tableWidget_2.removeRow(selected_row)
                self.ui.Category_tableWidget_2.setCurrentCell(-1, -1)
                self.ui.Category_tableWidget_2.clearSelection()
                self.clear_inventory()
                QMessageBox.information(self, "Thành công", f"Sản phẩm '{product_id}' đã được xóa!")
                self.load_product_data()  # Reset lựa chọn sau khi xóa
            else:
                QMessageBox.critical(self, "Lỗi", "Không tìm thấy sản phẩm!")
        except Exception as e:
            logger.error(f"Error deleting product: {e}")
            QMessageBox.critical(self, "Lỗi", f"Xóa sản phẩm thất bại: {e}")

    def import_inventory(self):
        self._handle_inventory_transaction("import")

    def export_inventory(self):
        self._handle_inventory_transaction("export")

    def _handle_inventory_transaction(self, action_type):
        """Xử lý giao dịch nhập/xuất kho"""
        selected_row = self.ui.Category_tableWidget_2.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa chọn sản phẩm nào!")
            return
        product_id = self.ui.Category_tableWidget_2.item(selected_row, 0).text()
        product_name = self.ui.Category_tableWidget_2.item(selected_row, 1).text()
        current_stock = int(self.ui.Category_tableWidget_2.item(selected_row, 3).text())

        dialog = self._create_transaction_dialog(product_name, current_stock, action_type)
        if dialog.exec() == QDialog.Accepted:
            quantity = self._validate_transaction_quantity(dialog.findChild(QLineEdit).text(), current_stock, action_type)
            if quantity is not None:
                new_stock = self.api.update_stock(product_id, quantity, action_type)
                self._process_transaction_result(new_stock, selected_row, quantity, action_type, current_stock)

    def _create_transaction_dialog(self, product_name, current_stock, action_type):
        """Tạo dialog cho giao dịch nhập/xuất kho"""
        dialog = QDialog(self)
        dialog.setWindowTitle(f"{'Nhập' if action_type == 'import' else 'Xuất'} kho")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"<b>Sản phẩm:</b> {product_name}\n<b>Tồn kho hiện tại:</b> {current_stock}"))
        qty_input = QLineEdit()
        qty_input.setPlaceholderText("Nhập số lượng")
        layout.addWidget(qty_input)
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Hủy")
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        dialog.setLayout(layout)
        ok_btn.clicked.connect(dialog.accept)
        cancel_btn.clicked.connect(dialog.reject)
        return dialog

    def _validate_transaction_quantity(self, qty_text, current_stock, action_type):
        """Kiểm tra số lượng giao dịch"""
        try:
            quantity = int(qty_text.strip())
            if quantity <= 0:
                QMessageBox.critical(self, "Lỗi", "Số lượng phải lớn hơn 0!")
                return None
            if action_type == "export" and quantity > current_stock:
                QMessageBox.critical(self, "Lỗi", f"Không thể xuất {quantity} (Tồn kho hiện tại: {current_stock})!")
                return None
            return quantity
        except ValueError:
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập số nguyên hợp lệ!")
            return None

    def _process_transaction_result(self, new_stock, row, quantity, action_type, current_stock):
        """Xử lý kết quả giao dịch"""
        if new_stock == -2:
            QMessageBox.critical(self, "Lỗi", f"Số lượng xuất vượt quá tồn kho ({current_stock})!")
        elif new_stock >= 0:
            self.ui.Category_tableWidget_2.setItem(row, 3, QTableWidgetItem(str(new_stock)))
            self.ui.stock.setText(str(new_stock))
            self.load_product_data()  # Reset lựa chọn sau khi nhập/xuất
            QMessageBox.information(self, "Thành công", f"Đã {'nhập' if action_type == 'import' else 'xuất'} {quantity} đơn vị!")
        else:
            QMessageBox.critical(self, "Lỗi", "Giao dịch thất bại!")

    def clear_inventory(self):
        """Xóa các trường nhập liệu trong tab Inventory Function và đặt lại trạng thái không chọn hàng"""
        try:
            # Xóa nội dung các trường nhập liệu
            for widget in [self.ui.name, self.ui.stock, self.ui.value, self.ui.Emp_Search_box, self.ui.cost]:
                widget.clear()
                logger.debug(
                    f"Đã xóa nội dung của widget: {widget.objectName() if hasattr(widget, 'objectName') else widget}")

            # Đặt lại các combobox về chỉ mục đầu tiên
            for combo in [self.ui.category, self.ui.location, self.ui.supplier_inv]:
                if combo.count() > 0:
                    combo.setCurrentIndex(0)
                    logger.debug(
                        f"Đã đặt lại combobox {combo.objectName() if hasattr(combo, 'objectName') else combo} về chỉ mục 0")
                else:
                    logger.warning(
                        f"Combobox {combo.objectName() if hasattr(combo, 'objectName') else combo} không có mục nào để đặt lại")

            # Tạo lại mã sản phẩm mới
            self._generate_product_id()
            logger.debug("Đã tạo lại mã sản phẩm mới")

            # Đặt lại trạng thái không chọn hàng trong bảng Category_tableWidget_2
            self.ui.Category_tableWidget_2.clearSelection()
            self.ui.Category_tableWidget_2.setCurrentCell(-1, -1)
            logger.debug("Đã đặt lại trạng thái không chọn hàng trong bảng Category_tableWidget_2")

            logger.info("Đã xóa các trường nhập liệu và đặt lại trạng thái trong tab Inventory Function")

        except Exception as e:
            logger.error(f"Lỗi khi xóa dữ liệu trong tab Inventory: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể xóa dữ liệu: {str(e)}")

    def _update_combo_boxes(self, category, location, supplier_id):
        """Cập nhật combo box với các giá trị mới"""
        try:
            if category and self.ui.category.findText(category) == -1:
                self.ui.category.addItem(category)
            self.ui.category.setCurrentText(category)

            if location and self.ui.location.findText(location) == -1:
                self.ui.location.addItem(location)
            self.ui.location.setCurrentText(location)

            supplier_ids = [self.ui.supplier_inv.itemText(i) for i in range(self.ui.supplier_inv.count())]
            if supplier_id and supplier_id not in supplier_ids and supplier_id != "Không có supplier":
                self.load_suppliers()
            if supplier_id in supplier_ids:
                self.ui.supplier_inv.setCurrentText(supplier_id)
        except Exception as e:
            logger.error(f"Error updating combo boxes: {e}")

    def load_selected_inventory(self, row, _):
        """Tải dữ liệu sản phẩm được chọn vào các trường nhập liệu"""
        if row < 0:
            return
        try:
            self.ui.id.setText(self.ui.Category_tableWidget_2.item(row, 0).text())
            self.ui.name.setText(self.ui.Category_tableWidget_2.item(row, 1).text())
            self.ui.category.setCurrentText(self.ui.Category_tableWidget_2.item(row, 2).text())
            self.ui.stock.setText(self.ui.Category_tableWidget_2.item(row, 3).text())
            self.ui.supplier_inv.setCurrentText(self.ui.Category_tableWidget_2.item(row, 4).text())
            self.ui.value.setText(self.ui.Category_tableWidget_2.item(row, 5).text())
            self.ui.cost.setText(self.ui.Category_tableWidget_2.item(row, 6).text())
            self.ui.location.setCurrentText(self.ui.Category_tableWidget_2.item(row, 7).text())
        except Exception as e:
            logger.error(f"Error loading selected inventory: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu sản phẩm: {e}")

    # --- Print Functions ---
    def print_invoices(self):
        """Print selected invoice to PDF with user-selected file path."""
        # Lấy hàng được chọn hiện tại
        selected_row = self.ui.TrackingInvoice_tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn 1 hóa đơn để in!")
            return

        try:
            # Lấy dữ liệu từ hàng được chọn
            invoice_data = {i: self.ui.TrackingInvoice_tableWidget.item(selected_row, i).text()
                            for i in range(6)}  # Lấy dữ liệu từ cột 0 đến 5
            invoice_id = invoice_data[0]  # Invoice ID từ cột 0

            # Tách danh sách sản phẩm từ cột "Product Name" (cột 1)
            product_names = invoice_data[1].split("\n")  # Tách các sản phẩm được gộp bằng \n
            quantities = invoice_data[3].split("\n")  # Số lượng (cột QTY)
            total_price = float(invoice_data[4])  # Tổng giá (cột Price)

            # Tạo danh sách sản phẩm để truyền vào create_pdf
            invoice_items = []
            for product_name in product_names:
                # Giả sử giá mỗi sản phẩm được tính bằng cách chia đều tổng giá
                price_per_item = total_price / len(product_names) if product_names else 0
                quantity = int(quantities[0]) if quantities else 0  # Sử dụng số lượng tổng
                item = {
                    "product_name": product_name,
                    "quantity": quantity,
                    "price_per_qty": price_per_item,
                    "total_price": price_per_item * quantity
                }
                invoice_items.append(item)

            # Sử dụng QFileDialog để chọn vị trí lưu file
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Invoice as PDF",
                f"{invoice_id}.pdf",
                "PDF Files (*.pdf)"
            )

            if not file_path:
                logger.debug("User canceled file save dialog.")
                return

            # Tạo PDF
            self.create_pdf(file_path, invoice_data, invoice_items)
            QMessageBox.information(self, "Success", f"Hóa đơn {invoice_id} đã được tạo trong:\n{file_path}")
            logger.info(f"Invoice {invoice_id} saved to: {file_path}")

            # Xóa lựa chọn hiện tại sau khi in thành công
            self.ui.TrackingInvoice_tableWidget.clearSelection()
            self.ui.TrackingInvoice_tableWidget.setCurrentCell(-1, -1)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tạo invoice: {str(e)}")
            logger.error(f"lỗi tạo pdf: {str(e)}")

    def create_pdf(self, file_name, invoice_data, invoice_items):
        """Create a professional PDF invoice from the selected invoice data."""
        c = canvas.Canvas(file_name, pagesize=A5)
        width, height = A5
        left_margin, right_margin, top_margin, bottom_margin = 1.5 * cm, 1.5 * cm, 3 * cm, 1.5 * cm

        # 1. Tiêu đề hóa đơn
        c.setFillColor(colors.darkblue)
        c.rect(0, height - top_margin, width, top_margin, fill=1)
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.white)
        c.drawCentredString(width / 2, height - top_margin + 0.9 * cm, "SALES INVOICE")

        # Thông tin công ty
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.black)
        company_info = [
            "Royal Company",
            "123 Business Road, District 1, Ho Chi Minh City",
            "Phone: (84) 123-456-789 | Email: info@royal.com"
        ]
        y = height - top_margin - 0.7 * cm
        for line in company_info:
            c.drawCentredString(width / 2, y, line)
            y -= 0.5 * cm

        # 2. Thông tin hóa đơn
        y_info = height - top_margin - 3.5 * cm
        table_width = width - left_margin - right_margin
        half_width = table_width / 2  # Chia đôi chiều rộng để đặt mã QR bên phải

        # Invoice Details (bên trái)
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.black)
        c.drawString(left_margin + 0.5 * cm, y_info, "Invoice Details:")
        c.setFont("Helvetica", 10)
        invoice_id = invoice_data[0]  # Invoice ID từ cột 0
        date = invoice_data[2]  # Invoice Date từ cột 2
        c.drawString(left_margin + 0.5 * cm, y_info - 0.6 * cm, f"Invoice ID: {invoice_id}")
        c.drawString(left_margin + 0.5 * cm, y_info - 1.2 * cm, f"Date: {date}")

        # Thêm mã QR (bên phải)
        total = float(invoice_data[4])  # Tổng giá từ cột Price (cột 4)
        qr_data = f"Invoice ID: {invoice_id}, Date: {date}, Total: {int(total):,} USD"
        qr_code = qr.QrCodeWidget(qr_data)
        qr_size = 2.5 * cm  # Kích thước mã QR (2.5cm x 2.5cm)
        d = Drawing(qr_size, qr_size)
        d.add(qr_code)
        qr_x = left_margin + half_width + 1.5 * cm  # Đặt mã QR bên phải
        qr_y = y_info - 2.0 * cm  # Dịch mã QR xuống để cân đối với Invoice Details
        renderPDF.draw(d, c, qr_x, qr_y)

        # 3. Bảng sản phẩm
        y_table_start = y_info - 4 * cm  # Điều chỉnh vị trí bảng sản phẩm
        col_widths = [table_width * 0.45, table_width * 0.15, table_width * 0.20, table_width * 0.20]  # Độ rộng cột
        headers = ["Product Name", "Qty", "Unit Price", "Total"]

        # Vẽ tiêu đề bảng
        c.setFillColor(colors.lightgrey)
        c.rect(left_margin, y_table_start, table_width, 0.8 * cm, fill=1, stroke=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.black)
        x = left_margin
        for i, header in enumerate(headers):
            c.drawCentredString(x + col_widths[i] / 2, y_table_start + 0.2 * cm, header)
            x += col_widths[i]

        # Vẽ đường viền dọc cho tiêu đề
        c.setStrokeColor(colors.black)
        x = left_margin
        for i in range(len(col_widths)):
            c.line(x, y_table_start + 0.8 * cm, x, y_table_start)
            x += col_widths[i]
        c.line(x, y_table_start + 0.8 * cm, x, y_table_start)

        # Vẽ dữ liệu bảng
        c.setFont("Helvetica", 9)
        y = y_table_start - 0.8 * cm
        for i, item in enumerate(invoice_items):
            y -= 0.8 * cm
            if i % 2 == 0:
                c.setFillColor(colors.whitesmoke)
            else:
                c.setFillColor(colors.white)
            c.rect(left_margin, y, table_width, 0.8 * cm, fill=1, stroke=1)

            c.setFillColor(colors.black)
            x = left_margin
            row_data = [
                item["product_name"][:18],  # Cắt ngắn tên sản phẩm nếu quá dài
                str(item["quantity"]),
                f"{int(item['price_per_qty']):,}",  # Bỏ .0, chỉ hiển thị số nguyên
                f"{int(item['total_price']):,}"  # Bỏ .0, chỉ hiển thị số nguyên
            ]
            for j, data in enumerate(row_data):
                if j == 0:  # Cột Product Name căn trái
                    c.drawString(x + 0.2 * cm, y + 0.2 * cm, data)
                else:  # Các cột số căn phải
                    c.drawRightString(x + col_widths[j] - 0.2 * cm, y + 0.2 * cm, data)
                x += col_widths[j]

            # Vẽ đường viền dọc cho dữ liệu
            c.setStrokeColor(colors.black)
            x = left_margin
            for j in range(len(col_widths)):
                c.line(x, y + 0.8 * cm, x, y)
                x += col_widths[j]
            c.line(x, y + 0.8 * cm, x, y)

        # 4. Tổng kết
        total = float(invoice_data[4])  # Tổng giá từ cột Price
        y_summary_start = y - 1.5 * cm
        summary_width = table_width * 0.5
        summary_x_start = width - right_margin - summary_width

        c.setFillColor(colors.lightgrey)
        c.rect(summary_x_start, y_summary_start - 2 * cm, summary_width, 2 * cm, fill=1, stroke=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.black)

        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(summary_x_start + summary_width / 2, y_summary_start - 1 * cm, f"Total: {int(total):,} USD")

        # 5. Footer
        y_footer = bottom_margin + 1 * cm
        c.setStrokeColor(colors.grey)
        c.line(left_margin, y_footer, width - right_margin, y_footer)
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(colors.grey)
        footer_width = width - left_margin - right_margin
        footer_x_center = left_margin + footer_width / 2
        c.drawCentredString(footer_x_center, bottom_margin + 0.7 * cm, "Thank you for shopping at Royal Company!")
        c.drawCentredString(footer_x_center, bottom_margin + 0.4 * cm, "Hotline: (84) 123-456-789")

        # Vẽ viền bao quanh toàn bộ nội dung
        c.setStrokeColor(colors.black)
        c.rect(left_margin, bottom_margin, table_width, height - top_margin - bottom_margin, stroke=1, fill=0)

        c.showPage()
        c.save()

    # --- Navigation Functions ---
    def show_Dashboard(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(0)
        self.update_dashboard_stats()
        self.show_revenue_chart()
        self.load_top_suppliers()
        self.load_top_products()
        self.load_recent_activities()
        self.load_weather()

    def show_InventoryFunction(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(2)

    def show_InvoiceStatus(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(1)

    def show_Supplier(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(4)

    def show_Account(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(3)

    def show_Report(self):
        self.ui.TrackingInvoice_2.setCurrentIndex(5)

    # --- Helper Methods ---
    def _validate_selection(self, table, item_type):
        """Kiểm tra lựa chọn trong bảng"""
        selected_row = table.currentRow()
        if selected_row == -1 or not table.selectedItems():
            QMessageBox.warning(self, "Warning", f"Please select a {item_type}!")
            return None
        return selected_row

    def on_category_changed(self, text):
        logger.debug(f"Category changed to: {text}")

    def on_location_changed(self, text):
        logger.debug(f"Location changed to: {text}")
    def closeEvent(self, event):
        """
        Override phương thức closeEvent để hiển thị thông báo xác nhận khi người dùng cố gắng đóng cửa sổ.
        """
        reply = QMessageBox.question(
            self,
            "Xác nhận thoát",
            "Bạn có muốn thoát ứng dụng không?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Nếu người dùng chọn "Yes", chấp nhận sự kiện đóng cửa sổ
            logger.info("Người dùng xác nhận thoát ứng dụng từ UserWindow.")
            event.accept()
        else:
            # Nếu người dùng chọn "No", bỏ qua sự kiện đóng cửa sổ
            logger.debug("Người dùng hủy thoát ứng dụng từ UserWindow.")
            event.ignore()