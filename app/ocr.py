import io

CHINESE_CHARS = set("""的一是在有我人他这个上们来到时大地为子中你说生国年着就那和要她出也得里后自以会家可下而过天去能对小多然于心学么之都好看起发当没成只如事把还用第样道想作种开美总从无情己面最女但现前些所同日手又行意动方期它头经长儿回位分爱老因很给名法间斯知世什两次使身者被高已亲其进此何与乐今家学""")

ENGLISH_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMBERS = set("0123456789")
PUNCTUATION = set("，。！？、；：""''（）{}[]【】<>《》/\\|·~@#$%^&*+-=")

def contains_valid_chars(text):
    for char in text:
        if char in CHINESE_CHARS or char in ENGLISH_CHARS or char in NUMBERS or char in PUNCTUATION:
            return True
    return False

def extract_text_from_image(image_bytes):
    try:
        try:
            import pytesseract
            from PIL import Image
            
            image = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(image, lang='chi_sim+eng')
            text = text.strip()
            
            if text and contains_valid_chars(text):
                return text
            return None
        except ImportError:
            return "图片文字识别功能暂不可用，请使用文字输入方式更新简介"
    except Exception as e:
        print(f"OCR error: {e}")
        return None