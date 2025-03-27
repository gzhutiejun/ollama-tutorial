import speech_recognition as sr

def audio_to_text(audio_file):
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        # Convert audio to text
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example audio file
    audio_file = "./data/cwd.wav"  # Replace with your audio file path

    # Convert audio to text
    transcription = audio_to_text(audio_file)

    # Output the transcription
    print("Transcription:", transcription)
