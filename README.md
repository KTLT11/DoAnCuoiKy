# AdminExFnct

AdminExFnct là một ứng dụng giao diện người dùng (GUI) được xây dựng bằng PySide6, cho phép quản lý người dùng, nhà cung cấp, sản phẩm, hóa đơn, và tạo báo cáo chi tiết. Ứng dụng tích hợp các tính năng như biểu đồ doanh thu, top nhà cung cấp/sản phẩm, và thông tin thời tiết.

## I. Cài đặt

### Yêu cầu
- Python 3.8 hoặc cao hơn
- MongoDB (đã cài đặt và chạy)
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
  WEATHER_API_KEY=your_openweathermap_api_key
- Để lấy WEATHER_API_KEY, đăng ký tại OpenWeatherMap và tạo một API key.
## II. SỬ DỤNG
### 1. Chạy ứng dụng
- Hiện tại, dự án chưa có file main.py. Bạn cần tạo file main.py trong thư mục gốc với nội dung sau để khởi chạy ứng dụng:
    ```python
    from services.admin_service import AdminExFnct_Process
    from PySide6.QtWidgets import QApplication
    import sys
    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = AdminExFnct_Process()
        window.show()
        sys.exit(app.exec())
- Sau đó, chạy ứng dụng bằng lệnh:
    ```bash
    python main.py
### 2. Đăng nhập
- Sử dụng username và password hợp lệ (được lưu trong collection users) để đăng nhập vào ứng dụng.
### 3. Khám phá tính năng
- Tab Dashboard: Xem biểu đồ doanh thu, top nhà cung cấp, top sản phẩm, hoạt động gần đây, và thông tin thời tiết.
- Tab Account: Quản lý người dùng (thêm, cập nhật, xóa).
- Tab Supplier: Quản lý nhà cung cấp (thêm, cập nhật, xóa).
- Tab Inventory: Quản lý sản phẩm (thêm, cập nhật, xóa, nhập/xuất kho).
- Tab Invoice: Xem và cập nhật trạng thái hóa đơn, in hóa đơn dưới dạng PDF.
- Tab Report: Tạo biểu đồ tròn để phân tích phân bố nhà cung cấp và tồn kho, với tùy chọn lọc và xuất biểu đồ.
## III. TÍNH NĂNG CHÍNH
- Quản lý người dùng: Thêm, cập nhật, xóa người dùng với các vai trò khác nhau.
- Quản lý nhà cung cấp: Quản lý thông tin nhà cung cấp, bao gồm tự động tạo supplier_id và kiểm tra số điện thoại hợp lệ.
- Quản lý sản phẩm: Thêm, cập nhật, xóa sản phẩm; hỗ trợ nhập/xuất kho và tự động tạo product_id.
- Quản lý hóa đơn: Xem danh sách hóa đơn, cập nhật trạng thái, và in hóa đơn dưới dạng PDF.
- Báo cáo: Tạo biểu đồ tròn để phân tích phân bố nhà cung cấp và tồn kho, với các tùy chọn lọc theo danh mục, màu sắc, và góc bắt đầu; hỗ trợ xuất biểu đồ dưới dạng PNG.
- Dashboard:
  - Biểu đồ doanh thu theo tuần.
  - Top 5 nhà cung cấp theo số lượng sản phẩm.
  - Top 5 sản phẩm bán chạy trong tuần.
  - Danh sách các hoạt động gần đây (thêm sản phẩm, tạo hóa đơn).
  - Thông tin thời tiết tại thành phố được chỉ định (mặc định: Ho Chi Minh City).
## IV. CẤU TRÚC DỰ ÁN
- database/API_Admin.py: Chứa các phương thức để tương tác với cơ sở dữ liệu MongoDB.
- services/admin_service.py: Chứa logic chính của ứng dụng, bao gồm giao diện và xử lý sự kiện.
- gui/Admin_ui.py: Chứa giao diện người dùng được tạo bởi Qt Designer (giả định).
- services/admin_infor_dialog.py: Chứa dialog để hiển thị thông tin người dùng (giả định).
- requirements.txt: Liệt kê các thư viện cần thiết.
- README.md: Hướng dẫn cài đặt và sử dụng
## V. NGƯỜI ĐÓNG GÓP
- Nhóm 11
## VI. GIẤY PHÉP
- Dự án này được cấp phép dưới....
## VII. LIÊN HỆ
- Nếu bạn có câu hỏi hoặc cần hỗ trợ, vui lòng liên hệ qua email: khainn23406@st.uel.edu.vn.