from ddgs import DDGS

ddgs = DDGS()

results = ddgs.news("bóng đá Việt Nam", max_results=5)

print("=== NEWS SEARCH ===\n")

for i, r in enumerate(results, start=1):
    print(f"Kết quả {i}:")
    print("Ngày:", r["date"])
    print("Tiêu đề:", r["title"])
    print("Nguồn:", r["source"])
    print("Link:", r["url"])
    print("Tóm tắt:", r["body"])
    print("-" * 50)
