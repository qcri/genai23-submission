import chromadb
from dotenv import load_dotenv
from langchain.embeddings.gpt4all import GPT4AllEmbeddings

CHROMA_DATA_PATH = "data/"
EMBED_MODEL = "text-embedding-04"
COLLECTION_NAME = "philosophy"

load_dotenv()

gpt4allembed = GPT4AllEmbeddings()

query = "What is philosophy?"

query_results = gpt4allembed.embed_query(query)
print(query_results)

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)

results = collection.query(
    query_embeddings=[query_results],
    n_results=5
)

print(results["documents"])