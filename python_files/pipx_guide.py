
"""
COMPREHENSIVE PYTHON PIPX GUIDE
=============================
This guide covers pipx package management concepts and usage.
Each section demonstrates different aspects of pipx with examples.
"""

import subprocess
import sys
from typing import List, Dict, Optional

# ===========================
# SECTION 1: PIPX OPERATIONS
# ===========================
"""
Basic pipx operations simulation.
"""
def simulate_pipx_install(package_name: str) -> bool:
    """Simulate pipx install command"""
    try:
        subprocess.run(['which', package_name], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def list_installed_apps() -> List[str]:
    """List installed applications"""
    try:
        result = subprocess.run(['which', '-a', 'python'], check=True, capture_output=True, text=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError:
        return []

# ===========================
# SECTION 2: APP MANAGEMENT
# ===========================
"""
Managing applications installed with pipx.
"""
def check_app_installed(app_name: str) -> bool:
    """Check if an application is installed"""
    try:
        subprocess.run(['which', app_name], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_app_version(app_name: str) -> Optional[str]:
    """Get version of installed application"""
    try:
        result = subprocess.run([app_name, '--version'], capture_output=True, text=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

# ===========================
# SECTION 3: ENVIRONMENT INFO
# ===========================
"""
Getting information about the pipx environment.
"""
def get_python_info() -> Dict[str, str]:
    """Get Python environment information"""
    return {
        'executable': sys.executable,
        'version': sys.version,
        'platform': sys.platform
    }

# Example usage
if __name__ == "__main__":
    print("Pipx Environment Information:")
    info = get_python_info()
    for key, value in info.items():
        print(f"{key.title()}: {value}")
    
    print("\nInstalled Applications:")
    for app in list_installed_apps():
        print(f"- {app}")
    
    test_apps = ['pip', 'python', 'black']
    print("\nChecking Applications:")
    for app in test_apps:
        installed = check_app_installed(app)
        version = get_app_version(app) if installed else None
        status = f"Installed (Version: {version})" if installed else "Not installed"
        print(f"{app}: {status}")
