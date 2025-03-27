from googletrans import Translator
import asyncio
async def detect_languages():
    async with Translator() as translator:
        result = await translator.detect('hello')
        print(result)
        return result
    
def translate_text_googletrans(input_text, target_language):
    try:
        # Initialize the Translator
        translator = Translator()

        # Perform translation
        translated = translator.translate(input_text, src='zh-cn', dest=target_language)
        return translated.text  # Ensure we access the 'text' attribute of the result
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example input text and target language
    input_text = "现金取款"  # "Hello, World" in Chinese
    target_language = "en"  # Translate to English

    # Perform translation
    translated_text = translate_text_googletrans(input_text, target_language)
    
    # Output the translated text
    print("Translated Text:", translated_text)
