from tavily import TavilyClient

tavily = TavilyClient(api_key="")

# Tìm kiếm thông thường
# response = tavily.search(query="Giá vàng hôm nay tại Việt Nam 2026", search_depth="basic")
response = tavily.search(query="Giá vàng hôm nay tại Việt Nam 2026", search_depth="advanced")
print("=== KẾT QUẢ TÌM KIẾM CƠ BẢN ===")
print(response)