from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_generate_excuse():
    payload = {"situation": "Late for work", "absurdity_level": 5}
    response = client.post("/generate", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "excuse" in response.json()["data"]
