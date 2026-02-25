from deep_translator import GoogleTranslator, single_detection
import time

def translate_with_deep_pure():
    original_text = "Hello, I am learning AI and Python."
    
    try:
        # 1. Khởi tạo Translator chính
        translator = GoogleTranslator(source='auto', target='vi')
        
        # 2. Lấy danh sách ngôn ngữ và kiểm tra lỗi NoneType
        lang_map = translator.get_supported_languages(as_dict=True)
        if not lang_map:
            print("Lỗi: Không thể lấy danh sách ngôn ngữ từ Google. Vui lòng kiểm tra mạng.")
            return

        # 3. Sử dụng single_detection của deep-translator
        # Mẹo: Để tránh trả về 'auto', văn bản cần đủ dài hoặc thử gọi lại
        try:
            detected_code = single_detection(original_text, api_key='none')
        except:
            detected_code = 'auto'

        # 4. Tra cứu tên ngôn ngữ từ mã code
        code_to_name = {v: k for k, v in lang_map.items()}
        
        # Nếu vẫn là 'auto', ta dùng kết quả từ lần dịch đầu tiên để xác định
        if detected_code == 'auto':
            # Dịch thử sang một ngôn ngữ bất kỳ
            translator.translate(original_text)
            # Một số phiên bản deep-translator sẽ cập nhật .source sau khi gọi translate()
            detected_code = translator.source if translator.source != 'auto' else 'en'

        detected_name = code_to_name.get(detected_code, "English").capitalize()

        print("=" * 70)
        print(f"[*] VĂN BẢN GỐC: {original_text}")
        print(f"[*] DETECT (DEEP-TRANSLATOR): {detected_name} ({detected_code})")
        print(f"[*] Đang dịch sang {len(lang_map)} ngôn ngữ...")
        print("=" * 70)
        print(f"{'Mã':<8} | {'Tên Ngôn Ngữ':<20} | {'Bản Dịch'}")
        print("-" * 70)

        # 5. Vòng lặp dịch
        for name, code in lang_map.items():
            try:
                translator.target = code
                result = translator.translate(original_text)
                print(f"{code:<8} | {name.title():<20} | {result}")
                
                # Nghỉ một chút để tránh bị Google block IP
                time.sleep(0.1)
            except Exception:
                continue

    except Exception as e:
        print(f"Lỗi phát sinh: {e}")

if __name__ == "__main__":
    translate_with_deep_pure()
    