from googletrans import Translator

translator = Translator()

def translate_text(text, lang):
    try:
        translation = translator.translate(text, dest=lang)
        return translation.text
    except Exception:
        return text  # Fallback to original