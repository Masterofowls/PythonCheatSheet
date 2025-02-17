
"""
COMPREHENSIVE PYTHON TESTING GUIDE
================================
This guide covers various testing approaches in Python using unittest and pytest.
Each section demonstrates different testing concepts with practical examples.
"""

import unittest
import pytest
from typing import List, Dict
import math

# ===========================
# SECTION 1: BASIC UNIT TESTS
# ===========================

class Calculator:
    """Simple calculator class for testing demonstration"""
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y
    
    @staticmethod
    def divide(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

class TestCalculator(unittest.TestCase):
    """Basic unit tests using unittest"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

# ===========================
# SECTION 2: PYTEST EXAMPLES
# ===========================

def is_palindrome(s: str) -> bool:
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

@pytest.mark.parametrize("input_str,expected", [
    ("radar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True)
])
def test_palindrome(input_str: str, expected: bool):
    """Test palindrome function with multiple inputs"""
    assert is_palindrome(input_str) == expected

# =============================
# SECTION 3: FIXTURE EXAMPLES
# =============================

@pytest.fixture
def sample_data():
    """Fixture providing sample data"""
    return {
        'numbers': [1, 2, 3, 4, 5],
        'metadata': {'created': '2024-01-01'}
    }

def test_data_structure(sample_data):
    """Test using fixture"""
    assert len(sample_data['numbers']) == 5
    assert isinstance(sample_data['metadata'], dict)

# ==============================
# SECTION 4: MOCK EXAMPLES
# ==============================

from unittest.mock import Mock, patch
import requests

class UserService:
    def get_user_data(self, user_id: int) -> Dict:
        response = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()

def test_user_service():
    """Test with mocked HTTP request"""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "John"}
        mock_get.return_value = mock_response
        
        service = UserService()
        data = service.get_user_data(1)
        
        assert data["name"] == "John"
        mock_get.assert_called_once()

# ===============================
# SECTION 5: EXCEPTION TESTING
# ===============================

class StringProcessor:
    @staticmethod
    def convert_to_int(s: str) -> int:
        if not s.strip():
            raise ValueError("Empty string")
        return int(s)

def test_string_processor_exceptions():
    """Test exception handling"""
    processor = StringProcessor()
    
    with pytest.raises(ValueError):
        processor.convert_to_int("")
    
    with pytest.raises(ValueError):
        processor.convert_to_int("   ")
    
    with pytest.raises(ValueError):
        processor.convert_to_int("abc")

# ================================
# SECTION 6: ASYNC TEST EXAMPLES
# ================================

import asyncio

async def async_square(x: float) -> float:
    await asyncio.sleep(0.1)  # Simulate async operation
    return x * x

@pytest.mark.asyncio
async def test_async_square():
    """Test async function"""
    result = await async_square(4)
    assert result == 16

# ================================
# SECTION 7: CLASS-BASED TESTING
# ================================

class TestStringMethods(unittest.TestCase):
    """Class demonstrating various assertion methods"""
    
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
    
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

# =================================
# SECTION 8: PARAMETERIZED TESTING
# =================================

@pytest.mark.parametrize("input_num,expected", [
    (4, 2),
    (9, 3),
    (16, 4),
    (25, 5)
])
def test_sqrt(input_num: float, expected: float):
    """Parameterized test for square root"""
    assert math.sqrt(input_num) == expected

# ==================================
# SECTION 9: TEST COVERAGE EXAMPLE
# ==================================

class StringUtils:
    @staticmethod
    def reverse(s: str) -> str:
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return s[::-1]
    
    @staticmethod
    def count_vowels(s: str) -> int:
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return sum(1 for char in s.lower() if char in 'aeiou')

class TestStringUtils(unittest.TestCase):
    """Test case demonstrating full coverage"""
    
    def test_reverse(self):
        utils = StringUtils()
        self.assertEqual(utils.reverse("hello"), "olleh")
        self.assertEqual(utils.reverse(""), "")
        with self.assertRaises(TypeError):
            utils.reverse(123)
    
    def test_count_vowels(self):
        utils = StringUtils()
        self.assertEqual(utils.count_vowels("hello"), 2)
        self.assertEqual(utils.count_vowels("AEIOU"), 5)
        self.assertEqual(utils.count_vowels(""), 0)
        with self.assertRaises(TypeError):
            utils.count_vowels(123)

# Main execution
if __name__ == '__main__':
    unittest.main()
