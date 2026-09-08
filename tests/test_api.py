from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@patch("app.main.answer_question")
def test_chat_endpoint(mock_answer_question):
    mock_answer_question.return_value = (
        "You can cancel an order before it has shipped."
    )

    response = client.post(
        "/chat",
        json={"message": "Can I cancel my order?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["answer"] == (
        "You can cancel an order before it has shipped."
    )

    mock_answer_question.assert_called_once_with(
        "Can I cancel my order?"
    )
