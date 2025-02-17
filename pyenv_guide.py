
"""
COMPREHENSIVE PYTHON PYENV GUIDE
==============================
This guide covers pyenv concepts and version management.
Each section demonstrates different aspects of pyenv with examples.
"""

import sys
import platform
from typing import List, Dict

# ===========================
# SECTION 1: PYTHON VERSION INFO
# ===========================
"""
Getting current Python version information.
"""
def get_python_info() -> Dict[str, str]:
    return {
        'version': sys.version,
        'implementation': platform.python_implementation(),
        'compiler': platform.python_compiler(),
        'build': platform.python_build()
    }

# ===========================
# SECTION 2: VERSION CHECKING
# ===========================
"""
Checking Python version compatibility.
"""
def check_version_compatibility(required_version: str) -> bool:
    current = tuple(map(int, platform.python_version().split('.')))
    required = tuple(map(int, required_version.split('.')))
    return current >= required

# ===========================
# SECTION 3: FEATURE DETECTION
# ===========================
"""
Detecting Python features based on version.
"""
def get_available_features() -> List[str]:
    features = []
    version = sys.version_info
    
    if version >= (3, 5):
        features.append("Type Hints")
    if version >= (3, 6):
        features.append("f-strings")
    if version >= (3, 7):
        features.append("DataClasses")
    if version >= (3, 8):
        features.append("Walrus Operator")
    if version >= (3, 9):
        features.append("Dictionary Union")
    if version >= (3, 10):
        features.append("Pattern Matching")
        
    return features

# ===========================
# SECTION 4: VERSION REQUIREMENTS
# ===========================
"""
Managing version-specific code.
"""
def run_version_specific_code():
    if sys.version_info >= (3, 6):
        message = f"Using Python {sys.version_info.major}.{sys.version_info.minor}"
    else:
        message = "Using Python {}.{}".format(
            sys.version_info.major, 
            sys.version_info.minor
        )
    return message

# Example usage
if __name__ == "__main__":
    print("Python Environment Information:")
    info = get_python_info()
    for key, value in info.items():
        print(f"{key.title()}: {value}")
        
    print("\nVersion Compatibility:")
    print(f"Compatible with Python 3.6+: {check_version_compatibility('3.6')}")
    
    print("\nAvailable Features:")
    for feature in get_available_features():
        print(f"- {feature}")
        
    print("\nVersion Specific Code:")
    print(run_version_specific_code())
