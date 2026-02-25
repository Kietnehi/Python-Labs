import asyncio
from googletrans import Translator, LANGUAGES

async def translate_all_languages(text):
    # Khởi tạo Translator trong context async
    async with Translator() as translator:
        print("=" * 60)
        print(f" ĐANG XỬ LÝ VĂN BẢN: '{text}'")
        print("=" * 60)

        # Thực hiện dịch thử một ngôn ngữ đầu tiên để lấy thông tin ngôn ngữ gốc (detect)
        # Chúng ta dùng 'en' làm đích tạm thời để kích hoạt quá trình auto-detect
        sample_res = await translator.translate(text, dest='en')
        source_code = sample_res.src
        source_name = LANGUAGES.get(source_code, "Không xác định").capitalize()

        print(f"[*] Phát hiện ngôn ngữ gốc: {source_name} ({source_code})")
        print(f"[*] Tổng số ngôn ngữ hỗ trợ: {len(LANGUAGES)}")
        print("-" * 60)
        print(f"{'Mã':<8} | {'Tên Ngôn Ngữ':<20} | {'Bản Dịch'}")
        print("-" * 60)

        # Duyệt qua toàn bộ danh sách ngôn ngữ trong LANGUAGES
        for lang_code, lang_name in LANGUAGES.items():
            try:
                # Dịch văn bản (Google sẽ tự hiểu source là gì từ cache hoặc auto)
                result = await translator.translate(text, dest=lang_code)
                
                # In kết quả theo cột
                print(f"{lang_code:<8} | {lang_name.capitalize():<20} | {result.text}")
                
                # NÊN CÓ: Nghỉ một chút để tránh bị Google "quét" vì gửi yêu cầu quá nhanh
                await asyncio.sleep(0.05) 
                
            except Exception as e:
                # Nếu gặp lỗi với một ngôn ngữ nào đó (ví dụ mạng lag), bỏ qua và tiếp tục
                continue

if __name__ == "__main__":
    # Bạn có thể thay đổi văn bản bất kỳ ở đây (Tiếng Nhật, Pháp, Trung...)
    target_text = "Chào bạn, tôi là trợ lý AI đang giúp bạn viết code."
    
    try:
        # Chạy vòng lặp sự kiện asyncio
        asyncio.run(translate_all_languages(target_text))
    except KeyboardInterrupt:
        print("\n[!] Đã dừng chương trình theo yêu cầu của người dùng.")
    except Exception as e:
        print(f"\n[!] Có lỗi xảy ra: {e}")