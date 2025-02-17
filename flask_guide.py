
"""
COMPREHENSIVE PYTHON FLASK GUIDE
===============================
This guide covers fundamental to advanced Flask concepts with practical examples.
Each section demonstrates different aspects of Flask web development.
"""

from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from functools import wraps

# ===========================
# SECTION 1: BASIC FLASK APP
# ===========================
"""
Creating a basic Flask application with routes.
"""
print("\n=== Basic Flask Setup ===")

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for sessions

@app.route('/')
def home():
    return 'Hello, Flask!'

# ===========================
# SECTION 2: ROUTE METHODS
# ===========================
"""
Handling different HTTP methods in Flask.
"""
print("\n=== Route Methods ===")

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "Data received", "data": data})
    return jsonify({"message": "Send data via POST"})

# ===========================
# SECTION 3: URL PARAMETERS
# ===========================
"""
Handling URL parameters and query strings.
"""
print("\n=== URL Parameters ===")

@app.route('/user/<username>')
def user_profile(username):
    return f'Profile page of {username}'

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f'Search results for: {query}'

# ===========================
# SECTION 4: TEMPLATES
# ===========================
"""
Using Jinja2 templates for rendering HTML.
"""
print("\n=== Templates ===")

@app.route('/template')
def template_example():
    user = {'name': 'John', 'age': 30}
    items = ['Apple', 'Banana', 'Orange']
    return render_template('example.html', user=user, items=items)

# ===========================
# SECTION 5: FORM HANDLING
# ===========================
"""
Processing form submissions.
"""
print("\n=== Form Handling ===")

@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f'Form submitted: {name} ({email})'
    return render_template('form.html')

# ===========================
# SECTION 6: SESSION HANDLING
# ===========================
"""
Managing user sessions.
"""
print("\n=== Session Handling ===")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f'Welcome {session["username"]}'

# ===========================
# SECTION 7: ERROR HANDLING
# ===========================
"""
Custom error handlers.
"""
print("\n=== Error Handling ===")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return 'Internal Server Error', 500

# ===========================
# SECTION 8: MIDDLEWARE
# ===========================
"""
Creating custom middleware.
"""
print("\n=== Middleware ===")

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "No authorization provided"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/protected')
@require_auth
def protected_route():
    return jsonify({"message": "Access granted"})

# ===========================
# SECTION 9: JSON APIs
# ===========================
"""
Building JSON APIs.
"""
print("\n=== JSON APIs ===")

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return jsonify(users)

# ===========================
# SECTION 10: FILE UPLOADS
# ===========================
"""
Handling file uploads.
"""
print("\n=== File Uploads ===")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    if file:
        filename = file.filename
        file.save(f'uploads/{filename}')
        return f'File {filename} uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
