import os
import io
from google.cloud import speech

def speech_to_text_google(audio_file):
    try:
        # Initialize the Google Speech-to-Text client
        client = speech.SpeechClient()  # Uses default credentials if already authenticated

        # Load the audio file
        with io.open(audio_file, "rb") as audio:
            content = audio.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        # Perform speech-to-text
        response = client.recognize(config=config, audio=audio)

        # Extract transcription
        transcription = " ".join([result.alternatives[0].transcript for result in response.results])
        return transcription
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Comment out the credentials line if using default authentication
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

    audio_file = "output1.mp3"  # Replace with your audio file path
    transcription = speech_to_text_google(audio_file)
    print("Transcription:", transcription)
