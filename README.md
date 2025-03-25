# AdminExFnct

AdminExFnct là một ứng dụng giao diện người dùng (GUI) được xây dựng bằng PySide6, cho phép quản lý người dùng, nhà cung cấp, sản phẩm, hóa đơn, và tạo báo cáo chi tiết. Ứng dụng tích hợp các tính năng như biểu đồ doanh thu, top nhà cung cấp/sản phẩm, và thông tin thời tiết.

## I. Cài đặt

### Yêu cầu
- Python >=3.10
- pyside6. pip install pyside6
- Thư viện môi trường dotenv. pip install dotenv
- MongoDB (đã cài đặt và chạy) pip install pymongo
- API key từ OpenWeatherMap (cho tính năng thời tiết)

### Bước cài đặt
1. **Clone kho lưu trữ**:
   ```bash
   git clone https://github.com/yourusername/AdminExFnct.git
   cd AdminExFnct
2. **Cài đặt các thư viện cần thiết**:
   ```bash 
    pip install -r requirements.txt

3. **Thiết lập cơ sở dữ liệu MongoDB**:
Đảm bảo MongoDB đã được cài đặt và đang chạy trên máy của bạn.
Tạo cơ sở dữ liệu với các collection sau:
- users: Lưu thông tin người dùng (username, password, role).
- suppliers: Lưu thông tin nhà cung cấp (supplier_id, category, supplier_name, contact_number, status).
- products: Lưu thông tin sản phẩm (product_id, product_name, category, current_stock, supplier_id, price_per_unit, cost_per_unit, location_number).
- invoices: Lưu thông tin hóa đơn (invoice_id, cart, invoice_date, total_price, status).
4. **Cấu hình biến môi trường**:
- Tạo file .env trong thư mục gốc của dự án với nội dung sau:
  ```text
  MONGO_URL=mongodb+srv://boygia757:123@cluster0.ur2jr.mongodb.net/
  MONGO_DB=group11
  MONGO_COLLECTION=doan
  WEATHER_API_KEY=69ada8d29fd956854bb9c76ed1024e4a
- Để lấy WEATHER_API_KEY, đăng ký tại OpenWeatherMap và tạo một API key.
## II. SỬ DỤNG
### 1. Chạy ứng dụng
- Hiện tại, dự án chưa có file main.py. Bạn cần tạo file main.py trong thư mục gốc với nội dung sau để khởi chạy ứng dụng:
    ```python
    import sys
    from PySide6.QtWidgets import QApplication
    from services.login_service import LoginWindow, AdminWindow, UserWindow


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        login_window = LoginWindow()
        login_window.show()
        sys.exit(app.exec())
- Sau đó, chạyquynh123
### 3. Khám phá tính năng
**ADMIN**
- Tab Dashboard: Xem biểu đồ doanh thu, top nhà cung cấp, top sản phẩm, hoạt động gần đây, và thông tin thời tiết.
- Tab Account: Quản lý người dùng (thêm, cập nhật, xóa).
- Tab Supplier: Quản lý nhà cung cấp (thêm, cập nhật, xóa).
- Tab Inventory: Quản lý sản phẩm (thêm, cập nhật, xóa, nhập/xuất kho).
- Tab Invoice: Xem và cập nhật trạng thái hóa đơn, in hóa đơn dưới dạng PDF.
- Tab Report: Tạo biểu đồ tròn để phân tích phân bố nhà cung cấp và tồn kho, với tùy chọn lọc và xuất biểu đồ.

**USER**
- Tab Inventory: Quản lý sản phẩm (search sản phẩm theo tiêu chí)
- Tab Invoice: Tạo, xem và cập nhật thông tin hóa đơn, xem trước hóa đơn và in hóa đơn về máy dướ dạng PDF
- Tab Report: Tạo biểu đồ phản ánh doanh thu bán hàng, top các sản phẩm bán chạy và số lượng hàng tồn kho
- Tab Dashboard (User): giao diện
## III. TÍNH NĂNG CHÍNH
**ADMIN**
- Quản lý Account: Thêm, cập nhật, xóa người dùng với các vai trò khác nhau.
- Quản lý Supplier: Quản lý thông tin nhà cung cấp, bao gồm tự động tạo supplier_id và kiểm tra số điện thoại hợp lệ.
- Quản lý Inventory Function: Thêm, cập nhật, xóa sản phẩm; hỗ trợ nhập/xuất kho và tự động tạo product_id.
- Quản lý Tracking Invoice: Xem danh sách hóa đơn, cập nhật trạng thái, và in hóa đơn dưới dạng PDF.
- Report: Tạo biểu đồ tròn để phân tích phân bố nhà cung cấp và tồn kho, với các tùy chọn lọc theo danh mục, màu sắc, và góc bắt đầu; hỗ trợ xuất biểu đồ dưới dạng PNG.
- Dashboard:
  - Biểu đồ doanh thu theo tuần 
  - Top 5 nhà cung cấp theo số lượng sản phẩm.
  - Top 5 sản phẩm bán chạy trong tuần.
  - Danh sách các hoạt động gần đây (thêm sản phẩm, tạo hóa đơn).
  - Thông tin thời tiết tại thành phố được chỉ định (mặc định: Ho Chi Minh City).
  
**USER**
- Trang chủ Dashboard: giao diện
- Trang Report: Thể hiện các biểu đồ Total Revenue, Total product, Stock giúp người dùng có cái nhìn tổng quan về các số liệu.
- Inventory Overview: Giúp người dùng quản lý các sản phẩm của công ty, tìm kiếm thông tin sản phẩm theo các tiêu chí: Product name, Categorry, Location number.
-  Invoice Management: Giúp người dùng quản lý hóa đơn, tìm kiếm hóa đơn theo nhiều tiêu chí, tạo hóa đơn, xóa hóa đơn và in bill. Ngoài ra còn lưu bản pdf hóa đơn về thiết bị.
## IV. CẤU TRÚC DỰ ÁN
- database/api.py, API_Admin.py, API_Login.py, API_User.py : Chứa các phương thức để tương tác với cơ sở dữ liệu MongoDB.
- gui/ admin_infor.py, admin_infor_rc.py, Admin_rc.py, Admin_ui.py, login_rc.py, login_ui.py, User_rc.py, User_ui.py: Chứa giao diện người dùng được tạo bởi Qt Designer.
- services/admin_infor_dialog.py, admin_service.py, login_service.py, user_service.py: Chứa logic chính của ứng dụng, bao gồm giao diện và xử lý sự kiện.
- .env
- main.py
- requirements.txt: Liệt kê các thư viện cần thiết.
- README.md: Hướng dẫn cài đặt và sử dụng
## V. NGƯỜI ĐÓNG GÓP
- Nhóm 11
## VI. GIẤY PHÉP
- Dự án này được cấp phép dưới....
## VII. LIÊN HỆ
- Nếu bạn có câu hỏi hoặc cần hỗ trợ, vui lòng liên hệ qua email: khainn23406@st.uel.edu.vn.
