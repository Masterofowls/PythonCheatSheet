
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

class GuideRunner:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Learning Hub")
        self.window.geometry("600x800")
        
        # Configure style
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), padding=10)
        style.configure("Category.TLabel", font=("Arial", 14, "bold"), padding=5)
        style.configure("Guide.TButton", font=("Arial", 11), padding=8)
        
        # Create main container
        self.main_container = ttk.Frame(self.window, padding="20")
        self.main_container.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title = ttk.Label(self.main_container, text="Python Learning Hub", style="Title.TLabel")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Guide categories
        self.guides = {
            "GUI Applications": [
                ("Advanced Calculator", "advanced_calculator.py"),
                ("PyQt Guide", "pyqt_guide.py"),
                ("Turtle Graphics", "turtle_guide.py"),
                ("PyGame Guide", "pygame_guide.py"),
            ],
            "Web Development": [
                ("Flask Guide", "flask_guide.py"),
                ("Django Guide", "django_guide.py"),
                ("Server Guide", "server_guide.py"),
            ],
            "Data & AI": [
                ("SQL Guide", "sql_guide.py"),
                ("JSON Guide", "json_guide.py"),
                ("AI Guide", "ai_guide.py"),
            ],
            "Development Tools": [
                ("Testing Guide", "testing_guide.py"),
                ("Pip Guide", "pip_guide.py"),
                ("Pipx Guide", "pipx_guide.py"),
                ("PyEnv Guide", "pyenv_guide.py"),
                ("PyPy Guide", "pypy_guide.py"),
            ]
        }
        
        # Create sections for each category
        current_row = 1
        for category, guide_list in self.guides.items():
            # Category label
            category_label = ttk.Label(
                self.main_container,
                text=category,
                style="Category.TLabel"
            )
            category_label.grid(row=current_row, column=0, columnspan=2, sticky="w", pady=(10, 5))
            current_row += 1
            
            # Create buttons for guides in this category
            for i, (name, file) in enumerate(guide_list):
                col = i % 2
                row = current_row + (i // 2)
                
                btn = ttk.Button(
                    self.main_container,
                    text=name,
                    style="Guide.TButton",
                    command=lambda f=file: self.run_guide(f)
                )
                btn.grid(row=row, column=col, pady=5, padx=10, sticky="ew")
            
            current_row += ((len(guide_list) + 1) // 2)
        
        # Quit button at the bottom
        quit_btn = ttk.Button(
            self.main_container,
            text="Exit Hub",
            style="Guide.TButton",
            command=self.window.quit
        )
        quit_btn.grid(row=current_row + 1, column=0, columnspan=2, pady=20)
        
        # Configure grid weights
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.columnconfigure(1, weight=1)
    
    def run_guide(self, file_name):
        if not os.path.exists(file_name):
            messagebox.showerror(
                "File Not Found",
                f"The guide file '{file_name}' was not found. Please make sure all guide files are present."
            )
            return
            
        try:
            subprocess.Popen([sys.executable, file_name])
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to run {file_name}:\n{str(e)}"
            )
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GuideRunner()
    app.run()
