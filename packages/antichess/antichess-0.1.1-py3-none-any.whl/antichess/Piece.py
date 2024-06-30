from enum import Enum

class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 5
    QUEEN = 6
    KING = 7
    EMPTY = 8

class PieceColor(Enum):
    WHITE = 1
    BLACK = 2
    EMPTY = 3

def pieceTypeFromRepr(r):
    dic = {
        "p" : PieceType.PAWN,
        "n" : PieceType.KNIGHT,
        "b" : PieceType.BISHOP,
        "r" : PieceType.ROOK,
        "q" : PieceType.QUEEN,
        "k" : PieceType.KING
    }
    return dic[r.lower()]

class Piece:
    def __init__(self, type=None, color=None, x=None, y=None):
        self.type = type
        self.color = color
        self.taken = False
        self.x = x
        self.y = y

    def value(self):
        dic = {
            PieceType.PAWN : 1,
            PieceType.KNIGHT : 3,
            PieceType.BISHOP : 3,
            PieceType.ROOK : 5,
            PieceType.QUEEN : 9,
            PieceType.KING : 3.5 #assuming king counts for 3.5 points
        }
        return dic[self.type]

    def isNull(self):
        return False

    def set_taken(self, t):
        if t:
            self.x = -1
            self.y = -1
        self.taken = t

    def __repr__(self):
        if self.taken:
            return "-"

        id = "p"
        if self.type == PieceType.KNIGHT:
            id = "n"
        elif self.type == PieceType.BISHOP:
            id = "b"
        elif self.type == PieceType.ROOK:
            id = "r"
        elif self.type == PieceType.QUEEN:
            id = "q"
        elif self.type == PieceType.KING:
            id = "k"

        if self.color == PieceColor.WHITE:
            return id.upper()
        return id

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        # place value encoding
        hsh = self.type.value * 10000 + self.color.value * 1000 + self.x * 100 + self.y * 10
        if not self.taken:
            hsh += 1

        return hsh

    def __eq__(self, other):
        return isinstance(other, Piece) and hash(self) == hash(other)
