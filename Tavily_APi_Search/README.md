
---
# Tavily_API_Search

Thư mục **Tavily_API_Search** chứa các script Python dùng để làm việc với **Tavily API**, phục vụ cho các tác vụ:

* Tìm kiếm web (cơ bản & nâng cao)
* Crawl dữ liệu từ website
* Trích xuất thông tin từ nội dung web
* Tự động hóa quy trình nghiên cứu
* Kiểm thử toàn bộ chức năng của Tavily API

Mục tiêu là xây dựng một workflow hoàn chỉnh cho **web search – crawling – extraction – research automation**.

---

## 📁 Cấu trúc thư mục

```
Tavily_API_Search/
│
├── basic_or_advance_search.py   # Tìm kiếm cơ bản và nâng cao
├── crawl.py                    # Crawl nội dung từ các URL
├── extract.py                  # Trích xuất thông tin từ dữ liệu crawl
├── research.py                 # Tự động hóa quy trình nghiên cứu
├── test_full.py                # Kiểm thử đầy đủ các chức năng Tavily API
├── test_map.py                 # Kiểm thử tìm kiếm theo vị trí / bản đồ
└── README.md                   # Tài liệu hướng dẫn
```

---

## 📄 Mô tả chi tiết các file

### 🔹 `basic_or_advance_search.py`

Script thực hiện:

* Tìm kiếm cơ bản (basic search) với Tavily API
* Tìm kiếm nâng cao (advanced search) với các tham số mở rộng

Chức năng chính:

* Gửi query tìm kiếm lên Tavily
* Nhận và hiển thị danh sách kết quả
* Hỗ trợ cấu hình số lượng kết quả, bộ lọc, nguồn dữ liệu

Phù hợp cho:

* Tra cứu thông tin nhanh
* So sánh kết quả tìm kiếm cơ bản và nâng cao

---

### 🔹 `crawl.py`

Script dùng để:

* Thu thập (crawl) nội dung từ các URL
* Lấy HTML hoặc văn bản của trang web
* Chuẩn bị dữ liệu cho bước trích xuất

Phù hợp khi:

* Đã có danh sách URL từ kết quả tìm kiếm
* Cần thu thập dữ liệu hàng loạt

---

### 🔹 `extract.py`

Script dùng để:

* Trích xuất thông tin quan trọng từ nội dung đã crawl
* Chuyển dữ liệu thô (HTML / text) thành dữ liệu có cấu trúc

Ví dụ thông tin trích xuất:

* Tiêu đề bài viết
* Mô tả ngắn
* Nội dung chính liên quan đến chủ đề

Ứng dụng:

* Tổng hợp dữ liệu nghiên cứu
* Phân tích nội dung tự động
* Xây dựng tập dữ liệu cho AI

---

### 🔹 `research.py`

Script tự động hóa quy trình **research**:

* Gửi yêu cầu nghiên cứu lên Tavily API
* Theo dõi trạng thái xử lý (polling)
* Lấy kết quả nghiên cứu khi hoàn tất

Phù hợp cho:

* Nghiên cứu chủ đề lớn
* Xây dựng hệ thống phân tích thông tin
* Chatbot / trợ lý nghiên cứu

---

### 🔹 `test_full.py`

Script kiểm thử toàn diện Tavily API:

* Kiểm tra API Key
* Thử nghiệm tìm kiếm, crawl, extract
* Hiển thị và đánh giá kết quả

Mục đích:

* Debug khi mới cấu hình API
* Đảm bảo tất cả chức năng hoạt động ổn định

---

### 🔹 `test_map.py`

Script kiểm thử chức năng tìm kiếm liên quan đến **bản đồ / vị trí địa lý**:

* Tìm kiếm theo khu vực
* Truy vấn dữ liệu gắn với vị trí
* Minh họa location-based search

Phù hợp khi:

* Làm việc với dữ liệu địa lý
* Xây dựng ứng dụng tìm kiếm theo khu vực

---

## ⚙️ Yêu cầu hệ thống

* Python 3.8 trở lên
* Một số thư viện phổ biến:

```bash
pip install requests python-dotenv
```

* Tài khoản và **API Key của Tavily**

---

## 🔑 Cấu hình Tavily API Key

### Cách 1: Dùng biến môi trường

Linux / macOS:

```bash
export TAVILY_API_KEY="YOUR_API_KEY"
```

Windows (PowerShell):

```powershell
setx TAVILY_API_KEY "YOUR_API_KEY"
```

---

### Cách 2: Dùng file `.env`

Tạo file `.env` trong thư mục gốc:

```
TAVILY_API_KEY=YOUR_API_KEY
```

---

## ▶️ Cách sử dụng

### Tìm kiếm cơ bản / nâng cao

```bash
python basic_or_advance_search.py
```

---

### Crawl dữ liệu

```bash
python crawl.py
```

---

### Trích xuất thông tin

```bash
python extract.py
```

---

### Chạy workflow nghiên cứu

```bash
python research.py
```

---

### Kiểm thử toàn bộ chức năng

```bash
python test_full.py
```

---

### Kiểm thử tìm kiếm theo bản đồ / vị trí

```bash
python test_map.py
```

---

## 🔄 Quy trình gợi ý (Workflow mẫu)

Một quy trình tiêu biểu:

1. Dùng `basic_or_advance_search.py` để tìm kiếm chủ đề
2. Lấy danh sách URL từ kết quả
3. Dùng `crawl.py` để thu thập nội dung
4. Dùng `extract.py` để trích xuất dữ liệu quan trọng
5. (Tuỳ chọn) Dùng `research.py` để tự động hóa nghiên cứu
6. Dùng `test_full.py` để kiểm tra toàn bộ hệ thống

---

## 📌 Lưu ý

* Không công khai API Key
* Giới hạn số lượng request để tránh vượt quota
* Một số tính năng nâng cao có thể yêu cầu gói Tavily trả phí

---

## 🤝 Đóng góp

Bạn có thể đóng góp bằng cách:

* Thêm ví dụ sử dụng cho từng script
* Tối ưu tốc độ crawl / extract
* Bổ sung logging và xử lý lỗi

---

## 📜 Giấy phép

Vui lòng xem file LICENSE (nếu có) để biết thông tin chi tiết.

---

