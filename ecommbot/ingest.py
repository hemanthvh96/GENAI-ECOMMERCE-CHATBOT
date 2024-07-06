import os
import pandas as pd

from dotenv import load_dotenv
from langchain_astradb import AstraDBVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from ecommbot.data_converter import dataconverter

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_COLLECTION = os.getenv("ASTRA_DB_COLLECTION")
ASTRA_DB_NAMESPACE = os.getenv("ASTRA_DB_NAMESPACE")

embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def ingestdata(storage):
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name=ASTRA_DB_COLLECTION,
        token=ASTRA_DB_APPLICATION_TOKEN,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        collection_indexing_policy={"allow": ["vector"]}
    )

    if storage == None:
        docs = dataconverter()
        inserted_ids = vstore.add_documents(docs)
        print(f"\nInserted {len(inserted_ids)} documents.")
    else:
        return vstore
    
    return vstore, inserted_ids

if __name__ == "__main__":
    vstore,inserted_ids = ingestdata(None)
    
    # FOR CHECKING
    # results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    # for res in results:
    #         print(f"* {res.page_content} [{res.metadata}]")

