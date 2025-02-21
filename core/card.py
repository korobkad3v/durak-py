import config as c

class Card:
    def __init__(self, str_rank: str, suit_name: str) -> None:
        self.str_rank:str = str_rank if str_rank in c.RANKS.keys() else None
        self.suit_name:str = suit_name if suit_name in c.SUITS.keys() else None

    def isValidCard(self) -> bool:
        return self.str_rank is not None and self.suit_name is not None

    def getCardIntRank(self) -> int:
        return c.RANKS[self.str_rank]

    def GUICard(self) -> None:
        graphic = f"[{self.str_rank}|{c.SUITS[self.suit_name]}]"

        return graphic
    
    