from langchain_ollama import ChatOllama
import json

def serialize_json_object(jsonObj: dict):
    if (jsonObj is None):
        return ""
    try:
        ret = json.dumps(jsonObj)
        return ret
    except Exception as error:
        print("serialize_json_object", error)
        return ""
    

local_llm = "llama3.2"
llm = ChatOllama(model=local_llm, temperature=0)
llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")
# schema = {
#     "amount": 0,
#     "currency": "",
#     "account":""
# }
# user_text = "I want to withdrawal 100 hong kong dollars from my credit account"
# instruction = '''
# extract amount, 
# extract currency (e.g. HKD, USD)
# extract account (e.g. credit, saving, debit, cheque)
# '''

schema = {
    "confirm": False,
    "cancel": False,
}
user_text = "no need"
instruction = '''
extract confirm (e.g. confirm, continue, yes)
extract cancel (e.g. exit, quit, cancel, no need)
'''
messages = [
    ("system", f"You are ChatOpenAI, a helpful assistant. "
    f"Your task is to extract structured data from user messages and only respond with JSON object as {serialize_json_object(schema)}"),
    ("human", "Extract following data:"
    f"{instruction}"
    f"Text: {user_text}")
]

# response = llm.invoke(messages)
response = llm_json_mode.invoke(messages)
print(response.content)

