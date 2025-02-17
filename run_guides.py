import tkinter as tk
from tkinter import ttk
import subprocess
import sys

class GuidesMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Learning Hub")
        self.window.geometry("600x800")

        # Configure style
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), padding=10)
        style.configure("Guide.TButton", font=("Arial", 12), padding=10)

        # Main container
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title = ttk.Label(
            main_frame,
            text="Python Learning Hub",
            style="Title.TLabel"
        )
        title.pack(pady=(0, 20))

        # Guide buttons
        guides = [
            ("Advanced Calculator", "advanced_calculator.py"),
            ("AI Guide", "ai_guide.py"),
            ("Django Guide", "django_guide.py"),
            ("Flask Guide", "flask_guide.py"),
            ("PyGame Guide", "pygame_guide.py"),
            ("Turtle Guide", "turtle_guide.py"),
            ("SQL Guide", "sql_guide.py"),
            ("JSON Guide", "json_guide.py"),
            ("Programming Test", "programming_test.py"),
            ("Packages Guide", "packages_guide.py")
        ]

        for name, file in guides:
            btn = ttk.Button(
                main_frame,
                text=name,
                style="Guide.TButton",
                command=lambda f=file: self.run_guide(f)
            )
            btn.pack(fill=tk.X, pady=5)

        # Exit button
        exit_btn = ttk.Button(
            main_frame,
            text="Exit",
            style="Guide.TButton",
            command=self.window.quit
        )
        exit_btn.pack(fill=tk.X, pady=(20, 0))

    def run_guide(self, file_name):
        subprocess.Popen([sys.executable, file_name])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    menu = GuidesMenu()
    menu.run()