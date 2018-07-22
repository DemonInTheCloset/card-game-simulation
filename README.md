# card-game-simulation

A short project about a card game, to simulate different play-styles and be able to compare strategies.


Game Rules:
===
The card game is played by two or more players that compete in who gets rid of their cards faster.

- The players start with seven piles (their hand) of cards, each one with one card more than the other, strating from pile 1 with 1 card, up to pile 7 with 7 cards, for a total of 28 cards, only the topmost card of each pile is visible.
- The game starts with a number of piles (playing piles) equal to the number of players that contain one card each, this card is visible.
- The players can move the visible cards from their hands, onto the playing pile that has a neighbour of the card they want to move, ie you can move an 8 into a playing pile that has a 7 or a 9 on top, this pile is updated to display the new card, ie the 8 you moved.
- The players can only see and move the topmost card of their hand (the ones that are visible), when a pile is empty, the player can move one card to the top of it releasing an unkown card from the pile that lost it's card.
- If there are no more movements possible or the players give up their turn, the playing piles are discarded and replaced with new, random cards.
- Once a player gets rid of their cards, the game ends and he has won.

Simulation:
===
Play-styles:
---
- **Null:** Each player gets a turn in wich they can move one card to the playing piles, moving cards inside their hands doesn't end the turn. It's a baseline for the rest of the playstiles, with a predicted win rate of 50-50, as it is wholly dependent on luck.
- **Different speeds:** the players have a ratio of how many moves they can make ie 3:4, for every 3 moves of player 1, player 2 makes 4, this means that if they took 12 seconds to make the moves, 1 would play every 4 seconds, and 2 every three, not that 2 would do four moves and then 1 would do 3.
- **Play AI:** one player would have an algorithm that would choose the string of cards that would allow it to get rid of the most cards, it comes in three levels; 1 takes in account their own hand, 2 takes in account all the players hands, and 3 predicts possible cards in their own hand. (there's also a .5 version for levels 2 and 3 that takes the player and opponent speed into account).
- **Combiened:** Combines the AI with the different speeds.

Objective:
===
Find out most effective play-style: ***¿Brains or Reactiontime?***
