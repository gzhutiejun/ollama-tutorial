import whisper


# Initialize the Whisper model
initial_prompt = "This is a conversation about banking services."

def speech_to_text(audio_file):
    try:
        # Load the Whisper model
        model = whisper.load_model("small")
        # Transcribe the audio file with float parameters
        response = model.transcribe(
            audio_file, 
            task="transcribe", 
            language="zh-cn", 
            temperature=0,
            fp16=False,  
            initial_prompt=initial_prompt
        )
        if response is not None:
            print(response["text"])
            return response["text"]
        
    except Exception as error:
        print("exception occurs", error)
        return ""

if __name__ == "__main__":
    audio_file = "check.mp3"  # Replace with your audio file path
    transcription = speech_to_text(audio_file)
    print("Transcription:", transcription)