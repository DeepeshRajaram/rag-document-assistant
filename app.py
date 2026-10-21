import streamlit as st

from src.rag_chain import ask_question

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="📚"
)

st.title("📚 RAG Document Assistant")


# -----------------------------------------
#------Session State Initialization--------
# ----------------------------------------- 

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------------------- 
#-----Clear Chat Button--------------------
# -----------------------------------------
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# -----------------------------------------
# ----Display Previous Messages------------
# -----------------------------------------
for chat in st.session_state.chat_history:
    st.chat_message("user").write(
        chat["question"]
    )

    st.chat_message("assistant").write(
        chat["answer"]
    )

# -----------------------------------------
# ----Chat Input---------------------------
# -----------------------------------------
question = st.chat_input(
    "Ask a question about the document"
)


# -----------------------------------------
# ----Process User Question----------------
# -----------------------------------------
if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching document"):
            answer, sources, docs = ask_question(
                question
            )

    # st.subheader("Answer")
    st.write(answer)

    with st.expander("View Retrieved Context"):
        for i, doc in enumerate(docs, start=1):
            st.markdown(f"### Chunk {i}")
            st.write(doc.page_content)
            st.divider()

    

    st.markdown("### Sources")
    unique_sources = list(set(sources))

    for source in unique_sources:
        st.write(source)

    st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
    )


