
# Basic Data Types and Variables
print("\n=== Basic Data Types ===")
integer_num = 42
float_num = 3.14
string_text = "Hello, Python!"
boolean_val = True
none_val = None

print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"String: {string_text}")
print(f"Boolean: {boolean_val}")
print(f"None: {none_val}")

# Operators
print("\n=== Operators ===")
a, b = 10, 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Strings
print("\n=== String Operations ===")
text = "Python Programming"
print(f"Original text: {text}")
print(f"Upper case: {text.upper()}")
print(f"Lower case: {text.lower()}")
print(f"Split words: {text.split()}")
print(f"Replace: {text.replace('Python', 'Cool')}")
print(f"Length: {len(text)}")
print(f"Slice: {text[0:6]}")

# Lists (Arrays)
print("\n=== Lists ===")
fruits = ["apple", "banana", "orange", "grape"]
print(f"Original list: {fruits}")
fruits.append("mango")
print(f"After append: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Sliced list: {fruits[1:3]}")
fruits.sort()
print(f"Sorted list: {fruits}")

# Dictionaries
print("\n=== Dictionaries ===")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
person["email"] = "john@example.com"
print(f"After adding email: {person}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# Control Flow
print("\n=== Control Flow ===")
# If-else
number = 15
if number > 20:
    print("Number is greater than 20")
elif number > 10:
    print("Number is greater than 10")
else:
    print("Number is less than or equal to 10")

# Loops
print("\n=== Loops ===")
# For loop
print("For loop with range:")
for i in range(5):
    print(i, end=" ")
print("\n")

# While loop
print("While loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print("\n")

# List comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(5)]
print(f"Squares using list comprehension: {squares}")

# Functions
print("\n=== Functions ===")
def calculate_area(length, width):
    """Calculate area of a rectangle"""
    return length * width

print(f"Area of rectangle (5x3): {calculate_area(5, 3)}")

# Lambda function
print("\n=== Lambda Functions ===")
square = lambda x: x**2
print(f"Square of 7 using lambda: {square(7)}")

# Error Handling
print("\n=== Error Handling ===")
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Error handling complete")

# Sets
print("\n=== Sets ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Advanced String Formatting
print("\n=== Advanced String Formatting ===")
name = "Alice"
age = 25
print("Basic format: My name is {} and I'm {} years old".format(name, age))
print(f"F-string: My name is {name} and I'm {age} years old")
print("Named format: My name is %(name)s and I'm %(age)d years old" % {"name": name, "age": age})

# Decorators
print("\n=== Decorators ===")
def timer_decorator(func):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end-start:.2f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

print(slow_function())

# Generators
print("\n=== Generators ===")
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")
for num in fibonacci_generator(10):
    print(num, end=" ")
print("\n")

# Context Managers
print("\n=== Context Managers ===")
from contextlib import contextmanager

@contextmanager
def temporary_value(obj, attr, value):
    old_value = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)

class Example:
    def __init__(self):
        self.value = 1

obj = Example()
print(f"Before: {obj.value}")
with temporary_value(obj, 'value', 2):
    print(f"During: {obj.value}")
print(f"After: {obj.value}")

# Advanced Data Structures
print("\n=== Advanced Data Structures ===")
from collections import defaultdict, Counter, deque

# DefaultDict
print("DefaultDict example:")
dd = defaultdict(list)
words = ["apple", "banana", "apple", "cherry"]
for word in words:
    dd[word[0]].append(word)
print(dd)

# Counter
print("\nCounter example:")
inventory = Counter(['apple', 'banana', 'apple', 'cherry', 'apple'])
print(inventory)
print(f"Most common item: {inventory.most_common(1)}")

# Deque (Double-ended queue)
print("\nDeque example:")
queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(0)
print(f"Deque: {queue}")
print(f"Pop right: {queue.pop()}")
print(f"Pop left: {queue.popleft()}")
print(f"Final deque: {queue}")

# Type Hints
print("\n=== Type Hints ===")
from typing import List, Dict, Optional

def process_data(numbers: List[int], config: Dict[str, str], debug: Optional[bool] = None) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

print(process_data([1, 2, 3, 4], {"mode": "average"}))

# Advanced List Operations
print("\n=== Advanced List Operations ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter and map in one line
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Squares of even numbers: {even_squares}")

# Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
square_dict = {x: x**2 for x in range(5)}
print(f"Square dictionary: {square_dict}")

# Unpacking
print("\n=== Unpacking ===")
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Advanced Exception Handling
print("\n=== Advanced Exception Handling ===")
class CustomError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

try:
    raise CustomError("Something went wrong", 500)
except CustomError as e:
    print(f"Caught custom error: {e.message} (Code: {e.error_code})")
