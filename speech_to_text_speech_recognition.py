import speech_recognition as sr

def speech_to_text_speech_recognition(audio_file):
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        # Perform speech-to-text
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    audio_file = "200846-customer.mp3"  
    transcription = speech_to_text_speech_recognition(audio_file)
    print("Transcription:", transcription)
