import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class QuizCreatorApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Quiz Creator")

        self.option_entries = {}
        self.option_image_paths = {}
        self.option_image_labels = {}
        self.correct_answer_variable = tk.StringVar
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

            image_path = tk.StringVar()
            self.option_image_paths[option_key] = image_path

            image_label = tk.Label(option_entry, textvariable=image_path, fg="grey", wraplength=150)
            image_label.grid(row=index, column=2, sticky="w", padx=5, pady=5)
            self.option_image_labels[option_key] = image_label

            upload_button = tk.Button(
                options_frame,
                text="Upload Image",
                command=lambda key=option_key: self.upload_image(key)
            )

        correct_label = tk.Label(main_frame, text="Correct Answer:", font=("Arial", 12))
        correct_label.grid(row=2, column=0, sticky="w", padx=5, pady=10)

        correct_dropdown = tk.OptionMenu(main_frame, self.correct_answer_variable, *self.option_keys)
        correct_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=10)


    def upload_image(self, option_key):
        pass

    def clear_image(self, option_key):
        pass


if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()