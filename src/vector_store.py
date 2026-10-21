from langchain_pinecone import PineconeVectorStore

def create_vector_store(chunks, embeddings):
    vector_store = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name="rag-documents"
    )

    return vector_store