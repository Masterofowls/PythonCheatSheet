import tkinter as tk
from tkinter import ttk
import subprocess
import sys

def run_guide(file_name):
    try:
        subprocess.Popen([sys.executable, file_name])
    except Exception as e:
        print(f"Error running {file_name}: {e}")

def main():
    root = tk.Tk()
    root.title("Python Guides")
    root.geometry("400x600")

    # Style configuration
    style = ttk.Style()
    style.configure("Guide.TButton", padding=10, font=('Arial', 11))

    # Main frame
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    # Title
    title = ttk.Label(frame, text="Python Learning Guides", font=('Arial', 16, 'bold'))
    title.pack(pady=(0, 20))

    # Guide buttons
    guides = [
        ("Advanced Calculator", "advanced_calculator.py"),
        ("Programming Test", "programming_test.py"),
        ("Packages Guide", "packages_guide.py"),
        ("PyEnv Guide", "pyenv_guide.py"),
        ("PyPy Guide", "pypy_guide.py"),
        ("SQL Guide", "sql_guide.py"),
        ("Turtle Guide", "turtle_guide.py"),
        ("PyGame Guide", "pygame_guide.py")
    ]

    for name, file in guides:
        btn = ttk.Button(
            frame,
            text=name,
            style="Guide.TButton",
            command=lambda f=file: run_guide(f)
        )
        btn.pack(fill=tk.X, pady=5)

    # Exit button
    exit_btn = ttk.Button(frame, text="Exit", style="Guide.TButton", command=root.quit)
    exit_btn.pack(fill=tk.X, pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    main()