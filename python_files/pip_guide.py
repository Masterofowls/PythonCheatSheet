"""
COMPREHENSIVE PYTHON PIP GUIDE
============================
This guide covers pip package management concepts and usage.
Each section demonstrates different aspects of pip with examples.
"""

import pkg_resources
import subprocess
from typing import List, Dict, Optional

# ===========================
# SECTION 1: PACKAGE INFO
# ===========================
"""
Getting package information.
"""
def get_installed_packages() -> List[str]:
    """Get list of installed packages"""
    return [f"{dist.key} {dist.version}"
            for dist in pkg_resources.working_set]

# ===========================
# SECTION 2: PACKAGE MANAGEMENT
# ===========================
"""
Package management utilities.
"""
def check_package_installed(package_name: str) -> bool:
    """Check if a package is installed"""
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def get_package_version(package_name: str) -> Optional[str]:
    """Get version of installed package"""
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

# ===========================
# SECTION 3: DEPENDENCY CHECK
# ===========================
"""
Checking package dependencies.
"""
def get_package_dependencies(package_name: str) -> List[str]:
    """Get package dependencies"""
    try:
        dist = pkg_resources.get_distribution(package_name)
        return [str(r) for r in dist.requires()]
    except pkg_resources.DistributionNotFound:
        return []

# ===========================
# SECTION 4: PACKAGE METADATA
# ===========================
"""
Getting package metadata.
"""
def get_package_metadata(package_name: str) -> Dict[str, str]:
    """Get package metadata"""
    try:
        dist = pkg_resources.get_distribution(package_name)
        return {
            'name': dist.key,
            'version': dist.version,
            'location': dist.location,
            'requires': str(dist.requires())
        }
    except pkg_resources.DistributionNotFound:
        return {}

# Example usage
if __name__ == "__main__":
    print("Installed Packages:")
    for pkg in get_installed_packages():
        print(f"- {pkg}")
        
    test_package = "requests"
    print(f"\nChecking {test_package}:")
    if check_package_installed(test_package):
        print(f"Version: {get_package_version(test_package)}")
        print("\nDependencies:")
        for dep in get_package_dependencies(test_package):
            print(f"- {dep}")
        print("\nMetadata:")
        for key, value in get_package_metadata(test_package).items():
            print(f"{key}: {value}")
    else:
        print(f"{test_package} is not installed")