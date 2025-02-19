
"""
COMPREHENSIVE PYTHON PYPY GUIDE
==============================
This guide covers PyPy concepts and optimizations.
Each section demonstrates different aspects of PyPy with examples.
"""

import time
import sys
from typing import List, Dict, Any

# ===========================
# SECTION 1: BASIC LOOP OPTIMIZATION
# ===========================
"""
Demonstrating PyPy's JIT optimization with loops.
"""
def compute_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total

# ===========================
# SECTION 2: LIST COMPREHENSION
# ===========================
"""
PyPy optimizes list comprehensions efficiently.
"""
def generate_squares(n: int) -> List[int]:
    return [i * i for i in range(n)]

# ===========================
# SECTION 3: RECURSIVE FUNCTIONS
# ===========================
"""
PyPy handles recursion with optimized trace compilation.
"""
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# ===========================
# SECTION 4: DICTIONARY OPERATIONS
# ===========================
"""
PyPy optimizes dictionary access patterns.
"""
def dict_operations(n: int) -> Dict[int, int]:
    d = {}
    for i in range(n):
        d[i] = i * i
    return d

# ===========================
# SECTION 5: PERFORMANCE COMPARISON
# ===========================
"""
Compare execution times between operations.
"""
def measure_performance(func: callable, *args: Any) -> float:
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time

# ===========================
# SECTION 6: NUMERIC OPERATIONS
# ===========================
"""
PyPy's efficient handling of numeric operations.
"""
def compute_series(n: int) -> float:
    return sum(1.0/i for i in range(1, n + 1))

# ===========================
# SECTION 7: STRING MANIPULATIONS
# ===========================
"""
String operations optimization in PyPy.
"""
def string_concat(n: int) -> str:
    result = ""
    for i in range(n):
        result += str(i)
    return result

# Example usage and performance measurement
if __name__ == "__main__":
    n = 1000000
    
    print("Performance measurements:")
    print(f"Loop sum time: {measure_performance(compute_sum, n):.4f} seconds")
    print(f"Squares generation time: {measure_performance(generate_squares, n):.4f} seconds")
    print(f"Factorial(20) time: {measure_performance(factorial, 20):.4f} seconds")
    print(f"Dictionary operations time: {measure_performance(dict_operations, n):.4f} seconds")
    print(f"Series computation time: {measure_performance(compute_series, n):.4f} seconds")
    print(f"String concatenation time: {measure_performance(string_concat, 1000):.4f} seconds")
    
    print("\nPython Implementation Info:")
    print(f"Implementation: {sys.implementation.name}")
    print(f"Version: {sys.version}")
