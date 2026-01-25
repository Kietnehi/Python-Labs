import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import re
import time

def get_manual_map(url):
    """
    Tìm và trả về danh sách các URL từ sitemap.xml hoặc bằng cách crawl trang web
    
    Args:
        url (str): URL của website cần map
    
    Returns:
        list: Danh sách các URL tìm thấy
    """
    print(f"🔍 Đang tìm Map thủ công cho: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    links_found = set()
    domain = urlparse(url).netloc
    
    # Chuẩn hóa URL (thêm schema nếu thiếu)
    if not urlparse(url).scheme:
        url = 'https://' + url
    
    # --- CÁCH 1: Thử tìm trong các file sitemap (Chuẩn SEO) ---
    sitemap_paths = [
        "/sitemap.xml",
        "/sitemap_index.xml",
        "/sitemap-index.xml",
        "/sitemap.php",
        "/sitemap.txt",
        "/sitemap.xml.gz"
    ]
    
    for path in sitemap_paths:
        sitemap_url = urljoin(url, path)
        try:
            print(f"  ↳ Đang thử: {sitemap_url}")
            response = requests.get(sitemap_url, headers=headers, timeout=15, allow_redirects=True)
            
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '').lower()
                
                if 'xml' in content_type or 'text/xml' in content_type:
                    print(f"✅ Tìm thấy file sitemap: {sitemap_url}")
                    
                    # Parse sitemap XML
                    soup = BeautifulSoup(response.content, 'lxml-xml')
                    
                    # Tìm tất cả URL trong sitemap (xử lý cả sitemap index)
                    urls = []
                    
                    # Tìm trong <loc> tags
                    loc_tags = soup.find_all('loc')
                    if loc_tags:
                        urls = [loc.text.strip() for loc in loc_tags]
                    else:
                        # Thử tìm trong <url> tags
                        url_tags = soup.find_all('url')
                        for url_tag in url_tags:
                            loc = url_tag.find('loc')
                            if loc:
                                urls.append(loc.text.strip())
                    
                    # Lọc các URL cùng domain
                    for found_url in urls:
                        parsed_url = urlparse(found_url)
                        if parsed_url.netloc == domain or not parsed_url.netloc:
                            # Chuẩn hóa URL
                            normalized_url = urlunparse(parsed_url._replace(
                                fragment='',  # Bỏ fragment (#)
                                query=''      # Có thể giữ query nếu muốn, hoặc bỏ
                            ))
                            links_found.add(normalized_url)
                    
                    if links_found:
                        print(f"  ↳ Tìm thấy {len(links_found)} URL từ sitemap")
                        return sorted(list(links_found))
                        
        except requests.exceptions.RequestException as e:
            continue
        except Exception as e:
            print(f"  ↳ Lỗi khi xử lý {sitemap_url}: {str(e)[:50]}...")
            continue
    
    # --- CÁCH 2: Cào trực tiếp các link từ trang chủ ---
    print("⚠️ Không tìm thấy sitemap, đang quét link trực tiếp từ trang chủ...")
    
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tìm tất cả các thẻ có href
        for tag in soup.find_all(['a', 'link'], href=True):
            href = tag['href'].strip()
            
            # Bỏ qua các link không cần thiết
            if href.startswith(('javascript:', 'mailto:', 'tel:', '#', 'data:')):
                continue
            
            # Chuyển link tương đối thành link tuyệt đối
            full_url = urljoin(url, href)
            
            # Parse và chuẩn hóa URL
            parsed = urlparse(full_url)
            
            # Chỉ lấy các link cùng domain
            if parsed.netloc == domain:
                # Chuẩn hóa URL
                normalized_url = urlunparse(parsed._replace(
                    fragment='',  # Bỏ fragment
                    path=parsed.path.rstrip('/') or '/'  # Chuẩn hóa path
                ))
                links_found.add(normalized_url)
        
        # Thử tìm trong robots.txt
        robots_url = urljoin(url, "/robots.txt")
        try:
            robots_response = requests.get(robots_url, headers=headers, timeout=10)
            if robots_response.status_code == 200:
                # Tìm Sitemap directive trong robots.txt
                for line in robots_response.text.split('\n'):
                    if line.lower().startswith('sitemap:'):
                        sitemap_url = line.split(':', 1)[1].strip()
                        print(f"  ↳ Tìm thấy sitemap trong robots.txt: {sitemap_url}")
                        # Có thể thêm logic để parse sitemap này
        except:
            pass
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi kết nối: {e}")
    except Exception as e:
        print(f"❌ Lỗi khi xử lý trang: {e}")
    
    result = sorted(list(links_found))
    print(f"  ↳ Tổng cộng tìm thấy {len(result)} URL")
    return result

# --- Hàm bổ trợ để lưu kết quả ---
def save_results_to_file(urls, filename="website_map.txt"):
    """Lưu kết quả vào file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Website Map - Generated at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*80 + "\n\n")
        for i, url in enumerate(urls, 1):
            f.write(f"{i:3d}. {url}\n")
    print(f"💾 Kết quả đã được lưu vào file: {filename}")

# --- CHẠY THỬ ---
if __name__ == "__main__":
    # Test với một số website
    test_urls = [
        "https://docs.tavily.com",
        # "https://example.com",
        # "google.com"  # Cũng xử lý được URL không có scheme
    ]
    
    for target in test_urls:
        print("\n" + "="*80)
        print(f"Bắt đầu mapping: {target}")
        print("="*80)
        
        try:
            map_results = get_manual_map(target)
            
            if map_results:
                print(f"\n✅ Kết quả Map (Tìm thấy {len(map_results)} link):")
                for i, link in enumerate(map_results[:20], 1):  # Hiển thị 20 link đầu
                    print(f"{i:3d}. {link}")
                
                if len(map_results) > 20:
                    print(f"... và {len(map_results) - 20} link nữa")
                
                # Lưu toàn bộ kết quả vào file
                domain = urlparse(target).netloc or target
                filename = f"{domain.replace('.', '_')}_map.txt"
                save_results_to_file(map_results, filename)
            else:
                print("❌ Không tìm thấy link nào!")
                
        except KeyboardInterrupt:
            print("\n⏹️ Đã dừng bởi người dùng")
            break
        except Exception as e:
            print(f"❌ Lỗi không xác định: {e}")