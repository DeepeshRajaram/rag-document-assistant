from src.rag_chain import ask_question


answer, sources = ask_question(
    "What is this document about?"
)

print("\nANSWER:")
print(answer)

print("\nSOURCES:")

for source in sources:
    print(source)
