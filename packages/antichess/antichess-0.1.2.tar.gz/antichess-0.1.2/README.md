
# antichess

`antichess` is a Python package for playing AntiChess, a chess variant where the goal is to have all of your pieces captured by your opponent. This package supports both two-player games and single-player games using strategic decision-making techniques such as Minimax with alpha-beta pruning, MCTS (Monte Carlo Tree Search), epsilon-greedy BFS (Breadth-First Search), and BFS.

## Features

- **Two-Player Mode**: Play against another human player.
- **Single-Player Mode**: Play against an automated opponent using advanced strategic techniques.
- **Rules and Gameplay**: Includes basic AntiChess rules and gameplay functionalities.
- **Board Display**: Visual representation of the board and game state.

## Installation

To use the `AntiChessGame` package, ensure you have Python 3.6 or higher installed. You can install the package directly if it is available on PyPI:

```bash
pip install antichess
```

## Usage

### Creating and Playing a New Two-Player Game

To create a new Two-Player AntiChess game:
```python
from antichess.AntiChessGame import AntiChessGame

# Set showRules as `True` to print rules before the game begins
game = AntiChessGame(singlePlayer=False, showRules=False)

game.play()
```

### Creating and Playing a New Single-Player Game

To play a single-player game against an automated opponent using a specified strategy:
```python
from antichess.AntiChessGame import AntiChessGame
from antichess.Piece import PieceColor

# Set showRules as `True` to print rules before the game begins
game = AntiChessGame(singlePlayer=True, showRules=False)

# If not specified, agentColor will default to black
game.playAgent(strategy="minimax-depth=5", agentColor=PieceColor.WHITE)
```

#### Currently Valid Strategies
- **Random** (`"random"`) selects a move at random.
- **BFS** (`"bfs-depth=2"`, `"bfs-depth=3"`) uses a breadth-first search.
- **Epsilon-Greedy BFS** (`"bfs-depth=2-e=.1"`, `"bfs-depth=3-e=.1"`) integrates an epsilon-greedy policy with the established BFS approach.
- **MCTS** (`"mcts-sims=1000-depth=10"`, `"mcts-sims=1000-depth=15"`, `"mcts-sims=1500-depth=10"`) performs a Monte Carlo Tree Search.
- **Minimax with Alpha-Beta Pruning** (`"minimax-depth=3"`, `"minimax-depth=5"`) uses the minimax algorithm with alpha-beta pruning.

### Game Rules

1.  All pieces move like they do in regular chess, except for castling and en passant, which are not allowed.
2.  Capturing the king does not end the game.
3.  The winner is the first player to have all of their pieces captured.
4.  If a piece can be captured during your turn, you must capture it.
5.  Moves must be entered in UCI chess notation.
6.  Typing 'moves' will print a list of valid moves for the current turn.
7.  Typing 'quit' will forfeit the game, with the opponent being the winner by default.

### Board Display

The board is displayed with ranks and files labeled.

## License

This package is licensed under the [GNU General Public License v3.0 License](.https://choosealicense.com/licenses/gpl-3.0/). See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please contact [divit.rawal+antichess@gmail.com](mailto:divit.rawal+antichess@gmail.com)

