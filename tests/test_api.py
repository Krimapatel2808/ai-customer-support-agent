from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_chat_endpoint():
    response = client.post(
        "/chat",
        json={"message": "Can I cancel my order?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert data["answer"]