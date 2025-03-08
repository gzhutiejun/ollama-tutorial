import ollama
import datetime

# print(ollama.list())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +" start ")
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Extract data from the following text message and always answer in the following json format, including number or amount, currency, account type, transaction type and if receipt is required: I want to withdraw 600 hong kong dollars from my credit account, and print receipt"
        }
    ]
)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +" complete ")
print(res["message"]["content"])