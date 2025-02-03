# the example works but the voice is not clear.
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the text you want to convert to audio
text = "Hello, this is a text-to-speech conversion example using pyttsx3."

# Set properties before adding anything to speak
engine.setProperty('rate', 100)    # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Get available voices and set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index to select different voices

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()