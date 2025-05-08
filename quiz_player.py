import tkinter as tk
from tkinter import filedialog
import json


class QuizPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Player")
        self.build_ui()
        self.questions= []

    def switch_frame(self, frame):
        for child in self.root.winfo_children():
            child.pack_forget()
        frame.pack(fill="both", expand=True)


    def build_ui(self):

        self.intro_frame = tk.Frame(self.root)
        tk.Label(
            self.intro_frame,
            text="ARE YOU READY TO PLAY?",
            font=("Courier", 28, "bold")
        ).pack(pady=20)
        tk.Button(
            self.intro_frame,
            text="LET'S START",
            font=("Courier", 14),
            command=lambda:self.switch_frame(self.intro_frame)
        ).pack()
        self.intro_frame.pack(fill="both", expand=True)

        self.file_selection_frame = tk.Frame(self.root)
        tk.Label(
            self.file_selection_frame,
            text="Select Quiz JSON File",
            font=("Courier", 14)
        ).pack(pady=10)
        tk.Button(
            self.file_selection_frame,
            text="Browse...",
            font=("Courier", 12),
            command=self.choose_file
        ).pack()

        self.quiz_frame = tk.Frame(self.root, padx=20, pady=20)
        self.questions_label = tk.Label(self.quiz_frame,
                                        wraplength=500,
                                        font=("Courier", 12)
                                        )
        self.questions_label.pack(pady=10)
        self.answer_buttons = {}
        for key in "abcd":
            btn = tk.Button(
            self.quiz_frame,
            width=40,
            font=("Courier", 12)
            )
            btn.pack(pady=3)
            self.answer_buttons[key] = btn

    def choose_file(self):
        fp = filedialog.askopenfilename(filetypes=[("JSON", "*.json"), ("All", "*.*")])
        print("Selected file:", fp)
        with open(fp, 'r') as f:
            self.questions = json.load(f)
        print("Loaded queations:", self.questions)


    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    QuizPlayer().run()