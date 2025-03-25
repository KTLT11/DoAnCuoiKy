import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

# Tải biến môi trường từ file .env
load_dotenv(find_dotenv())

# Lấy thông tin kết nối từ biến môi trường
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")

# Kiểm tra nếu không tìm thấy biến môi trường
if not MONGO_URL or not MONGO_DB:
    raise ValueError("Không tìm thấy MONGO_URL hoặc MONGO_DB trong file .env")

# Kết nối tới MongoDB
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

# Định nghĩa ánh xạ giữa file và collection
collection_map = {
    "product.json": "products",
    "invoice.json": "invoices",
    "supplier.json": "suppliers",
    "user.json": "users"
}

# Đường dẫn đến thư mục chứa các file JSON
data_folder = "data"

# Duyệt qua từng file trong thư mục và tải lên MongoDB
for file_name, collection_name in collection_map.items():
    file_path = os.path.join(data_folder, file_name)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Đảm bảo dữ liệu là danh sách trước khi insert vào MongoDB
            if isinstance(data, dict):
                data = [data]  # Chuyển dict thành list để insert

            # Thực hiện insert vào MongoDB
            db[collection_name].insert_many(data)
            print(f"Đã tải {file_name} vào collection '{collection_name}' thành công!")
    else:
        print(f" Không tìm thấy file {file_name}")

print(" Hoàn tất!")