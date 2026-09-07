from src.services.knowledge_base import load_knowledge_base


def test_load_knowledge_base():
    content = load_knowledge_base("data/faq.txt")

    assert content
    assert "RETURNS" in content
    assert "REFUNDS" in content
    