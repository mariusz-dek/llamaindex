from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai_key

documents = SimpleDirectoryReader(
    './data/articles/').load_data()
index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine(streaming=True)
response_stream = query_engine.query("What did the author do growing up?")
response_stream.print_response_stream()
