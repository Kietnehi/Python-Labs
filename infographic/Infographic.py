import base64
import requests
import json

prompt = """
Tạo cho tôi một infographic về tác động của biến đổi khí hậu đối với các hệ sinh thái đại dương
"""

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "google/gemini-3-pro-image-preview",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "modalities": ["image", "text"]
    })
)

result = response.json()


if result.get("choices"):
    message = result["choices"][0]["message"]
    if message.get("images"):
        for i, image in enumerate(message["images"]):
            image_url = image["image_url"]["url"]

            # Bỏ phần header "data:image/jpeg;base64,"
            base64_data = image_url.split(",")[1]

            image_bytes = base64.b64decode(base64_data)

            file_name = f"infographic_{i+1}.jpg"
            with open(file_name, "wb") as f:
                f.write(image_bytes)

            print(f"✅ Saved image: {file_name}")

