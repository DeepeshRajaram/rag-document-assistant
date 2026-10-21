from src.document_loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embeddings

docs = load_pdf("data\\HR-Guide_-Policy-and-Procedure-Template-pages-1.pdf")

print(f"Total pages: {len(docs)}")

print(docs[0].page_content[0:500])

chunks = split_documents(docs)

print(f"Total chunks: {len(chunks)}")


embeddings = get_embeddings()
vector = embeddings.embed_query(
    "What is artificial intelligence?"
)

print(len(vector))

