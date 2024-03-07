import pytest
import json

@pytest.mark.parametrize(
        ("headers", "body", "status", "code"),
        [
            ({}, {}, 415, 101),
            ({"Content-Type": "application/json"}, {"username": 1, "password": 1}, 400 ,104),
            ({"Content-Type": "application/json"}, {"username": "", "password": "test"}, 400 ,105),
            ({"Content-Type": "application/json"}, {"username": "test", "password": ""}, 400 ,105),
            ({"Content-Type": "application/json"}, {"username": "test", "password": "test"}, 201 ,100),
            ({"Content-Type": "application/json"}, {"username": "test", "password": "test"}, 409 ,106),
        ]
    )
def test_create_user(client, headers, body, status, code):
    result = client.post(
            "/api/v1/users",
            data=json.dumps(body),
            headers=headers
        )
    assert result.status_code == status
    assert result.get_json()["code"] == code

