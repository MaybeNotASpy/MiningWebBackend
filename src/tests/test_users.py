from starlette.testclient import TestClient

"""
/register POST tests
"""
def test_create_user_success(test_app: TestClient):
    response = test_app.post("/register")
    assert response.status_code == 201


def test_create_user_duplicate(test_app: TestClient):
    response = test_app.post("/register")
    assert response.status_code == 400


def test_create_user_missing_password(test_app: TestClient):
    response = test_app.post("/register")
    assert response.status_code == 400


"""
/login POST tests
"""
def test_login_incorrect_username(test_app: TestClient):
    response = test_app.post("/login")
    assert response.status_code == 400


def test_login_incorrect_password(test_app: TestClient):
    response = test_app.post("/login")
    assert response.status_code == 400


def test_login_success(test_app: TestClient):
    response = test_app.post("/login")
    assert response.status_code == 201


"""
/users/whoami GET tests
"""
def test_whoami_successful(test_app: TestClient):
    response = test_app.post("/users/whoami")
    assert response.status_code == 200


def test_whoami_no_auth(test_app: TestClient):
    response = test_app.post("/users/whoami")
    assert response.status_code == 401


def test_whoami_invalid_token(test_app: TestClient):
    response = test_app.post("/users/whoami")
    assert response.status_code == 400


"""
/user/{user_id} DELETE tests
"""
def test_invalid_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 400


def test_diff_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 403


def test_unauth_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 401


def test_delete_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 200
