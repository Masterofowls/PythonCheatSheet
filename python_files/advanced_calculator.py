
import tkinter as tk
from tkinter import ttk
import math
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename=f'calculator_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Advanced Calculator")
        self.window.geometry("400x600")
        self.window.configure(bg="#2c3e50")

        # Display
        self.display_var = tk.StringVar(value="0")
        self.display = ttk.Entry(
            self.window,
            textvariable=self.display_var,
            justify="right",
            font=("Arial", 24)
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Style configuration
        style = ttk.Style()
        style.configure(
            "Calc.TButton",
            padding=10,
            font=("Arial", 14),
            width=5
        )

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^2', 5, 2), ('1/x', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(
                self.window,
                text=text,
                style="Calc.TButton",
                command=lambda t=text: self.button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

        self.current_calculation = ""

    def button_click(self, value):
        current = self.display_var.get()
        
        try:
            if value == "C":
                self.display_var.set("0")
                self.current_calculation = ""
                logging.info("Display cleared")
            
            elif value == "=":
                result = eval(self.current_calculation or "0")
                self.display_var.set(result)
                logging.info(f"Calculation: {self.current_calculation} = {result}")
                self.current_calculation = str(result)
            
            elif value == "√":
                result = math.sqrt(float(current))
                self.display_var.set(result)
                logging.info(f"Square root: √{current} = {result}")
                self.current_calculation = str(result)
            
            elif value == "^2":
                result = float(current) ** 2
                self.display_var.set(result)
                logging.info(f"Square: {current}² = {result}")
                self.current_calculation = str(result)
            
            elif value == "1/x":
                result = 1 / float(current)
                self.display_var.set(result)
                logging.info(f"Reciprocal: 1/{current} = {result}")
                self.current_calculation = str(result)
            
            else:
                if current == "0" and value not in ".*/-+":
                    self.current_calculation = value
                else:
                    self.current_calculation += value
                self.display_var.set(self.current_calculation)
                logging.info(f"Input: {value}")
                
        except Exception as e:
            self.display_var.set("Error")
            logging.error(f"Error occurred: {str(e)}")
            self.current_calculation = ""

    def run(self):
        logging.info("Calculator started")
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
