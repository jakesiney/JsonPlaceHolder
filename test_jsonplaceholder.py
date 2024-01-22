import requests

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_create_task():
    payload = {
        "content": "test",
        "user_id": "test",
        "task_id": "test",
        "is_done": False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
