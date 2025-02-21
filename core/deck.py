
from core.card import Card
from core.playerHand import PlayerHand
import config as c
import random

class Deck():
    def __init__(self) -> None:
        self.deckcards:list[Card] = []

    def fill_deck(self):
        for suit in c.SUITS.keys():
            for rank in c.RANKS.keys():
                new_card = Card(str_rank=rank, suit_name=suit)
                if new_card.isValidCard():
                    self.deckcards.append(new_card)

        random.shuffle(self.deckcards)

    def deal_card(self, players:list[PlayerHand]) -> str:
        
        random.shuffle(self.deckcards)
        for i in range(len(players)):
            for _ in range(c.PLAYER_HAND_SIZE):
                players[i].addCardToHand(self.deckcards.pop())
        
        trump_suit_name = self.deckcards[0].suit_name
        return trump_suit_name

        