import whisper

# Initialize the Whisper model
model = whisper.model("small")

def speech_to_text(audio_file):
    try:
        # Transcribe the audio file
        result = model.transcribe(audio_file, fp16=False)
        return result['text']
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    #audio_file = "131718-customer.mp3"  # Replace with your audio file path
    # audio_file = "131134-customer.mp3"  # Replace with your audio file path
    audio_file = "test.mp3"  
    transcription = speech_to_text(audio_file)
    print("Transcription:", transcription)