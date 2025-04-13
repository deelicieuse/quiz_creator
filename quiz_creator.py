import tkinter as tk

class QuizCreatorApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Quix Creator")

if __name__ == "__main__":
    main_window = tk.Tk()
    quiz_app = QuizCreatorApp(main_window)
    main_window.mainloop()