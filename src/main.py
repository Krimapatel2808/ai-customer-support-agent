from services.knowledge_base import load_knowledge_base
from services.semantic_retriever import semantic_retrieve
from services.llm import generate_response


def main():
    question = input("Customer: ")

    knowledge_base = load_knowledge_base("data/faq.txt")

    relevant_sections = semantic_retrieve(
        question,
        knowledge_base,
    )
    if not relevant_sections:
      print("\nAssistant: I don't have enough information to answer that.")
    return

    context = "\n\n".join(relevant_sections)

    answer = generate_response(
    question,
    context,
)

    print("\nAssistant:", answer)

if __name__ == "__main__":
    main()