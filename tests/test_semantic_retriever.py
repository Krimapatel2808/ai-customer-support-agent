from src.services.knowledge_base import load_knowledge_base
from src.services.semantic_retriever import semantic_retrieve


def test_semantic_retrieve_refund_information():
    knowledge_base = load_knowledge_base("data/faq.txt")

    results = semantic_retrieve(
        "When will I get my money back?",
        knowledge_base,
    )

    assert len(results) > 0
    assert "REFUNDS" in results[0]

def test_semantic_retrieve_rejects_irrelevant_question():
    knowledge_base = load_knowledge_base("data/faq.txt")

    results = semantic_retrieve(
        "What is the capital of France?",
        knowledge_base,
    )

    assert results == []