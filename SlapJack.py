from typing import Deque, Tuple, List
from collections import deque
from random import shuffle

# TODO: give all decks a max length of 52 to catch errors
# TODO: Consider adding "'"s around each use of a user's name
# TODO: have consistent usage of '==', '!=', 'is', 'not' in your loops and conditionals

Card             = Tuple[str, str]
Deck             = Deque[Card]
Name_And_Control = Tuple[str, str]

# TODO - Use indices for card tuple for readability
SUITE:       int = 0
NUM:         int = 1
MAX_PLAYERS: int = 4
MIN_PLAYERS: int = 2

player_count_prompt:            str = "How many players do you want to play?"
get_name_prompt:                str = "Player {0} what would you like to be called?"
get_unused_name_prompt:         str = "That name (\"{0}\") is all ready being used. Player {1} can you please enter a different name?"
get_action_button_prompt:       str = "{0} what keyboard button would you like to be your slap button?"
get_valid_action_button_prompt: str = "Please enter a valid (any single character) keyboard character. The value you entered (\"{0}\") is either longer than a single character or already taken by another player. {1} can you please choose a different keyboard button?"
slap_prompt:                    str = "You can slap the deck now."
target_card:                    str = "jack"
invalid_player_count_error:     str = "Player count is not an integer within range [1, {0}] exclusive.".format(MAX_PLAYERS +1)

debt: Deque[int] = deque()

def get_player_count() -> int:
    try:
        count: int = int(input(player_count_prompt))
    
        while (count > MAX_PLAYERS) or (count < MIN_PLAYERS):
            count = int(input(invalid_player_count_error + " Please enter a valid number"))
        
        return count
    
    except (ValueError):
    
        return int(input(invalid_player_count_error + " Please enter a valid number"))


def generate_deck() -> Deck:
    """This method builds the deque that represents the deck."""

    card_suites:         List[str] = ["spade","heart","clubs","diamond"]
    card_positions:      List[str] = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    deck:                     Deck = deque(maxlen=52)

    for suite in card_suites:
        for position in card_positions:
            deck.append((suite, position))

    return deck

def generate_player_decks(player_count: int) -> List[Deque]:
    """This method generates all player hands"""

    if type(player_count) is int and (player_count <= MAX_PLAYERS and player_count >= MIN_PLAYERS):
        for _ in range(player_count):
            player_decks.append(deque(maxlen=52))
    else:
        raise ValueError(invalid_player_count_error)
    
    return player_decks

# TODO validate that the player_decks and the names line up in length and index matching
# TODO make sure players can't have the same names and controls
# TODO Defining rules for valid action buttons (a-z, A-Z, 0-9), make you inputs case insensative
# TODO make name check case insensative
# TODO Consider Auto uncapitalizing user names
# TODO: Consider wrapping your conditional and error statement in methods of_valid_length(name) or is_not_being_used() inner functions

def define_players_names_and_controls(number_of_players: int) -> List[Name_And_Control]:
    """This method allows player to set their names and slap button"""
    # Describe the overall how this loop works
    for player in range(number_of_players):

        name: str = input(get_name_prompt.format(player +1))

        # TODO make the validating loops functions, and the uniqueness checkers a function for both name and action_button.
        while len(name) < 0 or (name in [val[0] for val in names_and_controls]):
            name = input(get_unused_name_prompt.format(name, player +1))
        
        action_button: str = input(get_action_button_prompt.format(name))

        while len(action_button) != 1 or (action_button in [val[1] for val in names_and_controls]):
            action_button = input(get_valid_action_button_prompt.format(action_button, name))

        names_and_controls.append((name, action_button))
    
    return names_and_controls

# TODO vaildate if all cards are valid 
def deal_cards(player_decks: List[Deck], deck: Deck) -> None:
    """ This method distributs cards from a deck in abitary order between players.
    Cards are distributed such that player has close to the same amount of cards.
    This method should leave the deck empty and each hand should have cards."""

    for card in range(len(deck)):
        player_decks[card %len(player_decks)].append(deck.pop())


# TODO: add a timed print out of who's printing out what...
def place_card(move_from_deck: Deck, move_to_deck: Deck) -> None:
    """This method allow you to movecards from the top of one deck to the top of another."""
    move_to_deck.appendleft(move_from_deck.popleft())


# TODO: 
def make_pile_slappable(player_controls: List[Name_And_Control], player_decks: List[Deck], pile: Deck) -> None:
    """This is method allows users to slap the pile, and distributes awards
    and punishments based on game rules"""
    
    slaps: str = input(slap_prompt)
    slaps = validate_slaps(slaps, [control[1] for control in player_controls])

    # NOTE - Avoid unnecesary nested branch statements
    # if len(slaps) <= 0:
    #     return

    # if pile[0][1] is target_card:
        # print the index of the winning player could make an internal method find winnier
        # for i in range(len(player_controls)):
        #     if player_controls[i][1] == slaps[0]:
        #         print("player {0}, won this round".format(i))
    # else:
    #     pass

    if len(slaps) > 0:

        if pile[0][1] == target_card:

            # print the index of the winning player could make an internal method find winnier
            for i in range(len(player_controls)):
                if player_controls[i][1] == slaps[0]:
                    print("player {0}, won this round".format(i))
        else:
            pass


# TODO make this an inner function of make_pile_slappable()
def validate_slaps(slaps: str, action_buttons: List[str]) -> str:
    """This method removes all invalid action characters from the slaps string, if the string isn't empty and
    the first character in the slap string is not a valid input string."""

    print(action_buttons)

    if len(slaps) == 0 or slaps[0] in action_buttons:
        return slaps
    
    index = 0

    while index < len(slaps):
        if slaps[index] not in action_buttons:

            # NOTE - It is an antipattern to "modify" input, you should just accept or reject it

            slaps = slaps.replace(slaps[index], "")
        else:
            index += 1

    return slaps


# TODO Create a full solution to allow for handling non-int input tp the generate_player_decks()
# TODO Consider renameing hands to decks to avoid confusion
# TODO consider giving game_round a better name. It represents, each time a player plays choose a better name
if __name__ == '__main__':
    player_count: int = get_player_count()
    player_names_and_controls: List[Name_And_Control] = define_players_names_and_controls(player_count)

    deck: Deck = generate_deck()
    shuffle(deck)

    player_decks: List[Deck] = generate_player_decks(player_count)
    deal_cards(player_decks, deck)

    card_pile: Deck = deque()
    
    game_round:  int = 0
    game_winner: int = -1

    # Are there any conditions under which this could become infinite?
    while (game_winner < 0): 
        placing_player: int = game_round % player_count
        players_deck: Deck = player_decks[placing_player]

        # need to figure out how your handling
        place_card(players_deck, card_pile)
        make_pile_slappable(player_names_and_controls, player_decks, card_pile)

        print(card_pile)
        # open_slap_pile(player_controls, player_decks)
        # game_winner = check_for_winner(player_decks)
        game_round += 1
        if game_round == 3:
            break
    # end_game() # or play_again()