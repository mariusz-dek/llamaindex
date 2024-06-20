from pathlib import Path
from llama_index import VectorStoreIndex, download_loader
import openai_key

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('./data/seamless-proyecto.pdf'))

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Que es proyecto Seamless?")
print(response)

print('-----------')


response = query_engine.query("Que es clientes tenemos?")
print(response)
