from deep_translator import GoogleTranslator
from langdetect import detect
import time

def translate_with_perfect_detect():
    # Nội dung cần dịch
    original_text = "Hello, I am learning AI and Python."
    
    try:
        # --- BƯỚC 1: NHẬN DIỆN NGÔN NGỮ GỐC ---
        # Sử dụng langdetect để lấy mã ngôn ngữ (vd: 'en', 'vi')
        detected_code = detect(original_text)
        
        # --- BƯỚC 2: KHỞI TẠO TRANSLATOR ---
        translator = GoogleTranslator(source='auto', target='vi')
        lang_map = translator.get_supported_languages(as_dict=True)
        
        # Tạo bảng tra cứu ngược để lấy tên đầy đủ của ngôn ngữ gốc
        code_to_name = {v: k for k, v in lang_map.items()}
        detected_name = code_to_name.get(detected_code, "Không xác định").capitalize()

        print("=" * 70)
        print(f"[*] VĂN BẢN GỐC: {original_text}")
        print(f"[*] NGÔN NGỮ PHÁT HIỆN: {detected_name} ({detected_code})")
        print(f"[*] Đang chuẩn bị dịch sang {len(lang_map)} ngôn ngữ...")
        print("=" * 70)
        print(f"{'Mã':<8} | {'Tên Ngôn Ngữ':<20} | {'Bản Dịch'}")
        print("-" * 70)

        # --- BƯỚC 3: VÒNG LẶP DỊCH ĐA NGÔN NGỮ ---
        for name, code in lang_map.items():
            try:
                translator.target = code
                result = translator.translate(original_text)
                
                print(f"{code:<8} | {name.title():<20} | {result}")
                
                # Sleep ngắn để tránh bị Google quét
                time.sleep(0.05)
            except Exception:
                continue

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    # Nhắc lại: Đừng đặt tên file trùng với tên thư viện nhé!
    translate_with_perfect_detect()