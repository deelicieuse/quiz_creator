import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class QuizCreatorApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Quiz Creator")

        self.option_entries = {}
        self.option_imagepaths = {}
        self.option_image_labels = {}
        self.cirrect_answer_variable = tk.StringVar
        self.option_keys = ["a", "b", "c", "d"]

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root_window, padx=10, pady=10)
        main_frame.grid(row=0, column=0)

if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()