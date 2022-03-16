from starlette.testclient import TestClient


def test_create_user(test_app: TestClient):
    response = test_app.post("/register")
    assert response.status_code == 201


def test_delete_existing_user(test_app: TestClient):
    response = test_app.delete(f"/user/{test_app.user_id}")
    assert response.status_code == 204


def test_delete_nonexistant_user(test_app: TestClient):
    response = test_app.delete("/user/0")
    assert response.status_code == 404