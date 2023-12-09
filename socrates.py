import chromadb
from dotenv import load_dotenv
from langchain.embeddings.gpt4all import GPT4AllEmbeddings
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, AIMessagePromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from os import environ

load_dotenv()
CHROMA_DATA_PATH = "data/"
COLLECTION_NAME = "philosophy"

gpt4allembed = GPT4AllEmbeddings()
chroma_client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)
model = AzureChatOpenAI(azure_endpoint=environ['AZURE_OPENAI_ENDPOINT'], api_key=environ['AZURE_OPENAI_API_KEY'], openai_api_version=environ['OPENAI_API_VERSION'], model=environ['MODEL_NAME'])
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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

def generate_response(query: str, n_results: int = 10, return_documents=False) -> str:
    global model

    documents = query_for_documents(query, n_results=n_results)

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are a friendly chatbot that answers philosophical queries from the user."),
            MessagesPlaceholder(
                variable_name="chat_history"
            ),
            *[SystemMessage(
                content=doc
            ) for doc in documents],
            SystemMessage(content="Use only the previous messages to have a conversation with the user."),
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            )
        ]
    )

    chat_llm_chain = LLMChain(
        llm=model,
        prompt=prompt,
        memory=memory
    )

    result = chat_llm_chain.predict(human_input=query)

    return result
    
if __name__ == "__main__":
    print('-------------------------------------------------------------------')
    print(generate_response("Does language modify thought?", return_documents=True))
    print('-------------------------------------------------------------------')
    print(generate_response("How does this impact my thought?", return_documents=True))
