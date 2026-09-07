from services.knowledge_base import load_knowledge_base
from services.semantic_retriever import semantic_retrieve
from services.llm import generate_response


def main():
    question = "How long does a refund take?"

    knowledge_base = load_knowledge_base("data/faq.txt")

    relevant_sections = semantic_retrieve(
        question,
        knowledge_base,
    )

    context = "\n\n".join(relevant_sections)

    answer = generate_response(
        question,
        context,
    )

    print("Customer:", question)
    print("\nAssistant:", answer)


if __name__ == "__main__":
    main()