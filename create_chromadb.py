import chromadb
import json
from dotenv import load_dotenv
from langchain.embeddings.azure_openai import AzureOpenAIEmbeddings

load_dotenv()

embeddings = AzureOpenAIEmbeddings()
print(embeddings.azure_endpoint)
print(embeddings.openai_api_key)
print(embeddings.openai_api_version)

query_results = embeddings.embed_query("What is philosophy?")
print(query_results)

CHROMA_DATA_PATH = "data/"
EMBED_MODEL = "text-embedding-04"
COLLECTION_NAME = "philosophy"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"},
)

# results = collection.query(query_embeddings=[])

# print(results)

# with open("./data/parsed_data.json", "r", encoding="utf8") as f:
#     records = json.load(f)["RECORDS"]

# ids = []
# embeddings = []
# documents = []
# metadatas = []
# for record in records:
#     ids.append(record["id"])
#     embeddings.append(record["embedding"])
#     documents.append(record["content"])
#     metadata = {
#         "title": record["title"],
#         "url": record["url"],
#         "published_date": record["published_date"],
#         "content_length": record["content_length"]
#     }
#     metadatas.append(metadata)

# ids_batch_1 = ids[:5400]
# ids_batch_2 = ids[5400:]
# embeddings_batch_1 = embeddings[:5400]
# embeddings_batch_2 = embeddings[5400:]
# documents_batch_1 = documents[:5400]
# documents_batch_2 = documents[5400:]
# metadatas_batch_1 = metadatas[:5400]
# metadatas_batch_2 = metadatas[5400:]

# collection.add(
#     ids=ids_batch_1,
#     embeddings=embeddings_batch_1,
#     documents=documents_batch_1,
#     metadatas=metadatas_batch_1
# )

# collection.add(
#     ids=ids_batch_2,
#     embeddings=embeddings_batch_2,
#     documents=documents_batch_2,
#     metadatas=metadatas_batch_2
# )