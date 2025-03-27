from ollama import chat
import datetime
from pydantic import BaseModel

class Transaction(BaseModel):
    currency: str
    amount: int
    account: str

class Session(BaseModel): 
    transaction: str
    cancelled: bool

# print(ollama.list())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +" start ")
res = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "I want to withdraw 600 US dollars from my credit account, and print receipt",
        }
    ],

    format=Transaction.model_json_schema()
)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +" complete ")
print(res["message"]["content"])

'''
    messages=[
        {
            "role": "user",
            "content": "I want to withdraw 600 hong kong dollars from my credit account, and print receipt",
        }
    ],
'''
