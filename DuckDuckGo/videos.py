from ddgs import DDGS

ddgs = DDGS()

print("=== VIDEO SEARCH (NHIỀU TRANG) ===\n")

for page in range(1, 4):   # lấy 3 trang đầu
    print(f"\n===== PAGE {page} =====\n")

    results = ddgs.videos(
        query="bóng đá highlight",
        max_results=5,
        page=page
    )

    for i, r in enumerate(results, start=1):
        print(f"Video {i}:")
        print("Tiêu đề:", r.get("title"))
        print("Link:", r.get("content"))
        print("Thời lượng:", r.get("duration"))
        print("Nguồn:", r.get("publisher"))
        print("-" * 50)
