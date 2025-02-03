import ollama

# print(ollama.list())

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print(res["message"]["content"])