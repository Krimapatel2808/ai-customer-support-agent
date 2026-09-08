from src.services.agent import answer_question


def test_answer_question_with_supported_query():
    answer = answer_question("Can I cancel my order?")

    assert answer
    assert "cancel" in answer.lower()


def test_answer_question_with_unsupported_query():
    answer = answer_question("What is the capital of France?")

    assert answer == "I don't have enough information to answer that."