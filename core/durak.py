from core.deck import Deck
from core.playerHand import PlayerHand
from core.deck import Card

import config as c

class Durak:
    def __init__(self, numOfPlayers:int) -> None:
        self.deck:Deck = Deck()
        self.players:list[PlayerHand] = []
        self.numOfPlayers:int = numOfPlayers if 2 <= numOfPlayers <= 6 else 2
        self.attacker:int = None
        self.defender:int = None
        self.trump_suit:str = None

    def setup(self):
        self.__create_players()
        self.deck.fill_deck()
        self.trump_suit = self.deck.deal_card(players=self.players)
    
    def __create_players(self) -> None:
        for _ in range(self.numOfPlayers):
            self.players.append(PlayerHand(c.PLAYER_HAND_SIZE))

    # подсчет какая карта какую бьет 
    # trump_suit, то есть козырь, в данный момент для тестов - передаваемый параметр, а в финальной версии поле этого класса
    def compareCards(self, attackCard: Card, defendCard: Card, trump_suit: str):
        return (attackCard.suit_name == defendCard.suit_name and attackCard.getCardIntRank() > defendCard.getCardIntRank()) or (attackCard.suit_name == trump_suit and defendCard.suit_name != trump_suit)


    def test1(self):
        card1 = Card(str_rank="6", suit_name="clubs")
        card2 = Card(str_rank="7", suit_name="clubs")
        expected_value = False

        if self.compareCards(attackCard=card1, defendCard=card2, trump_suit="spades") is expected_value:
            print(f"Test 1 passed: {card1.GUICard()} cant beat {card2.GUICard()}")

    def test2(self):
        card1 = Card(str_rank="7", suit_name="clubs")
        card2 = Card(str_rank="6", suit_name="clubs")
        expected_value = True
        

        if self.compareCards(attackCard=card1, defendCard=card2, trump_suit="spades") is expected_value:
            print(f"Test 2 passed: {card1.GUICard()} beat {card2.GUICard()} ")

    def test3(self):
        card1 = Card(str_rank="6", suit_name="spades")
        card2 = Card(str_rank="Q", suit_name="clubs")
        expected_value = True
        trump_suit = "spades"
        if self.compareCards(attackCard=card1, defendCard=card2, trump_suit=trump_suit) is expected_value:
            print(f"Test 3 passed: {card1.GUICard()} beat {card2.GUICard()} trump suit is {trump_suit}")
    
    def test4(self):
        card1 = Card(str_rank="10", suit_name="spades")
        card2 = Card(str_rank="A", suit_name="spades")
        expected_value = False
        trump_suit = "spades"
        if self.compareCards(attackCard=card1, defendCard=card2, trump_suit=trump_suit) is expected_value:
            print(f"Test 4 passed: {card1.GUICard()}  cant beat {card2.GUICard()} trump suit is {trump_suit}")