from ddgs import DDGS

ddgs = DDGS()

results = ddgs.images("con mèo", max_results=5)

print("=== IMAGE SEARCH ===\n")

for i, r in enumerate(results, start=1):
    print(f"Hình {i}:")
    print("Tiêu đề:", r["title"])
    print("Link ảnh:", r["image"])
    print("Trang nguồn:", r["url"])
    print("-" * 50)
