# Slapjack Python Implementation

## Rules 

The goal of this game is to collect all the cards deck.

Each player will be given a set of cards selected from a shuffled deck, this set will contain an equal number of card as all other set given to other players in the game. Players cards are given out face down so no player know what cards are in their deck.

Each player places places a card on the center pile and turns over the card. Apon the card's turn over other player have the oppertunity to slap that card.

If the card on top of the pile is a Jack of any kind, then the first player to slap it gets to add the entire pile to their deck, and then resuffles their deck.

If the top card is not a jack then all player who slaped the deck must place (if possible) 3 cards on the center pile.

## Running the Game

from the command line, cd into the directory you downloaded the 'Slapjack.py' file into and run 'python3 Slapjack.py'

## Playing the Game

When the game startes you'll tell the program how many people are playing with you. It's assumped that only humans are playing this game and they're using the same keyboard to enter inputs.

After entering the amount of players you and all other players will be prompted to enter names and actions buttons(single characters only). Your name is what the game will refer to you as, and the action button will represent your slap.

When the deck is opened to be slaped, all player that choose to slap will slap and then press 'enter/return'. 

## Implementation Notes
I use deque instead of a standard list, because they offer faster appends() and pops(), actions that are heavly used in this program. 

I used pythons Type Hinting functionally to help in debugging and error catching. I used mypy as my type checker.

While I know it is an anti to modify input, for the validate_slaps() this was appropriate. Because it's better to give the end user the befiet of the doubt. Like in methods used by other programmer I do raise errors.

Card Distribution Method choice: 
- I had to choose between two methods: The rotating appending of distributed cards method, & all at once distribution.I choose the rotating distribution method, as it had the same time complexity as the other method, while being easier to implement and better simulates how an accutal deck of cards is most often distributed


### Code Style
Linting
- autopep8 
Us of type hints
- Static type checker mypy...
not using list conprehensions

usage of math-like <,>,<=,>= syntax
- minimize conditionals
- while not being too diffcult for users to use

### How I decided wheither or not raise an error or handle silently, and handle exceptions silently
- I felt that because this is designed to be a game for a general public rasing errors would be of little help to average user so exception were rasied sparingly and only in instances where a programmer might error and not the user.
- If the user errored the program would rerun

## Possible Improvements

seperate property list for players into single list or a player class



Use of curses to better manage keyboard inputs.

Allow for the ablity to exit the game anytime by pressing a character, could true all input getting methods into

### Code Base
Use a player class as opposed to multipule list.

### Game
Allow for multipule rounds
Allow for the ability to exit the game at anytime
Make inputs timed