
from src.services.knowledge_base import load_knowledge_base
from src.services.semantic_retriever import semantic_retrieve


TEST_CASES = [
    # Supported questions
    ("How long does a refund take?", "REFUNDS"),
    ("When will I get my money back?", "REFUNDS"),
    ("Can I get my money returned to my card?", "REFUNDS"),

    ("Can I cancel my order before it ships?", "ORDER CANCELLATION"),
    ("I want to stop an order that hasn't shipped yet.", "ORDER CANCELLATION"),

    ("How many days does delivery take?", "SHIPPING"),
    ("When should I expect my package?", "SHIPPING"),

    ("Can I return a product after receiving it?", "RETURNS"),
    ("Can I send back a personalized product?", "RETURNS"),

    ("When can I contact customer support?", "SUPPORT"),
    ("What are your support hours?", "SUPPORT"),

    # Unsupported questions
    ("What is the capital of France?", None),
    ("Do you sell laptops?", None),
    ("How do I book a flight?", None),
    ("What is the weather today?", None),
]


def test_semantic_retrieval_evaluation():
    knowledge_base = load_knowledge_base("data/faq.txt")

    supported_correct = 0
    supported_total = 0

    unsupported_correct = 0
    unsupported_total = 0

    for question, expected_category in TEST_CASES:
        results = semantic_retrieve(
            question,
            knowledge_base,
            top_k=2,
            threshold=0.5,
        )

        if expected_category is None:
            unsupported_total += 1

            if not results:
                unsupported_correct += 1

        else:
            supported_total += 1

            if results and any(
                expected_category in result
                for result in results
            ):
                supported_correct += 1

    supported_accuracy = supported_correct / supported_total
    unsupported_accuracy = unsupported_correct / unsupported_total
    overall_accuracy = (
        (supported_correct + unsupported_correct)
        / (supported_total + unsupported_total)
    )

    print(f"\nSupported retrieval: {supported_accuracy:.2%}")
    print(f"Unsupported rejection: {unsupported_accuracy:.2%}")
    print(f"Overall accuracy: {overall_accuracy:.2%}")

    assert supported_accuracy >= 0.80
    assert unsupported_accuracy >= 0.80