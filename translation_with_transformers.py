from transformers import pipeline

def translate_chinese_to_english(text):
    try:
        # Initialize the translation pipeline
        #translator = pipeline("translation_zh_to_en")
        translator = pipeline("translation_en_to_fr")
        translator("How old are you?")
        # Perform translation
        result = translator(text, max_length=512)
        return result[0]["translation_text"]
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example input text in Chinese
    input_text = "取款交易"

    # Perform translation
    translated_text = translate_chinese_to_english(input_text)

    # Output the translated text
    print("Translated Text:", translated_text)
