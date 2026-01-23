# DDGS - Dux Distributed Global Search

Thư viện Python cho **meta search** (tổng hợp kết quả từ nhiều công cụ tìm kiếm).

## Cài đặt

```bash
pip install -U ddgs
```

## Tính năng chính

### 1. API Server với MCP Integration
Chạy server FastAPI với Model Context Protocol (MCP):

**Docker Compose:**
```bash
git clone https://github.com/deedy5/ddgs && cd ddgs
docker-compose up --build
```

**Bash:**
```bash
git clone https://github.com/deedy5/ddgs && cd ddgs
chmod +x start_api.sh
./start_api.sh
```

**Endpoints:**
- `http://localhost:8000/mcp` - HTTP transport
- `http://localhost:8000/sse` - SSE transport
- `http://localhost:8000/docs` - API documentation
- `http://localhost:8000/health` - Health check

### 2. CLI Version
```bash
ddgs --help
```

### 3. Các Engine hỗ trợ

| Function | Available Backends |
|----------|-------------------|
| `text()` | bing, brave, duckduckgo, google, grokipedia, mojeek, yandex, yahoo, wikipedia |
| `images()` | duckduckgo |
| `videos()` | duckduckgo |
| `news()` | bing, duckduckgo, yahoo |
| `books()` | annasarchive |

## Sử dụng cơ bản

### Khởi tạo
```python
from ddgs import DDGS

ddgs = DDGS()
```

### Text Search
```python
results = ddgs.text(
    query="python programming",
    region="us-en",
    safesearch="moderate",
    max_results=10
)
```

### Image Search
```python
images = ddgs.images(
    query="butterfly",
    region="us-en",
    color="Monochrome",
    max_results=10
)
```

### Video Search
```python
videos = ddgs.videos(
    query="cars",
    region="us-en",
    duration="medium",
    resolution="high"
)
```

### News Search
```python
news = ddgs.news(
    query="sun",
    region="us-en",
    timelimit="m"
)
```

### Book Search
```python
books = ddgs.books(
    query="sea wolf jack london",
    max_results=10
)
```

## Cấu hình MCP điển hình
```json
{
  "mcpServers": {
    "ddgs-search": {
      "url": "http://localhost:8000/sse",
      "disabled": false,
      "alwaysAllow": []
    }
  }
}
```

## Thông số kỹ thuật
- **Python**: >= 3.10
- **License**: MIT
- **Homepage**: [GitHub Repository](https://github.com/deedy5/ddgs)

## Lưu ý
Thư viện này được phát triển cho mục đích giáo dục. Kết quả tìm kiếm phụ thuộc vào các backend được sử dụng.