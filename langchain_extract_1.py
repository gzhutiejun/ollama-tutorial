from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import json
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="ollama",
    model="llama3.2",
    base_url="http://localhost:11434/v1/",
    temperature=0,
    max_tokens=2000,
)


def extract_structural_data_with_langchain(input_text):
    try:
        # Define the schema for structured JSON output
        schema = {
            "name": None,
            "organization": None,
            "location": None,
            "email": None
        }

        # Define the prompt template
        prompt_template = """
        Extract the following information from the text:
        - Name
        - Organization
        - Location
        - Email

        Text: {text}

        Provide the output in JSON format with the keys: name, organization, location, email.
        """

        # Initialize the LangChain components
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = LLMChain(llm=llm, prompt=prompt)

        # Run the chain to extract data
        response = chain.invoke({"text": input_text})
        print(response)
        # Parse the response into the predefined schema
        extracted_data = json.loads(response)
        for key in schema:
            schema[key] = extracted_data.get(key, None)

        return schema
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

if __name__ == "__main__":
    # Example input text
    input_text = "John Doe works at OpenAI and lives in San Francisco. His email is john.doe@example.com."

    # Extract structural data
    structured_data = extract_structural_data_with_langchain(input_text)

    # Output the structured JSON
    print("Structured JSON:", json.dumps(structured_data, indent=4))
