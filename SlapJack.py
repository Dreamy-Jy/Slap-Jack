from typing import Deque, Tuple, List
from collections import deque, OrderedDict
from random import shuffle

# TODO: give all decks a max length of 52 to catch errors
# TODO: Consider adding "'"s around each use of a user's name
# TODO: have consistent usage of '==', '!=', 'is', 'not' in your loops and conditionals

Card             = Tuple[str, str]
Deck             = Deque[Card]
Name_And_Control = Tuple[str, str]

# TODO - Use indices for card tuple for readability
SUITE:            int = 0
POSITION:         int = 1
MAX_PLAYERS:      int = 4
MIN_PLAYERS:      int = 2
PENALTY:          int = 3 # FIXME Reword


player_count_prompt:            str = "How many players do you want to play?"
get_name_prompt:                str = "Player {0} what would you like to be called?"
get_unused_name_prompt:         str = "That name (\"{0}\") is all ready being used. Player {1} can you please enter a different name?"
get_action_button_prompt:       str = "{0} what keyboard button would you like to be your slap button?"
get_valid_action_button_prompt: str = "Please enter a valid (any single character) keyboard character. The value you entered (\"{0}\") is either longer than a single character or already taken by another player. {1} can you please choose a different keyboard button?"
slap_prompt:                    str = "You can slap the deck now."
target_card:                    str = "jack"
invalid_player_count_error:     str = "Player count is not an integer within range [1, {0}] exclusive.".format(MAX_PLAYERS +1)

end_game_message:               str = "{0} won the game, after {1} cards where placed Concrats! Thanks for playing!"

def get_player_count() -> int:
    """This method gets the valid player count from the user."""
    reenter_message: str = invalid_player_count_error + " Please enter a valid number"

    try:
        count: int = int(input(player_count_prompt))
    
        while (count > MAX_PLAYERS) or (count < MIN_PLAYERS):
            count = int(input(reenter_message))
        
        return count
    
    except ValueError:    
        return int(input(reenter_message))


def generate_deck() -> Deck:
    """This method builds the deque that represents the deck."""

    card_suites:         List[str] = ["spade","heart","clubs","diamond"]
    card_positions:      List[str] = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    deck:                     Deck = deque(maxlen=52)

    for suite in card_suites:
        for position in card_positions:
            deck.append((suite, position))

    return deck


def generate_player_decks(player_count: int) -> List[Deck]:
    """This method generates all player hands."""

    if type(player_count) != int and (player_count >= MAX_PLAYERS or player_count <= MIN_PLAYERS):
        raise ValueError(invalid_player_count_error)
    
    player_decks: List[Deck] = []

    for _ in range(player_count):
        player_decks.append(deque(maxlen=52))
    
    return player_decks


# TODO validate that the player_decks and the names line up in length and index matching
# TODO make sure players can't have the same names and controls
# TODO Defining rules for valid action buttons (a-z, A-Z, 0-9), make you inputs case insensative
# TODO make name check case insensative
# TODO Consider Auto uncapitalizing user names
# TODO: Consider wrapping your conditional and error statement in methods of_valid_length(name) or is_not_being_used() inner functions
def define_players_names_and_controls(number_of_players: int) -> List[Name_And_Control]:
    """This method allows player to set their names and slap button."""

    if type(number_of_players) != int and (number_of_players >= MAX_PLAYERS or number_of_players <= MIN_PLAYERS):
        raise ValueError(invalid_player_count_error)

    names_and_controls: List[Name_And_Control] = []

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
    if len(move_from_deck) == 0:
        return
    
    move_to_deck.appendleft(move_from_deck.popleft())


def make_pile_slappable(player_names_and_controls: List[Name_And_Control], player_decks: List[Deck], card_pile: Deck, player_debts: Deque[int]) -> None:
    """This is method allows users to slap the pile, and distributes awards and punishments
    based on game rules."""
    
    slaps: str = input(slap_prompt)
    player_controls_list: List[str] = [control[1] for control in player_names_and_controls]
    
    slaps = validate_slaps(slaps, player_controls_list)

    if len(slaps) <= 0:
        return

    if card_pile[0][POSITION] == target_card:
        winners_deck: Deck = player_decks[player_names_and_controls.index(slaps[0])] # type: ignore
        collect_pile(winners_deck, card_pile)
        return
    else:
        for player in slaps:
            for _ in range(PENALTY):
                player_debts.append(player_controls_list.index(player))
        print(player_debts)


def validate_slaps(slaps: str, action_buttons: List[str]) -> str:
    """This method removes all invalid action characters from the slaps string, if the string isn't empty.
    I also removes any duplicate valid control buttons."""

    if len(slaps) == 0:
        return slaps
    
    index = 0

    # removes characters from the string that are not action characters set by users.
    while index < len(slaps):
        if slaps[index] not in action_buttons:
            slaps = slaps.replace(slaps[index], "")
        else:
            index += 1
    
    # removes all character duplicates in a way that preserves order.
    slaps = "".join(OrderedDict.fromkeys(slaps))

    return slaps


def collect_pile(player_deck: Deck, card_pile: Deck) -> None:
    """This method allows player to add all cards on the card pile to their deck."""

    while (len(card_pile) > 0):
        place_card(player_deck, card_pile)
    
    shuffle(player_deck) # type: ignore

    
def clear_player_debts(player_decks: List[Deck], card_pile: Deck, player_debts: Deque[int]) -> None:
    """This method settles all debt, that players have accrued over the course of the game."""
    
    while (len(player_debts) > 0):
        players_deck: Deck = player_decks[player_debts[0]]
        
        place_card(players_deck, card_pile)
        make_pile_slappable(player_names_and_controls, player_decks, card_pile, player_debts)

        player_debts.popleft()

def check_for_winner(player_decks: List[Deck]) -> None:
    """This method checks if any player has won the game, and returns their index. If noone won we return -1."""

    DECK_LIMIT: int = 52

    for player in range(len(player_decks)):
        if len(player_decks[player]) == DECK_LIMIT:
            return player
    
    return -1


def endGame():

if __name__ == '__main__':
    player_count:                                    int = get_player_count()
    player_names_and_controls:    List[Name_And_Control] = define_players_names_and_controls(player_count)
    deck:                                           Deck = generate_deck()
    player_decks:                             List[Deck] = generate_player_decks(player_count)
    card_pile:                                      Deck = deque()
    player_debts:                             Deque[int] = deque()

    shuffle(deck) # type: ignore
    deal_cards(player_decks, deck)
    
    game_round:  int = 0
    game_winner: int = -1

    # Are there any conditions under which this could become infinite?
    while (game_winner < 0): 
        placing_player: int = game_round % player_count
        players_deck:  Deck = player_decks[placing_player]

        clear_player_debts(player_decks, card_pile, player_debts)
        place_card(players_deck, card_pile)
        make_pile_slappable(player_names_and_controls, player_decks, card_pile, player_debts)
        
        game_winner = check_for_winner(player_decks)
        game_round += 1
    
    print(end_game_message.format(game_winner, game_round -1))