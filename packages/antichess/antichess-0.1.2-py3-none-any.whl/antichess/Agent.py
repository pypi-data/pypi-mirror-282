import numpy as np
from .GameState import GameState, Null
from .Piece import Piece, PieceType, PieceColor, pieceTypeFromRepr

class MCTSNode:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = state.available_moves()
        self.depth = depth

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.wins / child.visits) + c_param * np.sqrt((2 * np.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def expand(self):
        move = self.untried_moves.pop()
        next_state = self.state.do_move(move)
        child_node = MCTSNode(next_state, parent=self, depth=self.depth + 1)
        self.children.append(child_node)
        return child_node

    def update(self, result):
        self.visits += 1
        self.wins += result


class Agent:
    def __init__(self, color, strategy=None):
        assert color == PieceColor.WHITE or color == PieceColor.BLACK, "Color must be PieceColor.WHITE or PieceColor.BLACK."
        self.color = color
        valid_strats = ["random",
                        "bfs-depth=2",
                        "bfs-depth=3",
                        "bfs-depth=2-e=.1",
                        "bfs-depth=3-e=.1",
                        "mcts-sims=1000-depth=10",
                        "mcts-sims=1000-depth=15",
                        "mcts-sims=1500-depth=10",
                        "minimax-depth=3",
                        "minimax-depth=5"]
        if strategy is None:
            print("Agent strategy not selected, defaulting to 'random'.")
            self.strategy = "random"
        elif not strategy in valid_strats:
            print(f"Specified strategy is not valid. Valid strategies are {valid_strats}.")
        else:
            self.strategy = strategy
            colorStr = "black" if self.color == PieceColor.BLACK else "white"
            print(f"Agent playing as {colorStr}, and using strategy {self.strategy}.")

    def get_move(self, gs):
        if self.strategy == "random":
            return self.random_move(gs)
        elif self.strategy == "bfs-depth=2":
            move_scores_dict = self.move_scores(gs, 2, self.__game_score, np.max)
            best_move = max(move_scores_dict, key=move_scores_dict.get)
            return best_move
        elif self.strategy == "bfs-depth=3":
            move_scores_dict = self.move_scores(gs, 3, self.__game_score, np.max)
            best_move = max(move_scores_dict, key=move_scores_dict.get)
            return best_move
        elif self.strategy == "bfs-depth=2-e=.1":
            move_scores_dict = self.move_scores(gs, 2, self.__game_score, np.max)
            best_move = max(move_scores_dict, key=move_scores_dict.get)
            if np.random.random() < .1:
                return np.random.choice(list(move_scores_dict.keys()))
            else:
                return best_move
        elif self.strategy == "bfs-depth=3-e=.1":
            move_scores_dict = self.move_scores(gs, 3, self.__game_score, np.max)
            best_move = max(move_scores_dict, key=move_scores_dict.get)
            if np.random.random() < .1:
                return np.random.choice(list(move_scores_dict.keys()))
            else:
                return best_move
        elif self.strategy == "mcts-sims=1000-depth=10":
            return self.mcts_move(gs, num_simulations=1000, max_depth=10)
        elif self.strategy == "mcts-sims=1000-depth=15":
            return self.mcts_move(gs, num_simulations=1000, max_depth=15)
        elif self.strategy == "mcts-sims=1500-depth=10":
            return self.mcts_move(gs, num_simulations=1500, max_depth=10)
        elif self.strategy == "minimax-depth=3":
            return self.minimax(gs, 3, -np.inf, np.inf, True)[1]
        elif self.strategy == "minimax-depth=5":
            return self.minimax(gs, 5, -np.inf, np.inf, True)[1]

    def random_move(self, gs):
        return np.random.choice(gs.available_moves())

    def move_scores(self, gs, depth, heuristic, metric):
        av_moves = gs.available_moves()
        if len(av_moves) == 0:
            return {}

        if depth == 0:
            return {move: heuristic(gs) for move in gs.available_moves()}

        move_scores_dict = {}
        for move in gs.available_moves():
            next_gs = gs.do_move(move)
            next_move_scores = self.move_scores(next_gs, depth - 1, heuristic, metric)
            if len(next_move_scores) != 0:
                move_scores_dict[move] = metric(list(next_move_scores.values()))
            else:
                move_scores_dict[move] = self.__game_score(next_gs)

        return move_scores_dict

    def __game_score(self, gs):
        if self.color == PieceColor.WHITE:
            return gs.black_score() - gs.white_score()
        else:
            return gs.white_score() - gs.black_score()

    def mcts_move(self, gs, num_simulations=1000, max_depth=15):
        root = MCTSNode(gs)

        for _ in range(num_simulations):
            node = root
            state = gs

            while node.is_fully_expanded() and node.children:
                node = node.best_child()
                state = node.state

            if not node.is_fully_expanded() and node.depth < max_depth:
                node = node.expand()
                state = node.state

            result = self.__mcts_simulate(state, max_depth - node.depth)

            while node:
                node.update(result)
                node = node.parent

        best_move = max(root.children, key=lambda c: c.visits).state.last_move
        return best_move

    def __mcts_simulate(self, state, remaining_depth):
        current_state = state
        depth = 0
        while not current_state.game_over() and depth < remaining_depth:
            current_state = current_state.do_move(np.random.choice(current_state.available_moves()))
            depth += 1
        if current_state.game_over():
            return 100 * current_state.result(self.color)
        else:
            return self.__game_score(current_state)

    def minimax(self, game_state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game_state.game_over():
            return self.__game_score(game_state), None

        best_move = None
        if maximizing_player:
            max_eval = -np.inf
            for move in game_state.available_moves():
                new_game_state = game_state.do_move(move, inplace=False)
                eval, _ = self.minimax(new_game_state, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = np.inf
            for move in game_state.available_moves():
                new_game_state = game_state.do_move(move, inplace=False)
                eval, _ = self.minimax(new_game_state, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
