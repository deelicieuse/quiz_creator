import tkinter as tk
import tkinter import filedialog, messagebox
import json
import os

class QuizCreatorApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Quix Creator")

        self.option_entries = {}
        self.option_imagepaths = {}
        self.option_image_labels = {}
        self.cirrect_answer_variable = tk.StringVar
        self.option_keys = ["a", "b", "c", "d"]

if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()