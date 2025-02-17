
"""
COMPREHENSIVE PYTHON JSON OPERATIONS GUIDE
========================================
This guide covers fundamental to advanced JSON operations in Python.
Each section demonstrates different aspects of JSON handling with clear explanations.
"""

import json
from typing import Any, Dict, List
from datetime import datetime

# ===========================
# SECTION 1: BASIC JSON OPERATIONS
# ===========================
"""
Basic JSON operations include converting Python objects to JSON and vice versa.
These operations are fundamental for working with JSON data.
"""
print("\n=== Basic JSON Operations ===")

# Python dict to JSON string
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(person)
print(f"Python dict to JSON string:\n{json_string}")

# JSON string to Python dict
decoded_person = json.loads(json_string)
print(f"\nJSON string to Python dict:\n{decoded_person}")

# ===========================
# SECTION 2: FORMATTED JSON
# ===========================
"""
JSON can be formatted for better readability using indentation
and sorting keys.
"""
print("\n=== Formatted JSON ===")

# Pretty printing JSON
formatted_json = json.dumps(person, indent=4, sort_keys=True)
print(f"Formatted JSON:\n{formatted_json}")

# ============================
# SECTION 3: COMPLEX JSON DATA
# ============================
"""
JSON can handle nested structures with arrays and objects.
"""
print("\n=== Complex JSON Data ===")

complex_data = {
    "name": "Tech Corp",
    "employees": [
        {"id": 1, "name": "Alice", "roles": ["developer", "team lead"]},
        {"id": 2, "name": "Bob", "roles": ["designer"]}
    ],
    "office_locations": {
        "main": "New York",
        "branches": ["London", "Tokyo"]
    }
}

print(f"Complex JSON:\n{json.dumps(complex_data, indent=2)}")

# ================================
# SECTION 4: FILE OPERATIONS
# ================================
"""
JSON data can be read from and written to files.
"""
print("\n=== JSON File Operations ===")

# Writing JSON to file
with open('data.json', 'w') as f:
    json.dump(complex_data, f, indent=4)
print("Written to data.json")

# Reading JSON from file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
print(f"\nRead from data.json:\n{json.dumps(loaded_data, indent=2)}")

# ================================
# SECTION 5: CUSTOM JSON ENCODING
# ================================
"""
Custom JSON encoders handle Python objects that aren't JSON-serializable
by default, like datetime objects.
"""
print("\n=== Custom JSON Encoding ===")

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data_with_date = {
    "name": "Event",
    "timestamp": datetime.now()
}

encoded_data = json.dumps(data_with_date, cls=CustomEncoder, indent=2)
print(f"Custom encoded JSON:\n{encoded_data}")

# ================================
# SECTION 6: JSON SCHEMA VALIDATION
# ================================
"""
Basic JSON validation can be implemented using Python.
For production use, consider using libraries like jsonschema.
"""
print("\n=== JSON Validation ===")

def validate_person_json(data: Dict[str, Any]) -> bool:
    required_fields = ["name", "age", "city"]
    return all(field in data for field in required_fields)

# Test validation
valid_json = {"name": "John", "age": 30, "city": "New York"}
invalid_json = {"name": "John", "age": 30}

print(f"Valid JSON validation: {validate_person_json(valid_json)}")
print(f"Invalid JSON validation: {validate_person_json(invalid_json)}")

# ================================
# SECTION 7: JSON MERGING
# ================================
"""
Merging multiple JSON objects is a common operation.
"""
print("\n=== JSON Merging ===")

json1 = {"name": "John", "age": 30}
json2 = {"city": "New York", "occupation": "developer"}

# Merge using dict unpacking
merged_json = {**json1, **json2}
print(f"Merged JSON:\n{json.dumps(merged_json, indent=2)}")

# ================================
# SECTION 8: JSON PATH TRAVERSAL
# ================================
"""
Accessing nested JSON data using path-like syntax.
"""
print("\n=== JSON Path Traversal ===")

def get_json_value(data: Dict[str, Any], path: str) -> Any:
    keys = path.split('.')
    result = data
    for key in keys:
        if isinstance(result, dict):
            result = result.get(key)
        else:
            return None
    return result

nested_json = {
    "user": {
        "personal": {
            "name": "John",
            "contact": {
                "email": "john@example.com"
            }
        }
    }
}

print(f"Value at 'user.personal.contact.email': {get_json_value(nested_json, 'user.personal.contact.email')}")

# ================================
# SECTION 9: JSON ARRAY OPERATIONS
# ================================
"""
Working with JSON arrays (Python lists) in various ways.
"""
print("\n=== JSON Array Operations ===")

json_array = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Filter JSON array
filtered = [item for item in json_array if item["id"] > 1]
print(f"Filtered array:\n{json.dumps(filtered, indent=2)}")

# Map JSON array
mapped = [{"name": item["name"].upper()} for item in json_array]
print(f"\nMapped array:\n{json.dumps(mapped, indent=2)}")

# ================================
# SECTION 10: ERROR HANDLING
# ================================
"""
Proper error handling for JSON operations is crucial.
"""
print("\n=== JSON Error Handling ===")

def safe_json_loads(json_str: str) -> Dict[str, Any]:
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}

# Test with invalid JSON
invalid_json_str = '{"name": "John", age: 30}'  # Missing quotes around 'age'
result = safe_json_loads(invalid_json_str)
print(f"Result of parsing invalid JSON: {result}")
