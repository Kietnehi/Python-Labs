# Translate — Dịch Văn Bản Đa Ngôn Ngữ

Folder này chứa các script Python để **dịch văn bản sang nhiều ngôn ngữ** bằng cách sử dụng Google Translate thông qua các thư viện khác nhau (`googletrans`, `deep-translator`, `langdetect`). Không cần API key trả phí.

---

## Cấu trúc file

| File | Mô tả |
|------|-------|
| `google_trans.py` | Dịch văn bản sang toàn bộ ngôn ngữ dùng thư viện `googletrans` (async) |
| `deep_translators.py` | Dịch văn bản sang toàn bộ ngôn ngữ dùng `deep-translator` + `langdetect` |
| `deep_translators_api.py` | Tương tự `deep_translators.py` nhưng dùng `single_detection` của `deep-translator` để phát hiện ngôn ngữ |
| `support_languages.py` | Xuất danh sách ngôn ngữ được hỗ trợ ra 2 file `.txt` |
| `languages_googletrans.txt` | Danh sách mã + tên ngôn ngữ của thư viện `googletrans` |
| `languages_deep_translator.txt` | Danh sách mã + tên ngôn ngữ của thư viện `deep-translator` |

---

## Mô tả chi tiết từng file

### `google_trans.py`
- Sử dụng **`googletrans`** với cú pháp **async/await**.
- Tự động **phát hiện ngôn ngữ gốc** (auto-detect) của văn bản đầu vào.
- Dịch sang toàn bộ các ngôn ngữ trong `googletrans.LANGUAGES` (~100+ ngôn ngữ).
- Có delay `0.05s` giữa mỗi lần dịch để tránh bị Google chặn IP.

### `deep_translators.py`
- Sử dụng **`deep-translator`** + **`langdetect`**.
- Dùng `langdetect.detect()` để nhận diện ngôn ngữ gốc chính xác.
- Dịch sang toàn bộ ngôn ngữ được `deep-translator` hỗ trợ (~160+ ngôn ngữ).
- Có delay `0.05s` giữa mỗi lần dịch.

### `deep_translators_api.py`
- Tương tự `deep_translators.py` nhưng dùng **`single_detection`** của `deep-translator` thay vì `langdetect`.
- Xử lý trường hợp phát hiện trả về `'auto'` bằng cách fallback sang `'en'`.
- Delay `0.1s` để bảo vệ khỏi bị Google rate-limit.

### `support_languages.py`
- Tiện ích để **xuất danh sách ngôn ngữ** ra file `.txt`.
- Tạo ra 2 file:
  - `languages_googletrans.txt` — danh sách ngôn ngữ của `googletrans`
  - `languages_deep_translator.txt` — danh sách ngôn ngữ của `deep-translator`
- Hữu ích khi cần tra cứu mã ngôn ngữ (vd: `vi`, `en`, `ja`, `zh-cn`).

---

## Cài đặt thư viện

```bash
pip install googletrans==4.0.0-rc1
pip install deep-translator
pip install langdetect
```

---

## Cách chạy

```bash
# Dịch dùng googletrans (async)
python google_trans.py

# Dịch dùng deep-translator + langdetect
python deep_translators.py

# Dịch dùng deep-translator + single_detection
python deep_translators_api.py

# Xuất danh sách ngôn ngữ hỗ trợ ra file .txt
python support_languages.py
```

---

## Output mẫu

```
======================================================================
[*] VĂN BẢN GỐC: Hello, I am learning AI and Python.
[*] NGÔN NGỮ PHÁT HIỆN: English (en)
[*] Đang chuẩn bị dịch sang 160 ngôn ngữ...
======================================================================
Mã       | Tên Ngôn Ngữ         | Bản Dịch
----------------------------------------------------------------------
vi       | Vietnamese           | Xin chào, tôi đang học AI và Python.
ja       | Japanese             | こんにちは、私はAIとPythonを学んでいます。
zh-CN    | Chinese (Simplified) | 你好，我正在学习AI和Python。
...
```

---

## Lưu ý

- Tất cả script đều dùng **Google Translate miễn phí** (không cần API key).
- Tránh gửi quá nhiều yêu cầu trong thời gian ngắn để không bị chặn IP — các script đã có sẵn `sleep` delay.
- Không đặt tên file trùng với tên thư viện (vd: không đặt tên file là `deep_translator.py` hay `googletrans.py`).
