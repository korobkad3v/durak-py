from core.card import Card

class PlayerHand:
    def __init__(self, sizeOfHand: int) -> None:
        self.sizeOfHand:int = sizeOfHand
        self.handCards:list[Card] = []

    def addCardToHand(self, cardToAdd:list[Card]):
        if self.sizeOfHand > len(self.handCards):
            self.handCards.append(cardToAdd)
    