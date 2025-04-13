import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from tkinter.messagebox import showerror


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

        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=4, pady=15)

        save_button = tk.Button(button_frame, text="Save Question", command=self.save_question)
        save_button.pack(side="left", padx=10)

        clear_form_button = tk.Button(button_frame, text="Clear Form", command=self.clear_form)
        clear_form_button.pack(side="left", padx=10)

        exit_button = tk.Button(button_frame, text="Exit", command=self.root_window.quit)
        exit_button.pack(side="left", padx=10)

    def save_question(self):
        file_path = filedialog.asksaveasfilename(
            title="Save Quiz File",
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
            initialfile="quiz_data.json"
        )

        if not file_path:
            return

        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    try:
                        questions_list = json.load(file)
                        if not isinstance(questions_list, list):
                            raise ValueError("Existing file does not contain a list")
                    except json.JSONDecodeError:
                        questions_list = []
            else:
                questions_list = []

            questions_list = [single_question_data]

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(questions_list, file, indent=4)

            messagebox.showinfo("Success", f"Question saved successfully to\n{file_path}")
            self.clear_form()

        except Exception as error:
            messagebox.showerror("Save Error", f"An wrror occured while saving: \n{error}")

        messagebox.showinfo("File Selected", f"Selected path: {file_path}")




    def clear_form(self):
        self.question_entry.delete(0, tk.END)
        for key in self.option_keys:
            self.option_entries[key].delete(0, tk.END)
            self.clear_image(key)
        self.correct_answer_variable.set(self.option_keys[0])
        self.question_entry.focus_set()



    def upload_image(self, option_key):
        file_path = filedialog.askopenfilename(
            title=f"Select Image for Option {option_key.upper()}",
            filetypess=[("Image Files", "*.png *.jpg *.jpeg *.gif"), ("All Files", ".")]
        )
        
        if file_path:
            file_name = os.path.basemame(file_path)
            self.option_image_paths[option_key].set(file_path)
            self.option_image_paths[option_key].confic(text=file_name)
            messagebox.showinfo("Image Selected", f"Image '{file_name}' selected for Option {option_key.upper()}.")
        else:
            self.option_image_paths[option_key].set("")
            self.option_image_labels[option_key].config(text="")

    def clear_image(self, option_key):
        self.option_image_paths[option_key].set("")
        self.option_image_labels[option_key].config(text="")


if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()