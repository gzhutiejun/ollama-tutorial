from TTS.api import TTS

def text_to_speech(text, lang='en'):
    # Initialize the TTS engine
    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
    # Generate speech from text
    tts.tts_to_file(text=text, file_path="tts-output.mp3")

    print("Audio saved as output.wav")


text = "Hello, this is a text-to-speech example using tts."
text_to_speech(text)