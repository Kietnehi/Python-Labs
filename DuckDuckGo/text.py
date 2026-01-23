import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from ddgs import DDGS

query = input("Nhập nội dung cần tìm: ")

print("\nKẾT QUẢ TÌM KIẾM:\n")

with DDGS() as ddgs:
    results = list(ddgs.text(query, max_results=5))

if not results:
    print("❌ Không tìm thấy kết quả nào.")
else:
    for i, r in enumerate(results, start=1):
        print(f"Kết quả {i}:")
        print("Tiêu đề:", r.get("title"))
        print("Link:", r.get("href"))
        print("Mô tả:", r.get("body"))
        print("-" * 50)
