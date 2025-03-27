import whisper

# Initialize the Whisper model
model = whisper.load_model("small")

def speech_to_text(audio_file):
    try:
        # Transcribe the audio file
        result = model.transcribe(audio_file, fp16=False)
        return result['text']
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    audio_file = "check.mp3"  # Replace with your audio file path
    transcription = speech_to_text(audio_file)
    print("Transcription:", transcription)