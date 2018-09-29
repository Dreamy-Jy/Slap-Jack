from typing import Deque, Tuple, List
from collections import deque
from random import shuffle

Card = Tuple[str, str]
Deck = Deque[Card]

player_count_prompt: str = "how many players do you want to play?"

# TODO: make this method smaller. 
def generate_deck() -> Deck:
    """This method builds the deque that represents the deck."""
    card_types = ["spade","heart","clubs","diamond"]
    card_positions = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    return deque([(ct, p) for ct in card_types for p in card_positions], maxlen=52)


def generate_hands(player_count: int) -> List[Deque]:
    """This method generates all player hands"""
    if type(player_count) != int:
        print("Wrong input type fam") # TODO: add a error raise for this method, and a graceful catch
    elif not (2 <= player_count <= 4):
        print("\tPlayer count is out of range") # TODO: add in an error case of more less players
    return [ deque() for _ in range(player_count)] # TODO: make conditional returns


# TODO vaild cards are 
def deal_cards(player_decks: List[Deck], deck: Deck) -> None:
    """ This method distributs cards from a deck in abitary order between players.
    Cards are distributed such that player has close to the same amount of cards
    This method should leave the deck empty and each hand should have cards."""

    for card in range(len(deck)):
        player_decks[card%(len(player_decks))].append(deck.pop())


def place_card(move_from_deck: Deck, move_to_deck: Deck) -> None:
    """This method allow you to movecards from the top of one deck to the top of another."""
    move_to_deck.appendleft(move_from_deck.popleft())


if __name__ == '__main__':
    number_of_players: int = int(input(player_count_prompt))

    deck: Deck = generate_deck()
    shuffle(deck)

    # TODO Considering rename hands to decks to avoid confusion
    player_hands: List[Deck] = generate_hands(number_of_players) # TODO Create a full solution to allow for handling non-int input
    deal_cards(player_hands, deck)

    card_pile: Deck = deque()
    
    game_round: int = 0 # TODO considering this var represents, each time a player plays choose a better name
    game_winner: int = -1
    while(game_winner < 0):
        placeing_player: int = game_round % number_of_players
        players_deck: Deck = player_hands[placeing_player]

        place_card(players_deck, card_pile)
        print(card_pile)
        # open_slap_pile(player_controls, player_hands)
        # game_winner = check_for_winner(player_hands)
        game_round += 1
        game_winner = 1
    # end_game() # or play_again()