import chromadb
from dotenv import load_dotenv
from langchain.embeddings.gpt4all import GPT4AllEmbeddings
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from os import environ

load_dotenv()
CHROMA_DATA_PATH = "data/"
COLLECTION_NAME = "philosophy"

gpt4allembed = GPT4AllEmbeddings()
chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

def query_for_documents(query: str, n_results: int = 10, text_only=True) -> list[str]:
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

def generate_response(query: str, n_results: int = 10) -> str:

    documents = query_for_documents(query, n_results=n_results)

    model = AzureChatOpenAI(azure_endpoint=environ['AZURE_OPENAI_ENDPOINT'], api_key=environ['AZURE_OPENAI_API_KEY'], openai_api_version=environ['OPENAI_API_VERSION'], model=environ['MODEL_NAME'])

    messages = [SystemMessage(content='use only information from the following texts to answer the query from the user'), SystemMessage(content='\n'.join(documents)), HumanMessage(content=query)]

    print(messages)

    result = model(messages=messages)

    return result.content
    

print('-------------------------------------------------------------------')
print(generate_response('Does language modify thoughts?'))
