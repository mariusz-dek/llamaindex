from pathlib import Path
from llama_index import VectorStoreIndex, download_loader
import openai_key

ImageReader = download_loader("ImageReader")

# If the Image has key-value pairs text, use text_type = "key_value"
loader = ImageReader(text_type="key_value")
documents = loader.load_data(file=Path('./data/receipt1.jpg'))

index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine()
response = query_engine.query("Show me data")
print(response)
