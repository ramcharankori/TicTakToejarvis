import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.buttons = [[None] * 3 for _ in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text="", font=("Helvetica", 24),
                                                   width=6, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player == "X":
            self.buttons[row][col]["text"] = "X"
            if self.check_winner("X"):
                self.end_game("X wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "O"
                self.ai_move()

    def ai_move(self):
        best_score = -float("inf")
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "O"
                    score = self.minimax(0, False)
                    self.buttons[row][col]["text"] = ""

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            self.buttons[best_move[0]][best_move[1]]["text"] = "O"
            if self.check_winner("O"):
                self.end_game("O wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "X"

    def minimax(self, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "draw": 0}

        winner = self.check_winner("X" if is_maximizing else "O")
        if winner:
            return scores[winner]

        if self.check_draw():
            return scores["draw"]

        best_score = -float("inf") if is_maximizing else float("inf")

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "X" if is_maximizing else "O"
                    score = self.minimax(depth + 1, not is_maximizing)
                    self.buttons[row][col]["text"] = ""

                    if is_maximizing:
                        best_score = max(best_score, score)
                    else:
                        best_score = min(best_score, score)

        return best_score

    def check_winner(self, player):
        for row in range(3):
            if all(self.buttons[row][col]["text"] == player for col in range(3)):
                return player
        for col in range(3):
            if all(self.buttons[row][col]["text"] == player for row in range(3)):
                return player
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return player
        return None

    def check_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
