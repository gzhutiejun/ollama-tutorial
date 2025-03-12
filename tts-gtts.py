from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    # Initialize the TTS engine
    tts = gTTS(text=text, lang=lang)
    
    # Save the speech to an audio file
    tts.save('output1.mp3')
    
    # Play the audio file (optional)
    #os.system('start output.mp3')  # Use 'afplay output.mp3' on macOS or 'mpg321 output.mp3' on Linux

# Example usage
text = 'Hello, which services do you want to do?'
text_to_speech(text)