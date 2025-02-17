
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
