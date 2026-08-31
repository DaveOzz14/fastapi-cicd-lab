from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from FastAPI"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP"
    }


def test_get_user():
    response = client.get("/users/10")

    assert response.status_code == 200
    assert response.json() == {
        "id": 10,
        "name": "David"
    }