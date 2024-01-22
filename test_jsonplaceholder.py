import requests

ENDPOINT = "https://jsonplaceholder.typicode.com/users"

response = requests.get(ENDPOINT)
print(response)
print(response.status_code)

data = response.json()
print(data)
print(data[0])

status_code = response.status_code
print(status_code)


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert status_code == 200
    pass
