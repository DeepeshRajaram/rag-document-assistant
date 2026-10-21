# from src.document_loader import load_pdf
# from src.splitter import split_documents
# from src.embeddings import get_embeddings
# from src.vector_store import create_vector_store
# from src.pinecone_setup import get_pinecone_index
# from dotenv import load_dotenv
# import os


from src.rag_chain import get_retriever

retriever = get_retriever()

results = retriever.invoke("What is the document about ?")


for doc in results:
    print(doc.page_content[:300])
    print("=" * 50)


# get_pinecone_index()


# docs = load_pdf("data\\HR-Guide_-Policy-and-Procedure-Template-pages-1.pdf")

# chunks = split_documents(docs)
# embeddings = get_embeddings()
# create_vector_store(chunks, embeddings)

# print("Document indexed successfully")






