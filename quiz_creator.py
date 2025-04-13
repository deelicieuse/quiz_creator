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

        question_label = tk.Label(main_frame, text="Enter your question:", font=("Arial", 12, "bold"))
        question_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.question_entry = tk.Entry(main_frame, width=60)
        self.question_entry.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        options_frame = tk.LabelFrame(main_frame, text="Options", padx=10, pady=10)
        options_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=10)

        for index, option_key in enumerate(self.option_keys):
            option_label = tk.Label(options_frame, text=f"Option {option_key.upper()} Text:", font=("Arial", 10))
            option_label.grid(row=index, column=0, sticky="w", padx=5, pady=5)

            option_entry = tk.Entry(options_frame, width=40)
            option_entry.grid(row=index, column=1, padx=5, pady=5)
            self.option_entries[option_key] = option_entry


if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()