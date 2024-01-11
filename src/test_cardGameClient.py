import pytest
from fastapi.testclient import TestClient
from cardGame import app

client = TestClient(app)

def test_create_game():
    response = client.post("/api/games/", json={"name": "Game1"})
    assert response.status_code == 200
    assert response.json() == 1


def test_players_join_game():
    players = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    for player in players:
        response = client.post("/api/games/1/join/", json={"name": player})
        assert response.status_code == 200
        assert response.json() == {"message": f"{player} has joined the game."}

def test_start_game():
    response = client.post("/api/games/1/start/")
    assert response.status_code == 200
    assert "Game has started." in response.json()["message"]

def test_show_all_players_cards_game():
    response = client.post("/api/games/1/all_cards_by_player/", json={"name": "Game1"})
    assert response.status_code == 200
    assert response.json() == {"message": "Game has started."}