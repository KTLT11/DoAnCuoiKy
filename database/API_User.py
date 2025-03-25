from database.api import Database
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("user_api.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class UserFunc_Api:
    def __init__(self):
        self.db = Database()
        self.products_collection = self.db.products
        self.invoices_collection = self.db.invoices
        self.users = self.db.users

    def get_max_invoice_id(self):
        """Lấy invoice_id lớn nhất từ database và trả về giá trị tiếp theo dạng 'invoiceXXX'."""
        try:
            max_invoice = self.invoices_collection.find_one(
                {"invoice_id": {"$regex": "^INV\\d{3}$"}},
                sort=[("invoice_id", -1)]
            )
            if max_invoice and "invoice_id" in max_invoice:
                current_max = int(max_invoice["invoice_id"].replace("INV", ""))
                new_invoice_id = f"INV{current_max + 1:03d}"
                logger.debug(f"Max invoice_id hiện tại: {max_invoice['invoice_id']}, invoice_id mới: {new_invoice_id}")
                return new_invoice_id
            logger.debug("Không tìm thấy hóa đơn nào, trả về invoice_id mặc định: INV001")
            return "INV001"  # Giá trị mặc định nếu không có hóa đơn nào
        except Exception as e:
            logger.error(f"Error getting max invoice_id: {e}")
            return "INV001"  # Trả về mặc định nếu có lỗi

    def get_products(self):
        """Lấy danh sách sản phẩm."""
        return list(self.products_collection.find({}, {"_id": 0}))

    def get_invoices(self):
        """Lấy danh sách hóa đơn."""
        return list(self.invoices_collection.find({}, {"_id": 0}))

    def search_products(self, search_text, search_criteria):
        """Tìm kiếm sản phẩm theo tiêu chí."""
        query = {}
        if search_criteria == "Product name":
            query["product_name"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Category":
            query["category"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Location number":
            query["location_number"] = {"$regex": search_text, "$options": "i"}
        return list(self.products_collection.find(query, {"_id": 0}))

    def search_invoices(self, search_text, search_criteria):
        """Tìm kiếm hóa đơn theo tiêu chí."""
        query = {}
        if search_criteria == "Invoice":
            query["invoice_id"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Invoice_Date":
            query["invoice_date"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Status":
            query["status"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Product":
            query["cart.product_name"] = {"$regex": search_text, "$options": "i"}
        elif search_criteria == "Price":
            query = {
                "$expr": {
                    "$gt": [
                        {"$size": {
                            "$filter": {
                                "input": "$cart",
                                "as": "item",
                                "cond": {
                                    "$regexMatch": {
                                        "input": {"$toString": "$$item.price"},
                                        "regex": str(search_text)
                                    }
                                }
                            }
                        }},
                        0
                    ]
                }
            }
        return list(self.invoices_collection.find(query, {"_id": 0}))

    def find_invoice(self, date, product_name):
        """Tìm hóa đơn theo invoice_id và product_name trong cart."""
        try:
            return self.invoices_collection.find_one(
                {
                    "invoice_date": date,
                    "cart.product_name": product_name
                },
                {"_id": 0}
            )
        except Exception as e:
            logger.error(f"Error finding invoice with date {date} and product {product_name}: {e}")
            return None

    def add_new_invoice(self, date, product_name, quantity, price, total_price):
        """Thêm hóa đơn mới với invoice_id tự động."""
        invoice_id = self.get_max_invoice_id()
        invoice_data = {
            "invoice_id": invoice_id,
            "invoice_date": date,
            "cart": [{
                "product_name": product_name,
                "quantity": quantity,
                "price": price,
            }],
            "total_price": total_price,
            "status": "prepare"
        }
        self.invoices_collection.insert_one(invoice_data)
        logger.info(f"Added new invoice with ID: {invoice_id}")
        return self.update_total_products()

    def update_existing_invoice(self, date, product_name, quantity, price, total_price):
        """Cập nhật hóa đơn đã tồn tại."""
        self.invoices_collection.update_one(
            {"invoice_date": date, "cart.product_name": product_name},
            {"$set": {"cart.$.quantity": quantity, "cart.$.price": price, "total_price": total_price}}
        )
        logger.info(f"Updated invoice for {product_name} on {date}")
        return self.update_total_products()

    def update_total_products(self):
        """Cập nhật tổng số lượng sản phẩm."""
        total_quantity = sum(
            sum(item["quantity"] for item in invoice.get("cart", []))
            for invoice in self.invoices_collection.find({}, {"cart": 1})
        )
        return total_quantity

    def delete_invoice(self, invoice_id, product_name, invoice_date):
        """Xóa một sản phẩm cụ thể trong cart của hóa đơn theo invoice_id, product_name và invoice_date."""
        try:
            # Tìm hóa đơn theo invoice_id
            invoice = self.invoices_collection.find_one({"invoice_id": invoice_id})
            if not invoice:
                logger.warning(f"Không tìm thấy hóa đơn với invoice_id '{invoice_id}' để xóa.")
                return False

            # Lọc bỏ sản phẩm cần xóa khỏi cart
            cart = invoice.get("cart", [])
            updated_cart = [
                item for item in cart
                if not (item.get("product_name") == product_name and invoice.get("invoice_date") == invoice_date)
            ]

            if updated_cart:
                # Nếu vẫn còn sản phẩm trong cart, cập nhật hóa đơn
                total_price = sum(item.get("total_price", 0) for item in updated_cart)
                self.invoices_collection.update_one(
                    {"invoice_id": invoice_id},
                    {
                        "$set": {
                            "cart": updated_cart,
                            "total_price": total_price
                        }
                    }
                )
                logger.info(f"Đã xóa sản phẩm '{product_name}' khỏi hóa đơn '{invoice_id}'.")
            else:
                # Nếu cart rỗng, xóa toàn bộ hóa đơn
                self.invoices_collection.delete_one({"invoice_id": invoice_id})
                logger.info(f"Cart rỗng, đã xóa toàn bộ hóa đơn '{invoice_id}'.")

            return True
        except Exception as e:
            logger.error(f"Lỗi khi xóa sản phẩm '{product_name}' trong hóa đơn '{invoice_id}': {str(e)}")
            raise

    def get_total_invoice_price(self):
        """Tính tổng giá trị của tất cả hóa đơn."""
        total_price = sum(
            invoice.get("total_price", 0)
            for invoice in self.invoices_collection.find({}, {"total_price": 1})
        )
        return total_price

    def add_new_invoice_full(self, invoice_data):
        self.db.invoices.insert_one(invoice_data)
        return self.update_total_products()

    def update_user(self, old_username, updated_data):
        """Cập nhật thông tin người dùng trong cơ sở dữ liệu"""
        try:
            result = self.users.update_one(
                {"username": old_username},
                {"$set": updated_data}
            )
            return result.modified_count > 0  # Trả về True nếu cập nhật thành công
        except Exception as e:
            logger.error(f"Error updating user {old_username}: {e}")
            return False

    def find_invoice_by_id(self, invoice_id):
        """Tìm hóa đơn theo invoice_id và loại bỏ trường _id."""
        try:
            return self.invoices_collection.find_one({"invoice_id": invoice_id}, {"_id": 0})
        except Exception as e:
            logger.error(f"Error finding invoice by ID {invoice_id}: {e}")
            return None

    def update_existing_invoice_full(self, invoice_id, invoice_data):
        """Cập nhật toàn bộ thông tin hóa đơn."""
        try:
            self.invoices_collection.update_one(
                {"invoice_id": invoice_id},
                {"$set": {
                    "cart": invoice_data["cart"],
                    "invoice_date": invoice_data["invoice_date"],
                    "total_price": invoice_data["total_price"],
                    "status": invoice_data["status"]
                }}
            )
            logger.info(f"Updated invoice {invoice_id} successfully.")
        except Exception as e:
            logger.error(f"Error updating invoice {invoice_id}: {e}")
            raise

    def update_invoice_status(self, invoice_id, status):
        """Cập nhật trạng thái của hóa đơn trong MongoDB."""
        try:
            result = self.invoices_collection.update_one(
                {"invoice_id": invoice_id},
                {"$set": {"status": status}}
            )
            if result.modified_count > 0:
                logger.info(f"Updated status of invoice {invoice_id} to {status}")
                return True
            else:
                logger.warning(f"No invoice found with ID {invoice_id} to update status")
                return False
        except Exception as e:
            logger.error(f"Error updating invoice status: {e}")
            raise

    def get_product_by_name(self, product_name):
        """Lấy thông tin sản phẩm theo tên từ collection products."""
        return self.products_collection.find_one({"product_name": product_name})

    def get_invoice_by_id(self, invoice_id):
        """Lấy hóa đơn theo invoice_id."""
        try:
            invoice = self.invoices_collection.find_one({"invoice_id": invoice_id})
            return invoice
        except Exception as e:
            logger.error(f"Error fetching invoice with ID {invoice_id}: {e}")
            return None

