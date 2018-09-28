# Slapjack Python Implementation

## Rules 

The goal of this game is to collect all the cards deck.

Each player will be given a set of cards selected from a shuffled deck, this set will contain an equal number of card as all other set given to other players in the game. Players cards are given out face down so no player know what cards are in their deck.

Each player places places a card on the center pile and turns over the card. Apon the card's turn over other player have the oppertunity to slap that card.

If the card on top of the pile is Jack of any kind, then the first player to slap it gets to add the entire pile to their deck, and then resuffles their deck.

If the top card is not a jack then all player who slaped the deck must place (if possible) 3 cards on the center pile.

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

### Card Distribution Method choice
I had to choose between two methods: The rotating appending of distributed cards method, & all at once distribution.
Choose the rotating distribution method, as it had the same time complexity as the other method, while being easier to
implement and better simulates how an accutal deck of cards is most often distributed.

## Possible Improvements

Threads to add a automated timing.

Use of curses to better manage keyboard inputs.

Improve code readablitly and type hinting by using custom types
Better type hinting and 