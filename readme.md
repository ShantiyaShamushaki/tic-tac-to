# Tic-Tac-Toe Game with Minimax Algorithm and Alpha-Beta Pruning
## Overview
This Python script implements a console-based Tic-Tac-Toe game using a game tree with the Minimax algorithm and Alpha-Beta pruning for the AI player. The game allows a human player to play against an AI opponent, which makes optimal moves to maximize its chances of winning or force a draw.

## Features
- Human vs AI Tic-Tac-Toe gameplay.
- Minimax algorithm with Alpha-Beta pruning for efficient decision-making.
- Interactive console interface for player moves.
- Clear display of the game board after each move.
- Endgame detection to declare the winner or a draw.

## Classes
### Game
The Game class represents the Tic-Tac-Toe game and includes the following methods:

- `__init__(self):` Initializes the game with an empty 3x3 board and sets the starting turn to player 1.
- `change_turn(self):` Switches the turn between players.
- `available_moves(self):` Generates available moves on the current board.
- `evaluate(self, depth, is_maximizer, alpha, beta):` Evaluates the game state using the Minimax algorithm with Alpha-Beta pruning.
- `ai_move(self):` Determines the AI's optimal move using the Minimax algorithm and updates the game board.
- `rows(self), columns(self), diagonals(self):` Generates iterators for rows, columns, and diagonals of the game board.
- `check_winner(self): `Checks for a winner or a draw on the current board.
- `__str__(self)`: Returns a string representation of the current game board.

## Usage
1. Run the script.
2. Choose your symbol (1 for X, 0 for O).
3. Input moves for human player and witness the AI's optimal moves.
4. The game ends when a player wins, loses, or the game ends in a draw.

## Example
```
python
Copy code
if __name__ == "__main__":
    player = int(input("Choose your Symbol (1 => X, 0 => O): "))
    game = Game()
    while True:
        print(game)
        result_game = game.check_winner()
        if result_game is not None:
            if result_game == 100:
                print("X won!")
            elif result_game == -100:
                print("O won!")
            else:
                print("Draw!")
            break
        if game.turn == player:
            i, j = map(int, input("Enter a tuple like (0-2, 0-2):").split())
            game.map[i][j] = player
        else:
            game.ai_move()
        game.change_turn()
```

### Future Improvements
- Implement a graphical user interface (GUI) for a more user-friendly experience.
- Allow players to choose their symbols dynamically.
- Optimize the AI algorithm further for enhanced performance.
- Handle invalid user inputs gracefully.
- Feel free to explore and enhance the code to suit your preferences and requirements. Happy gaming!



