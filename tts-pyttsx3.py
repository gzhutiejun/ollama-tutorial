import pyttsx3


def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f'Voice ID: {voice.id} - Name: {voice.name} - Lang: {voice.languages}')
def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', "com.apple.eloquence.en-US.Flo")
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def text_to_speech_to_file(text, filename):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    
    # Save speech to an audio file
    engine.save_to_file(text, filename)
    engine.runAndWait()

#get_voices()
# Example usage
text = 'Hello, which services do you want to do?'
text_to_speech(text)


filename = 'output2.mp3'
#text_to_speech_to_file(text, filename)