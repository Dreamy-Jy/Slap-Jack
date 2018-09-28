from typing import Deque, Tuple, List
from collections import deque
from random import shuffle

# TODO: make this method smaller. 
def generate_deck() -> Deque[Tuple[str, str]]:
    """This method builds the deque that represents the deck."""
    deck: deque = deque(maxlen = 52)

    for card_type in ["spade","heart","clubs","diamond"]:
        for position in ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]:
            deck.append((card_type, position))
    
    return deck


def generate_hands(player_count: int) -> List[Deque]:
    """This method generates all player hands"""
    if type(player_count) != int:
        print("Wrong input type fam") # TODO: add a error raise for this method, and a graceful catch
    elif not (2 <= player_count <= 4):
        print("\tPlayer count is out of range") # TODO: add in an error case of more less players
    return [ deque() for _ in range(player_count)] # TODO: make conditional returns


# TODO vaild cards are 
def deal_cards(player_decks: List[Deque], deck: Deque[Tuple[str, str]]) -> None:
    """ This method distributs cards from a deck in abitary order between players.
    Cards are distributed such that player has close to the same amount of cards
    This method should leave the deck empty and each hand should have cards."""

    for card in range(len(deck)):
        player_decks[card%(len(player_decks))].append(deck.pop())


player_count_prompt: str = "how many players do you want to play?"

deck: Deque[Tuple[str, str]] = generate_deck()
shuffle(deck)

player_hands: List[Deque[Tuple[str , str]]] = generate_hands(int(input(player_count_prompt))) # TODO Create a full solution to allow for handling non-int input
deal_cards(player_hands, deck)

card_pile: Deque[Tuple[str, str]] = deque()



for player_deck in player_hands:
    print("\n")
    print(len(player_deck))
    print(player_deck)

print("\nThis is the whole deck")
print(len(deck))
print(deck) # REMINDER: don't use confiting variable names it straight redefines.

if __name__ == '__main__':