from pathlib import Path
from llama_index import download_loader
from llama_index import VectorStoreIndex
import openai_key

JSONReader = download_loader("JSONReader")

loader = JSONReader()
documents = loader.load_data(Path('./data/data_JSON.json'))


index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine()
response = query_engine.query("Is there Viajes?")
print(response)
