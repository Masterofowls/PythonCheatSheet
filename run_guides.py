from flask import Flask, render_template_string
import importlib
import sys
from typing import Dict, Callable
import time

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Guides Directory</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .guide { margin: 20px 0; padding: 10px; border: 1px solid #ddd; }
        .file-content { background: #f5f5f5; padding: 15px; border-radius: 5px; margin-top: 10px; white-space: pre-wrap; display: none; }
        .toggle-btn { padding: 5px 10px; background: #4CAF50; color: white; border: none; border-radius: 3px; cursor: pointer; }
        .toggle-btn:hover { background: #45a049; }
    </style>
    <script>
        function toggleCode(element) {
            const content = element.nextElementSibling;
            const isVisible = content.style.display === 'block';
            content.style.display = isVisible ? 'none' : 'block';
            element.textContent = isVisible ? 'Show Code' : 'Hide Code';
        }
    </script>
</head>
<body>
    <h1>Python Guides Directory</h1>
    {% for name, description in demos.items() %}
    <div class="guide">
        <h3>{{ name }}</h3>
        <p>{{ description }}</p>
        {% if files.get(name) %}
            <button class="toggle-btn" onclick="toggleCode(this)">Show Code</button>
            <div class="file-content">{{ files.get(name) }}</div>
        {% endif %}
    </div>
    {% endfor %}
</body>
</html>
"""

demos: Dict[str, str] = {
    "Common Usage Guide": "Comprehensive Python Programming Guide",
    "Advanced Calculator": "GUI Calculator Application",
    "AI Guide": "Artificial Intelligence Examples",
    "Directory Guide": "Python Guides Directory",
    "Django Guide": "Django Web Framework Guide",
    "Flask Guide": "Flask Web Framework Guide",
    "JSON Guide": "JSON Processing Guide",
    "Packages Guide": "Modern Python Packages Guide",
    "PIP Guide": "Python Package Manager Guide",
    "PIPX Guide": "PIPX Package Management Guide",
    "Programming Test": "Programming Test Examples",
    "PyEnv Guide": "Python Environment Guide",
    "PyGame Guide": "PyGame Development Guide",
    "PyPy Guide": "PyPy Implementation Guide",
    "PyQt Guide": "PyQt GUI Development Guide",
    "Server Guide": "Python Server Implementations",
    "SQL Guide": "SQL Operations Guide",
    "Testing Guide": "Python Testing Guide",
    "Turtle Guide": "Python Turtle Graphics Guide"
}

def read_file_content(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return None

@app.route('/')
def home():
    files = {
        "Common Usage Guide": read_file_content('commonusage.py'),
        "Advanced Calculator": read_file_content('advanced_calculator.py'),
        "AI Guide": read_file_content('ai_guide.py'),
        "Directory Guide": read_file_content('directory_guide.py'),
        "Django Guide": read_file_content('django_guide.py'),
        "Flask Guide": read_file_content('flask_guide.py'),
        "JSON Guide": read_file_content('json_guide.py'),
        "Packages Guide": read_file_content('packages_guide.py'),
        "PIP Guide": read_file_content('pip_guide.py'),
        "PIPX Guide": read_file_content('pipx_guide.py'),
        "Programming Test": read_file_content('programming_test.py'),
        "PyEnv Guide": read_file_content('pyenv_guide.py'),
        "PyGame Guide": read_file_content('pygame_guide.py'),
        "PyPy Guide": read_file_content('pypy_guide.py'),
        "PyQt Guide": read_file_content('pyqt_guide.py'),
        "Server Guide": read_file_content('server_guide.py'),
        "SQL Guide": read_file_content('sql_guide.py'),
        "Testing Guide": read_file_content('testing_guide.py'),
        "Turtle Guide": read_file_content('turtle_guide.py')
    }
    return render_template_string(HTML_TEMPLATE, demos=demos, files=files)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)