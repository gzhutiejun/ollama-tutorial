import torch
from sparktts import SparkTTS

def text_to_speech(text, model_dir='pretrained_models/Spark-TTS-0.5B'):
    # Load the pre-trained model
    model = SparkTTS.from_pretrained(model_dir)
    
    # Generate speech
    audio = model.generate(text)
    
    # Save the audio to a file
    with open('output.wav', 'wb') as f:
        f.write(audio)
    
    print('Audio generated successfully!')

# Example usage
text = 'Hello, this is a test of the Spark-TTS text-to-speech system.'
text_to_speech(text)