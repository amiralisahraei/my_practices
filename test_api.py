from fastapi.testclient import TestClient
from api import app
from fastapi import HTTPException

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}, "The respone is differet"


def test_amir():
    response = client.get("/amir")
    assert response.status_code == 200
    assert response.json() == {"msg": "I am amirali from Iran"}, "The respone is differet for amir request"


