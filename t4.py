from langchain_community.llms import Ollama

llm = Ollama(base_url="http://localhost:11434", model="llama3.2")
prompts = ["capital of China"]
res = llm.generate(prompts)
print(res.generations[0][0].text)
