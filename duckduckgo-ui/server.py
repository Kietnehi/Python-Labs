import warnings
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import theo đúng code gốc của bạn
# (Nếu bạn có file ddgs.py thì nó sẽ chạy dòng đầu, nếu không có thì tìm trong thư viện cài đặt)
try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS

# Tắt cảnh báo DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)
CORS(app) # Cho phép Frontend Next.js gọi API

# --- CÁC HÀM SEARCH (TUÂN THỦ LOGIC CỦA BẠN) ---
# Lưu ý: Thay vì print() ra màn hình console, mình return list() để trả dữ liệu về Frontend

def search_text(ddgs, query, max_results):
    return list(ddgs.text(query, max_results=max_results))

def search_news(ddgs, query, max_results):
    return list(ddgs.news(query, max_results=max_results))

def search_images(ddgs, query, max_results):
    return list(ddgs.images(query, max_results=max_results))

def search_videos(ddgs, query, max_results):
    return list(ddgs.videos(query, max_results=max_results))

def search_books(ddgs, query, max_results):
    # Dùng trực tiếp hàm books như code bạn đã test
    return list(ddgs.books(query, max_results=max_results))

# --- API ROUTE ---

@app.route('/api/search', methods=['GET'])
def search_api():
    # Lấy tham số từ URL
    query = request.args.get('q')
    search_type = request.args.get('type', 'text') # text, news, images, videos, books
    
    try:
        max_results = int(request.args.get('max_results', 5))
    except ValueError:
        max_results = 5

    if not query:
        return jsonify({'error': 'Thiếu từ khóa tìm kiếm (q)'}), 400

    # Log ra console để bạn theo dõi (Đã sửa lỗi maxResults -> max_results)
    print(f"🔍 Đang tìm kiếm: '{query}' | Loại: {search_type} | SL: {max_results}")

    results = []
    
    try:
        with DDGS() as ddgs:
            # Mapping request type sang đúng hàm của bạn
            if search_type == '1' or search_type == 'text':
                results = search_text(ddgs, query, max_results)
                
            elif search_type == '2' or search_type == 'news':
                results = search_news(ddgs, query, max_results)
                
            elif search_type == '3' or search_type == 'images':
                results = search_images(ddgs, query, max_results)
                
            elif search_type == '4' or search_type == 'videos':
                results = search_videos(ddgs, query, max_results)
                
            elif search_type == '5' or search_type == 'books':
                results = search_books(ddgs, query, max_results)
                
            else:
                # Mặc định
                results = search_text(ddgs, query, max_results)

        return jsonify(results)

    except Exception as e:
        print(f"❌ Lỗi Server: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Server đang chạy tại http://127.0.0.1:5000")
    # Giữ use_reloader=False để tránh lỗi restart vòng lặp trên Windows của bạn
    app.run(port=5000, debug=True, use_reloader=False)