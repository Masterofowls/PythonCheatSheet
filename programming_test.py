
import tkinter as tk
from tkinter import ttk, messagebox
import json
from typing import Dict, List
import random

class ProgrammingTest(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Modern Programming Test")
        self.geometry("800x600")
        self.configure(bg="#2C3E50")
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Modern.TFrame", background="#2C3E50")
        self.style.configure("Title.TLabel", 
                           font=("Helvetica", 24, "bold"),
                           background="#2C3E50",
                           foreground="#ECF0F1")
        self.style.configure("Question.TLabel", 
                           font=("Helvetica", 14),
                           background="#2C3E50",
                           foreground="#ECF0F1",
                           wraplength=700)
        self.style.configure("Score.TLabel", 
                           font=("Helvetica", 16, "bold"),
                           background="#2C3E50",
                           foreground="#27AE60")
        self.style.configure("Modern.TButton",
                           font=("Helvetica", 12),
                           padding=10)
        self.style.configure("Answer.TRadiobutton",
                           background="#2C3E50",
                           foreground="#ECF0F1",
                           font=("Helvetica", 12))
        
        # Test data
        self.questions = {
            "beginner": [
                {
                    "question": "What is the output of print(2 + 2)?",
                    "options": ["4", "22", "2 + 2", "Error"],
                    "correct": "4"
                },
                {
                    "question": "Which of these is a valid Python variable name?",
                    "options": ["2variable", "_variable", "my-var", "class"],
                    "correct": "_variable"
                }
            ],
            "intermediate": [
                {
                    "question": "What is a decorator in Python?",
                    "options": [
                        "A function that takes another function as argument",
                        "A class that inherits from another class",
                        "A type of loop",
                        "A string formatting method"
                    ],
                    "correct": "A function that takes another function as argument"
                },
                {
                    "question": "What does the 'yield' keyword do?",
                    "options": [
                        "Pauses function execution and returns a value",
                        "Terminates the program",
                        "Creates a new thread",
                        "Defines a new class"
                    ],
                    "correct": "Pauses function execution and returns a value"
                }
            ],
            "advanced": [
                {
                    "question": "What is a metaclass in Python?",
                    "options": [
                        "A class that inherits from multiple classes",
                        "A class that defines how a class behaves",
                        "A class that cannot be instantiated",
                        "A class with only static methods"
                    ],
                    "correct": "A class that defines how a class behaves"
                }
            ]
        }
        
        self.current_level = "beginner"
        self.current_question = 0
        self.score = 0
        self.max_questions = len(self.questions[self.current_level])
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self, style="Modern.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="Python Programming Test",
            style="Title.TLabel"
        )
        self.title_label.pack(pady=(0, 20))
        
        # Level indicator
        self.level_label = ttk.Label(
            self.main_frame,
            text=f"Level: {self.current_level.capitalize()}",
            style="Score.TLabel"
        )
        self.level_label.pack(pady=(0, 10))
        
        # Score
        self.score_label = ttk.Label(
            self.main_frame,
            text=f"Score: {self.score}/{self.max_questions}",
            style="Score.TLabel"
        )
        self.score_label.pack(pady=(0, 20))
        
        # Question
        self.question_label = ttk.Label(
            self.main_frame,
            style="Question.TLabel"
        )
        self.question_label.pack(pady=(0, 20))
        
        # Answer options
        self.answer_var = tk.StringVar()
        self.options_frame = ttk.Frame(self.main_frame, style="Modern.TFrame")
        self.options_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Navigation buttons
        self.button_frame = ttk.Frame(self.main_frame, style="Modern.TFrame")
        self.button_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.submit_btn = ttk.Button(
            self.button_frame,
            text="Submit",
            style="Modern.TButton",
            command=self.check_answer
        )
        self.submit_btn.pack(side=tk.RIGHT, padx=5)
        
        self.retry_btn = ttk.Button(
            self.button_frame,
            text="Retry Level",
            style="Modern.TButton",
            command=self.retry_level
        )
        self.retry_btn.pack(side=tk.LEFT, padx=5)
        
        self.show_question()
        
    def show_question(self):
        question_data = self.questions[self.current_level][self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
        
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Create new options
        for option in question_data["options"]:
            rb = ttk.Radiobutton(
                self.options_frame,
                text=option,
                value=option,
                variable=self.answer_var,
                style="Answer.TRadiobutton"
            )
            rb.pack(anchor=tk.W, pady=5)
    
    def check_answer(self):
        if not self.answer_var.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return
            
        correct_answer = self.questions[self.current_level][self.current_question]["correct"]
        if self.answer_var.get() == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/{self.max_questions}")
        
        self.current_question += 1
        if self.current_question < self.max_questions:
            self.show_question()
            self.answer_var.set("")
        else:
            self.finish_level()
    
    def finish_level(self):
        passing_score = self.max_questions * 0.7
        if self.score >= passing_score:
            next_level = {
                "beginner": "intermediate",
                "intermediate": "advanced",
                "advanced": "completed"
            }[self.current_level]
            
            if next_level == "completed":
                messagebox.showinfo("Congratulations!", 
                                  "You've completed all levels!\n"
                                  f"Final score: {self.score}/{self.max_questions}")
                self.retry_level()
            else:
                if messagebox.askyesno("Level Complete!", 
                                     f"You passed with score {self.score}/{self.max_questions}!\n"
                                     "Would you like to proceed to the next level?"):
                    self.current_level = next_level
                    self.current_question = 0
                    self.score = 0
                    self.max_questions = len(self.questions[self.current_level])
                    self.level_label.config(text=f"Level: {self.current_level.capitalize()}")
                    self.score_label.config(text=f"Score: {self.score}/{self.max_questions}")
                    self.show_question()
                    self.answer_var.set("")
        else:
            messagebox.showinfo("Level Failed", 
                              f"Your score: {self.score}/{self.max_questions}\n"
                              "You need 70% to pass. Try again!")
            self.retry_level()
    
    def retry_level(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}/{self.max_questions}")
        self.show_question()
        self.answer_var.set("")

if __name__ == "__main__":
    app = ProgrammingTest()
    app.mainloop()
