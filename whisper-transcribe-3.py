from transformers import pipeline
import torch
print(torch.__version__)
print(torch.cuda.is_available())

def speech_to_text_pipeline(audio_file):
    try:
        # Initialize the Whisper pipeline with fallback to CPU
        #transcriber = pipeline("automatic-speech-recognition", model="alvanlii/whisper-small-cantonese")
        transcriber = pipeline("automatic-speech-recognition", model="max-at-Parami/whisper-small-zh-hk")


        # Transcribe the audio file
        result = transcriber(audio_file)  # Ensure compatibility with `input_features`
        return result.get("text", "No transcription available")
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example audio file
    audio_file = "teller.mp3"  # Replace with your audio file path

    # Perform transcription
    transcription = speech_to_text_pipeline(audio_file)

    # Output the transcription
    print("Transcription:", transcription)