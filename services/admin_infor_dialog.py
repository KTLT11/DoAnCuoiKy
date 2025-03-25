from PySide6.QtWidgets import QDialog, QMessageBox, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from gui.admin_infor import Ui_Form  # Import giao diện từ file admin_infor.ui
import logging

# Thiết lập logging
logger = logging.getLogger(__name__)

class AdminInforDialog(QDialog):
    def __init__(self, user_data, api, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user_data = user_data  # Dữ liệu tài khoản đang đăng nhập
        self.api = api  # API để cập nhật thông tin tài khoản
        self.original_username = user_data.get("username", "")  # Lưu username ban đầu để cập nhật

        # Thiết lập giao diện ban đầu
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """Thiết lập giao diện ban đầu"""
        # Hiển thị thông tin tài khoản
        self.ui.name.setText(self.user_data.get("username", ""))
        self.ui.password.setText(self.user_data.get("password", ""))  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit
        self.ui.role.setText(self.user_data.get("role", ""))

        role = self.user_data.get("role", "").capitalize()  # Lấy role và viết hoa chữ cái đầu
        self.setWindowTitle(f"{role} Information")

        # Không cho phép chỉnh sửa Role
        self.ui.role.setReadOnly(True)
        self.ui.role.setStyleSheet("background-color: #E0E0E0; color: #333333;")

        if self.user_data.get("role", "").lower() == "user":
            self.ui.name.setReadOnly(True)
            self.ui.name.setStyleSheet("background-color: #E0E0E0; color: #333333;")
            logger.debug(f"Username field locked for user: {self.original_username}")

        # Thiết lập chế độ ẩn mật khẩu ban đầu
        self.ui.password.setEchoMode(QLineEdit.Password)  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit

        # Tùy chỉnh giao diện nút
        self.ui.update.setStyleSheet("""
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
        self.ui.done.setStyleSheet("""
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

        # Thêm nút ẩn/hiện mật khẩu
        self.toggle_password_btn = QPushButton("Show", self)
        self.toggle_password_btn.setGeometry(480, 190, 50, 31)  # Đặt vị trí ngay bên phải ô Password
        self.toggle_password_btn.setStyleSheet("""
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

    def setup_connections(self):
        """Kết nối các sự kiện"""
        self.ui.update.clicked.connect(self.update_user_info)
        self.ui.done.clicked.connect(self.close)
        self.toggle_password_btn.clicked.connect(self.toggle_password_visibility)

    def toggle_password_visibility(self):
        """Ẩn/hiện mật khẩu"""
        if self.ui.password.echoMode() == QLineEdit.Password:  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit
            self.ui.password.setEchoMode(QLineEdit.Normal)  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit
            self.toggle_password_btn.setText("Hide")
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit
            self.toggle_password_btn.setText("Show")

    def update_user_info(self):
        """Cập nhật thông tin tài khoản"""
        new_username = self.ui.name.text().strip()
        new_password = self.ui.password.text().strip()  # Sửa từ self.ui.pass thành self.ui.passwordLineEdit

        if not new_password:
            QMessageBox.warning(self, "Warning", "Password cannot be empty!")
            return

            # Nếu role là "user", giữ nguyên username cũ
        role = self.user_data.get("role", "").lower()
        if role == "user":
            if new_username != self.original_username:
                QMessageBox.warning(self, "Warning", "Users are not allowed to change their username!")
                new_username = self.original_username  # Giữ nguyên username cũ
            logger.debug(f"User role detected, username kept as: {new_username}")

        if not new_username:  # Kiểm tra sau khi xử lý role
            QMessageBox.warning(self, "Warning", "Username cannot be empty!")
            return

        # Dữ liệu mới để cập nhật
        updated_data = {
            "username": new_username,
            "password": new_password,
            "role": self.user_data.get("role", "")  # Role không thay đổi
        }

        # Gọi API để cập nhật thông tin tài khoản
        success = self.api.update_user(self.original_username, updated_data)
        if success:
            # Cập nhật lại user_data để phản ánh thay đổi
            self.user_data["username"] = new_username
            self.user_data["password"] = new_password
            QMessageBox.information(self, "Success", "User information updated successfully!")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Failed to update user information.")