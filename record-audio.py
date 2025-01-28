
import sounddevice as sd
import scipy.io.wavfile as wav

# Parameters
duration = 5  # seconds
fs = 16000  # Sample rate

print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs,  channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording finished")

# Save the audio to a file
wav.write('./data/output.wav', fs, audio)
print("Audio saved as output.wav")