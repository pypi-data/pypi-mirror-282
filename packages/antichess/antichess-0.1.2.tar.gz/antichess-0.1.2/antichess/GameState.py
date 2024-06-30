from .Piece import Piece, PieceType, PieceColor, pieceTypeFromRepr
import numpy as np
import copy
from functools import cache #TODO: caching

class Null:
    def __init__(self):
        self.color = PieceColor.EMPTY
        self.type = PieceType.EMPTY

    def __repr__(self):
        return '·'

    def __eq__(self, other):
        return other is None

    def __bool__(self):
        return False

    def isNull(self):
        return True

class GameState():
    def __init__(self, boardState=None, colorToMove=PieceColor.WHITE, singlePlayer=True):
        self.singlePlayer = singlePlayer
        self.white_pieces = []
        self.black_pieces = []
        self.colorToMove = colorToMove
        if boardState is None:
            self.board = self.__setup_new_board()
        else:
            self.board = boardState
            #populate piece lists
            for i in range(8):
                for j in range(8):
                    if boardState[i][j].color == PieceColor.WHITE:
                        self.white_pieces.append(boardState[i][j])
                    elif boardState[i][j].color == PieceColor.BLACK:
                        self.black_pieces.append(boardState[i][j])
        self.last_move = None

    def available_moves(self):
        if self.game_over():
            return []
        colorToMove = self.colorToMove
        moves = []
        assert colorToMove == PieceColor.WHITE or colorToMove == PieceColor.BLACK
        corr_piece_list = None
        if colorToMove == PieceColor.WHITE:
            corr_piece_list = self.white_pieces
        else:
            corr_piece_list = self.black_pieces

        for piece in corr_piece_list:
            if piece.taken: #sanity check
                continue
            if piece.type == PieceType.PAWN:
                moves += self.__available_pawn_moves(piece)
            elif piece.type == PieceType.ROOK:
                moves += self.__available_rook_moves(piece)
            elif piece.type == PieceType.KNIGHT:
                moves += self.__available_knight_moves(piece)
            elif piece.type == PieceType.BISHOP:
                moves += self.__available_bishop_moves(piece)
            elif piece.type == PieceType.QUEEN:
                #should be no overlap
                moves += self.__available_bishop_moves(piece)
                moves += self.__available_rook_moves(piece)
            elif piece.type == PieceType.KING:
                moves += self.__available_king_moves(piece)

        return sorted(self.__filter_forced_take(moves, colorToMove))

    def __filter_forced_take(self, moves, colorToMove):
        force_take_moves = []
        oppColor = PieceColor.BLACK if colorToMove == PieceColor.WHITE else PieceColor.WHITE
        for move in moves:
            endX, endY = self.__square_to_coords(move[2:4])
            if self.board[endX][endY].color == oppColor:
                force_take_moves.append(move)

        if len(force_take_moves) == 0:
            return moves
        return force_take_moves

    def __available_pawn_moves(self, piece):
        available = []
        if self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + 1))
        if piece.y - 1 > -1 and self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y - 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y - 1))
        if self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + 2)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + 2))
        if piece.y - 2 > -1 and  self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y - 2)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y - 2))
        if self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y + 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y + 1))
        if piece.x - 1 > -1 and self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y + 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y + 1))
        if piece.y - 1 > -1 and self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y - 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y - 1))
        if piece.x - 1 > -1 and piece.y - 1 > -1 and self.__is_valid_move(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y - 1)):
            available.append(self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y - 1))
        available += self.__available_pawn_promotions(piece)
        return available

    def __available_pawn_promotions(self, piece):
        av = []
        if piece.color == PieceColor.WHITE and piece.y == 7:
            if piece.y == 7: #already at edge (should never happen, but good check)
                return av
            if self.board[piece.x][piece.y + 1].isNull():
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")
            if piece.x - 1 > -1 and self.board[piece.x - 1][piece.y + 1].color == PieceColor.BLACK:
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y + 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")
            if piece.x + 1 < 8 and self.board[piece.x + 1][piece.y + 1].color == PieceColor.BLACK:
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y + 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")
        elif piece.color == PieceColor.BLACK and piece.y == 1:
            if piece.y == 0: #already at edge (should never happen, but good check)
                return av
            if self.board[piece.x][piece.y - 1].isNull():
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y - 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")
            if piece.x - 1 > -1 and self.board[piece.x - 1][piece.y - 1].color == PieceColor.WHITE:
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x - 1, piece.y - 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")
            if piece.x + 1 < 8 and self.board[piece.x + 1][piece.y - 1].color == PieceColor.WHITE:
                base = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + 1, piece.y - 1)
                av.append(base + "q")
                av.append(base + "n")
                av.append(base + "b")
                av.append(base + "r")

        return av

    def __available_rook_moves(self, piece):
        available = []
        vert = 1
        while piece.y + vert < 8:
            tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + vert)
            if self.__is_valid_move(tent_move):
                available.append(tent_move)
            vert += 1
        vert = -1
        while piece.y + vert > -1:
            tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x, piece.y + vert)
            if self.__is_valid_move(tent_move):
                available.append(tent_move)
            vert -= 1
        horz = 1
        while piece.x + horz < 8:
            tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + horz, piece.y)
            if self.__is_valid_move(tent_move):
                available.append(tent_move)
            horz += 1
        horz = -1
        while piece.x + horz > -1:
            tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + horz, piece.y)
            if self.__is_valid_move(tent_move):
                available.append(tent_move)
            horz -= 1
        return available

    def __available_knight_moves(self, piece):
        available = []
        possible_offsets = {(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)}
        for i, j in possible_offsets:
            if piece.x + i < 8 and piece.x + i > -1 and piece.y + j < 8 and piece.y + j > -1:
                tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + i, piece.y + j)
                if self.__is_valid_move(tent_move):
                    available.append(tent_move)
        return available

    def __available_bishop_moves(self, piece):
        available = []
        possible_unit_offsets = {(1,1), (-1,1), (-1,-1), (1,-1)}
        for unit_offset in possible_unit_offsets:
            multiplicative_factor = 1
            while piece.x + unit_offset[0]*multiplicative_factor < 8 and piece.x + unit_offset[0]*multiplicative_factor > -1 and piece.y + unit_offset[1]*multiplicative_factor < 8 and piece.y + unit_offset[1]*multiplicative_factor > -1:
                tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + unit_offset[0]*multiplicative_factor, piece.y + unit_offset[1]*multiplicative_factor)
                if self.__is_valid_move(tent_move):
                    available.append(tent_move)
                multiplicative_factor += 1

        return available

    def __available_king_moves(self, piece):
        available = []
        possible_offsets = {(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)}
        for i, j in possible_offsets:
            if piece.x + i < 0 or piece.x + i > 7 or piece.y + j < 0 or piece.y + j > 8:
                continue
            tent_move = self.__coords_to_square(piece.x, piece.y) + self.__coords_to_square(piece.x + i, piece.y + j)
            if self.__is_valid_move(tent_move):
                available.append(tent_move)

        return available


    def print_board(self):
        print(np.flip(self.board.transpose(), axis=0))

    def __setup_new_board(self):
        b = np.full((8, 8), Null(), dtype=object)

        for i in range(8):
            p = Piece(PieceType.PAWN, PieceColor.BLACK, i, 6)
            self.black_pieces.append(p)
            b[i][6] = p

        for i in range(8):
            p = Piece(PieceType.PAWN, PieceColor.WHITE, i, 1)
            self.white_pieces.append(p)
            b[i][1] = p

        piece_positions = [
            (PieceType.ROOK, PieceColor.BLACK, 0, 7), (PieceType.ROOK, PieceColor.BLACK, 7, 7),
            (PieceType.ROOK, PieceColor.WHITE, 0, 0), (PieceType.ROOK, PieceColor.WHITE, 7, 0),
            (PieceType.KNIGHT, PieceColor.BLACK, 1, 7), (PieceType.KNIGHT, PieceColor.BLACK, 6, 7),
            (PieceType.KNIGHT, PieceColor.WHITE, 1, 0), (PieceType.KNIGHT, PieceColor.WHITE, 6, 0),
            (PieceType.BISHOP, PieceColor.BLACK, 2, 7), (PieceType.BISHOP, PieceColor.BLACK, 5, 7),
            (PieceType.BISHOP, PieceColor.WHITE, 2, 0), (PieceType.BISHOP, PieceColor.WHITE, 5, 0),
            (PieceType.KING, PieceColor.BLACK, 4, 7), (PieceType.KING, PieceColor.WHITE, 4, 0),
            (PieceType.QUEEN, PieceColor.BLACK, 3, 7), (PieceType.QUEEN, PieceColor.WHITE, 3, 0)
        ]

        for piece_type, color, x, y in piece_positions:
            piece = Piece(piece_type, color, x, y)
            if color == PieceColor.WHITE:
                self.white_pieces.append(piece)
            else:
                self.black_pieces.append(piece)
            b[x][y] = piece

        return b

    def __square_to_coords(self, square):
        col = ord(square[0]) - ord('a')
        row = int(square[1]) - 1
        return col, row  # FLIPPED & zero indexed

    def __coords_to_square(self, x, y):
        square = chr(x + ord('a')) + str(y + 1)
        return square

    def __parse_uci_move(self, uci_move):
        start_square = uci_move[:2]
        startX, startY = self.__square_to_coords(start_square)
        end_square = uci_move[2:4]
        endX, endY = self.__square_to_coords(end_square)
        promoted_piece = uci_move[4] if len(uci_move) == 5 else None
        return startX, startY, endX, endY, promoted_piece

    def __is_castling(self, uci_move):
        startX, startY, endX, endY, promoted_piece = self.__parse_uci_move(uci_move)
        startKing = bool(self.board[startX][startY].type == PieceType.KING)
        return uci_move in {"e1g1", "e1c1", "e8g8", "e8c8"} and startKing

    def __path_not_obstructed(self, startX, startY, endX, endY):
        #checks only straight line paths
        if startX == endX:
            step = 0
            if startY < endY:
                step = 1
            else:
                step = -1
            multiplicative_factor = 1
            while startY + step*multiplicative_factor != endY:
                if not self.board[startX][startY + step*multiplicative_factor].isNull():
                    return False
                multiplicative_factor += 1
        elif startY == endY:
            step = 0
            if startX < endX:
                step = 1
            else:
                step = -1
            multiplicative_factor = 1
            while startX + step*multiplicative_factor != endX:
                if not self.board[startX + step * multiplicative_factor][startY].isNull():
                    return False
                multiplicative_factor += 1
        elif abs(startX - endX) == abs(startY - endY):
            x_step = 1 if startX < endX else -1
            y_step = 1 if startY < endY else -1
            for i in range(1, abs(startX - endX)):
                if not self.board[startX + i * x_step][startY + i * y_step].isNull():
                    return False
        else:
            return False #neither straight nor diagonal movement
        return True

    def __obeys_piece_movement_rules(self, piece, endX, endY):
        if piece.type == PieceType.KING:
            return (abs(piece.x - endX) == 0 and abs(piece.y - endY) == 1) ^ (abs(piece.x - endX) == 1 and abs(piece.y - endY) == 0)
        elif piece.type == PieceType.ROOK and self.__path_not_obstructed(piece.x, piece.y, endX, endY):
            return (abs(piece.x - endX) == 0 and abs(piece.y - endY) != 0) ^ (abs(piece.x - endX) != 0 and abs(piece.y - endY) == 0)
        elif piece.type == PieceType.BISHOP and self.__path_not_obstructed(piece.x, piece.y, endX, endY):
            return abs(piece.x - endX) == abs(piece.y - endY)
        elif piece.type == PieceType.QUEEN and self.__path_not_obstructed(piece.x, piece.y, endX, endY):
            return abs(piece.x - endX) == abs(piece.y - endY) or (abs(piece.x - endX) == 0 and abs(piece.y - endY) != 0) or (abs(piece.x - endX) != 0 and abs(piece.y - endY) == 0)
        elif piece.type == PieceType.KNIGHT: #can jump, so no obstructed path call
            return (abs(piece.x - endX) == 2 and abs(piece.y - endY) == 1) ^ (abs(piece.x - endX) == 1 and abs(piece.y - endY) == 2)
        elif piece.type == PieceType.PAWN:
            #does not yet support en passant
            correct_direction = bool((piece.color == PieceColor.WHITE and piece.y < endY) or (piece.color == PieceColor.BLACK and piece.y > endY))
            firstMove = bool((piece.y == 1 and piece.color == PieceColor.WHITE) or (piece.y == 6 and piece.color == PieceColor.BLACK))
            validDeltaY = bool((firstMove and (abs(piece.y - endY) == 2 or abs(piece.y - endY) == 1)) or (not firstMove and abs(piece.y - endY) == 1))
            taking = bool((not isinstance(self.board[endX][endY], Null)) and self.board[endX][endY].color != piece.color)
            validDeltaX = bool((taking and abs(piece.x - endX) == 1) or (not taking and abs(piece.x - endX) == 0))
            return correct_direction and validDeltaX and validDeltaY

    def __is_valid_move(self, uci_move):
        startX, startY, endX, endY, promoted_piece = self.__parse_uci_move(uci_move)
        if startX == endX and startY == endY: #must move
            return False
        if startX < 0 or startY < 0 or endX < 0 or endY < 0 or startX > 7 or startY > 7 or endX > 7 or endY > 7:
            return False
        if self.board[startX][startY].isNull():
            return False
        if self.board[startX][startY].color == self.board[endX][endY].color:
            return False
        if promoted_piece is not None and (promoted_piece == "p" or (self.board[startX][startY].type != PieceType.PAWN)):  # must promote pawn and cannot promote any piece that is not pawn
            return False
        if promoted_piece is not None and ((endY == 7 and self.board[startX][startY].color != PieceColor.WHITE) or (endY != 0 and self.board[startX][startY].color != PieceColor.BLACK)):  # tries to promote pawn when not allowed
            return False
        if self.__is_castling(uci_move): #castling not supported in antichess
            return False
        return self.__obeys_piece_movement_rules(self.board[startX][startY], endX, endY)

    def do_move(self, uci_move, inplace=False):
        if not self.singlePlayer:
            inplace=True
        startX, startY, endX, endY, promoted_piece = self.__parse_uci_move(uci_move)
        if not uci_move in self.available_moves():
            raise ValueError(f"{uci_move} is not a valid move.")
        if inplace:
            if promoted_piece is not None:
                self.board[startX][startY].x = endX
                self.board[startX][startY].y = endY
                self.board[endX][endY] = self.board[startX][startY]
                self.board[endX][endY].type = pieceTypeFromRepr(promoted_piece)
            else:
                if self.board[endX][endY].color != PieceColor.EMPTY:
                    self.__take(endX, endY)
                self.board[startX][startY].x = endX
                self.board[startX][startY].y = endY
                self.board[endX][endY] = self.board[startX][startY]
                self.board[startX][startY] = Null()
            self.toggleColor()
            self.last_move = uci_move
        else:
            gs = GameState(boardState=copy.deepcopy(self.board), colorToMove=self.colorToMove)
            gs.do_move(uci_move, inplace=True)
            gs.toggleColor()
            gs.last_move = uci_move
            return gs

    def toggleColor(self):
        self.colorToMove = PieceColor.WHITE if self.colorToMove == PieceColor.BLACK else PieceColor.BLACK

    def __take(self, x, y):
        if self.board[x][y].color == PieceColor.WHITE:
            self.white_pieces.remove(self.board[x][y])
        else:
            self.black_pieces.remove(self.board[x][y])
        self.board[x][y].set_taken(True)
        self.board[x][y] = Null()

    def black_score(self):
        score = 0
        for piece in self.black_pieces:
            if not piece.taken:
                score += piece.value()
        return score

    def white_score(self):
        score = 0
        for piece in self.white_pieces:
            if not piece.taken:
                score += piece.value()
        return score

    def game_over(self):
        return self.white_score() == 0 or self.black_score() == 0

    def result(self, color): # for mcts
        if (color == PieceColor.WHITE and self.white_score() == 0) or (color == PieceColor.BLACK and self.black_score() == 0):
            return 1
        if (color == PieceColor.WHITE and self.black_score() == 0) or (color == PieceColor.BLACK and self.white_score() == 0):
            return -1
