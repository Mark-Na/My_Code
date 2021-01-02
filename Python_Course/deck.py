from random import shuffle
import card
class Deck:
    def __init__(self):
        allowed_suit = ['Hearts','Diamonds','Clubs','Spades']
        allowed_value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for value in (allowed_value):
            for suit in (allowed_suit):
                self.cards.append(card.Card(suit,value))
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self,num):
        dealt = []
        while num!=0:
            if len(self.cards) == 0:
                raise ValueError("All cards have been dealt")
            elif num>len(self.cards):
                num = len(self.cards)
            
            else:
                dealt.append(self.cards.pop())
                num-=1
        return dealt
    
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards
    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,num):
        return self._deal(num)

    def __iter__ (self):
        return iter(self.cards)

my_deck = Deck()
my_deck.shuffle()
for card in my_deck:
    print(card)


