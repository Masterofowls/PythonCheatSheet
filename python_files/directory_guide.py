
"""
PYTHON GUIDES DIRECTORY
======================
This file provides examples of running each guide with sample outputs.
"""

import importlib
import sys
from typing import Callable, Dict
import time

def run_guide(name: str, operation: Callable):
    """Run a guide with proper formatting"""
    print(f"\n{'='*50}")
    print(f"Running {name}")
    print('='*50)
    try:
        operation()
    except Exception as e:
        print(f"Error running {name}: {e}")
    print(f"\n{'='*50}\n")

def calculator_demo():
    print("Running Advanced Calculator...")
    print("Please run advanced_calculator.py directly for the GUI calculator")

def pygame_demo():
    print("Running PyGame Guide...")
    print("Please run pygame_guide.py directly for the interactive game window")

def turtle_demo():
    print("Running Turtle Guide...")
    print("Please run turtle_guide.py directly for the graphics window")

def sql_demo():
    print("Running SQL Guide...")
    print("Please run sql_guide.py directly for the SQL operations demo")

def json_demo():
    print("Running JSON Guide...")
    print("Please run json_guide.py directly for JSON operations examples")

def flask_demo():
    print("Running Flask Guide...")
    print("Please run flask_guide.py directly for Flask web framework examples")

def main():
    # Dictionary of demos
    demos: Dict[str, Callable] = {
        "Advanced Calculator": calculator_demo,
        "PyGame": pygame_demo,
        "Turtle": turtle_demo,
        "SQL": sql_demo,
        "JSON": json_demo,
        "Flask": flask_demo
    }
    
    print("Python Guides Directory")
    print("=====================")
    
    # Run each demo
    for name, demo in demos.items():
        run_guide(name, demo)
        time.sleep(1)  # Small delay between demos
    
    print("\nGuide Execution Complete!")
    print("To run specific guides:")
    print("1. Advanced Calculator: python advanced_calculator.py")
    print("2. PyGame Guide: python pygame_guide.py")
    print("3. Turtle Guide: python turtle_guide.py")
    print("\nOther guides are modules that can be imported and used in your code.")

if __name__ == "__main__":
    main()
