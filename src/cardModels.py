# cardModels.py
from pydantic import BaseModel
from enum import Enum, auto


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


    def all_cards_by_player(self):
        for player in self.players:
            print(f"{player.name} has {len(player.hand)} cards in their hand.")
            for card in player.hand:
                print(f"\t{card.rank} of {card.suit}")


class PlayerIn(BaseModel):
    name: str
