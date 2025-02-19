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
        .file-content { background: #f5f5f5; padding: 15px; border-radius: 5px; margin-top: 10px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Python Guides Directory</h1>
    {% for name, description in demos.items() %}
    <div class="guide">
        <h3>{{ name }}</h3>
        <p>{{ description }}</p>
        {% if files.get(name) %}
            <div class="file-content">{{ files.get(name) }}</div>
        {% endif %}
    </div>
    {% endfor %}
</body>
</html>
"""

demos: Dict[str, str] = {
    "Advanced Calculator": "GUI Calculator (run advanced_calculator.py locally)",
    "PyGame": "Interactive Game Demo (run pygame_guide.py locally)",
    "Turtle": "Graphics Demo (run turtle_guide.py locally)",
    "SQL": "SQL Operations Examples (run sql_guide.py)",
    "JSON": "JSON Processing Examples (run json_guide.py)",
    "Flask": "Web Framework Examples (run flask_guide.py)"
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
        "Flask": read_file_content('flask_guide.py'),
        "SQL": read_file_content('sql_guide.py'),
        "JSON": read_file_content('json_guide.py'),
        "Advanced Calculator": read_file_content('advanced_calculator.py')
    }
    return render_template_string(HTML_TEMPLATE, demos=demos, files=files)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)