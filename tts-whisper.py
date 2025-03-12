import openai
import whisper

# Initialize the Whisper model
model = whisper.load_model("small")

def text_to_speech(text):
    # Generate speech from text using Whisper
    audio = model.transcribe(text)
    return audio

if __name__ == "__main__":
    text = "Hello, this is a text-to-speech example using OpenAI Whisper."
    audio = text_to_speech(text)
    print("audio generated")
    # Save the audio to a file
    with open("output.wav", "wb") as f:
        f.write(audio)
    print("Audio saved as output.wav")