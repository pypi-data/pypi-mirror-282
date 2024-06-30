import numpy as np
from .GameState import GameState, Null
from .Piece import Piece, PieceType, PieceColor, pieceTypeFromRepr
from .Agent import Agent

class AntiChessGame:
    def __init__(self, boardState=None, colorToMove=None, singlePlayer=True, showRules=False):
        if boardState is not None and colorToMove is None:
            raise ValueError("If defining board state, color to move must also be defined.")
        if boardState is None and (colorToMove is not None or colorToMove != PieceColor.WHITE):
            print("Board state not defined. Initializing new board and defaulting color to move as white.")

        if colorToMove is None:
            colorToMove = PieceColor.WHITE

        self.showRules = showRules

        self.gs = GameState(boardState=boardState, colorToMove=colorToMove, singlePlayer=singlePlayer)

    def play(self):
        assert self.gs.singlePlayer == False, "Use playAgent() to play against an agent in single player mode."
        if self.showRules:
            print("""Rules:
                    1. All pieces move the same as they do in regular chess, with the exception of castling and en passant, neither of which is allowed.
                    2. Capturing the king in AntiChess does not end the game.
                    3. The winner is the first person to have all of their pieces captured.
                    4. If you can capture an opponent's piece during your turn, you must capture it.
                    5. Moves must be entered in UCI chess notation.
                    6. Typing 'moves' into the prompt will print a list of valid moves for the turn.
                    7. Typing 'quit' into the prompt will forfeit the game. By default, your opponent will win.

                    """)
        while True:
            if self.gs.game_over():
                winner = "black" if self.gs.black_score() == 0 else "white"
                print(f"Game Over! {winner} won.")
                break
            self.display_board()
            if self.__get_move():
                if self.gs.colorToMove == PieceColor.WHITE:
                    print("Black wins by forfeit.")
                    break
                else:
                    print("White wins by forfeit.")
                    break

    def playAgent(self, strategy=None, agentColor=PieceColor.BLACK):
        assert self.gs.singlePlayer == True, "Use play() to play against an agent in two player mode."
        assert agentColor == PieceColor.WHITE or agentColor == PieceColor.BLACK, "Agent color must be black or white."
        agent = Agent(strategy=strategy, color=agentColor)
        agentcolorStr = "black" if agentColor == PieceColor.BLACK else "white"
        if self.showRules:
            print("""Rules:
                    1. All pieces move the same as they do in regular chess, with the exception of castling and en passant, neither of which is allowed.
                    2. Capturing the king in AntiChess does not end the game.
                    3. The winner is the first person to have all of their pieces captured.
                    4. If you can capture an opponent's piece during your turn, you must capture it.
                    5. Moves must be entered in UCI chess notation.
                    6. Typing 'moves' into the prompt will print a list of valid moves for the turn.
                    7. Typing 'quit' into the prompt will forfeit the game. By default, your opponent will win.

                    """)
        while True:
            if self.gs.game_over():
                winner = "black" if self.gs.black_score() == 0 else "white"
                print(f"Game Over! {winner} won.")
                break
            self.display_board()
            if self.gs.colorToMove == agentColor:
                print(f"{agentcolorStr} move > thinking...", end="", flush=True)
                uci_move = agent.get_move(self.gs)
                self.gs.do_move(uci_move, inplace=True)
                print(f"\r{agentcolorStr} move > {uci_move}                   ")
            elif self.__get_move():
                if self.gs.colorToMove == PieceColor.WHITE:
                    print("Black wins by forfeit.")
                    break
                else:
                    print("White wins by forfeit.")
                    break

    def display_board(self):
        board = np.flip(self.gs.board.transpose(), axis=0)
        print()
        for i in range(8, 0, -1):
            row_str = " ".join([str(x) for x in board[8-i]])
            print(f"{i}│ {row_str}")
        print("  ————————————————")
        print("   a b c d e f g h")
        print()

    def __get_move(self): # returns True if quitting
        while True:
            toMove = "white" if self.gs.colorToMove == PieceColor.WHITE else "black"
            try:
                move = input(f"{toMove} move > ")
                if move == "quit":
                    return True
                if move == "moves":
                    print(self.gs.available_moves())
                else:
                    self.gs.do_move(move, inplace=True)
                    break
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print(f"Something went wrong: {e}")
                break
