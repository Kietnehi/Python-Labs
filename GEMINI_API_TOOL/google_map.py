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
def print_grounding(response):
    candidate = response.candidates[0]

    print("\n===== GENERATED TEXT =====")

    # Cách an toàn để lấy text
    text = None

    # Ưu tiên response.text (helper của SDK)
    if hasattr(response, "text") and response.text:
        text = response.text
    elif candidate.content and candidate.content.parts:
        for part in candidate.content.parts:
            if hasattr(part, "text") and part.text:
                text = part.text
                break

    if text:
        print(text)
    else:
        print("(No text content returned by model)")

    grounding = candidate.grounding_metadata
    if not grounding:
        print("\n(No grounding metadata returned)")
        return

    # In nguồn Google Maps
    if grounding.grounding_chunks:
        print("\n===== SOURCES (groundingChunks) =====")
        for i, chunk in enumerate(grounding.grounding_chunks):
            maps = chunk.maps
            print(f"[{i}] {maps.title}")
            print(f"    URI: {maps.uri}")
            print(f"    Place ID: {maps.place_id}")

    # In mapping đoạn text ↔ nguồn
    if grounding.grounding_supports:
        print("\n===== CITATION MAPPING (groundingSupports) =====")
        for sup in grounding.grounding_supports:
            seg = sup.segment
            print(f"- Text [{seg.start_index}:{seg.end_index}]: \"{seg.text}\"")
            print(f"  -> Source indices: {sup.grounding_chunk_indices}")

    # In widget token nếu có
    if grounding.google_maps_widget_context_token:
        print("\n===== WIDGET CONTEXT TOKEN =====")
        print(grounding.google_maps_widget_context_token)
        print("\n(Use token này với <gmp-places-contextual> trong Google Maps JS API)")



# ================================
# TEST 1: Tìm quán ăn gần vị trí (near me)
# ================================
print("\n\n######## TEST 1: Restaurants near here ########")

prompt1 = "What are the best Italian restaurants within a 15-minute walk from here?"

response1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt1,
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                # Ví dụ: Downtown Los Angeles
                lat_lng=types.LatLng(latitude=34.050481, longitude=-118.248526)
            )
        ),
    ),
)

print_grounding(response1)


# ================================
# TEST 2: Hỏi về địa điểm cụ thể
# ================================
print("\n\n######## TEST 2: Place-specific question ########")

prompt2 = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt2,
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                lat_lng=types.LatLng(latitude=34.050481, longitude=-118.248526)
            )
        ),
    ),
)

print_grounding(response2)


# ================================
# TEST 3: Cá nhân hóa theo sở thích
# ================================
print("\n\n######## TEST 3: Personalized recommendation ########")

prompt3 = "Which family-friendly restaurants near here have the best playground reviews?"

response3 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt3,
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                # Austin, TX
                lat_lng=types.LatLng(latitude=30.2672, longitude=-97.7431)
            )
        ),
    ),
)

print_grounding(response3)


# ================================
# TEST 4: Lập lịch trình + bật widget
# ================================
print("\n\n######## TEST 4: Itinerary + Widget ########")

prompt4 = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response4 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt4,
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                # San Francisco
                lat_lng=types.LatLng(latitude=37.78193, longitude=-122.40476)
            )
        ),
    ),
)

print_grounding(response4)


print("\n\n====== DONE: All Google Maps Grounding tests completed ======")
