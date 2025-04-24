from app import app

def test_index_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Welcome to Task Manager" in response.data
