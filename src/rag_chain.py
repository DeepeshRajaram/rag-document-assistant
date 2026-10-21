import os
from dotenv import load_dotenv
from langchain_openai import (OpenAIEmbeddings, ChatOpenAI)
from langchain_pinecone import PineconeVectorStore

load_dotenv()

def get_retriever():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings
    )

    return vector_store.as_retriever(
        search_kwargs={"k":3}
    )


def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    

def ask_question(question, chat_history=None):
    retriever = get_retriever()
    llm = get_llm()
    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    sources = []

    for doc in docs:
        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "N/A"
        )

        sources.append(
            f"({source} (Page {page})"
        )

    prompt= f"""
    You are a helpful assistant.

    Answer only from the provided context,
    If the answer is not available in the context,
    say: "I could not find that information in the document."

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)
    return response.content, sources, docs