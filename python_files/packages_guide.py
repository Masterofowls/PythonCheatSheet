
"""
MODERN PYTHON PACKAGES GUIDE
===========================
A comprehensive guide to useful modern Python packages and their applications.
"""

import tkinter as tk
from tkinter import ttk
import webbrowser
from typing import Dict, List

class PackagesGuide:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Modern Python Packages Guide")
        self.window.geometry("800x600")
        
        # Define packages with their descriptions
        self.packages: Dict[str, Dict[str, List[tuple]]] = {
            "Data Science & ML": [
                ("pandas", "Data manipulation and analysis library", "Data frames, series, data cleaning"),
                ("numpy", "Numerical computing library", "Arrays, mathematical operations"),
                ("scikit-learn", "Machine learning library", "ML algorithms, preprocessing, model evaluation"),
                ("pytorch", "Deep learning framework", "Neural networks, GPU acceleration"),
                ("tensorflow", "Deep learning framework", "Neural networks, production deployment")
            ],
            "Web Development": [
                ("fastapi", "Modern web framework", "High performance, automatic API docs"),
                ("httpx", "HTTP client", "Async HTTP requests, modern HTTP features"),
                ("starlette", "ASGI framework", "Lightweight web/API framework"),
                ("uvicorn", "ASGI server", "Lightning-fast ASGI server"),
                ("pydantic", "Data validation", "Type hints, data serialization")
            ],
            "Developer Tools": [
                ("black", "Code formatter", "Uncompromising code formatting"),
                ("ruff", "Fast Python linter", "10-50x faster than traditional linters"),
                ("mypy", "Static type checker", "Type checking using type hints"),
                ("rich", "Terminal formatting", "Beautiful terminal output"),
                ("typer", "CLI builder", "Build CLIs with type hints")
            ],
            "Testing & Quality": [
                ("pytest", "Testing framework", "Powerful test framework"),
                ("hypothesis", "Property-based testing", "Generate test cases automatically"),
                ("coverage", "Code coverage", "Measure code test coverage"),
                ("faker", "Fake data generator", "Generate realistic fake data"),
                ("locust", "Load testing", "Load and performance testing")
            ],
            "Utilities": [
                ("poetry", "Dependency management", "Modern package management"),
                ("tqdm", "Progress bars", "Smart progress meter"),
                ("pillow", "Image processing", "Image manipulation library"),
                ("requests", "HTTP library", "Human-friendly HTTP client"),
                ("python-dotenv", "Environment variables", "Load environment variables from file")
            ]
        }
        
        # Create main container
        self.main_container = ttk.Frame(self.window, padding="20")
        self.main_container.grid(row=0, column=0, sticky="nsew")
        
        # Configure style
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), padding=10)
        style.configure("Category.TLabel", font=("Arial", 14, "bold"), padding=5)
        style.configure("Package.TLabel", font=("Arial", 11))
        
        # Title
        title = ttk.Label(
            self.main_container,
            text="Modern Python Packages Guide",
            style="Title.TLabel"
        )
        title.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Create sections for each category
        current_row = 1
        for category, packages in self.packages.items():
            # Category label
            category_label = ttk.Label(
                self.main_container,
                text=category,
                style="Category.TLabel"
            )
            category_label.grid(row=current_row, column=0, columnspan=3, sticky="w", pady=(10, 5))
            current_row += 1
            
            # Package information
            for package, description, features in packages:
                package_label = ttk.Label(
                    self.main_container,
                    text=f"{package}:",
                    style="Package.TLabel",
                    width=15
                )
                package_label.grid(row=current_row, column=0, sticky="w", padx=(20, 0))
                
                desc_label = ttk.Label(
                    self.main_container,
                    text=description,
                    wraplength=300
                )
                desc_label.grid(row=current_row, column=1, sticky="w", padx=10)
                
                features_label = ttk.Label(
                    self.main_container,
                    text=features,
                    wraplength=300
                )
                features_label.grid(row=current_row, column=2, sticky="w", padx=10)
                
                current_row += 1
        
        # Configure grid weights
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.main_container.columnconfigure(1, weight=1)
        self.main_container.columnconfigure(2, weight=1)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    guide = PackagesGuide()
    guide.run()
