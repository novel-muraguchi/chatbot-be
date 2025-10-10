from fastapi.testclient import TestClient

from chatbot_be.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
