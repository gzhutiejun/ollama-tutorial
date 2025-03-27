import whisper

def speech_to_text_whisper(audio_file):
    try:
        # Load the Whisper model
        model = whisper.load_model("medium")

        # Transcribe the audio file
        result = model.transcribe(audio_file, fp16=False)
        return result['text']
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    #audio_file = "200846-customer.mp3"  
    #audio_file = "131718-customer.mp3"  
    audio_file = "check.mp3" 
    #audio_file = "195351-teller.mp3"  
    transcription = speech_to_text_whisper(audio_file)
    print("Transcription:", transcription)
