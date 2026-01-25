import os
from dotenv import load_dotenv
from tavily import TavilyClient

# 1. Cấu hình
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(api_key=TAVILY_API_KEY)

def explore_website_structure(target_url):
    print(f"🌐 Đang quét sơ đồ website: {target_url} ...")
    
    try:
        # Gọi hàm map để lấy danh sách URL nội bộ
        # Lưu ý: Map hoạt động tốt nhất với domain gốc hoặc trang docs
        response = tavily.map(url=target_url)
        
        # Cập nhật 2026: Kết quả thường nằm trong 'results'
        urls = response.get('results', [])
        
        if not urls:
            print("⚠️ Không tìm thấy URL nào hoặc Website chặn quyền truy cập Map.")
            return

        print(f"✅ Tìm thấy tổng cộng: {len(urls)} đường dẫn nội bộ.")
        print("-" * 30)
        
        # Phân loại và hiển thị 10 URL đầu tiên
        for i, url in enumerate(urls[:10], 1):
            print(f"{i}. {url}")
            
        if len(urls) > 10:
            print(f"... và {len(urls) - 10} đường dẫn khác.")

    except Exception as e:
        print(f"❌ Lỗi khi thực hiện Map: {e}")

if __name__ == "__main__":
    # Test với một số website phổ biến (nên dùng trang docs hoặc blog)
    test_url = "https://docs.tavily.com" 
    explore_website_structure(test_url)