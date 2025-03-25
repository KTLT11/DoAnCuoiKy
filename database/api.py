from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

class Database:
    def __init__(self):
        # Tải biến môi trường từ file .env
        load_dotenv(find_dotenv())

        # Lấy thông tin kết nối từ biến môi trường
        mongo_url = os.getenv("MONGO_URL")  # Lấy URL MongoDB từ .env
        db_name = os.getenv("MONGO_DB")     # Lấy tên database từ .env

        # Kiểm tra nếu không tìm thấy biến môi trường
        if not mongo_url or not db_name:
            raise ValueError("Không tìm thấy MONGO_URL hoặc MONGO_DB trong file .env")

        # Kết nối MongoDB
        self.client = MongoClient(mongo_url)

        # Chọn database
        self.db = self.client[db_name]

        # Khai báo collections
        self.products = self.db["products"]
        self.invoices = self.db["invoices"]
        self.users = self.db["users"]
        self.suppliers = self.db["suppliers"]

    def get_collection(self, name):
        """Trả về collection theo tên"""
        return self.db[name]