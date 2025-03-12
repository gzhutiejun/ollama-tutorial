from transformers import pipeline

def text_to_speech(text):
    # Initialize the TTS pipeline
    tts_pipeline = pipeline("text-to-speech", model="openai/whisper-small")
    
    # Generate speech
    audio = tts_pipeline(text)
    
    # Save the audio to a file
    with open('output.wav', 'wb') as f:
        f.write(audio["audio"])
    
    print('Audio generated successfully!')

# Example usage
text = 'Hello, this is a test of the transformers text-to-speech pipeline.'
text_to_speech(text)