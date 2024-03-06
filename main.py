from os import system
from itertools import chain


class Game:
    def __init__(self):
        self.map = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.turn = 1

    def change_turn(self):
        self.turn = 1 if self.turn == 0 else 0

    def available_moves(self):
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell is None:
                    yield i, j

    def evaluate(self, depth=0, is_maximizer=False, alpha=float("-inf"), beta=float("inf")):
        result = self.check_winner()
        if result is not None:
            if is_maximizer:
                return result + depth
            else:
                return result - depth

        if is_maximizer:
            max_eval = float("-inf")
            for i, j in self.available_moves():
                self.map[i][j] = 1
                eval_child = self.evaluate(depth + 1, False, alpha, beta)
                self.map[i][j] = None
                max_eval = max(max_eval, eval_child)
                alpha = max(alpha, eval_child)
                if alpha >= beta:
                    break
            return max_eval
        else:
            min_eval = float("inf")
            for i, j in self.available_moves():
                self.map[i][j] = 0
                eval_child = self.evaluate(depth + 1, True, alpha, beta)
                self.map[i][j] = None
                min_eval = min(min_eval, eval_child)
                beta = min(beta, eval_child)
                if alpha >= beta:
                    break
            return min_eval

    def ai_move(self):
        best_move = None
        if self.turn == 1:
            best_eval = float("-inf")
            for i, j in self.available_moves():
                self.map[i][j] = 1
                this_move_eval = self.evaluate()
                if this_move_eval > best_eval:
                    best_move = i, j
                    best_eval = this_move_eval
                self.map[i][j] = None
        else:
            best_eval = float("inf")
            for i, j in self.available_moves():
                self.map[i][j] = 0
                this_move_eval = self.evaluate(is_maximizer=True)
                if this_move_eval < best_eval:
                    best_move = i, j
                    best_eval = this_move_eval
                self.map[i][j] = None
        i, j = best_move
        self.map[i][j] = 1 if self.turn == 1 else 0

    def rows(self):
        for row in self.map:
            yield row

    def columns(self):
        for i in range(3):
            yield [self.map[0][i], self.map[1][i], self.map[2][i]]

    def diagonals(self):
        yield [self.map[0][0], self.map[1][1], self.map[2][2]]
        yield [self.map[0][2], self.map[1][1], self.map[2][0]]

    def check_winner(self):
        have_move = False
        for sqe in chain(self.rows(), self.columns(), self.diagonals()):
            if None not in sqe:
                if 1 in sqe and 0 not in sqe:
                    return 100
                if 0 in sqe and 1 not in sqe:
                    return -100
            else:
                have_move = True
        return None if have_move else 0

    def __str__(self):
        output = ""
        for i in range(3):
            for j in range(3):
                if self.map[i][j] == 1:
                    output += " X"
                elif self.map[i][j] == 0:
                    output += " O"
                else:
                    output += "  "
                if j != 2:
                    output += "|"
            if i != 2:
                output += "\n" + "-"*9 + "\n"
        return output


if __name__ == "__main__":
    player = int(input("choose your Symbol (1 => X, 0 => O): "))
    game = Game()
    while True:
        system("cls")
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
            i, j = map(int, input("Enter a tuple like(0-3)(0-3):").split())
            game.map[i][j] = player
        else:
            game.ai_move()
        game.change_turn()
