from src.services.knowledge_base import load_knowledge_base
from src.services.retriever import retrieve


def test_retrieve_refund_information():
    knowledge_base = load_knowledge_base("data/faq.txt")

    results = retrieve("How long does a refund take?", knowledge_base)

    assert len(results) > 0
    assert "REFUNDS" in results[0]