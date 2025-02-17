"""
COMPREHENSIVE PYTHON TURTLE GUIDE
===============================
This guide covers turtle graphics concepts and drawing.
Each section demonstrates different aspects of turtle graphics.
"""

import turtle
from typing import List, Tuple
import math

# ===========================
# SECTION 1: BASIC SETUP
# ===========================
"""
Basic turtle setup and movement.
"""
def setup_turtle() -> turtle.Turtle:
    """Initialize and configure turtle"""
    t = turtle.Turtle()
    t.speed(6)  # Set drawing speed (1-10)
    return t

def reset_turtle(t: turtle.Turtle):
    """Reset turtle to center"""
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# ===========================
# SECTION 2: BASIC SHAPES
# ===========================
"""
Drawing basic geometric shapes.
"""
def draw_square(t: turtle.Turtle, size: int):
    """Draw a square"""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_circle(t: turtle.Turtle, radius: int):
    """Draw a circle"""
    t.circle(radius)

def draw_star(t: turtle.Turtle, size: int):
    """Draw a five-pointed star"""
    for _ in range(5):
        t.forward(size)
        t.right(144)

# ===========================
# SECTION 3: COMPLEX PATTERNS
# ===========================
"""
Creating complex patterns using turtle.
"""
def draw_spiral(t: turtle.Turtle, start_len: int, increment: int):
    """Draw a square spiral"""
    length = start_len
    for i in range(20):
        t.forward(length)
        t.right(90)
        length += increment

def draw_flower(t: turtle.Turtle, radius: int, petals: int):
    """Draw a flower pattern"""
    for _ in range(petals):
        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.left(360/petals)

# ===========================
# SECTION 4: COLORS
# ===========================
"""
Working with colors and fills.
"""
def colorful_pattern(t: turtle.Turtle):
    """Draw a colorful pattern"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.width(2)
    
    for color in colors:
        t.color(color)
        t.begin_fill()
        draw_star(t, 50)
        t.end_fill()
        t.right(60)

# Example usage
def main():
    # Setup
    screen = turtle.Screen()
    screen.title("Turtle Graphics Guide")
    screen.bgcolor("white")
    t = setup_turtle()
    
    # Draw various shapes
    draw_square(t, 100)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    
    draw_circle(t, 50)
    t.penup()
    t.goto(150, 0)
    t.pendown()
    
    draw_star(t, 100)
    t.penup()
    t.goto(0, 150)
    t.pendown()
    
    draw_spiral(t, 5, 5)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    
    draw_flower(t, 30, 8)
    reset_turtle(t)
    
    colorful_pattern(t)
    
    # Hide turtle and keep window open
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()