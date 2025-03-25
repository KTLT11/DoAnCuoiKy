import sys
import logging
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QComboBox
from PySide6 import QtCore
from gui.login_ui import Ui_Form
from services.admin_service import AdminExFnct_Process
from services.user_service import UserWindow
from database.API_Login import Database
from datetime import datetime, timedelta
import os

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- CỬA SỔ ADMIN --------------------

class AdminWindow(AdminExFnct_Process):
    def __init__(self, login_window, user_data=None):
        super().__init__(login_window=login_window, user_data=user_data)

# -------------------- CỬA SỔ USER --------------------
class CustomUserWindow(UserWindow):  # Renamed to avoid naming conflict
    def __init__(self, login_window, user_data = None):
        super().__init__(login_window=login_window, user_data = user_data)  # Gọi hàm khởi tạo lớp cha

        # Kiểm tra nếu self.ui đã được thiết lập
        if hasattr(self, "ui"):
            logger.debug(f"CustomUserWindow.__init__: login_window = {self.login_window}")

            # Kiểm tra nếu logout_btn tồn tại trong UI trước khi kết nối
            if hasattr(self.ui, "logout_btn"):
                self.ui.logout_btn.clicked.connect(self.logout)
            else:
                logger.warning("logout_btn không tồn tại trong Ui_MainWindow! Kiểm tra thiết kế UI.")
        else:
            logger.error("self.ui chưa được khởi tạo! Đảm bảo lớp UserWindow gọi setupUi() đúng cách.")

    def logout(self):
        """Handle logout process"""
        if QMessageBox.question(self, "Log Out", "Are you sure you want to log out?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.close()  # Close the UserWindow

            # Debug: Log the value of self.login_window
            logger.debug(f"CustomUserWindow.logout: self.login_window = {self.login_window}")

            # Check if self.login_window is an instance of QWidget
            if isinstance(self.login_window, QWidget):
                self.login_window.show()  # Show the login window
            else:
                logger.error(f"self.login_window is not an instance of QWidget: {self.login_window}")
                QMessageBox.critical(self, "Error", "Cannot return to login screen. Please restart the application.")

# -------------------- CỬA SỔ ĐĂNG NHẬP --------------------
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        logger.info("Khởi tạo LoginWindow thành công")

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = Database()  # Kết nối MongoDB

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Kết nối sự kiện cho các nút
        self.ui.login.clicked.connect(self.login)
        self.ui.forgot.clicked.connect(self.forgot_password)
        self.ui.exit.clicked.connect(self.confirm_exit)

    def show(self):
        super().show()
        self.ui.password.clear()  # Xóa ô password
        logger.debug("LoginWindow displayed, username and password fields cleared.")

    def confirm_exit(self):
        """Xử lý xác nhận thoát ứng dụng"""
        confirm = QMessageBox.question(
            self,
            "Exit ?",
            "Do you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            self.close()
            QApplication.quit()

    def forgot_password(self):
        """Xử lý quên mật khẩu - Hiển thị danh sách Admin"""
        try:
            admins = self.db.get_users_by_role("admin")
            if admins:
                admin_names = [f"👤 {admin['username']}" for admin in admins]
                message = "Please contact the following Admins for support: \n\n" + "\n".join(admin_names)
            else:
                message = "Hiện chưa có Admin nào xuất hiện trong hệ thống!"
            QMessageBox.information(self, "Support", message, QMessageBox.Ok)
        except Exception as e:
            logger.error(f"Lỗi khi lấy danh sách Admin: {str(e)}")
            QMessageBox.critical(self, "Lỗi hệ thống", "Không thể kết nối đến cơ sở dữ liệu!", QMessageBox.Ok)

    # In LoginWindow class (second document)
    def login(self):
        """Xử lý đăng nhập với giới hạn số lần thử"""
        username = self.ui.user_name.text().strip()
        password = self.ui.password.text().strip()
        selected_role = self.ui.role.currentText().lower()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter complete information!!")
            return

        user = self.db.get_user(username)
        if not user:
            QMessageBox.warning(self, "Error", "Account does not exist!")
            return

        # Kiểm tra trạng thái khóa tài khoản
        lock_until = user.get("lock_until")
        if lock_until and lock_until > datetime.now():
            remaining_time = (lock_until - datetime.now()).seconds // 60
            QMessageBox.warning(self, "Error", f"Account locked! Please try again in {remaining_time} minutes.")
            return
        elif lock_until and lock_until <= datetime.now():
            # Nếu thời gian khóa đã hết, tự động mở khóa
            self.db.update_user_nha(username, {"lock_until": None, "login_attempts": 0})
            logger.info(f"Account {username} has been automatically unlocked!!!")
            user = self.db.get_user(username)  # Lấy lại dữ liệu user sau khi cập nhật

        stored_password = user.get("password", "")
        actual_role = user.get("role", "").lower()
        login_attempts = user.get("login_attempts", 0)

        # Kiểm tra role
        if selected_role != actual_role:
            QMessageBox.warning(self, "Error",
                              f"Your role is wrong!\n"
                              f"Your role is: {actual_role.capitalize()}")
            return

        # Kiểm tra mật khẩu
        if password == stored_password:
            # Đăng nhập thành công, reset số lần thử
            self.db.update_user_nha(username, {"login_attempts": 0, "lock_until": None})
            logger.info(f"Login successful for {username}")

            if actual_role == "admin":
                self.admin_window = AdminWindow(login_window=self, user_data=user)
                self.admin_window.show()
            else:
                self.user_window = CustomUserWindow(login_window=self, user_data=user)
                self.user_window.show()
            self.close()  # Đóng cửa sổ đăng nhập
        else:
            # Đăng nhập thất bại--> tăng số lần thử
            login_attempts += 1
            max_attempts = 3
            if login_attempts >= max_attempts:
                lock_time = datetime.now() + timedelta(minutes=10)
                self.db.update_user_nha(username, {
                    "login_attempts": login_attempts,
                    "lock_until": lock_time
                })
                QMessageBox.warning(self, "Error",
                                  "You have entered the wrong password 3 times! Account is locked for 10 minutes!")
                logger.warning(f"Account {username} is locked due to too many attempts!!")
            else:
                self.db.update_user_nha(username, {"login_attempts": login_attempts})
                remaining_attempts = max_attempts - login_attempts
                QMessageBox.warning(self, "Error",
                                  f"Incorrect password! You have {remaining_attempts} attempts left.")
            logger.info(f"Login failed for {username}. Number of attempts: {login_attempts}")