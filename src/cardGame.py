from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum, auto
from typing import List

app = FastAPI()

# Simulated game state
games = {}


class Rank(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_card(self, card: Card):
        self.hand.append(card)


class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.deck = []

    def add_player(self, player: Player):
        self.players.append(player)

    def initialize_deck(self):
        ranks = list(Rank)
        suits = list(Suit)
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]

    def start_game(self):
        self.initialize_deck()
        for player in self.players:
            for _ in range(5):  # Deal 5 cards to each player (adjust as needed)
                card = self.deck.pop()
                player.draw_card(card)


class PlayerIn(BaseModel):
    name: str


@app.post("/api/games/", response_model=int)
async def create_game(player: PlayerIn):
    game_id = len(games) + 1
    new_game = Game()
    new_player = Player(player.name)
    new_game.add_player(new_player)
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
    return {"message": "Game has started."}

