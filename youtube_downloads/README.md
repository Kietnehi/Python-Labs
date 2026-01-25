
---

# 📘 Test_YouTube.ipynb – Công cụ đa năng làm việc với YouTube

Notebook **Test_YouTube.ipynb** là một bộ công cụ Python giúp bạn làm việc với nội dung YouTube một cách toàn diện:

* Lấy transcript (phụ đề) từ video YouTube (tiếng Việt, tiếng Anh, nhiều ngôn ngữ).
* Tải video, audio (MP3), phụ đề và playlist.
* Xem thông tin chi tiết của video.
* Cung cấp giao diện dòng lệnh (CLI) đơn giản để thao tác nhanh.

Notebook phù hợp cho các mục đích:

* Thu thập dữ liệu video phục vụ NLP / phân tích nội dung.
* Tải video / audio để học offline.
* Trích xuất phụ đề để dịch, tóm tắt hoặc huấn luyện mô hình.

---

## ✨ Tính năng chính

### 1. Lấy transcript (phụ đề) YouTube

* Sử dụng thư viện **youtube_transcript_api** và **yt_dlp**.
* Hỗ trợ:

  * Link đầy đủ và link rút gọn (youtu.be).
  * Nhiều ngôn ngữ (tiếng Việt, tiếng Anh, …).
* Có ví dụ:

  * Lấy transcript trực tiếp từ video.
  * Lưu transcript ra file `.txt`.

---

### 2. Tải video / audio / phụ đề YouTube

Thông qua class **YouTubeDownloader** (dựa trên `yt_dlp`):

* 🎥 Tải video với nhiều mức chất lượng khác nhau.
* 🎧 Tải **chỉ audio** và chuyển sang định dạng MP3.
* 📂 Tải **toàn bộ playlist**.
* 📝 Tải **phụ đề** với nhiều ngôn ngữ.
* ℹ️ Xem **thông tin chi tiết video**:

  * Tiêu đề
  * Kênh
  * Mô tả
  * Thời lượng
  * Danh sách định dạng (format) có sẵn

---

### 3. Hiển thị các định dạng tải về

* Liệt kê toàn bộ format video/audio mà YouTube cung cấp.
* Cho phép người dùng chọn format phù hợp (độ phân giải, codec, chỉ audio…).

---

### 4. Giao diện dòng lệnh (CLI)

Notebook cung cấp một **menu CLI đơn giản** để người dùng chọn chức năng:

* Tải video
* Tải audio (MP3)
* Tải playlist
* Tải phụ đề
* Xem thông tin video
* Hiển thị danh sách format

Phù hợp để sử dụng nhanh mà không cần chỉnh sửa nhiều code.

---

### 5. Một số cell hướng dẫn bổ sung (đang comment)

* Có cell hướng dẫn:

  * Tìm kiếm và lấy nội dung trang web bằng **DuckDuckGo**.
* Hiện tại các cell này đang bị comment, có thể mở ra để mở rộng chức năng crawl dữ liệu web.

---

## 🛠️ Yêu cầu môi trường

* Python >= 3.8
* Jupyter Notebook / JupyterLab

### Thư viện cần thiết

```bash
pip install youtube-transcript-api yt-dlp
```

(Tùy chọn thêm nếu dùng các cell mở rộng)

```bash
pip install duckduckgo-search requests beautifulsoup4
```

---

## 🚀 Cách sử dụng

### 1. Mở notebook

```bash
jupyter notebook Test_YouTube.ipynb
```

Hoặc mở bằng JupyterLab / VS Code.

---

### 2. Lấy transcript từ video

Ví dụ:

* Nhập link YouTube (đầy đủ hoặc rút gọn).
* Chọn ngôn ngữ (`vi`, `en`, …).
* Chạy cell để:

  * In transcript ra màn hình
  * Hoặc lưu transcript ra file `.txt`

---

### 3. Tải video / audio / phụ đề

Sử dụng class `YouTubeDownloader`:

* Tải video:

```python
downloader.download_video(url, quality="best")
```

* Tải audio MP3:

```python
downloader.download_audio(url)
```

* Tải playlist:

```python
downloader.download_playlist(playlist_url)
```

* Tải phụ đề:

```python
downloader.download_subtitle(url, lang="vi")
```

---

### 4. Sử dụng menu CLI

Chạy cell menu, sau đó chọn chức năng trong danh sách:

```
1. Tải video
2. Tải audio (MP3)
3. Tải playlist
4. Tải phụ đề
5. Xem thông tin video
6. Xem danh sách định dạng
0. Thoát
```

Chỉ cần nhập số tương ứng và làm theo hướng dẫn.

---

## 📂 Cấu trúc notebook (tóm tắt)

* Cell cài đặt & import thư viện
* Các hàm lấy transcript (youtube_transcript_api, yt_dlp)
* Class `YouTubeDownloader`:

  * Download video
  * Download audio
  * Download playlist
  * Download subtitle
  * Get video info
  * List formats
* Menu CLI
* Cell mở rộng (DuckDuckGo, crawl web – đang comment)

---

## ⚠️ Lưu ý

* Việc tải video / audio từ YouTube cần tuân thủ **Điều khoản dịch vụ của YouTube** và luật bản quyền tại quốc gia của bạn.
* Chỉ nên sử dụng cho mục đích:

  * Cá nhân
  * Học tập / nghiên cứu
* Không khuyến khích sử dụng cho mục đích thương mại trái phép.

---

## 📌 Gợi ý mở rộng

Bạn có thể phát triển thêm:

* Tự động dịch transcript (Google Translate / OpenAI API).
* Tóm tắt nội dung video từ transcript.
* Lưu transcript dưới dạng JSON / CSV.
* Kết hợp với crawl web để xây dựng bộ dữ liệu lớn.

---

## 📜 License

Notebook này sử dụng các thư viện mã nguồn mở:

* `youtube-transcript-api`
* `yt-dlp`

Vui lòng tuân thủ license của từng thư viện khi sử dụng và phân phối lại.


