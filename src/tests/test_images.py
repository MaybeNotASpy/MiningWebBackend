from starlette.testclient import TestClient

"""
/images GET tests
"""
def test_create_user_success(test_app: TestClient):
    response = test_app.post("/register")
    assert response.status_code == 201


"""
/images POST tests
"""
def test_login_incorrect_username(test_app: TestClient):
    response = test_app.post("/login")
    assert response.status_code == 400



"""
/image/{user_id} GET tests
"""
def test_invalid_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 400


"""
/image/{user_id} DELETE tests
"""
def test_invalid_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 400


"""
/image/{user_id} PATCH tests
"""
def test_invalid_user(test_app: TestClient):
    response = test_app.post("/user/{user_id}")
    assert response.status_code == 400