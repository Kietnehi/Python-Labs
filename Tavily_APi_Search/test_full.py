import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load file .env
load_dotenv()

# Lấy biến môi trường
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    print("❌ Lỗi: Chưa tìm thấy TAVILY_API_KEY trong file .env")
else:
    print("✅ API KEY đã sẵn sàng:", TAVILY_API_KEY[:10] + "...")

# Khởi tạo Client
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# --- BLOCK 1: SMART SEARCH ---
def test_search():
    print("\n--- 1. TESTING SMART SEARCH ---")
    response = tavily.search(
        query="Sự kiện công nghệ nổi bật nhất tháng 1/2026",
        search_depth="advanced",
        max_results=3,
        include_answer=True,
        topic="general"
    )
    print(f"Câu trả lời nhanh: {response.get('answer')}")
    for r in response['results']:
        print(f"- {r['title']}: {r['url']}")

# --- BLOCK 2: CONTEXT EXTRACTION (Đã sửa để lấy nội dung sạch hơn) ---
def test_extract():
    print("\n--- 2. TESTING EXTRACT CONTENT ---")
    # Sử dụng một trang báo thay vì Wikipedia để tránh mã rác navigation
    urls = ["https://vnexpress.net/ai-chuyen-biet-va-robot-hinh-nguoi-xu-huong-cong-nghe-2026-4999739.html"]
    response = tavily.extract(urls=urls)
    
    raw_content = response['results'][0].get('raw_content', 'Không lấy được nội dung')
    # Lọc bỏ các dòng menu ngắn hoặc icon điều hướng (thường dưới 30 ký tự)
    lines = [line.strip() for line in raw_content.split('\n') if len(line.strip()) > 50]
    clean_content = "\n".join(lines[:3]) # Lấy 3 đoạn văn chính đầu tiên
    
    print(f"Nội dung sạch trích xuất:\n{clean_content}...")

# --- BLOCK 3: RESEARCH (Thay thế qna_search để hết báo lỗi Deprecation) ---
def test_research():
    print("\n--- 3. TESTING RESEARCH (OFFICIAL 2026) ---")
    try:
        # Thay vì dùng qna_search (đã cũ), dùng search với include_answer=True 
        # và search_depth="advanced" để có kết quả tương đương nhưng chi tiết hơn.
        response = tavily.search(
            query="So sánh chi tiết DeepSeek-V3 và GPT-5",
            search_depth="advanced",
            include_answer=True,
            max_results=5
        )
        print(f"Kết quả nghiên cứu tổng hợp: {response.get('answer')}")
    except Exception as e:
        print(f"Lỗi Block 3: {e}")

# --- BLOCK 4: SITE MAPPING (Sửa lỗi danh sách rỗng []) ---
def test_map():
    print("\n--- 4. TESTING SITE MAP ---")
    # Thử với domain chính thức để đảm bảo có kết quả (một số subdomain có thể chặn crawl)
    response = tavily.map(url="https://tavily.com")
    
    # Cấu trúc mới 2026: Trả về kết quả trong key 'results'
    urls = response.get('results', []) 
    if not urls:
        # Dự phòng cho các phiên bản cũ hơn
        urls = response.get('result', response.get('map', []))
        
    print(f"Các trang tìm thấy: {urls[:5]}") 

# --- BLOCK 5: SMART CRAWL ---
def test_crawl():
    print("\n--- 5. TESTING SMART CRAWL ---")
    try:
        # Sử dụng tham số chính xác để quét trong một domain
        response = tavily.search(
            query="API documentation",
            include_domains=["docs.tavily.com"],
            search_depth="advanced"
        )
        print(f"Số lượng trang đã tìm (crawl) từ domain: {len(response['results'])}")
        for r in response['results'][:2]:
            print(f"  + {r['url']}")
    except Exception as e:
        print(f"Lỗi Block 5: {e}")

# --- THỰC THI TEST ---
if __name__ == "__main__":
    try:
        test_search()
        test_extract()
        test_research()
        test_map()
        test_crawl()
    except Exception as e:
        print(f"\n⚠️ Lỗi hệ thống: {e}")