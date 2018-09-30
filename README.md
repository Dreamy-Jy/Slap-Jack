# Slapjack Python Implementation

## Rules 

The goal of this game is to collect all the cards deck.

Each player will be given a set of cards selected from a shuffled deck, this set will contain an equal number of card as all other set given to other players in the game. Players cards are given out face down so no player know what cards are in their deck.

Each player places places a card on the center pile and turns over the card. Apon the card's turn over other player have the oppertunity to slap that card.

If the card on top of the pile is Jack of any kind, then the first player to slap it gets to add the entire pile to their deck, and then resuffles their deck.

If the top card is not a jack then all player who slaped the deck must place (if possible) 3 cards on the center pile.

## Rule
- valid names
- valid action keys
- how to play

## Implementation

Use of deque in stead of a standard list:

- This game involves alot of poping and appending, as card flow between player, the deque data structure implements these functions effeciently, helping to improve profromance.

random.shuffle()

Card Representation:
- ('Type', 'position')
    - Types: "spade","heart","clubs","diamond"
    - Positions: "ace","2","3","4","5","6","7","8","9","10","jack","queen","king"
    - Why: this notation allows use to 

Type Hinting
- to prevent errors
    - ```stack: int = 1```

Unit testing (python's built in module)
- separt file
- raising the proper errors

Write DOCSTRINGs for everything
Spell check docstrings

The choice to modify the user's input, and to have error handling without rasing any exceptions
The use of inner methods, methods not used else where in code

My usage of Globals

### Card Distribution Method choice
I had to choose between two methods: The rotating appending of distributed cards method, & all at once distribution.
Choose the rotating distribution method, as it had the same time complexity as the other method, while being easier to
implement and better simulates how an accutal deck of cards is most often distributed.

### Checking Choice


## Tooling

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


Threads to add a automated timing.

Use of curses to better manage keyboard inputs.

Allow for the ablity to exit the game anytime by pressing a character, could true all input getting methods into

### Code Base

Use a player class as opposed to multipule list.

### Game
Allow for multipul rounds
Allow for the ability to exit the game at anytime