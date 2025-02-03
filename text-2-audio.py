# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-to-audio", model="declare-lab/tango2")

text = "[clears throat] This is a test ... and I just took a long pause."
output = pipe(text)

from IPython.display import Audio
Audio(output["audio"], rate=output["sampling_rate"])