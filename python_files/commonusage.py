
"""
COMPREHENSIVE PYTHON PROGRAMMING GUIDE
====================================
This guide covers fundamental to advanced Python programming concepts with practical examples.
Each section demonstrates different aspects of Python with clear explanations and outputs.
"""

# =============================================
# SECTION 1: FUNDAMENTAL DATA TYPES & VARIABLES
# =============================================
"""
Python's basic data types form the foundation of all programming.
These include numbers, strings, booleans, and the special None type.
"""
print("\n=== Basic Data Types ===")
integer_num = 42        # Whole numbers
float_num = 3.14       # Decimal numbers
string_text = "Hello, Python!"  # Text data
boolean_val = True     # Logical values
none_val = None       # Represents absence of value

print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"String: {string_text}")
print(f"Boolean: {boolean_val}")
print(f"None: {none_val}")

# =============================================
# SECTION 2: DATA STRUCTURES
# =============================================
"""
Python provides several built-in data structures for organizing data.
"""
print("\n=== Data Structures ===")

# Lists - Ordered, mutable sequences
my_list = [1, 2, 3, "four", 5.0]
print("List:", my_list)
my_list.append(6)
print("After append:", my_list)

# Tuples - Ordered, immutable sequences
my_tuple = (1, 2, "three")
print("Tuple:", my_tuple)

# Dictionaries - Key-value pairs
my_dict = {"name": "Python", "version": 3.11}
print("Dictionary:", my_dict)
print("Version:", my_dict["version"])

# Sets - Unordered collection of unique elements
my_set = {1, 2, 3, 3, 2, 1}
print("Set:", my_set)  # Duplicates are removed

# =============================================
# SECTION 3: CONTROL FLOW
# =============================================
"""
Control flow statements determine the execution path of the program.
"""
print("\n=== Control Flow ===")

# If-elif-else conditions
x = 10
if x > 20:
    print("x is greater than 20")
elif x > 5:
    print("x is greater than 5 but less than or equal to 20")
else:
    print("x is less than or equal to 5")

# For loops
print("\nFor loop example:")
for i in range(3):
    print(f"Iteration {i}")

# While loops
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# =============================================
# SECTION 4: FUNCTIONS
# =============================================
"""
Functions are reusable blocks of code that perform specific tasks.
"""
print("\n=== Functions ===")

# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

# Lambda function (anonymous function)
square = lambda x: x * x

print(greet("Python"))
print(f"2 to the power of 3: {power(2, 3)}")
print(f"Square of 4: {square(4)}")

# =============================================
# SECTION 5: ERROR HANDLING
# =============================================
"""
Error handling helps manage exceptions and errors gracefully.
"""
print("\n=== Error Handling ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Division successful!")
finally:
    print("This always executes")

# =============================================
# SECTION 6: CLASSES AND OBJECTS
# =============================================
"""
Object-oriented programming concepts in Python.
"""
print("\n=== Classes and Objects ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

person = Person("Alice", 30)
print(person.greet())

# =============================================
# SECTION 7: FILE OPERATIONS
# =============================================
"""
Common file operations in Python.
"""
print("\n=== File Operations ===")

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello from Python!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File content:", content)

# =============================================
# SECTION 8: DECORATORS
# =============================================
"""
Demonstrates the use of decorators in Python.
"""
print("\n=== Decorators ===")

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end-start:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def example_function():
    import time
    time.sleep(1)
    return "Function completed"

print(example_function())

# =============================================
# SECTION 9: CONTEXT MANAGERS
# =============================================
"""
Using context managers with 'with' statement.
"""
print("\n=== Context Managers ===")

class Timer:
    def __enter__(self):
        from time import time
        self.start = time()
        return self

    def __exit__(self, *args):
        from time import time
        self.end = time()
        print(f"Operation took: {self.end - self.start:.2f} seconds")

with Timer():
    import time
    time.sleep(0.5)
    print("Operation completed")

# =============================================
# SECTION 10: GENERATORS
# =============================================
"""
Generator functions and expressions.
"""
print("\n=== Generators ===")

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence:")
for num in fibonacci_generator(5):
    print(num, end=" ")
print()

# Generator expression
squares = (x**2 for x in range(5))
print("Squares:", list(squares))

if __name__ == "__main__":
    print("\nGuide execution complete!")
