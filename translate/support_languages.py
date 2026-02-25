from googletrans import LANGUAGES as google_langs
from deep_translator import GoogleTranslator
import os

def export_language_lists():
    print(" đang bắt đầu trích xuất danh sách ngôn ngữ...")

    # --- XỬ LÝ GOOGLETRANS ---
    try:
        file_google = "languages_googletrans.txt"
        with open(file_google, "w", encoding="utf-8") as f:
            f.write(f"{'Ký hiệu':<10} | {'Tên ngôn ngữ'}\n")
            f.write("-" * 30 + "\n")
            # googletrans.LANGUAGES là một dict {mã: tên}
            for code, name in google_langs.items():
                f.write(f"{code:<10} | {name.capitalize()}\n")
        print(f" thành công: Đã tạo file '{file_google}'")
    except Exception as e:
        print(f" lỗi khi xử lý googletrans: {e}")

    # --- XỬ LÝ DEEP_TRANSLATOR ---
    try:
        file_deep = "languages_deep_translator.txt"
        # Lấy danh sách từ deep_translator
        deep_langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        
        with open(file_deep, "w", encoding="utf-8") as f:
            f.write(f"{'Ký hiệu':<10} | {'Tên ngôn ngữ'}\n")
            f.write("-" * 30 + "\n")
            # deep_translator trả về {tên: mã} nên ta đảo ngược lại để in cho đẹp
            for name, code in deep_langs_dict.items():
                f.write(f"{code:<10} | {name.capitalize()}\n")
        print(f" thành công: Đã tạo file '{file_deep}'")
    except Exception as e:
        print(f" lỗi khi xử lý deep_translator: {e}")

    print("\n Xong! Bạn có thể kiểm tra 2 file .txt trong thư mục hiện tại.")

if __name__ == "__main__":
    export_language_lists()