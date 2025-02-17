
import tkinter as tk
from tkinter import ttk
import subprocess
import sys

class GuideRunner:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Guides Runner")
        self.window.geometry("400x600")
        
        # Create main frame
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title label
        title_label = ttk.Label(main_frame, text="Python Guides", font=("Arial", 20))
        title_label.grid(row=0, column=0, pady=10)
        
        # Create buttons for each guide
        guides = [
            ("Advanced Calculator", "advanced_calculator.py"),
            ("AI Guide", "ai_guide.py"),
            ("Django Guide", "django_guide.py"),
            ("Flask Guide", "flask_guide.py"),
            ("PyGame Guide", "pygame_guide.py"),
            ("PyQt Guide", "pyqt_guide.py"),
            ("SQL Guide", "sql_guide.py"),
            ("Testing Guide", "testing_guide.py"),
            ("Turtle Guide", "turtle_guide.py"),
            ("Server Guide", "server_guide.py"),
            ("JSON Guide", "json_guide.py"),
            ("Pip Guide", "pip_guide.py"),
            ("Pipx Guide", "pipx_guide.py"),
            ("PyEnv Guide", "pyenv_guide.py"),
            ("PyPy Guide", "pypy_guide.py")
        ]
        
        # Create a button for each guide
        for i, (name, file) in enumerate(guides, 1):
            btn = ttk.Button(
                main_frame,
                text=name,
                command=lambda f=file: self.run_guide(f)
            )
            btn.grid(row=i, column=0, pady=5, padx=10, sticky="ew")
        
        # Quit button
        quit_btn = ttk.Button(main_frame, text="Quit", command=self.window.quit)
        quit_btn.grid(row=len(guides)+1, column=0, pady=20)
        
        # Configure grid
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
    
    def run_guide(self, file_name):
        try:
            subprocess.Popen([sys.executable, file_name])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to run {file_name}: {str(e)}")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GuideRunner()
    app.run()
