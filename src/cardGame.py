from fastapi import FastAPI, HTTPException
from typing import List
from cardModels import Rank, Suit, Card, Player, PlayerIn, Game

app = FastAPI()

# Simulated game state
games = {}

@app.post("/api/games/", response_model=int)
async def create_game(player: PlayerIn):
    game_id = len(games) + 1
    new_game = Game()
    games[game_id] = new_game
    return game_id


@app.post("/api/games/{game_id}/join/")
async def join_game(game_id: int, player: PlayerIn):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    games[game_id].add_player(Player(player.name))
    return {"message": f"{player.name} has joined the game."}


@app.post("/api/games/{game_id}/start/")
async def start_game(game_id: int):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    games[game_id].start_game()
    return {"message": f"Game has started. Game# {game_id}"}


@app.post("/api/games/{game_id}/all_cards_by_player/")
async def all_cards_by_player(game_id: int):
    print(f"Game_id: {game_id}")
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    games[game_id].all_cards_by_player()
    return {"message": "Game has started."}
