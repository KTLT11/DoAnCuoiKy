import logging
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        """Kết nối MongoDB"""
        # Tải biến môi trường từ file .env
        load_dotenv(find_dotenv())

        try:
            # Lấy thông tin kết nối từ biến môi trường
            mongo_url = os.getenv("MONGO_URL")
            db_name = os.getenv("MONGO_DB")

            # Kiểm tra nếu không tìm thấy biến môi trường
            if not mongo_url or not db_name:
                logger.error("Không tìm thấy MONGO_URL hoặc MONGO_DB trong file .env")
                raise ValueError("Không tìm thấy MONGO_URL hoặc MONGO_DB trong file .env")

            # Kết nối MongoDB
            self.client = MongoClient(mongo_url)

            # Chọn database
            self.db = self.client[db_name]
            self.users = self.db["users"]
            logger.info("Kết nối MongoDB thành công!")
        except Exception as e:
            logger.error(f"Lỗi kết nối MongoDB: {e}")
            raise

    def get_user(self, username):
        """Tìm kiếm người dùng trong MongoDB"""
        try:
            return self.users.find_one({"username": username})
        except Exception as e:
            logger.error(f"Lỗi truy vấn MongoDB: {e}")
            return None

    def get_users_by_role(self, role):
        """Lấy danh sách user theo vai trò"""
        try:
            return list(self.users.find({"role": role}))
        except Exception as e:
            logger.error(f"Lỗi khi lấy danh sách người dùng theo vai trò: {e}")
            return []

    def update_user_nha(self, username, data):
        """Cập nhật thông tin người dùng"""
        try:
            self.users.update_one({"username": username}, {"$set": data})
            logger.info(f"Đã cập nhật thông tin cho {username}")
        except Exception as e:
            logger.error(f"Lỗi khi cập nhật user: {e}")