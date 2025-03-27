from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI LLM with local LLM configuration
llm = ChatOpenAI(
    api_key="ollama",
    model="llama3.2",
    base_url="http://localhost:11434/v1/",
    temperature=0,
    max_tokens=2000,
)

def translate_text(input_text, target_language):
    try:
        # Define the prompt template for translation
        prompt_template = """
        Translate the following text into {language}:

        Text: {text}

        Provide only the translated text.
        """

        # Initialize the LangChain components
        prompt = PromptTemplate(template=prompt_template, input_variables=["text", "language"])
        chain = LLMChain(llm=llm, prompt=prompt)

        # Run the chain to perform translation
        response = chain.run({"text": input_text, "language": target_language})
        return response.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example input text and target language
    input_text = "取款交易"
    target_language = "english"  # Replace with the desired target language

    # Perform translation
    translated_text = translate_text(input_text, target_language)

    # Output the translated text
    print("Translated Text:", translated_text)
