from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import json

# Initialize the ChatOpenAI LLM with local LLM configuration
llm = ChatOpenAI(
    api_key="ollama",
    model="llama3.2",
    base_url="http://localhost:11434/v1/",
    temperature=0,
    max_tokens=2000,
)

def extract_structural_data(input_text):
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

        # Parse the response into the predefined schema
        extracted_data = json.loads(response)
        for key in schema:
            schema[key] = extracted_data.get(key, None)

        return schema
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

def extract_customer_answers(input_text):
    try:
        # Define the schema for structured JSON output
        schema = {
            "customer_name": None,
            "account_number": None,
            "transaction_type": None,
            "transaction_amount": None
        }

        # Define the prompt template
        prompt_template = """
        Extract the following information from the customer's answers:
        - Customer Name
        - Account Number
        - Transaction Type (e.g., deposit, withdrawal)
        - Transaction Amount

        Text: {text}

        Provide the output in JSON format with the keys: customer_name, account_number, transaction_type, transaction_amount.
        """

        # Initialize the LangChain components
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = LLMChain(llm=llm, prompt=prompt)

        # Run the chain to extract data
        response = chain.invoke({"text": input_text})

        # Parse the response into the predefined schema
        extracted_data = json.loads(response)
        for key in schema:
            schema[key] = extracted_data.get(key, None)

        return schema
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

if __name__ == "__main__":
    # Example input text
    input_text = "My name is Jane Doe. My account number is 123456789. I want to deposit $500."

    # Extract structural data
    structured_data = extract_customer_answers(input_text)

    # Output the structured JSON
    print("Structured JSON:", json.dumps(structured_data, indent=4))
