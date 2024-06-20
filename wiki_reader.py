from llama_index import VectorStoreIndex, download_loader
import openai_key

WikipediaReader = download_loader("WikipediaReader")

loader = WikipediaReader()
documents = loader.load_data(
    pages=['Berlin', 'Rome', 'Tokyo', 'Canberra', 'Santiago'])

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("How many people live in Berlin vs in Tokyo?")
print(response)
