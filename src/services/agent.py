from src.services.knowledge_base import load_knowledge_base
from src.services.semantic_retriever import semantic_retrieve
from src.services.llm import generate_response


def answer_question(question: str) -> str:
    knowledge_base = load_knowledge_base("data/faq.txt")

    relevant_sections = semantic_retrieve(
        question,
        knowledge_base,
    )

    if not relevant_sections:
        return "I don't have enough information to answer that."

    context = "\n\n".join(relevant_sections)

    return generate_response(
        question,
        context,
    )