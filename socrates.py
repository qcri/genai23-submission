import chromadb
from dotenv import load_dotenv
from langchain.embeddings.gpt4all import GPT4AllEmbeddings

load_dotenv()
CHROMA_DATA_PATH = "data/"
COLLECTION_NAME = "philosophy"

gpt4allembed = GPT4AllEmbeddings()
chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)


def query_for_documents(query: str, n_results: int = 4, text_only=True) -> list[str]:
    global gpt4allembed, chroma_client

    query_results = gpt4allembed.embed_query(query)

    collection = chroma_client.get_collection(
        name=COLLECTION_NAME
    )

    query_results = collection.query(
        query_embeddings=[query_results],
        n_results=n_results
    )

    if text_only:
        return query_results["documents"][0]
    else:
        return query_results

print(query_for_documents("What is philosophy?", 3))