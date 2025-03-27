from langdetect import detect, detect_langs

def detect_language(text):
    try:
        # Detect the primary language
        language = detect(text)
        
        # Detect probabilities for multiple languages
        probabilities = detect_langs(text)
        
        return {"language": language, "probabilities": str(probabilities)}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

if __name__ == "__main__":
    # Example input text
    input_text = "100 港币"  # Replace with your text

    # Detect language
    result = detect_language(input_text)

    # Output the detected language and probabilities
    print("Detection Result:", result['language'])
