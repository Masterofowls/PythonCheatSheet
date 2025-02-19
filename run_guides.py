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
    </style>
</head>
<body>
    <h1>Python Guides Directory</h1>
    {% for name, description in demos.items() %}
    <div class="guide">
        <h3>{{ name }}</h3>
        <p>{{ description }}</p>
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

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, demos=demos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)