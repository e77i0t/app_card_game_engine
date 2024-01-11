import pytest
from fastapi.testclient import TestClient
from cardGame import app

client = TestClient(app)

def test_create_game():
    response = client.post("/api/games/", json={"name": "Player1"})
    assert response.status_code == 200
    assert response.json() == 1

def test_join_game():
    client.post("/api/games/", json={"name": "Player1"})
    response = client.post("/api/games/1/join/", json={"name": "Player2"})
    assert response.status_code == 200
    assert response.json() == {"message": "Player2 has joined the game."}


def test_join_game_twice():
    client.post("/api/games/", json={"name": "Player2"})
    response = client.post("/api/games/1/join/", json={"name": "Player2"})
    assert response.status_code == 200
    assert response.json() == {"message": "Player2 has joined the game."}
    client.post("/api/games/", json={"name": "Player2"})
    response = client.post("/api/games/1/join/", json={"name": "Player2"})
    assert response.status_code == 200
    assert response.json() == {"message": "Player2 has joined the game."}


def test_start_game():
    client.post("/api/games/", json={"name": "Player1"})
    client.post("/api/games/1/join/", json={"name": "Player2"})
    response = client.post("/api/games/1/start/")
    assert response.status_code == 200
    assert response.json() == {"message": "Game has started."}