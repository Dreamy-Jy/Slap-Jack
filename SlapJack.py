from collections import deque
from random import shuffle

#🧐🤓 unit test that the deck is the correct length
# how to 
def generate_deck() -> deque:
    """This method builds the deque that represents the deck."""
    deck: deque = deque(maxlen = 52)

    for card_type in ["spade","heart","clubs","diamond"]:
        for position in ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]:
            deck.append((card_type, position))
    
    return deck


def generate_hands( , ):
    """This method generates all player hands"""


deck: deque = generate_deck()
shuffle(deck))

print(len(deck))
