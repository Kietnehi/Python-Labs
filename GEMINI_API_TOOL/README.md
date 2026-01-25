Dưới đây là một bản **README.md** hoàn chỉnh (bằng tiếng Việt) dựa trên mô tả bạn cung cấp. Bạn có thể copy trực tiếp vào file `README.md` trong thư mục `GEMINI_API_TOOL` và chỉnh sửa thêm nếu cần.

---

# GEMINI_API_TOOL

Thư mục **GEMINI_API_TOOL** chứa các công cụ và script phục vụ việc làm việc, thử nghiệm và xử lý dữ liệu liên quan đến **Google Gemini API** cùng một số tác vụ bổ trợ như bản đồ, tìm kiếm trích dẫn và phân tích dữ liệu.

## 📁 Cấu trúc thư mục

```
GEMINI_API_TOOL/
│
├── Code_Execution.ipynb
├── google_map.py
├── Search_Citation.py
└── sales.csv
```

## 📌 Mô tả các thành phần

### 1. `Code_Execution.ipynb`

* Notebook Jupyter dùng để chạy thử và minh họa các đoạn code liên quan đến Gemini API.
* Có thể bao gồm:

  * Ví dụ gọi API Gemini
  * Xử lý dữ liệu mẫu
  * Kiểm thử các script trong thư mục

### 2. `google_map.py`

* Script Python dùng để tương tác với **Google Maps API**.
* Mục đích có thể bao gồm:

  * Geocoding / Reverse geocoding
  * Lấy thông tin vị trí, bản đồ
  * Kết hợp Gemini API cho các tác vụ phân tích hoặc hỏi đáp theo vị trí

### 3. `Search_Citation.py`

* Script Python phục vụ tìm kiếm và tạo trích dẫn.
* Có thể sử dụng:

  * Gemini API
  * Hoặc các API tìm kiếm khác để lấy nguồn tham khảo (web, học thuật, tài liệu)

### 4. `sales.csv`

* File dữ liệu mẫu về **doanh số bán hàng**.
* Được dùng cho:

  * Phân tích dữ liệu
  * Minh họa trong `Code_Execution.ipynb`
  * Thử nghiệm khả năng xử lý dữ liệu của Gemini API

## ⚙️ Yêu cầu hệ thống

* Python 3.8+
* Jupyter Notebook (nếu sử dụng `Code_Execution.ipynb`)
* Các thư viện phổ biến:

  * `requests`
  * `pandas`
  * `googlemaps` (nếu dùng Google Maps API)
  * SDK / thư viện chính thức cho Gemini API (nếu có)

## 🔑 Thiết lập môi trường


1. Thiết lập biến môi trường cho API key:

   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   export GOOGLE_MAPS_API_KEY="your_google_maps_api_key_here"
   ```

## ▶️ Cách sử dụng

### Chạy notebook

```bash
jupyter notebook Code_Execution.ipynb
```

### Chạy script Google Maps

```bash
python google_map.py
```

### Chạy script tìm kiếm & trích dẫn

```bash
python Search_Citation.py
```

## 📊 Ví dụ ứng dụng

* Thử nghiệm gọi Gemini API để phân tích dữ liệu bán hàng trong `sales.csv`
* Kết hợp Gemini + Google Maps để hỏi đáp theo vị trí
* Tự động tìm kiếm nguồn tham khảo và tạo trích dẫn cho báo cáo

## 📝 Ghi chú

* Đây là thư mục phục vụ **thử nghiệm và nghiên cứu**, không phải hệ thống production.
* Hãy đảm bảo bảo mật API key và không commit trực tiếp vào repository công khai.

---

