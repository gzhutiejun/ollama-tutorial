from transformers import pipeline

def extract_structural_data(text):
    try:
        # Initialize the transformers pipeline for named entity recognition (NER)
        ner_pipeline = pipeline("ner", grouped_entities=True)

        # Extract structural data
        entities = ner_pipeline(text)
        return entities
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example text to extract structural data from
    example_text = "John Doe works at OpenAI and lives in San Francisco. His email is john.doe@example.com."

    # Extract structural data
    structural_data = extract_structural_data(example_text)
    print("Extracted Structural Data:", structural_data)
