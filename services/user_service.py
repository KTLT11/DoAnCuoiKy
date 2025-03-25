import re
import logging
import random

from PySide6.QtCharts import QLineSeries, QChart, QValueAxis, QChartView, QPieSeries, QBarSet, QBarSeries, \
    QBarCategoryAxis, QDateTimeAxis
from PySide6.QtGui import QFont, QPainter, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QWidget, QAbstractItemView, QFileDialog, \
    QTextEdit, QHBoxLayout, QLabel, QGridLayout
from PySide6.QtCore import QDate, Qt, QDateTime

from gui.User_ui import Ui_MainWindow
from gui.login_ui import Ui_Form
from database.api import Database
from database.API_User import UserFunc_Api
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from services.admin_infor_dialog import AdminInforDialog

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("user_window.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton

class InvoicePreviewDialog(QDialog):
    def __init__(self, bill_html, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Invoice Preview")
        self.setMinimumSize(300, 400)

        # Tạo layout
        layout = QVBoxLayout()

        # Tạo QTextEdit để hiển thị hóa đơn
        self.bill_display = QTextEdit()
        self.bill_display.setReadOnly(True)
        self.bill_display.setFont(QFont("Courier New", 10))
        self.bill_display.setHtml(bill_html)
        layout.addWidget(self.bill_display)

        # Tạo nút đóng
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)



class UserWindow(QMainWindow):
    def __init__(self, login_window=None, user_data = None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.api = UserFunc_Api()
        self.login_window = login_window
        self.current_user = user_data  # Set the user data passed from LoginWindow
        logger.debug(
            f"CustomUserWindow.__init__: login_window = {self.login_window}, current_user = {self.current_user}")
        self.current_expression = ""
        logger.debug(f"UserWindow.__init__: login_window = {self.login_window}")

        self.db = Database()
        self.products_collection = self.db.products
        self.invoices_collection = self.db.invoices
        self.invoices = []
        self.temp_bill_items = []

        self._setup_widgets()
        self._setup_connections()
        self._initialize_ui()
        self.load_invoice_data()
        self.load_product_data()
        self.update_total_product()
        # Áp dụng stylesheet để làm nổi bật tab hiện tại
        self.apply_tab_stylesheet()
        # Khóa không cho bấm trực tiếp vào tab
        self.ui.tabWidget.tabBar().setExpanding(True)
        self.ui.tabWidget.tabBar().setEnabled(True)
        #set mặc định là dashboard
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.info.clicked.connect(self.show_user_info_dialog)

        # Thêm các thuộc tính mới cho Dashboard
        self.dashboard_widget = QWidget()
        self.dashboard_layout = QVBoxLayout(self.dashboard_widget)
        self.ui.tabWidget.insertTab(1, self.dashboard_widget, "Report")  # Đặt lại Dashboard làm tab đầu tiên

        self._setup_dashboard()


    def _setup_dashboard(self):
        """Thiết lập giao diện Dashboard với biểu đồ và thông tin tổng quan."""
        # 1. Nhãn thông tin tổng quan
        overview_layout = QHBoxLayout()
        self.total_revenue_label = QLabel("Total Revenue (This Month): $0.00")
        self.total_invoices_label = QLabel("Total Invoices (This Month): 0")
        self.total_products_sold_label = QLabel("Total Products Sold (This Month): 0")

        # Tùy chỉnh màu sắc và kiểu chữ
        self.total_revenue_label.setStyleSheet("color: darkgreen; font-weight: bold;")
        self.total_invoices_label.setStyleSheet("color: darkblue; font-weight: bold;")
        self.total_products_sold_label.setStyleSheet("color: darkred; font-weight: bold;")

        for label in [self.total_revenue_label, self.total_invoices_label, self.total_products_sold_label]:
            label.setFont(QFont("Arial", 12, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            overview_layout.addWidget(label)

        self.dashboard_layout.addLayout(overview_layout)

        # 2. Sử dụng QGridLayout để sắp xếp biểu đồ
        chart_layout = QGridLayout()
        chart_layout.setSpacing(10)  # Thêm khoảng cách giữa các biểu đồ

        # 3. Biểu đồ doanh thu (Line Chart)
        revenue_chart = self.create_revenue_chart()
        revenue_view = QChartView(revenue_chart)
        revenue_view.setRenderHint(QPainter.Antialiasing)
        revenue_view.setStyleSheet("border: 1px solid lightgray;")  # Thêm viền
        chart_layout.addWidget(revenue_view, 0, 0)  # Cột 0, hàng 0

        # 4. Biểu đồ sản phẩm bán chạy (Pie Chart)
        product_chart = self.create_product_chart()
        product_view = QChartView(product_chart)
        product_view.setRenderHint(QPainter.Antialiasing)
        product_view.setStyleSheet("border: 1px solid lightgray;")
        chart_layout.addWidget(product_view, 0, 1)  # Cột 1, hàng 0

        # 5. Biểu đồ tồn kho theo danh mục (Bar Chart)
        category_chart = self.create_category_chart()
        category_view = QChartView(category_chart)
        category_view.setRenderHint(QPainter.Antialiasing)
        category_view.setStyleSheet("border: 1px solid lightgray;")
        chart_layout.addWidget(category_view, 1, 0, 1, 2)  # Cột 0-1, hàng 1

        self.dashboard_layout.addLayout(chart_layout)
        self.update_dashboard_data()

    def create_revenue_chart(self):
        """Tạo biểu đồ đường hiển thị doanh thu theo ngày."""
        series = QLineSeries()
        series.setName("Revenue Over Time")

        # Lấy dữ liệu từ invoices_collection
        invoices = self.api.get_invoices()
        revenue_by_date = {}
        for invoice in invoices:
            date = invoice.get("invoice_date")
            total = invoice.get("total_price", 0)
            if date in revenue_by_date:
                revenue_by_date[date] += total
            else:
                revenue_by_date[date] = total

        # Sắp xếp theo ngày và thêm vào series
        for date in sorted(revenue_by_date.keys()):
            qdate = QDate.fromString(date, "dd/MM/yyyy")
            series.append(QDateTime(qdate).toMSecsSinceEpoch(), revenue_by_date[date])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Revenue Trend")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Sử dụng QDateTimeAxis cho trục X
        axis_x = QDateTimeAxis()
        axis_x.setTitleText("Date")
        axis_x.setFormat("dd/MM/yyyy")
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Revenue ($)")
        axis_y.setLabelFormat("%.2f")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        return chart

    def create_product_chart(self):
        """Tạo biểu đồ tròn hiển thị tỷ lệ sản phẩm bán chạy."""
        series = QPieSeries()
        series.setHoleSize(0.35)  # Tạo hiệu ứng donut

        # Tính tổng quantity của từng sản phẩm
        product_sales = {}
        invoices = self.api.get_invoices()
        for invoice in invoices:
            for item in invoice.get("cart", []):
                name = item.get("product_name", "Unknown")
                qty = item.get("quantity", 0)
                product_sales[name] = product_sales.get(name, 0) + qty

        # Thêm vào series với màu sắc tùy chỉnh
        colors = [QColor("#1f77b4"), QColor("#ff7f0e"), QColor("#2ca02c"), QColor("#d62728")]
        for idx, (name, qty) in enumerate(product_sales.items()):
            slice_ = series.append(name, qty)
            slice_.setLabelVisible(True)  # Hiển thị nhãn trên biểu đồ
            slice_.setLabel(f"{name}: {qty}")
            slice_.setColor(colors[idx % len(colors)])  # Gán màu sắc

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Top Selling Products")
        chart.legend().setAlignment(Qt.AlignRight)

        return chart

    def create_category_chart(self):
        """Tạo biểu đồ cột hiển thị số lượng sản phẩm theo danh mục."""
        bar_set = QBarSet("Stock by Category")
        categories = []
        products = self.api.get_products()
        category_stock = {}

        for product in products:
            cat = product.get("category", "Unknown")
            stock = product.get("current_stock", 0)
            category_stock[cat] = category_stock.get(cat, 0) + stock
            if cat not in categories:
                categories.append(cat)

        for stock in category_stock.values():
            bar_set.append(stock)

        # Thêm nhãn giá trị trên cột
        bar_set.setLabelColor(QColor("black"))
        for i, stock in enumerate(category_stock.values()):
            bar_set.setLabel(str(stock))

        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Stock by Category")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Stock Quantity")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        return chart

    def update_dashboard_data(self):
        """Cập nhật dữ liệu cho Dashboard, chỉ tính dữ liệu trong tháng hiện tại."""
        current_month = QDate.currentDate().toString("MM/yyyy")
        invoices = self.api.get_invoices()
        filtered_invoices = [
            inv for inv in invoices
            if QDate.fromString(inv.get("invoice_date"), "dd/MM/yyyy").toString("MM/yyyy") == current_month
        ]

        total_revenue = sum(invoice.get("total_price", 0) for invoice in filtered_invoices)
        total_invoices = len(filtered_invoices)
        total_products_sold = sum(
            sum(item.get("quantity", 0) for item in invoice.get("cart", []))
            for invoice in filtered_invoices
        )

        self.total_revenue_label.setText(f"Total Revenue (This Month): ${total_revenue:,.2f}")
        self.total_invoices_label.setText(f"Total Invoices (This Month): {total_invoices}")
        self.total_products_sold_label.setText(f"Total Products Sold (This Month): {total_products_sold}")

    def show_dashboard(self):
        """Hiển thị tab Dashboard và cập nhật dữ liệu."""
        self.ui.tabWidget.setCurrentIndex(1)
        self.update_dashboard_data()
        logger.debug("Chuyển đến tab Dashboard và cập nhật dữ liệu.")

    def create_revenue_chart(self):
        """Tạo biểu đồ đường hiển thị doanh thu theo ngày."""
        series = QLineSeries()
        series.setName("Revenue Over Time")

        # Lấy dữ liệu từ invoices_collection
        invoices = self.api.get_invoices()
        revenue_by_date = {}
        for invoice in invoices:
            date = invoice.get("invoice_date")
            total = invoice.get("total_price", 0)
            if date in revenue_by_date:
                revenue_by_date[date] += total
            else:
                revenue_by_date[date] = total

        # Sắp xếp theo ngày và thêm vào series
        for date in sorted(revenue_by_date.keys()):
            qdate = QDate.fromString(date, "dd/MM/yyyy")
            series.append(qdate.toJulianDay(), revenue_by_date[date])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Revenue Trend")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QValueAxis()
        axis_x.setTitleText("Date (Julian Day)")
        axis_x.setLabelFormat("%i")
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Revenue ($)")
        axis_y.setLabelFormat("%.2f")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        return chart

    def create_product_chart(self):
        """Tạo biểu đồ tròn hiển thị tỷ lệ sản phẩm bán chạy."""
        series = QPieSeries()
        series.setHoleSize(0.35)  # Tạo hiệu ứng donut

        # Tính tổng quantity của từng sản phẩm
        product_sales = {}
        invoices = self.api.get_invoices()
        for invoice in invoices:
            for item in invoice.get("cart", []):
                name = item.get("product_name", "Unknown")
                qty = item.get("quantity", 0)
                product_sales[name] = product_sales.get(name, 0) + qty

        # Thêm vào series
        for name, qty in product_sales.items():
            series.append(name, qty)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Top Selling Products")
        chart.legend().setAlignment(Qt.AlignRight)

        return chart

    def create_category_chart(self):
        """Tạo biểu đồ cột hiển thị số lượng sản phẩm theo danh mục."""
        bar_set = QBarSet("Stock by Category")
        categories = []
        products = self.api.get_products()
        category_stock = {}

        for product in products:
            cat = product.get("category", "Unknown")
            stock = product.get("current_stock", 0)
            category_stock[cat] = category_stock.get(cat, 0) + stock
            if cat not in categories:
                categories.append(cat)

        for stock in category_stock.values():
            bar_set.append(stock)

        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Stock by Category")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Stock Quantity")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        return chart

    def update_dashboard_data(self):
        """Cập nhật dữ liệu cho Dashboard."""
        invoices = self.api.get_invoices()
        total_revenue = sum(invoice.get("total_price", 0) for invoice in invoices)
        total_invoices = len(invoices)
        total_products_sold = sum(
            sum(item.get("quantity", 0) for item in invoice.get("cart", []))
            for invoice in invoices
        )

        self.total_revenue_label.setText(f"Total Revenue: ${total_revenue:,.2f}")
        self.total_invoices_label.setText(f"Total Invoices: {total_invoices}")
        self.total_products_sold_label.setText(f"Total Products Sold: {total_products_sold}")

    def show_dashboard(self):
        """Hiển thị tab Dashboard và cập nhật dữ liệu."""
        self.ui.tabWidget.setCurrentIndex(0)
        self.update_dashboard_data()
        logger.debug("Chuyển đến tab Dashboard và cập nhật dữ liệu.")
    def _setup_widgets(self):
        """Thiết lập widgets với kiểm tra tập trung và khóa chỉnh sửa bảng."""
        required_widgets = {
            "search_input": "Emp_Search_box_2",
            "search_button": "search_track_inventory",
            "table_inventory": "Category_tableWidget",
            "invoice_search_input": "Sales_Search_Product_Input",
            "invoice_search_button": "search_Invoice_btn",
            "table_invoices": "Sales_Product_tableWidget"
        }
        for attr, widget_name in required_widgets.items():
            try:
                widget = getattr(self.ui, widget_name)
                if "table" in attr:  # Khóa chỉnh sửa cho các bảng
                    widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                setattr(self, attr, widget)
            except AttributeError:
                logger.error(f"Widget '{widget_name}' not found.")
                setattr(self, attr, None)

        # Khóa chỉnh sửa cho các bảng khác
        self.ui.Sales_Product_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Product_Cart_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Chuyển Costomer_Bill_Area_2 thành QTextEdit nếu cần
        self.ui.Costomer_Bill_Area_2 = QTextEdit()
        self.ui.Costomer_Bill_Area_2.setReadOnly(True)  # Chỉ cho phép đọc
        self.ui.Costomer_Bill_Area_2.setVisible(False)  # Ẩn Costomer_Bill_Area_2

    def _setup_connections(self):
        """Thiết lập kết nối sự kiện."""
        connections = {
            self.ui.Employee_Button.clicked: self.show_inventory,
            self.ui.Supplier_Button.clicked: self.show_invoice,
            self.ui.Dash_Button.clicked: self.show_dashboard,
            self.ui.Supplier_Button_2.clicked: self.show_report,
            self.ui.Add_Update_Cart_Btn.clicked: self.add_update_invoice,
            self.ui.Cart_Clear_Btn.clicked: self.save_to_mongodb,
            self.ui.delete_invoice_btn.clicked: self.delete_invoice,
            self.ui.Sales_Product_tableWidget.cellClicked: self.on_sales_table_clicked,
            self.ui.Product_Cart_tableWidget.cellClicked: self.on_cart_table_clicked,
            self.ui.Generate_Bill_Btn_2.clicked: self.generate_bill,
            self.ui.Print_Bill_Btn_2.clicked: self.download_pdf,
            self.ui.logout_Btn.clicked: self.logout,
            self.ui.Clear_All_Btn_2.clicked: self.clear_inputs,
        }
        for signal, slot in connections.items():
            signal.connect(slot)
        if self.search_button:
            self.search_button.clicked.connect(self.search_inventory)
        if self.invoice_search_button:
            self.invoice_search_button.clicked.connect(self.search_invoices)

        self.ui.id.returnPressed.connect(self.fetch_product_price)

    def _initialize_ui(self):
        """Khởi tạo giao diện người dùng."""
        try:
            self.ui.date.setDate(QDate.currentDate())
            self.ui.date.setDisplayFormat("dd/MM/yyyy")
            self.ui.Calc_Input.setText("0")
            self.ui.Cart_Clear_Btn.setText("Save")
        except AttributeError as e:
            logger.error(f"Error initializing UI components: {e}")

    def handle_exception(self, action, error, msg_for_user):
        """Xử lý lỗi chung."""
        logger.error(f"Lỗi khi {action}: {error}")
        QMessageBox.critical(self, "Error", f"{msg_for_user}: {str(error)}")

    def validate_inputs(self, fields, error_message="Vui lòng nhập đầy đủ thông tin!"):
        """Kiểm tra các trường đầu vào."""
        if not all(fields.values()):
            QMessageBox.warning(self, "Warning", error_message)
            return False
        return True

    def validate_numeric(self, value, field_name, min_value=None, max_value=None):
        """Kiểm tra giá trị số với ràng buộc."""
        try:
            num = float(value) if '.' in value else int(value)
            if min_value is not None and num < min_value:
                QMessageBox.warning(self, "Warning", f"{field_name} phải >= {min_value}!")
                return None
            if max_value is not None and num > max_value:
                QMessageBox.warning(self, "Warning", f"{field_name} phải <= {max_value}!")
                return None
            return num
        except ValueError:
            QMessageBox.warning(self, "Warning", f"{field_name} phải là số!")
            return None

    def populate_table(self, table, data, headers, row_mapping):
        """Hàm chung để điền dữ liệu vào bảng."""
        table.setRowCount(len(data))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(data):
            for col, value in enumerate(row_mapping(item)):
                table.setItem(row, col, QTableWidgetItem(str(value)))

    def login(self, username, password):
        """Xử lý đăng nhập"""
        try:
            # Tìm người dùng trong MongoDB
            user = self.api.users.find_one({"username": username, "password": password}, {"_id": 0})
            if user:
                self.current_user = user  # Lưu thông tin tài khoản
                self.show()  # Hiển thị giao diện Admin
                return True
            else:
                QMessageBox.critical(self, "Error", "Tên đăng nhập hoặc mật khẩu không hợp lệ!")
                return False
        except Exception as e:
            logger.error(f"Error during login: {e}")
            QMessageBox.critical(self, "Error", f"Login failed: {e}")
            return False

    def show_user_info_dialog(self):
        """Hiển thị hộp thoại thông tin tài khoản"""
        if not self.current_user:
            QMessageBox.critical(self, "Error", "Không có thông tin đăng nhập!")
            return

        # Tạo và hiển thị hộp thoại
        dialog = AdminInforDialog(self.current_user, self.api, self)
        dialog.exec()

    def load_product_data(self):
        """Tải dữ liệu sản phẩm."""
        try:
            products = list(self.api.get_products())
            headers = ["Product Name", "Category", "Current Stock", "Supplier", "Stock Value", "Stock Cost",
                       "Location Number"]
            row_mapping = lambda p: [
                p.get("product_name", "N/A"), p.get("category", "N/A"), p.get("current_stock", "0"),
                p.get("supplier_id", "N/A"), f"{p.get('cost_per_unit', 0):.2f}", f"{p.get('price_per_unit', 0):.2f}",
                p.get("location_number", "N/A")
            ]
            self.populate_table(self.ui.Category_tableWidget, products, headers, row_mapping)
            logger.info("Dữ liệu sản phẩm đã tải thành công!")
        except Exception as e:
            self.handle_exception("tải dữ liệu sản phẩm", e, "Failed to load products")

    def search_inventory(self):
        """Tìm kiếm sản phẩm trong kho."""
        if not self.search_input:
            logger.error("Search input widget is not initialized.")
            QMessageBox.critical(self, "Lỗi", "Không thể thực hiện tìm kiếm.")
            return

        search_text = self.search_input.text().strip().lower()
        search_criteria = self.ui.Emp_SearchBy_Comb_2.currentText()

        if not search_text:
            logger.debug("Ô tìm kiếm trống, tải lại dữ liệu ban đầu.")
            self.load_product_data()
            return

        try:
            filtered_products = list(self.api.search_products(search_text, search_criteria))
            self.display_data(filtered_products)
            logger.info(f"Tìm kiếm sản phẩm với từ khóa '{search_text}' và tiêu chí '{search_criteria}' thành công.")
        except ValueError as e:
            QMessageBox.warning(self, "Cảnh báo", str(e))
            logger.warning(f"Giá trị tìm kiếm không hợp lệ: {search_text}")
        except Exception as e:
            self.handle_exception("tìm kiếm sản phẩm", e, "Lỗi khi tìm kiếm")

    def display_data(self, products):
        """Hiển thị dữ liệu sản phẩm."""
        if not self.table_inventory:
            logger.error("Inventory table widget is not initialized.")
            return
        headers = ["Product Name", "Category", "Current Stock", "Supplier", "Stock Value", "Stock Cost",
                   "Location Number"]
        row_mapping = lambda p: [
            p.get("product_name", "N/A"), p.get("category", "N/A"), p.get("current_stock", "0"),
            p.get("supplier_id", "N/A"), f"{p.get('cost_per_unit', 0):.2f}", f"{p.get('price_per_unit', 0):.2f}",
            p.get("location_number", "N/A")
        ]
        self.populate_table(self.table_inventory, products, headers, row_mapping)

    def load_invoice_data(self):
        """Tải dữ liệu hóa đơn."""
        try:
            invoices = list(self.api.get_invoices())
            flat_data = [(inv, item) for inv in invoices for item in inv.get("cart", [])]

            # Bảng Sales_Product_tableWidget (All Invoice)
            headers1 = ["Invoice ID", "Product Name", "Invoice Date", "QTY", "Price", "Total", "Status"]
            row_mapping1 = lambda inv, item: [
                inv.get("invoice_id", "N/A"), item.get("product_name", "N/A"), inv.get("invoice_date", "N/A"),
                item.get("quantity", "0"), f"{item.get('price_per_qty', 0):.2f}", f"{inv.get('total_price', 0):.2f}",
                inv.get("status", "N/A")
            ]
            self.populate_table(self.ui.Sales_Product_tableWidget, flat_data, headers1, lambda x: row_mapping1(*x))

        except Exception as e:
            self.handle_exception("tải dữ liệu hóa đơn", e, "Failed to load invoices")

    def display_invoices(self, invoices):
        """Hiển thị hóa đơn đã lọc."""
        if not self.table_invoices:
            logger.error("Invoices table widget is not initialized.")
            return
        self.table_invoices.setRowCount(0)
        headers = ["Invoice ID", "Product Name", "Invoice Date", "QTY", "Price", "Total", "Status"]
        for invoice in invoices:
            for item in invoice.get("cart", []):
                row = self.table_invoices.rowCount()
                self.table_invoices.insertRow(row)
                values = [
                    invoice.get("invoice_id", "N/A"), item.get("product_name", "N/A"),
                    invoice.get("invoice_date", "N/A"),
                    item.get("quantity", "0"), f"{item.get('price', 0):.2f}", f"{invoice.get('total_price', 0):.2f}",
                    invoice.get("status", "N/A")
                ]
                for col, value in enumerate(values):
                    self.table_invoices.setItem(row, col, QTableWidgetItem(str(value)))

    def search_invoices(self):
        """Tìm kiếm hóa đơn."""
        if not self.invoice_search_input:
            logger.error("Invoice search input widget is not initialized.")
            QMessageBox.critical(self, "Lỗi", "Không thể thực hiện tìm kiếm.")
            return

        search_text = self.invoice_search_input.text().strip().lower()
        search_criteria = self.ui.comboBox.currentText()

        try:
            if not search_text:
                self.load_invoice_data()
                logger.info("Ô tìm kiếm trống, hiển thị lại dữ liệu ban đầu.")
                return

            if search_criteria == "Price":
                if not search_text.isdigit():
                    QMessageBox.warning(self, "Warning", "Giá trị tìm kiếm theo giá phải là số nguyên!")
                    return
                price_pattern = f".*{search_text}.*"
                filtered_invoices = list(self.api.search_invoices(price_pattern, search_criteria))
            else:
                filtered_invoices = list(self.api.search_invoices(search_text, search_criteria))

            self.display_invoices(filtered_invoices)
            logger.info(f"Tìm kiếm hóa đơn với từ khóa '{search_text}' và tiêu chí '{search_criteria}' thành công.")
        except Exception as e:
            self.handle_exception("tìm kiếm hóa đơn", e, "Lỗi khi tìm kiếm hóa đơn")

    def on_sales_table_clicked(self, row, col):
        """Xử lý khi người dùng chọn một dòng trong Sales_Product_tableWidget."""
        # Đồng bộ hóa với Product_Cart_tableWidget
        self.ui.Product_Cart_tableWidget.setCurrentCell(row, 0)  # Chọn dòng tương ứng trong bảng kia
        self.ui.Product_Cart_tableWidget.clearSelection()  # Xóa lựa chọn trước đó
        self.ui.Product_Cart_tableWidget.selectRow(row)  # Chọn dòng mới
        logger.debug(f"Đã chọn dòng {row} trong Sales_Product_tableWidget, đồng bộ với Product_Cart_tableWidget.")

        # Lấy invoice_id từ dòng được chọn
        table = self.ui.Sales_Product_tableWidget
        invoice_id = table.item(row, 0).text()  # Cột Invoice ID

        # Truy vấn tất cả sản phẩm thuộc invoice_id từ cơ sở dữ liệu
        try:
            invoice = self.api.get_invoice_by_id(invoice_id)
            if not invoice:
                QMessageBox.warning(self, "Warning", f"Không tìm thấy hóa đơn với ID '{invoice_id}'!")
                return

            # Lưu dữ liệu hóa đơn được chọn để sử dụng sau này
            self.selected_invoice_data = invoice.get("cart", [])
            logger.debug(f"Dữ liệu hóa đơn được chọn: {self.selected_invoice_data}")

            # Hiển thị dữ liệu của sản phẩm đầu tiên trong các ô nhập liệu (nếu cần)
            if self.selected_invoice_data:
                first_item = self.selected_invoice_data[0]
                product_name = first_item.get("product_name", "")
                invoice_date = invoice.get("invoice_date", "")
                quantity = first_item.get("quantity", 0)
                price = first_item.get("price_per_qty", 0)

                self.ui.id.setText(product_name)
                try:
                    date = QDate.fromString(invoice_date, "dd/MM/yyyy")
                    self.ui.date.setDate(date if date.isValid() else QDate.currentDate())
                except Exception as e:
                    logger.error(f"Error parsing date '{invoice_date}': {e}")
                    self.ui.date.setDate(QDate.currentDate())
                self.ui.Cuantity_Bill_Area.setText(str(quantity))
                self.ui.Price_PreQty_Bill_Area.setText(f"{price:.2f}")

                # Tính tổng giá trị cho sản phẩm đầu tiên (hiển thị trên Calc_Input)
                total_price = quantity * price
                if quantity >= 50:
                    discount = total_price * 0.05
                    total_price -= discount
                self.ui.Calc_Input.setText(f"{total_price:.2f}")
                self.current_expression = f"{total_price:.2f}"

        except Exception as e:
            self.handle_exception("lấy dữ liệu hóa đơn", e, "Lỗi khi lấy dữ liệu hóa đơn")    #

    def on_cart_table_clicked(self, row, col):
        """Xử lý khi người dùng chọn một dòng trong Product_Cart_tableWidget."""
        # Đồng bộ hóa với Sales_Product_tableWidget (nếu cần)
        self.ui.Sales_Product_tableWidget.clearSelection()  # Xóa lựa chọn trong bảng bên trái
        self.ui.Sales_Product_tableWidget.setCurrentCell(-1, -1)
        logger.debug(f"Đã chọn dòng {row} trong Product_Cart_tableWidget.")

        # Lấy dữ liệu từ hàng được chọn trong Product_Cart_tableWidget
        table = self.ui.Product_Cart_tableWidget
        invoice_date = table.item(row, 0).text()  # Cột Invoice Date
        product_name = table.item(row, 1).text()  # Cột Product Name
        quantity = table.item(row, 2).text()  # Cột QTY
        price = table.item(row, 3).text()  # Cột Price
        total_price = table.item(row, 4).text()  # Cột Total Price

        # Hiển thị dữ liệu lên các ô nhập liệu
        self.ui.id.setText(product_name)
        try:
            date = QDate.fromString(invoice_date, "dd/MM/yyyy")
            self.ui.date.setDate(date if date.isValid() else QDate.currentDate())
        except Exception as e:
            logger.error(f"Error parsing date '{invoice_date}': {e}")
            self.ui.date.setDate(QDate.currentDate())
        self.ui.Cuantity_Bill_Area.setText(quantity)
        self.ui.Price_PreQty_Bill_Area.setText(price)

        # Hiển thị tổng giá trị lên Calc_Input
        self.ui.Calc_Input.setText(total_price)
        self.current_expression = total_price

        # Lưu thông tin sản phẩm được chọn để sử dụng khi cập nhật
        self.selected_cart_item = {
            "row": row,
            "product_name": product_name,
            "invoice_date": invoice_date,
            "quantity": int(quantity),
            "price_per_qty": float(price),
            "total_price": float(total_price)
        }
        logger.debug(f"Dữ liệu sản phẩm được chọn từ Product_Cart_tableWidget: {self.selected_cart_item}")

    def add_update_invoice(self):
        """Thêm hoặc cập nhật tất cả sản phẩm của hóa đơn được chọn vào bảng giữa (lưu tạm thời)."""
        # Kiểm tra xem có hàng nào được chọn trong bảng bên trái (Sales_Product_tableWidget) không
        selected_row = self.ui.Sales_Product_tableWidget.currentRow()

        if selected_row != -1:
            # Có hàng được chọn trong bảng bên trái, ưu tiên dữ liệu hóa đơn đã chọn
            if not hasattr(self, "selected_invoice_data") or not self.selected_invoice_data:
                QMessageBox.warning(self, "Cảnh báo", "Dữ liệu hóa đơn được chọn không hợp lệ!")
                return

            # Xóa danh sách temp_bill_items hiện tại để tránh trùng lặp
            self.temp_bill_items.clear()

            # Thêm tất cả sản phẩm từ hóa đơn đã chọn vào temp_bill_items
            for item in self.selected_invoice_data:
                product_name = item.get("product_name", "")
                invoice_date = item.get("invoice_date", self.ui.date.date().toString("dd/MM/yyyy"))
                quantity = item.get("quantity", 0)
                price = item.get("price_per_qty", 0)

                # Kiểm tra tồn kho
                try:
                    product = self.api.get_product_by_name(product_name)
                    if not product:
                        QMessageBox.warning(self, "Cảnh báo", f"Không tìm thấy sản phẩm '{product_name}' trong kho!")
                        continue
                    current_stock = product.get("current_stock", 0)
                    if quantity > current_stock:
                        QMessageBox.warning(self, "Cảnh báo",
                                            f"Số lượng tồn kho của '{product_name}' chỉ còn {current_stock}. Không đủ hàng để bán!")
                        logger.warning(
                            f"Số lượng bán ({quantity}) vượt quá tồn kho ({current_stock}) cho sản phẩm '{product_name}'.")
                        continue
                except Exception as e:
                    self.handle_exception("kiểm tra tồn kho", e, "Lỗi khi kiểm tra tồn kho")
                    continue

                # Tính toán total_price và chiết khấu
                total_price = float(quantity) * float(price)
                discount = 0
                if float(quantity) >= 50:
                    discount = total_price * 0.05
                    total_price -= discount

                # Chuẩn bị dữ liệu sản phẩm
                new_item = {
                    "product_name": product_name,
                    "quantity": int(quantity),
                    "price_per_qty": float(price),
                    "total_price": total_price,
                    "discount": discount,
                    "invoice_date": invoice_date,
                }
                self.temp_bill_items.append(new_item)
                logger.info(
                    f"Thêm sản phẩm từ hóa đơn vào temp_bill_items: {new_item['product_name']}, Ngày: {new_item['invoice_date']}")

            QMessageBox.information(self, "Thành công", "Tất cả sản phẩm từ hóa đơn đã được thêm vào bảng tạm thời!")

        else:
            # Không có hàng nào được chọn trong bảng bên trái, sử dụng các trường nhập liệu
            date = self.ui.date.date().toString("dd/MM/yyyy")
            inputs = {
                "date": date,
                "product_name": self.ui.id.text().strip(),
                "quantity": self.ui.Cuantity_Bill_Area.text().strip(),
                "price_per_qty": self.ui.Price_PreQty_Bill_Area.text().strip()
            }
            logger.debug(f"Dữ liệu từ ô nhập liệu: {inputs}")

            if not inputs["product_name"] or not inputs["quantity"] or not inputs["price_per_qty"]:
                QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin từ các ô nhập liệu!")
                return

            if not self.validate_inputs(inputs):
                logger.warning("Dữ liệu nhập liệu không hợp lệ, dừng xử lý.")
                return

            product_name = inputs["product_name"]
            invoice_date = inputs["date"]
            quantity = self.validate_numeric(inputs["quantity"], "Số lượng", min_value=1)
            price = self.validate_numeric(inputs["price_per_qty"], "Giá", min_value=0)
            if quantity is None or price is None:
                logger.warning("Số lượng hoặc giá không hợp lệ, dừng xử lý.")
                return

            # Kiểm tra tồn kho
            try:
                product = self.api.get_product_by_name(product_name)
                if not product:
                    QMessageBox.warning(self, "Cảnh báo", f"Không tìm thấy sản phẩm '{product_name}' trong kho!")
                    return
                current_stock = product.get("current_stock", 0)
                if quantity > current_stock:
                    QMessageBox.warning(self, "Cảnh báo",
                                        f"Số lượng tồn kho của '{product_name}' chỉ còn {current_stock}. Không đủ hàng để bán!")
                    logger.warning(
                        f"Số lượng bán ({quantity}) vượt quá tồn kho ({current_stock}) cho sản phẩm '{product_name}'.")
                    return
            except Exception as e:
                self.handle_exception("kiểm tra tồn kho", e, "Lỗi khi kiểm tra tồn kho")
                return

            # Tính toán total_price và chiết khấu
            total_price = float(quantity) * float(price)
            discount = 0
            if float(quantity) >= 50:
                discount = total_price * 0.05
                total_price -= discount

            # Chuẩn bị dữ liệu sản phẩm
            item = {
                "product_name": product_name,
                "quantity": int(quantity),
                "price_per_qty": float(price),
                "total_price": total_price,
                "discount": discount,
                "invoice_date": invoice_date,
            }
            logger.debug(f"Item được chuẩn bị: {item}")

            # Thêm hoặc cập nhật sản phẩm trong temp_bill_items
            for i, temp_item in enumerate(self.temp_bill_items):
                if temp_item["product_name"] == item["product_name"]:
                    self.temp_bill_items[i] = item
                    logger.info(
                        f"Cập nhật sản phẩm trong temp_bill_items: {item['product_name']}, Ngày: {item['invoice_date']}")
                    QMessageBox.information(self, "Thành công", "Sản phẩm đã được cập nhật trong bảng tạm thời!")
                    break
            else:
                self.temp_bill_items.append(item)
                logger.info(
                    f"Thêm sản phẩm mới vào temp_bill_items: {item['product_name']}, Ngày: {item['invoice_date']}")
                QMessageBox.information(self, "Thành công", "Sản phẩm đã được thêm vào bảng tạm thời!")

        # Cập nhật bảng giữa và giao diện
        self._update_cart_table()

        # Xóa lựa chọn trong bảng bên trái để tránh ưu tiên dữ liệu bảng trong lần tiếp theo
        self.ui.Sales_Product_tableWidget.clearSelection()
        self.ui.Sales_Product_tableWidget.setCurrentCell(-1, -1)
    def delete_invoice(self):
        """Xóa hóa đơn được chọn từ bảng bên trái hoặc bảng giữa."""
        # Xác định bảng nào đang được chọn
        selected_row_left = self.ui.Sales_Product_tableWidget.currentRow()  # Bảng bên trái
        selected_row_cart = self.ui.Product_Cart_tableWidget.currentRow()  # Bảng giữa

        if selected_row_left == -1 and selected_row_cart == -1:
            logger.warning("Không có hàng nào được chọn để xóa.")
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một hàng để xóa!")
            return

        if selected_row_left != -1:
            # Trường hợp 1: Xóa từ bảng bên trái (Sales_Product_tableWidget)
            table = self.ui.Sales_Product_tableWidget
            invoice_id = table.item(selected_row_left, 0).text()  # Cột Invoice ID
            product_name = table.item(selected_row_left, 1).text()  # Cột Product Name
            invoice_date = table.item(selected_row_left, 2).text()  # Cột Invoice Date

            # Xác nhận xóa
            reply = QMessageBox.question(
                self, "Xác nhận",
                f"Bạn có chắc chắn muốn xóa sản phẩm '{product_name}' trong hóa đơn '{invoice_id}' vào ngày '{invoice_date}'?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.No:
                logger.debug(f"Người dùng hủy xóa sản phẩm: {invoice_id}, {product_name}, {invoice_date}")
                return

            try:
                # Xóa sản phẩm từ MongoDB
                if self.api.delete_invoice(invoice_id, product_name, invoice_date):
                    logger.info(f"Đã xóa sản phẩm '{product_name}' khỏi hóa đơn '{invoice_id}' trong MongoDB.")
                else:
                    logger.warning(f"Không tìm thấy sản phẩm '{product_name}' trong hóa đơn '{invoice_id}' để xóa.")
                    QMessageBox.warning(self, "Lỗi",
                                        f"Không tìm thấy sản phẩm '{product_name}' trong hóa đơn '{invoice_id}' để xóa!")
                    return

                # Xóa hàng trong bảng bên trái
                self.ui.Sales_Product_tableWidget.removeRow(selected_row_left)
                logger.debug(f"Đã xóa hàng {selected_row_left} trong Sales_Product_tableWidget.")

                # Xóa các hàng tương ứng trong bảng giữa (Product_Cart_tableWidget)
                row = 0
                while row < self.ui.Product_Cart_tableWidget.rowCount():
                    if (self.ui.Product_Cart_tableWidget.item(row, 1).text() == product_name and
                            self.ui.Product_Cart_tableWidget.item(row, 0).text() == invoice_date):
                        self.ui.Product_Cart_tableWidget.removeRow(row)
                        logger.debug(f"Đã xóa hàng {row} trong Product_Cart_tableWidget.")
                    else:
                        row += 1

                # Xóa sản phẩm khỏi temp_bill_items
                self.temp_bill_items = [
                    item for item in self.temp_bill_items
                    if not (item["product_name"] == product_name and item["invoice_date"] == invoice_date)
                ]
                self._update_cart_table()
                self._update_bill_preview()

                # Cập nhật tổng giá trị và tổng sản phẩm
                total_invoice_price = self.api.get_total_invoice_price()
                updated_total = self.api.update_total_products()
                self.ui.Calc_Input.setText(f"{total_invoice_price:.2f}")
                self.current_expression = f"{total_invoice_price:.2f}"
                self.ui.Label_Total_Products.setText(f"{updated_total}")
                self.ui.Label_Total_Products.repaint()

                # Không chọn dòng mới sau khi xóa
                self.ui.Sales_Product_tableWidget.clearSelection()
                self.ui.Sales_Product_tableWidget.setCurrentCell(-1, -1)
                self.ui.Product_Cart_tableWidget.clearSelection()
                self.ui.Product_Cart_tableWidget.setCurrentCell(-1, -1)

                # Tải lại dữ liệu để đồng bộ
                self.load_invoice_data()

                QMessageBox.information(self, "Thành công",
                                        f"Sản phẩm '{product_name}' trong hóa đơn '{invoice_id}' đã được xóa!")
                logger.info(
                    f"Sản phẩm đã được xóa từ bảng bên trái: {invoice_id}, {product_name}, Ngày: {invoice_date}")

            except Exception as e:
                logger.error(f"Lỗi khi xóa sản phẩm từ bảng bên trái: {str(e)}")
                self.handle_exception("xóa sản phẩm", e, "Lỗi khi xóa dữ liệu")

        else:
            # Trường hợp 2: Xóa từ bảng giữa (Product_Cart_tableWidget)
            table = self.ui.Product_Cart_tableWidget
            invoice_date = table.item(selected_row_cart, 0).text()  # Cột Invoice Date
            product_name = table.item(selected_row_cart, 1).text()  # Cột Product Name

            # Xác nhận xóa
            reply = QMessageBox.question(
                self, "Xác nhận",
                f"Bạn có chắc chắn muốn xóa sản phẩm '{product_name}' vào ngày '{invoice_date}' khỏi danh sách hóa đơn tạm thời? (Hành động này không ảnh hưởng đến dữ liệu đang có)",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.No:
                logger.debug(f"Người dùng hủy xóa sản phẩm từ danh sách hóa đơn tạm thời: {product_name}, {invoice_date}")
                return

            try:
                # Xóa hàng trong bảng giữa
                self.ui.Product_Cart_tableWidget.removeRow(selected_row_cart)
                logger.debug(f"Đã xóa hàng {selected_row_cart} trong Product_Cart_tableWidget.")

                # Xóa sản phẩm khỏi temp_bill_items
                self.temp_bill_items = [
                    item for item in self.temp_bill_items
                    if not (item["product_name"] == product_name and item["invoice_date"] == invoice_date)
                ]
                self._update_cart_table()
                self._update_bill_preview()

                # Không chọn dòng mới sau khi xóa
                self.ui.Product_Cart_tableWidget.clearSelection()
                self.ui.Product_Cart_tableWidget.setCurrentCell(-1, -1)

                QMessageBox.information(self, "Thành công",
                                        f"Sản phẩm '{product_name}' vào ngày '{invoice_date}' đã được xóa khỏi danh sách hóa đơn tạm thời!")
                logger.info(f"Sản phẩm đã được xóa từ danh sách hóa đơn tạm thời: {product_name}, Ngày: {invoice_date}")

            except Exception as e:
                logger.error(f"Lỗi khi xóa sản phẩm từ danh sách hóa đơn tạm thời: {str(e)}")
                self.handle_exception("xóa sản phẩm", e, "Lỗi khi xóa dữ liệu")

    def clear_inputs(self):
        """Xóa dữ liệu nhập trên giao diện."""
        self.ui.id.clear()
        self.ui.Cuantity_Bill_Area.clear()
        self.ui.Price_PreQty_Bill_Area.clear()
        self.ui.Calc_Input.setText("0")
        self.current_expression = ""
        self.ui.Costomer_Bill_Area_2.clear()
        self.ui.Product_Cart_tableWidget.setRowCount(0)
        logger.debug("Đã xóa dữ liệu nhập trên giao diện.")

    def update_total_product(self):
        """Cập nhật tổng số lượng sản phẩm."""
        total_quantity = self.api.update_total_products()
        self.ui.Label_Total_Products.setText(f"{total_quantity}")
        self.ui.Label_Total_Products.repaint()
        logger.debug(f"Tổng số lượng sản phẩm đã được cập nhật: {total_quantity}")

    def show_dashboard(self):
        self.ui.tabWidget.setCurrentIndex(0)
        logger.debug("Chuyển đến tab Dashboard.")

    def show_report(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def show_inventory(self):
        self.ui.tabWidget.setCurrentIndex(2)
        logger.debug("Chuyển đến tab Inventory.")

    def show_invoice(self):
        self.ui.tabWidget.setCurrentIndex(3)
        logger.debug("Chuyển đến tab Invoice.")

    def show_user_info_dialog(self):
        """Hiển thị hộp thoại thông tin tài khoản"""
        if not self.current_user:
            QMessageBox.critical(self, "Error", "No user is currently logged in!")
            return

        # Tạo và hiển thị hộp thoại
        dialog = AdminInforDialog(self.current_user, self.api, self)
        dialog.exec()

    def logout(self):
        """Đăng xuất."""
        reply = QMessageBox.question(self, "Logout", "Bạn có chắc chắn muốn đăng xuất?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            logger.info("Người dùng đã đăng xuất.")
            self.close()
            if isinstance(self.login_window, QWidget):
                self.login_window.show()
                logger.debug("Đã mở lại cửa sổ đăng nhập.")
            else:
                logger.warning("Tạo mới cửa sổ đăng nhập vì không có tham chiếu hợp lệ.")
                self.login_window = QWidget()
                self.ui_login = Ui_Form()
                self.ui_login.setupUi(self.login_window)
                self.login_window.show()

    def load_data_from_table(self, row, _):
        """Tải dữ liệu từ bảng vào giao diện và chuẩn bị cho nút Invoice."""
        table = self.ui.Sales_Product_tableWidget
        product_name = table.item(row, 1).text()
        invoice_date = table.item(row, 2).text()
        quantity = table.item(row, 3).text()
        price = table.item(row, 4).text()

        self.ui.id.setText(product_name)
        try:
            date = QDate.fromString(invoice_date, "dd/MM/yyyy")
            self.ui.date.setDate(date if date.isValid() else QDate.currentDate())
        except Exception as e:
            logger.error(f"Error parsing date '{invoice_date}': {e}")
            self.ui.date.setDate(QDate.currentDate())
        self.ui.Cuantity_Bill_Area.setText(quantity)
        self.ui.Price_PreQty_Bill_Area.setText(price)

        try:
            quantity = int(quantity.strip())
            price = float(price.strip())
            total_price = quantity * price
            if quantity >= 50:
                discount = total_price * 0.05
                total_price -= discount
            self.ui.Calc_Input.setText(f"{total_price:.2f}")
            self.current_expression = f"{total_price:.2f}"
        except ValueError:
            logger.warning("Dữ liệu số lượng hoặc giá không hợp lệ, đặt về 0.")
            self.ui.Calc_Input.setText("0")

        # Lưu dữ liệu tạm thời để sử dụng khi bấm nút Invoice
        self.selected_invoice_data = {
            "product_name": product_name,
            "invoice_date": invoice_date,
            "quantity": quantity,
            "price": price,
            "total_price": total_price,
            "discount": discount if quantity >= 50 else 0
        }

    def _update_cart_table(self):
        """
        Cập nhật bảng Product_Cart_tableWidget với dữ liệu từ self.temp_bill_items.
        Logic:
        1. Xóa toàn bộ dữ liệu hiện tại trong bảng.
        2. Đặt số dòng và cột cho bảng.
        3. Điền dữ liệu từ self.temp_bill_items vào bảng.
        """
        # Xóa toàn bộ dữ liệu hiện tại trong bảng
        self.ui.Product_Cart_tableWidget.clear()
        headers = ["Invoice Date", "Product Name", "QTY", "Price", "Total Price"]
        self.ui.Product_Cart_tableWidget.setRowCount(len(self.temp_bill_items))
        self.ui.Product_Cart_tableWidget.setColumnCount(len(headers))
        self.ui.Product_Cart_tableWidget.setHorizontalHeaderLabels(headers)

        for row, item in enumerate(self.temp_bill_items):
            values = [
                item["invoice_date"],
                item["product_name"],
                str(item["quantity"]),
                f"{item['price_per_qty']:.2f}",
                f"{item['total_price']:.2f}"
            ]
            for col, value in enumerate(values):
                self.ui.Product_Cart_tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        # Đảm bảo bảng được vẽ lại
        self.ui.Product_Cart_tableWidget.repaint()
        logger.debug("Đã cập nhật bảng Product_Cart_tableWidget với danh sách tạm thời.")

    def fetch_product_price(self):
        """Truy vấn giá bán từ cơ sở dữ liệu dựa trên tên sản phẩm."""
        product_name = self.ui.id.text().strip()
        if not product_name:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập tên sản phẩm!")
            return

        try:
            # Truy vấn sản phẩm từ collection products
            product = self.api.get_product_by_name(product_name)
            if product:
                price = product.get("price_per_unit", 0)
                self.ui.Price_PreQty_Bill_Area.setText(f"{price:.2f}")
                logger.info(f"Tìm thấy sản phẩm '{product_name}' với giá bán: {price}")
            else:
                QMessageBox.warning(self, "Warning", f"Không tìm thấy sản phẩm '{product_name}' trong kho!")
                self.ui.Price_PreQty_Bill_Area.clear()
                logger.warning(f"Không tìm thấy sản phẩm '{product_name}' trong cơ sở dữ liệu.")
        except Exception as e:
            self.handle_exception("truy vấn giá sản phẩm", e, "Lỗi khi truy vấn sản phẩm")

    from PySide6.QtGui import QFont

    def _update_bill_preview(self):
        """Cập nhật giao diện xem trước hóa đơn với định dạng HTML và căn chỉnh đẹp hơn."""
        # Đặt phông chữ cố định (monospace) cho Costomer_Bill_Area_2
        font = QFont("Courier New", 10)  # Sử dụng phông chữ monospace
        self.ui.Costomer_Bill_Area_2.setFont(font)
        self.ui.Costomer_Bill_Area.setFont(font)

        if not self.temp_bill_items:
            self.bill_text = "Chưa có sản phẩm trong hóa đơn."
            self.ui.Costomer_Bill_Area.setPlainText(self.bill_text)
            self.ui.Costomer_Bill_Area_2.setHtml(
                "<p style='color: gray; text-align: center;'>Chưa có sản phẩm trong hóa đơn.</p>")
            logger.debug(f"Không có sản phẩm trong hóa đơn, đặt bill_text: {self.bill_text}")
            return

        # Gộp các mục trùng lặp (nếu có)
        merged_items = {}
        for item in self.temp_bill_items:
            key = (item["product_name"], item["price_per_qty"])
            if key in merged_items:
                merged_items[key]["quantity"] += item["quantity"]
                merged_items[key]["total_price"] += item["total_price"]
                merged_items[key]["discount"] += item["discount"]
            else:
                merged_items[key] = item.copy()

        self.temp_bill_items = list(merged_items.values())
        subtotal = sum(item["total_price"] for item in self.temp_bill_items)

        # Định nghĩa độ rộng của từng cột (số ký tự)
        col_widths = {
            "product_name": 20,
            "quantity": 8,
            "price": 10,
            "total": 10
        }

        # Tạo nội dung HTML cho hóa đơn
        bill_html = """
        <div style='font-family: "Courier New", monospace; font-size: 10pt;'>
            <h2 style='color: darkblue; text-align: center;'>SALES INVOICE</h2>
            <p style='color: darkblue; text-align: center;'>
                Transaction Date: {}
            </p>
            <hr style='border: 1px solid darkblue;'>
            <table style='width: 100%; border-collapse: collapse;'>
                <tr style='background-color: lightgray; font-weight: bold;'>
                    <td style='width: {}ch; text-align: left; padding: 5px;'>Product Name</td>
                    <td style='width: {}ch; text-align: right; padding: 5px;'>Qty</td>
                    <td style='width: {}ch; text-align: right; padding: 5px;'>Price</td>
                    <td style='width: {}ch; text-align: right; padding: 5px;'>Total</td>
                </tr>
        """.format(
            self.ui.date.date().toString('dd/MM/yyyy'),
            col_widths["product_name"],
            col_widths["quantity"],
            col_widths["price"],
            col_widths["total"]
        )

        # Thêm dữ liệu từng mục
        for idx, item in enumerate(self.temp_bill_items):
            product_name = item["product_name"][:col_widths["product_name"] - 2]
            # Xen kẽ màu nền cho các hàng
            row_color = "#f0f0f0" if idx % 2 == 0 else "#ffffff"
            bill_html += f"""
                <tr style='background-color: {row_color};'>
                    <td style='text-align: left; padding: 5px;'>{product_name}</td>
                    <td style='text-align: right; padding: 5px;'>{item['quantity']}</td>
                    <td style='text-align: right; padding: 5px;'>{item['price_per_qty']:,}</td>
                    <td style='text-align: right; padding: 5px;'>{item['total_price']:,}</td>
                </tr>
            """
            if item["discount"] > 0:
                bill_html += f"""
                    <tr style='background-color: {row_color}; color: red;'>
                        <td style='text-align: left; padding: 5px;'>(Discount 5%</td>
                        <td style='text-align: right; padding: 5px;'></td>
                        <td style='text-align: right; padding: 5px;'></td>
                        <td style='text-align: right; padding: 5px;'>{-item['discount']:,})</td>
                    </tr>
                """

        # Thêm Subtotal
        bill_html += """
                <tr>
                    <td colspan='4'><hr style='border: 1px solid darkblue;'></td>
                </tr>
                <tr style='font-weight: bold;'>
                    <td colspan='3' style='text-align: left; padding: 5px;'>Subtotal</td>
                    <td style='text-align: right; padding: 5px; color: darkgreen;'>{:,} USD</td>
                </tr>
            </table>
        </div>
        """.format(subtotal)

        # Cập nhật nội dung HTML vào Costomer_Bill_Area_2 (nhưng không hiển thị)
        self.bill_text = bill_html
        self.ui.Costomer_Bill_Area.setPlainText(self.bill_text)  # Giữ lại cho mục đích debug
        self.ui.Costomer_Bill_Area_2.setHtml(self.bill_text)  # Lưu nội dung HTML
        logger.debug(f"Đã cập nhật nội dung HTML vào Costomer_Bill_Area_2: {self.ui.Costomer_Bill_Area_2.toHtml()}")
    def save_to_mongodb(self):
        """Lưu dữ liệu từ bảng giữa vào MongoDB với invoice_id mới, sau đó xóa dữ liệu."""
        if not self.temp_bill_items:
            QMessageBox.warning(self, "Lỗi", "Không có sản phẩm trong danh sách hóa đơn tạm thời để lưu!")
            return

        # Tạo invoice_id mới
        invoice_id = self.api.get_max_invoice_id()
        self.current_invoice_id = invoice_id



        # Chuẩn bị dữ liệu hóa đơn
        invoice_data = {
            "invoice_id": invoice_id,
            "cart": self.temp_bill_items,
            "invoice_date": self.ui.date.date().toString("dd/MM/yyyy"),
            "total_price": sum(item["total_price"] for item in self.temp_bill_items),
            "status": "Pending"
        }

        try:
            # Lưu vào MongoDB
            self.api.add_new_invoice_full(invoice_data)
            QMessageBox.information(self, "Thành công",
                                    f"Hóa đơn {invoice_id} đã được lưu vào MongoDB!")

            # Xóa dữ liệu trong bảng giữa và các ô nhập liệu
            self.temp_bill_items.clear()
            self.ui.id.clear()
            self.ui.Cuantity_Bill_Area.clear()
            self.ui.Price_PreQty_Bill_Area.clear()
            self.ui.Calc_Input.setText("0")
            self.current_expression = ""
            self.ui.Costomer_Bill_Area_2.clear()
            self.ui.Product_Cart_tableWidget.setRowCount(0)
            self.load_invoice_data()
            logger.debug("Đã xóa dữ liệu trong danh sách hóa đơn tạm thời và các ô nhập liệu sau khi lưu vào MongoDB.")
        except Exception as e:
            self.handle_exception("lưu hóa đơn vào MongoDB", e, "Không thể lưu hóa đơn")

    def generate_bill(self):
        """Hiển thị hóa đơn từ bảng giữa dưới dạng một hộp thoại xem trước."""
        if not self.temp_bill_items:
            QMessageBox.warning(self, "Lỗi", "Không có sản phẩm trong danh sách hóa đơn tạm thời để tạo hóa đơn!")
            return

        # Cập nhật nội dung hóa đơn
        self._update_bill_preview()

        # Hiển thị hóa đơn trong một hộp thoại
        dialog = InvoicePreviewDialog(self.bill_text, self)
        dialog.exec()

        QMessageBox.information(self, "Thành công", "Hóa đơn xem trước đã được hiển thị!")
    def download_pdf(self):
        """Tạo và tải xuống file PDF từ nội dung hóa đơn mà không lưu vào MongoDB."""
        if not self.temp_bill_items:
            QMessageBox.warning(self, "Lỗi", "Không có sản phẩm trong hóa đơn để tải xuống!")
            return

        # Sử dụng self.bill_text đã được tạo trong _update_bill_preview
        if not self.bill_text or self.bill_text == "Chưa có sản phẩm trong hóa đơn.":
            QMessageBox.warning(self, "Lỗi", "Không có nội dung hóa đơn để tải xuống!")
            return

        # Tạo invoice_id để đặt tên file (không lưu vào MongoDB)
        invoice_id = self.api.get_max_invoice_id() # Lấy invoice_id mới để đặt tên file

        # Tạo và tải file PDF
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Lưu hóa đơn dưới dạng PDF",
            f"{invoice_id}.pdf",
            "PDF Files (*.pdf)"
        )

        if not file_path:
            logger.debug("Người dùng đã hủy việc chọn vị trí lưu file.")
            return

        try:
            self.create_pdf(file_path, self.bill_text)
            self.temp_bill_items.clear()
            self._update_bill_preview()
            self.load_invoice_data()
            QMessageBox.information(self, "Hóa đơn",
                                    f"Hóa đơn {invoice_id} đã được tải xuống tại:\n{file_path}")
            logger.info(f"Hóa đơn đã được tải xuống tại: {file_path}")
        except Exception as e:
            self.handle_exception("tạo file PDF", e, "Không thể tạo file PDF")

    def create_pdf(self, file_name, bill_text):
        """Tạo file PDF từ hóa đơn với định dạng chuyên nghiệp và đẹp mắt."""
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

            # 2. Thông tin hóa đơn và thông tin khách hàng
            y_info = height - top_margin - 3.5 * cm
            table_width = width - left_margin - right_margin
            half_width = table_width / 2  # Chia đôi chiều rộng để đặt hai cột

            # Invoice Details (bên trái)
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(colors.black)
            c.drawString(left_margin + 0.5 * cm, y_info, "Invoice Details:")
            c.setFont("Helvetica", 10)
            invoice_id = self.api.get_max_invoice_id()  # Lấy invoice_id từ API
            date = self.ui.date.date().toString("dd/MM/yyyy")
            c.drawString(left_margin + 0.5 * cm, y_info - 0.6 * cm, f"Invoice ID: {invoice_id}")
            c.drawString(left_margin + 0.5 * cm, y_info - 1.2 * cm, f"Date: {date}")

            # Thêm mã QR (bên phải)
            total = sum(item["total_price"] for item in self.temp_bill_items)
            qr_data = f"Invoice ID: IN{invoice_id}, Date: {date}, Total: {int(total):,} USD"
            qr_code = qr.QrCodeWidget(qr_data)
            qr_size = 2.5 * cm  # Kích thước mã QR (2.5cm x 2.5cm)
            d = Drawing(qr_size, qr_size)
            d.add(qr_code)
            qr_x = left_margin + half_width + 1.5 * cm  # Đặt mã QR bên phải
            qr_y = y_info - 2.0 * cm  # Căn chỉnh theo chiều dọc với Invoice Details
            renderPDF.draw(d, c, qr_x, qr_y)

        # 3. Bảng sản phẩm
        y_table_start = y_info - 4 * cm
        table_width = width - left_margin - right_margin
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
            c.line(x, y_table_start + 0.8 * cm, x, y_table_start)  # Loại bỏ stroke
            x += col_widths[i]
        c.line(x, y_table_start + 0.8 * cm, x, y_table_start)  # Loại bỏ stroke

        # Vẽ dữ liệu bảng
        c.setFont("Helvetica", 9)
        y = y_table_start - 0.8 * cm
        for i, item in enumerate(self.temp_bill_items):
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
                f"{int(item['price_per_qty']):,}",  # Thêm dấu phân cách hàng nghìn
                f"{int(item['total_price']):,}"  # Thêm dấu phân cách hàng nghìn
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
                c.line(x, y + 0.8 * cm, x, y)  # Loại bỏ stroke
                x += col_widths[j]
            c.line(x, y + 0.8 * cm, x, y)  # Loại bỏ stroke

        # 4. Tổng kết
        total = sum(item["total_price"] for item in self.temp_bill_items)
        y_summary_start = y - 1.5 * cm
        summary_width = table_width * 0.5
        summary_x_start = width - right_margin - summary_width

        c.setFillColor(colors.lightgrey)
        c.rect(summary_x_start, y_summary_start - 2 * cm, summary_width, 2 * cm, fill=1, stroke=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.black)

        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(summary_x_start + summary_width / 2, y_summary_start - 1 * cm, f"Total: {int(total):,} USD")

        # c.setStrokeColor(colors.black)
        # c.line(summary_x_start, y_summary_start - 1.5 * cm, summary_x_start + summary_width, y_summary_start - 1.5 * cm)

        # 5. Footer
        y_footer = bottom_margin + 1 * cm
        c.setStrokeColor(colors.grey)
        c.line(left_margin, y_footer, width - right_margin, y_footer)
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(colors.grey)
        footer_width = width - left_margin - right_margin
        footer_x_center = left_margin + footer_width / 2
        c.drawCentredString(footer_x_center, bottom_margin + 0.7 * cm, "Thank you for shopping at Royal Company!")
        c.drawCentredString(footer_x_center, bottom_margin + 0.4 * cm,
                            "Hotline: (84) 123-456-789")

        # Vẽ viền bao quanh toàn bộ nội dung
        c.setStrokeColor(colors.black)
        c.rect(left_margin, bottom_margin, table_width, height - top_margin - bottom_margin, stroke=1, fill=0)

        c.showPage()
        c.save()


    def apply_tab_stylesheet(self):
        """Áp dụng stylesheet để làm nổi bật tab hiện tại bằng màu xám."""
        tab_stylesheet = """
            QTabBar::tab {
                padding: 8px;
                border: 1px solid #C4C4C3;
                border-bottom: none;
                background: #E0E0E0;  /* Màu nền mặc định cho tab không được chọn */
            }
            QTabBar::tab:selected {
                background: #A9A9A9;  /* Màu xám cho tab được chọn */
                font-weight: bold;
            }
            QTabBar::tab:!selected {
                background: #E0E0E0;  /* Màu nền cho tab không được chọn */
            }
            QTabBar::tab:hover {
                background: #D0D0D0;  /* Màu khi hover */
            }
        """
        self.ui.tabWidget.setStyleSheet(tab_stylesheet)
        logger.debug("Đã áp dụng stylesheet cho tabWidget.")