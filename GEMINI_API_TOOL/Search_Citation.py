from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load file .env
load_dotenv()

# Lấy biến môi trường
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Khởi tạo client
client = genai.Client(api_key=GEMINI_API_KEY)

# Khai báo tool Google Search
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

# Cấu hình request với grounding
config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

# Prompt test (nên hỏi thông tin mới, ví dụ sự kiện gần đây)
prompt = "Who won the Euro 2024 final and what was the score?"

# Gọi API
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config,
)

# In câu trả lời thuần
print("=== RAW ANSWER ===")
print(response.text)

# ---- Hàm chèn citation inline từ groundingMetadata ----
def add_citations(response):
    text = response.text
    meta = response.candidates[0].grounding_metadata

    supports = meta.grounding_supports
    chunks = meta.grounding_chunks

    # Sort ngược để không làm lệch index khi chèn
    sorted_supports = sorted(
        supports, key=lambda s: s.segment.end_index, reverse=True
    )

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i+1}]({uri})")

            citation_string = " " + ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# In câu trả lời có citation
print("\n=== ANSWER WITH CITATIONS ===")
print(add_citations(response))

# ---- In thêm thông tin debug ----
print("\n=== SEARCH QUERIES USED ===")
for q in response.candidates[0].grounding_metadata.web_search_queries:
    print("-", q)

print("\n=== SOURCES ===")
for i, chunk in enumerate(response.candidates[0].grounding_metadata.grounding_chunks):
    print(f"[{i+1}] {chunk.web.title} -> {chunk.web.uri}")
