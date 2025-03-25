# from PySide6.QtWidgets import QMessageBox
# from pymongo import MongoClient
# from database.api import Database
# import logging
# from datetime import datetime, timedelta
# from bson.objectid import ObjectId
#
# # Thiết lập logging
# logger = logging.getLogger(__name__)
#
# class AdminExFnct_Api(Database):
#     def __init__(self):
#         super().__init__()
#
#     def update_invoice_status(self, invoice_id, new_status):
#         """Cập nhật trạng thái hóa đơn trong cơ sở dữ liệu"""
#         try:
#             # Giả định bạn sử dụng một cơ sở dữ liệu (ví dụ: SQLite, MongoDB, v.v.)
#             # Cập nhật trạng thái của hóa đơn với invoice_id
#             # Ví dụ với MongoDB:
#             result = self.db.invoices.update_one(
#                 {"invoice_id": invoice_id},
#                 {"$set": {"status": new_status}}
#             )
#             return result.modified_count > 0
#         except Exception as e:
#             logger.error(f"Error updating invoice status: {e}")
#             return False
#
#     # Trong class API
#
#     def get_all_products_with_categories(self):
#         """Lấy tất cả sản phẩm cùng với danh sách category và location"""
#         try:
#             products = list(self.products.find({}, {"_id": 0}))
#             categories = sorted(set(product.get("category", "") for product in products))
#             locations = sorted(set(product.get("location_number", "") for product in products))
#             return {
#                 "products": products,
#                 "categories": categories,
#                 "locations": locations
#             }
#         except Exception as e:
#             logger.error(f"Error in get_all_products_with_categories: {e}")
#             return {"products": [], "categories": [], "locations": []}
#
#     def get_reorder_status(self):
#         """Trả về danh sách sản phẩm và trạng thái Reorder"""
#         try:
#             products = list(self.products.find({}, {"_id": 0, "product_id": 1, "current_stock": 1}))
#             for product in products:
#                 current_stock = int(product.get("current_stock", 0))
#                 product["reorder_status"] = "Yes" if current_stock <= 10 else "No"
#             return products
#         except Exception as e:
#             logger.error(f"Error in get_reorder_status: {e}")
#             return []
#
#     def get_product_by_id(self, product_id):
#         """Lấy thông tin sản phẩm theo ID"""
#         try:
#             return self.products.find_one({"product_id": product_id}, {"_id": 0}) or {}
#         except Exception as e:
#             logger.error(f"Error in get_product_by_id: {e}")
#             return {}
#
#     def add_product(self, product_data):
#         """Thêm sản phẩm vào MongoDB"""
#         try:
#             if self.products.find_one({"product_id": product_data["product_id"]}):
#                 return -1  # Product ID đã tồn tại
#             self.products.insert_one(product_data)
#             return 0  # Thành công
#         except Exception as e:
#             logger.error(f"Error in add_product: {e}")
#             return -1
#
#     def update_product(self, product_id, updated_data):
#         """Cập nhật sản phẩm trong MongoDB"""
#         try:
#             result = self.products.update_one({"product_id": product_id}, {"$set": updated_data})
#             return result.modified_count > 0
#         except Exception as e:
#             logger.error(f"Error in update_product: {e}")
#             return False
#
#     def delete_product(self, product_id):
#         """Xóa sản phẩm khỏi MongoDB"""
#         try:
#             result = self.products.delete_one({"product_id": product_id})
#             return result.deleted_count > 0
#         except Exception as e:
#             logger.error(f"Error in delete_product: {e}")
#             return False
#
#     def search_product(self, search_field, search_value):
#         """Tìm kiếm sản phẩm theo trường dữ liệu"""
#         try:
#             query = {search_field: {"$regex": search_value, "$options": "i"}}
#             return list(self.products.find(query, {"_id": 0}))
#         except Exception as e:
#             logger.error(f"Error in search_product: {e}")
#             return []
#
#     def update_stock(self, product_id, quantity, action_type):
#         """Cập nhật số lượng tồn kho với kiểm tra hợp lệ"""
#         try:
#             product = self.products.find_one({"product_id": product_id})
#             if not product:
#                 return -1
#             current_stock = int(product.get("current_stock", 0))
#             if action_type == "import":
#                 new_stock = current_stock + quantity
#             elif action_type == "export":
#                 if quantity > current_stock:
#                     return -2
#                 new_stock = current_stock - quantity
#             else:
#                 return -1  # Invalid action_type
#             result = self.products.update_one({"product_id": product_id}, {"$set": {"current_stock": new_stock}})
#             return new_stock if result.modified_count > 0 else -1
#         except Exception as e:
#             logger.error(f"Error in update_stock: {e}")
#             return -1
#
#     def get_all_invoices(self):
#         """Lấy toàn bộ hóa đơn từ MongoDB"""
#         try:
#             return list(self.invoices.find({}, {"_id": 0}))
#         except Exception as e:
#             logger.error(f"Error in get_all_invoices: {e}")
#             return []
#
#     def search_invoice(self, search_field, search_value):
#         """Tìm kiếm hóa đơn theo invoice_id, invoice_date, status, product_name, quantity, price"""
#         try:
#             query = {}
#             if search_field == "invoice_id":
#                 query = {"invoice_id": search_value.strip()}
#             elif search_field in ["invoice_date", "status"]:
#                 query = {search_field: {"$regex": search_value.strip(), "$options": "i"}}
#             elif search_field == "product_name":
#                 query = {"cart.product_name": {"$regex": search_value.strip(), "$options": "i"}}
#             elif search_field == "quantity":
#                 query = {"cart.quantity": int(search_value)}
#             elif search_field == "price":
#                 query = {"total_price": float(search_value)}
#             return list(self.invoices.find(query, {"_id": 0}))
#         except ValueError as e:
#             logger.error(f"ValueError in search_invoice: {e}")
#             return []
#         except Exception as e:
#             logger.error(f"Error in search_invoice: {e}")
#             return []
#
#     def update_invoice_status(self, invoice_id, new_status):
#         """Cập nhật trạng thái hóa đơn trong MongoDB"""
#         try:
#             result = self.invoices.update_one({"invoice_id": invoice_id}, {"$set": {"status": new_status}})
#             return result.modified_count > 0
#         except Exception as e:
#             logger.error(f"Error in update_invoice_status: {e}")
#             return False
#
#     def get_users(self):
#         """Lấy danh sách người dùng"""
#         try:
#             return list(self.users.find({}, {"_id": 0, "username": 1, "password": 1, "role": 1}))
#         except Exception as e:
#             logger.error(f"Error in get_users: {e}")
#             return []
#
#     def add_user(self, user_data):
#         """Thêm người dùng mới"""
#         try:
#             result = self.users.insert_one(user_data)
#             return result.inserted_id is not None
#         except Exception as e:
#             logger.error(f"Error in add_user: {e}")
#             return False
#
#     def update_user(self, old_username, new_data):
#         """Cập nhật thông tin người dùng"""
#         try:
#             result = self.users.update_one({"username": old_username}, {"$set": new_data})
#             return result.modified_count > 0
#         except Exception as e:
#             logger.error(f"Error in update_user: {e}")
#             return False
#
#     def delete_user(self, username):
#         """Xóa người dùng"""
#         try:
#             result = self.users.delete_one({"username": username})
#             return result.deleted_count > 0
#         except Exception as e:
#             logger.error(f"Error in delete_user: {e}")
#             return False
#
#     def search_users(self, search_field, search_text):
#         """Tìm kiếm người dùng"""
#         try:
#             query = {search_field: {"$regex": f".*{search_text}.*", "$options": "i"}}
#             return list(self.users.find(query, {"_id": 0}))
#         except Exception as e:
#             logger.error(f"Error in search_users: {e}")
#             return []
#
#     def get_suppliers(self):
#         """Lấy danh sách nhà cung cấp"""
#         try:
#             return list(self.suppliers.find({}, {"_id": 0}))
#         except Exception as e:
#             logger.error(f"Error in get_suppliers: {e}")
#             return []
#
#     def add_supplier(self, supplier_data):
#         """Thêm nhà cung cấp mới"""
#         try:
#             if self.suppliers.find_one({"supplier_id": supplier_data["supplier_id"]}):
#                 return False  # Supplier ID already exists
#             result = self.suppliers.insert_one(supplier_data)
#             return result.inserted_id is not None
#         except Exception as e:
#             logger.error(f"Error in add_supplier: {e}")
#             return False
#
#     def update_supplier(self, supplier_id, new_data):
#         """Cập nhật thông tin nhà cung cấp"""
#         try:
#             result = self.suppliers.update_one({"supplier_id": supplier_id}, {"$set": new_data})
#             return result.modified_count > 0
#         except Exception as e:
#             logger.error(f"Error in update_supplier: {e}")
#             return False
#
#     def delete_supplier(self, supplier_id):
#         """Xóa nhà cung cấp"""
#         try:
#             result = self.suppliers.delete_one({"supplier_id": supplier_id})
#             return result.deleted_count > 0
#         except Exception as e:
#             logger.error(f"Error in delete_supplier: {e}")
#             return False
#
#     def search_suppliers(self, search_field, search_text):
#         """Tìm kiếm nhà cung cấp"""
#         try:
#             query = {search_field: {"$regex": f".*{search_text}.*", "$options": "i"}}
#             return list(self.suppliers.find(query, {"_id": 0}))
#         except Exception as e:
#             logger.error(f"Error in search_suppliers: {e}")
#             return []
#
#     def get_all_suppliers(self):
#         """Lấy danh sách supplier_id từ collection suppliers"""
#         try:
#             suppliers = list(self.suppliers.find({}, {"_id": 0, "supplier_id": 1}))
#             return [supplier["supplier_id"] for supplier in suppliers]
#         except Exception as e:
#             logger.error(f"Error in get_all_suppliers: {e}")
#             return []
#
#     def get_products(self):
#         """Lấy danh sách sản phẩm với dữ liệu đã được làm sạch"""
#         try:
#             products = list(self.products.find({}, {"_id": 0}))
#             cleaned_products = []
#             for product in products:
#                 try:
#                     product["current_stock"] = int(product.get("current_stock", 0))
#                     cleaned_products.append(product)
#                 except (ValueError, TypeError):
#                     logger.warning(f"Invalid current_stock for product {product.get('product_id')}: {product.get('current_stock')}")
#                     product["current_stock"] = 0
#                     cleaned_products.append(product)
#             return cleaned_products
#         except Exception as e:
#             logger.error(f"Error in get_products: {e}")
#             return []
#
#     def get_max_product_id(self):
#         """Lấy product_id lớn nhất và tạo mã mới"""
#         try:
#             products = list(self.products.find({}, {"product_id": 1, "_id": 0}))
#             max_id = 0
#             for product in products:
#                 product_id = product.get("product_id", "")
#                 if product_id.startswith("P") and product_id[1:].isdigit():
#                     num = int(product_id[1:])
#                     max_id = max(max_id, num)
#             return f"P{str(max_id + 1).zfill(3)}"
#         except Exception as e:
#             logger.error(f"Error in get_max_product_id: {e}")
#             return "P001"
#
#     def get_reorder_stats(self):
#         """Lấy thống kê reorder"""
#         try:
#             reorder_count = self.products.count_documents({"current_stock": {"$lte": 10}})
#             out_of_stock_count = self.products.count_documents({"current_stock": 0})
#             current_stock_count = self.products.count_documents({"current_stock": {"$gt": 10}})
#             return reorder_count, out_of_stock_count, current_stock_count
#         except Exception as e:
#             logger.error(f"Error in get_reorder_stats: {e}")
#             return 0, 0, 0
#
#     # Trong API_Admin.py, thêm vào class AdminExFnct_Api
#     from datetime import datetime, timedelta
#     from bson.objectid import ObjectId
#
#     def get_revenue_by_week(self, start_date=None, end_date=None):
#         """Lấy dữ liệu doanh thu theo tuần từ collection invoices"""
#         if not start_date:
#             start_date = datetime.now() - timedelta(weeks=4)
#         if not end_date:
#             end_date = datetime.now()
#
#         pipeline = [
#             {
#                 "$match": {
#                     "invoice_date": {
#                         "$exists": True,
#                         "$ne": None,
#                         "$regex": "^(\\d{4}-\\d{2}-\\d{2}|\\d{2}/\\d{2}/\\d{4})$"
#                     }
#                 }
#             },
#             {
#                 "$addFields": {
#                     "invoice_date_converted": {
#                         "$cond": {
#                             "if": {
#                                 "$regexMatch": {
#                                     "input": "$invoice_date",
#                                     "regex": "^\\d{4}-\\d{2}-\\d{2}$"
#                                 }
#                             },
#                             "then": {
#                                 "$dateFromString": {
#                                     "dateString": "$invoice_date",
#                                     "format": "%Y-%m-%d"
#                                 }
#                             },
#                             "else": {
#                                 "$dateFromString": {
#                                     "dateString": "$invoice_date",
#                                     "format": "%d/%m/%Y"
#                                 }
#                             }
#                         }
#                     }
#                 }
#             },
#             {
#                 "$match": {
#                     "invoice_date_converted": {"$gte": start_date, "$lte": end_date}
#                 }
#             },
#             {
#                 "$group": {
#                     "_id": {
#                         "$dateToString": {
#                             "format": "%Y-%U",
#                             "date": "$invoice_date_converted"
#                         }
#                     },
#                     "total_value": {"$sum": "$total_price"}
#                 }
#             },
#             {"$sort": {"_id": 1}}
#         ]
#         try:
#             result = list(self.invoices.aggregate(pipeline))
#             if not result:
#                 logger.debug("No revenue data found for the specified date range.")
#                 return []
#             return [{"week": item["_id"], "total_value": item["total_value"]} for item in result]
#         except Exception as e:
#             logger.error(f"Error in get_revenue_by_week: {e}")
#             return []
#
#     def get_top_products_sold(self, start_date=None, limit=5):
#         """Lấy top sản phẩm bán chạy trong tuần"""
#         if not start_date:
#             start_date = datetime.now() - timedelta(weeks=1)  # 1 tuần gần nhất
#
#         pipeline = [
#             # Lọc các document có invoice_date hợp lệ
#             {
#                 "$match": {
#                     "invoice_date": {
#                         "$exists": True,
#                         "$ne": None,
#                         "$regex": "^(\\d{4}-\\d{2}-\\d{2}|\\d{2}/\\d{2}/\\d{4})$"
#                     }
#                 }
#             },
#             # Chuyển đổi invoice_date từ chuỗi thành datetime
#             {
#                 "$addFields": {
#                     "invoice_date_converted": {
#                         "$cond": {
#                             "if": {
#                                 "$regexMatch": {
#                                     "input": "$invoice_date",
#                                     "regex": "^\\d{4}-\\d{2}-\\d{2}$"
#                                 }
#                             },
#                             "then": {
#                                 "$dateFromString": {
#                                     "dateString": "$invoice_date",
#                                     "format": "%Y-%m-%d"
#                                 }
#                             },
#                             "else": {
#                                 "$dateFromString": {
#                                     "dateString": "$invoice_date",
#                                     "format": "%d/%m/%Y"
#                                 }
#                             }
#                         }
#                     }
#                 }
#             },
#             {
#                 "$match": {
#                     "invoice_date_converted": {"$gte": start_date}
#                 }
#             },
#             {"$unwind": "$cart"},
#             # Nhóm theo product_name
#             {
#                 "$group": {
#                     "_id": "$cart.product_name",
#                     "total_sold": {"$sum": "$cart.quantity"}
#                 }
#             },
#             {
#                 "$project": {
#                     "product_name": "$_id",
#                     "total_sold": 1,
#                     "_id": 0
#                 }
#             },
#             {"$sort": {"total_sold": -1}},
#             {"$limit": limit}
#         ]
#         try:
#             result = list(self.invoices_collection.aggregate(pipeline))
#             if not result:
#                 print("No top products data found for the specified date range.")
#                 return []
#             return result
#         except Exception as e:
#             print(f"Error in get_top_products_sold: {e}")
#             return []
#
#     def get_recent_activities(self, limit=5):
#         """Lấy các hoạt động gần đây"""
#         activities = []
#
#         # Lấy các sản phẩm vừa được thêm
#         new_products = self.products_collection.find(
#             {}, {"product_name": 1, "_id": 1}
#         ).sort("_id", -1).limit(limit)
#         for product in new_products:
#             # Suy ra thời gian từ _id
#             timestamp = ObjectId(product["_id"]).generation_time
#             activities.append({
#                 "message": f"Product '{product['product_name']}' added to inventory",
#                 "timestamp": timestamp
#             })
#
#         # Lấy các hóa đơn vừa được tạo
#         new_invoices = self.invoices_collection.find(
#             {}, {"invoice_id": 1, "_id": 1}
#         ).sort("_id", -1).limit(limit)
#         for invoice in new_invoices:
#             timestamp = ObjectId(invoice["_id"]).generation_time
#             activities.append({
#                 "message": f"Invoice '{invoice['invoice_id']}' created",
#                 "timestamp": timestamp
#             })
#
#         # Sắp xếp theo thời gian
#         activities.sort(key=lambda x: x["timestamp"], reverse=True)
#         return activities[:limit]
import logging
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from database.api import Database

