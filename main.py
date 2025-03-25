# main.py
import sys
from PySide6.QtWidgets import QApplication
from services.login_service import LoginWindow, AdminWindow, UserWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())