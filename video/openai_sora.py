from openai import OpenAI
import base64
from openai import OpenAI
import time
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")



video = client.videos.create(
    prompt="A calico cat playing a piano on stage",
    model="sora-2",
    seconds="8",
    size="720x1280"  # ✅ hợp lệ
)

video_id = video.id
print(f"🎬 Video job created: {video_id}")

# Chờ render xong
while True:
    status = client.videos.retrieve(video_id)
    print(f"⏳ Status: {status.status} | Progress: {status.progress}%")

    if status.status == "completed":
        break

    if status.status == "failed":
        raise Exception(f"❌ Failed: {status.error}")

    time.sleep(5)

# Tải video về
response = client.videos.download_content(video_id=video_id)

with open("output.mp4", "wb") as f:
    f.write(response.read())

print("🎉 Video đã tải xong: output.mp4")