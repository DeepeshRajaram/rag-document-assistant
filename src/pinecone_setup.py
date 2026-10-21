from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

def get_pinecone_index():
    
    pc = Pinecone(
        api_key = os.getenv("PINECONE_API_KEY")
    )
    

    index_name = os.getenv("PINECONE_INDEX_NAME")

    existing_indexes = [
        index["name"] for index in pc.list_indexes()
    ]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1",
            )
        )
    else:
        print(f"Index already exists: {index_name}")

    return pc.Index(index_name)