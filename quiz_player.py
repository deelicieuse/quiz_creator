import tkinter as tk

class QuizPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Player")

    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    QuizPlayer().run()