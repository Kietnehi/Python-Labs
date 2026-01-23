from ddgs import DDGS

ddgs = DDGS()

results = ddgs.books("harry potter", max_results=5)

print("=== BOOK SEARCH ===\n")

for i, r in enumerate(results, start=1):
    print(f"Sách {i}:")
    print("Tên:", r["title"])
    print("Tác giả:", r["author"])
    print("NXB:", r["publisher"])
    print("Link:", r["url"])
    print("-" * 50)
