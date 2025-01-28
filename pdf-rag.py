from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/emvbook3.pdf"
model = "llama3.2"

if doc_path:
    loader = UnstructuredPDFLoader(doc_path)
    data = loader.load()
    print("done loading")
else:
    print("Load a PDF file")

content = data[0].page_content
print(content[:100])
