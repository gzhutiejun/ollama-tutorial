from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat_model = ChatOpenAI(
    api_key="ollama",
    model="llama3.2",
    base_url="http://localhost:11434/v1/",
    temperature=0,
    max_tokens=500,
)

