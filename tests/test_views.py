from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_manifests() -> None:
    response = client.get("/manifests/")
    assert response.status_code == 200