# Thiết lập logging
logger = logging.getLogger(__name__)

class AdminExFnct_Api(Database):
    def __init__(self):
        super().__init__()
        self.users = self.db.users
        self.suppliers = self.db.suppliers
        self.products = self.db.products
        self.invoices = self.db.invoices

    # --- User-related methods ---
    def get_users(self):
        """Lấy danh sách người dùng"""
        try:
            return list(self.users.find({}, {"_id": 0, "username": 1, "password": 1, "role": 1}))
        except Exception as e:
            logger.error(f"Error in get_users: {e}")
            return []

    def add_user(self, user_data):
        """Thêm người dùng mới"""
        try:
            result = self.users.insert_one(user_data)
            return result.inserted_id is not None
        except Exception as e:
            logger.error(f"Error in add_user: {e}")
            return False

    def update_user(self, old_username, new_data):
        """Cập nhật thông tin người dùng"""
        try:
            result = self.users.update_one({"username": old_username}, {"$set": new_data})
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error in update_user: {e}")
            return False

    def delete_user(self, username):
        """Xóa người dùng"""
        try:
            result = self.users.delete_one({"username": username})
            return result.deleted_count > 0
        except Exception as e:
            logger.error(f"Error in delete_user: {e}")
            return False

    def search_users(self, search_field, search_text):
        """Tìm kiếm người dùng theo trường và giá trị"""
        try:
            query = {search_field: {"$regex": f".*{search_text}.*", "$options": "i"}}
            return list(self.users.find(query, {"_id": 0}))
        except Exception as e:
            logger.error(f"Error in search_users: {e}")
            return []

    # --- Supplier-related methods ---
    def get_suppliers(self):
        """Lấy danh sách nhà cung cấp"""
        try:
            return list(self.suppliers.find({}, {"_id": 0}))
        except Exception as e:
            logger.error(f"Error in get_suppliers: {e}")
            return []

    def add_supplier(self, supplier_data):
        """Thêm nhà cung cấp mới"""
        try:
            result = self.suppliers.insert_one(supplier_data)
            return result.inserted_id is not None
        except Exception as e:
            logger.error(f"Error in add_supplier: {e}")
            return False

    def update_supplier(self, supplier_id, new_data):
        """Cập nhật thông tin nhà cung cấp"""
        try:
            result = self.suppliers.update_one({"supplier_id": supplier_id}, {"$set": new_data})
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error in update_supplier: {e}")
            return False

    def delete_supplier(self, supplier_id):
        """Xóa nhà cung cấp"""
        try:
            result = self.suppliers.delete_one({"supplier_id": supplier_id})
            return result.deleted_count > 0
        except Exception as e:
            logger.error(f"Error in delete_supplier: {e}")
            return False

    def search_suppliers(self, search_field, search_text):
        """Tìm kiếm nhà cung cấp theo trường và giá trị"""
        try:
            query = {search_field: {"$regex": f".*{search_text}.*", "$options": "i"}}
            return list(self.suppliers.find(query, {"_id": 0}))
        except Exception as e:
            logger.error(f"Error in search_suppliers: {e}")
            return []

    # --- Product-related methods ---
    def get_products(self):
        """Lấy danh sách sản phẩm"""
        try:
            return list(self.products.find({}, {"current_stock": 1, "category": 1, "_id": 0}))
        except Exception as e:
            logger.error(f"Error in get_products: {e}")
            return []

    def add_product(self, product_data):
        """Thêm sản phẩm mới"""
        try:
            existing_product = self.products.find_one({"product_id": product_data["product_id"]})
            if existing_product:
                return -1
            result = self.products.insert_one(product_data)
            return 0 if result.inserted_id else -1
        except Exception as e:
            logger.error(f"Error in add_product: {e}")
            return -1

    def update_product(self, product_id, updated_data):
        """Cập nhật thông tin sản phẩm"""
        try:
            result = self.products.update_one({"product_id": product_id}, {"$set": updated_data})
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error in update_product: {e}")
            return False

    def delete_product(self, product_id):
        """Xóa sản phẩm"""
        try:
            result = self.products.delete_one({"product_id": product_id})
            return result.deleted_count > 0
        except Exception as e:
            logger.error(f"Error in delete_product: {e}")
            return False

    def search_product(self, search_field, search_text):
        """Tìm kiếm sản phẩm theo trường và giá trị"""
        try:
            query = {search_field: {"$regex": f".*{search_text}.*", "$options": "i"}}
            return list(self.products.find(query, {"_id": 0}))
        except Exception as e:
            logger.error(f"Error in search_product: {e}")
            return []

    def get_all_products_with_categories(self):
        """Lấy tất cả sản phẩm cùng với danh mục và vị trí"""
        try:
            products = list(self.products.find({}, {"_id": 0}))
            categories = self.products.distinct("category")
            locations = self.products.distinct("location_number")
            return {
                "products": products,
                "categories": categories,
                "locations": locations
            }
        except Exception as e:
            logger.error(f"Error in get_all_products_with_categories: {e}")
            return {"products": [], "categories": [], "locations": []}

    def get_max_product_id(self):
        """Lấy product_id lớn nhất để tạo ID mới"""
        try:
            products = list(self.products.find({}, {"product_id": 1, "_id": 0}))
            if not products:
                return "P001"
            product_ids = [p["product_id"] for p in products if p.get("product_id", "").startswith("P") and p["product_id"][1:].isdigit()]
            if not product_ids:
                return "P001"
            max_id = max(int(pid[1:]) for pid in product_ids)
            return f"P{max_id + 1:03d}"
        except Exception as e:
            logger.error(f"Error in get_max_product_id: {e}")
            return "P001"

    def update_stock(self, product_id, quantity, action_type):
        """Cập nhật số lượng tồn kho"""
        try:
            product = self.products.find_one({"product_id": product_id})
            if not product:
                return -1
            current_stock = product.get("current_stock", 0)
            if action_type == "export":
                if quantity > current_stock:
                    return -2
                new_stock = current_stock - quantity
            else:  # import
                new_stock = current_stock + quantity
            self.products.update_one({"product_id": product_id}, {"$set": {"current_stock": new_stock}})
            return new_stock
        except Exception as e:
            logger.error(f"Error in update_stock: {e}")
            return -1

    def get_reorder_stats(self):
        """Lấy thống kê số lượng sản phẩm cần đặt lại"""
        try:
            reorder_count = self.products.count_documents({"current_stock": {"$lt": 10}})
            out_of_stock_count = self.products.count_documents({"current_stock": 0})
            current_stock_count = self.products.count_documents({"current_stock": {"$gte": 10}})
            return reorder_count, out_of_stock_count, current_stock_count
        except Exception as e:
            logger.error(f"Error in get_reorder_stats: {e}")
            return 0, 0, 0

    # --- Invoice-related methods ---
    def get_all_invoices(self):
        """Lấy tất cả hóa đơn"""
        try:
            return list(self.invoices.find({}, {"_id": 0}))
        except Exception as e:
            logger.error(f"Error in get_all_invoices: {e}")
            return []

    def search_invoice(self, search_field, search_value):
        """Tìm kiếm hóa đơn theo trường và giá trị"""
        try:
            query = {}
            if search_field == "invoice_id":
                query = {"invoice_id": {"$regex": f".*{search_value}.*", "$options": "i"}}
            elif search_field == "product_name":
                query = {"cart.product_name": {"$regex": f".*{search_value}.*", "$options": "i"}}
            elif search_field == "invoice_date":
                query = {"invoice_date": {"$regex": f".*{search_value}.*", "$options": "i"}}
            elif search_field == "quantity":
                try:
                    qty = int(search_value)
                    query = {"cart.quantity": qty}
                except ValueError:
                    logger.warning(f"Giá trị tìm kiếm cho quantity không phải số nguyên: {search_value}")
                    return []
            elif search_field == "total_price":
                try:
                    price = float(search_value)
                    query = {"total_price": price}
                except ValueError:
                    logger.warning(f"Giá trị tìm kiếm cho total_price không phải số thực: {search_value}")
                    return []
            elif search_field == "status":
                query = {"status": {"$regex": f".*{search_value}.*", "$options": "i"}}
            else:
                logger.warning(f"Trường tìm kiếm không hợp lệ: {search_field}")
                return []

            return list(self.invoices.find(query, {"_id": 0}))
        except Exception as e:
            logger.error(f"Lỗi khi tìm kiếm hóa đơn: {e}")
            return []

    def update_invoice_status(self, invoice_id, new_status):
        """Cập nhật trạng thái cho tất cả hóa đơn có cùng invoice_id trong MongoDB"""
        try:
            result = self.invoices.update_many(
                {"invoice_id": invoice_id},
                {"$set": {"status": new_status}}
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error in update_invoice_status: {e}")
            return False

    # --- Dashboard-related methods ---
    def get_revenue_by_week(self, start_date=None, end_date=None):
        """Lấy dữ liệu doanh thu theo tuần từ collection invoices"""
        if not start_date:
            start_date = datetime.now() - timedelta(weeks=8)  # Lấy dữ liệu 4 tuần gần nhất
        if not end_date:
            end_date = datetime.now()

        pipeline = [
            # Lọc các document có invoice_date hợp lệ
            {
                "$match": {
                    "invoice_date": {
                        "$exists": True,
                        "$ne": None,
                        "$regex": "^(\\d{4}-\\d{2}-\\d{2}|\\d{2}/\\d{2}/\\d{4})$"
                    }
                }
            },
            # Chuyển đổi invoice_date từ chuỗi thành datetime
            {
                "$addFields": {
                    "invoice_date_converted": {
                        "$cond": {
                            "if": {
                                "$regexMatch": {
                                    "input": "$invoice_date",
                                    "regex": "^\\d{4}-\\d{2}-\\d{2}$"
                                }
                            },
                            "then": {
                                "$dateFromString": {
                                    "dateString": "$invoice_date",
                                    "format": "%Y-%m-%d"
                                }
                            },
                            "else": {
                                "$dateFromString": {
                                    "dateString": "$invoice_date",
                                    "format": "%d/%m/%Y"
                                }
                            }
                        }
                    }
                }
            },
            # Lọc theo khoảng thời gian
            {
                "$match": {
                    "invoice_date_converted": {"$gte": start_date, "$lte": end_date}
                }
            },
            # Nhóm theo tuần
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "format": "%Y-%U",
                            "date": "$invoice_date_converted"
                        }
                    },
                    "total_value": {"$sum": "$total_price"}
                }
            },
            {"$sort": {"_id": 1}},
            {"$limit": 30}  # Giới hạn số tuần để tránh truy vấn quá lớn
        ]
        try:
            result = list(self.invoices.aggregate(pipeline))
            if not result:
                logger.debug("No revenue data found for the specified date range.")
                return []
            return [{"week": item["_id"], "total_value": item["total_value"]} for item in result]
        except Exception as e:
            logger.error(f"Error in get_revenue_by_week: {e}")
            return []

    def get_top_suppliers(self, limit=5):
        """Lấy top nhà cung cấp theo số lượng sản phẩm cung cấp"""
        pipeline = [
            {"$group": {
                "_id": "$supplier_id",
                "product_count": {"$sum": 1}
            }},
            {"$lookup": {
                "from": "suppliers",
                "localField": "_id",
                "foreignField": "supplier_id",
                "as": "supplier_info"
            }},
            {"$unwind": "$supplier_info"},
            {"$project": {
                "supplier_name": "$supplier_info.supplier_name",
                "product_count": 1,
                "_id": 0
            }},
            {"$sort": {"product_count": -1}},
            {"$limit": limit}
        ]
        try:
            return list(self.products.aggregate(pipeline))
        except Exception as e:
            logger.error(f"Error in get_top_suppliers: {e}")
            return []

    def get_top_products_sold(self, start_date=None, limit=5):
        """Lấy top sản phẩm bán chạy trong tuần"""
        if not start_date:
            start_date = datetime.now() - timedelta(weeks=1)  # 1 tuần gần nhất

        pipeline = [
            # Lọc các document có invoice_date hợp lệ
            {
                "$match": {
                    "invoice_date": {
                        "$exists": True,
                        "$ne": None,
                        "$regex": "^(\\d{4}-\\d{2}-\\d{2}|\\d{2}/\\d{2}/\\d{4})$"
                    }
                }
            },
            # Chuyển đổi invoice_date từ chuỗi thành datetime
            {
                "$addFields": {
                    "invoice_date_converted": {
                        "$cond": {
                            "if": {
                                "$regexMatch": {
                                    "input": "$invoice_date",
                                    "regex": "^\\d{4}-\\d{2}-\\d{2}$"
                                }
                            },
                            "then": {
                                "$dateFromString": {
                                    "dateString": "$invoice_date",
                                    "format": "%Y-%m-%d"
                                }
                            },
                            "else": {
                                "$dateFromString": {
                                    "dateString": "$invoice_date",
                                    "format": "%d/%m/%Y"
                                }
                            }
                        }
                    }
                }
            },
            # Lọc theo khoảng thời gian
            {
                "$match": {
                    "invoice_date_converted": {"$gte": start_date}
                }
            },
            {"$unwind": "$cart"},
            # Nhóm theo product_name
            {
                "$group": {
                    "_id": "$cart.product_name",
                    "total_sold": {"$sum": "$cart.quantity"}
                }
            },
            {
                "$project": {
                    "product_name": "$_id",
                    "total_sold": 1,
                    "_id": 0
                }
            },
            {"$sort": {"total_sold": -1}},
            {"$limit": limit}
        ]
        try:
            result = list(self.invoices.aggregate(pipeline))
            if not result:
                logger.debug("No top products data found for the specified date range.")
                return []
            return result
        except Exception as e:
            logger.error(f"Error in get_top_products_sold: {e}")
            return []

    def get_recent_activities(self, limit=5):
        """Lấy các hoạt động gần đây"""
        activities = []

        # Lấy các sản phẩm vừa được thêm
        try:
            new_products = self.products.find(
                {}, {"product_name": 1, "_id": 1}
            ).sort("_id", -1).limit(limit)
            for product in new_products:
                timestamp = ObjectId(product["_id"]).generation_time
                activities.append({
                    "message": f"Product '{product['product_name']}' added to inventory",
                    "timestamp": timestamp
                })
        except Exception as e:
            logger.error(f"Error fetching new products for recent activities: {e}")

        # Lấy các hóa đơn vừa được tạo
        try:
            new_invoices = self.invoices.find(
                {}, {"invoice_id": 1, "_id": 1}
            ).sort("_id", -1).limit(limit)
            for invoice in new_invoices:
                timestamp = ObjectId(invoice["_id"]).generation_time
                activities.append({
                    "message": f"Invoice '{invoice['invoice_id']}' created",
                    "timestamp": timestamp
                })
        except Exception as e:
            logger.error(f"Error fetching new invoices for recent activities: {e}")

        # Sắp xếp theo thời gian
        activities.sort(key=lambda x: x["timestamp"], reverse=True)
        return activities[:limit]

    def update_dashboard_stats(self):
        """Cập nhật số liệu thống kê cho dashboard"""
        try:
            # Lấy dữ liệu doanh thu theo tuần
            revenue_data = self.get_revenue_by_week()

            # Lấy top sản phẩm bán chạy
            top_products = self.get_top_products_sold()

            # Lấy hoạt động gần đây
            recent_activities = self.get_recent_activities()

            # Trả về dữ liệu để cập nhật giao diện (giả định)
            return {
                "revenue_data": revenue_data,
                "top_products": top_products,
                "recent_activities": recent_activities
            }

        except KeyboardInterrupt:
            logger.warning("Cập nhật dashboard bị gián đoạn bởi người dùng (KeyboardInterrupt).")
            return None  # Trả về None để giao diện xử lý
        except Exception as e:
            logger.error(f"Lỗi khi cập nhật dashboard: {e}")
            return None
