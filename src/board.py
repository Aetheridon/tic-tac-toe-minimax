import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.root, text=" ", font=('Arial', 24),
                    width=5, height=2,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def on_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == " ":
            button["text"] = self.player
            button["state"] = "disabled"

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
