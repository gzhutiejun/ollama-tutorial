from langchain_google_community import SpeechToTextLoader

project_id = "myprojectid"
audio_file = "./data/output.wav"
# or a local file path: file_path = "./audio.wav"

loader = SpeechToTextLoader(project_id=project_id, file_path=audio_file)

docs = loader.load()

print(docs[0].page_content)