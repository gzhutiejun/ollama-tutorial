from ollama import Ollama

# Initialize Ollama
ollm = Ollama(model="llama3.2")

# Load and preprocess text
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

text_data = extract_text_from_pdf("./data/emvbook3.pdf")

# Train the model
ollm.train(text_data)
ollm.save("./data/emvmodel")