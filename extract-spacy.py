import spacy
import json

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the text to be processed
# text = "Apple is looking at buying U.K. startup for $1 billion."
text = "I want to withdraw 100 hong kong dollar from my account"
# Process the text with the spaCy pipeline
doc = nlp(text)

# Extract entities and convert to JSON format
entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
json_data = json.dumps(entities, indent=4)

# Print the JSON data
print(json_data)