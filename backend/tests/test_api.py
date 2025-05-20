import requests


def test_get_user():
    response = requests.get("http://localhost:8000/users/user", json={"user_id": 1})
    print(response.status_code)
    print(response.content)
    pass


test_get_user()
