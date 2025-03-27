from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    api_key="ollama",
    model="llama3.2",
    base_url="http://localhost:11434/v1/",
    temperature=0,
    max_tokens=2000,
)


# Sample text message
#text_message = "I want to deposit 200 hong kong dollars into my saving account, and print receipt"
text_message = "I want to withdraw 200 hong kong dollars from my credit account, and print receipt"

# Define the messages for extraction
messages = [
    ("system", "You are a helpful assistant that extracts data from text messages and outputs it in JSON format."),
    ("human", f"Extract data from the following text message, including number or amount, currency, account type, transaction type and if receipt is required: {text_message}")
]

# Get the extracted data
response = llm.invoke(messages)

# Output the JSON data
print(response.content)