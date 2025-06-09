from engine import Board, best_move, terminal, utility
import tkinter as tk


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = Board()

        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.status_label = tk.Label(self.root, text="", font=('Arial', 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.draw_board()

    def draw_board(self):
        for r_index, row in enumerate(self.board.board):
            for c_index, col in enumerate(row):
                btn = tk.Button(
                    self.root,
                    text=col,
                    font=('Arial', 24),
                    width=5,
                    height=2,
                    command=lambda r=r_index, c=c_index: self.on_click(r, c)
                )
                btn.grid(row=r_index, column=c_index)
                self.buttons[r_index][c_index] = btn

    def on_click(self, r_index, c_index):
        if self.board.board[r_index][c_index] != " " or terminal(self.board):
            return
        self.board.board[r_index][c_index] = "X"
        self.update_board()

        if not terminal(self.board):
            r_ai, c_ai = best_move(self.board, "O")
            self.board.board[r_ai][c_ai] = "O"
            self.update_board()
            
        self.check_game_outcome()

    def update_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"] = self.board.board[r][c]
                self.buttons[r][c]["state"] = (
                    "disabled" if self.board.board[r][c] != " " else "normal"
                )


    def check_game_outcome(self):
        if terminal(self.board):
            result = utility(self.board)
            if result == 1:
                self.status_label["text"] = "X wins!"
            elif result == -1:
                self.status_label["text"] = "O wins!"
            else:
                self.status_label["text"] = "It's a draw!"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
