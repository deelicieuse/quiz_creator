import tkinter as tk

class QuizPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Player")
        self.build_ui()

    def build_ui(self):
        self.intro_frame = tk.Frame(self.root)
        tk.Label(self.intro_frame, text="ARE YOU READY TO PLAY?", font=("Courier", 28, "bold")).pack(pady=20)
        tk.Button(self.intro_frame, text="LET'S START", font=("Courier", 14)).pack()
        self.intro_frame.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    QuizPlayer().run()