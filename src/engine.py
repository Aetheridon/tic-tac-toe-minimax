import copy


class Board:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]


def terminal(board: Board):
    b = board.board
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ":
            return True
        if b[0][i] == b[1][i] == b[2][i] != " ":
            return True

    if b[0][0] == b[1][1] == b[2][2] != " ":
        return True
    if b[0][2] == b[1][1] == b[2][0] != " ":
        return True

    for row in board.board:
        for col in row:
            if col == " ":
                return False

    return True


def utility(board: Board):
    b = board.board

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == "X":
            return 1
        elif b[i][0] == b[i][1] == b[i][2] == "O":
            return -1

        if b[0][i] == b[1][i] == b[2][i] == "X":
            return 1
        elif b[0][i] == b[1][i] == b[2][i] == "O":
            return -1

    if b[0][0] == b[1][1] == b[2][2] == "X":
        return 1
    elif b[0][0] == b[1][1] == b[2][2] == "O":
        return -1

    if b[0][2] == b[1][1] == b[2][0] == "X":
        return 1
    elif b[0][2] == b[1][1] == b[2][0] == "O":
        return -1

    if terminal(board):
        return 0


def actions(board: Board):
    actions = []
    for r_index, row in enumerate(board.board):
        for c_index, col in enumerate(row):
            if col == " ":
                actions.append([r_index, c_index])
    return actions


def result(board: Board, action, player):
    new_board = Board()
    new_board.board = copy.deepcopy(board.board)
    new_board.board[action[0]][action[1]] = player
    return new_board


def minimax(board: Board, player, alpha=float("-inf"), beta=float("inf")):
    if terminal(board):
        return utility(board)

    if player == "X":
        best_value = float("-inf")
        for action in actions(board):
            child_board = result(board, action, "X")
            score = minimax(child_board, "O", alpha, beta)
            best_value = max(best_value, score)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float("inf")
        for action in actions(board):
            child_board = result(board, action, "O")
            score = minimax(child_board, "X", alpha, beta)
            best_value = min(best_value, score)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value


def best_move(board: Board, player):
    best_action = None
    if player == "X":
        best_score = float("-inf")
        for action in actions(board):
            child_board = result(board, action, player)
            score = minimax(child_board, "O")
            if score > best_score:
                best_score = score
                best_action = action
    else:
        best_score = float("inf")
        for action in actions(board):
            child_board = result(board, action, player)
            score = minimax(child_board, "X")
            if score < best_score:
                best_score = score
                best_action = action
    return best_action
