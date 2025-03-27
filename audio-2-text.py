

from transformers import pipeline

# Load the pipeline for automatic speech recognition (ASR)
asr_pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-small")

# Path to the audio file
audio_file = "./data/cwd.wav"

# Perform the transcription
result = asr_pipeline(audio_file)

# Print the transcribed text
print("Transcribed text:", result["text"])