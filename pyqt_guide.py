
"""
COMPREHENSIVE PYTHON QT (PyQt) GUIDE
===================================
This guide covers fundamental to advanced PyQt concepts for GUI development.
Each section demonstrates different aspects of PyQt with examples.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                           QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
                           QMessageBox, QComboBox, QTextEdit)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon
import sys

# ===========================
# SECTION 1: BASIC WINDOW
# ===========================
"""
Creating a basic PyQt window application.
"""
class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic PyQt Window")
        self.setGeometry(100, 100, 400, 300)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Add a label
        label = QLabel("Hello, PyQt!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

# ===========================
# SECTION 2: BUTTONS & EVENTS
# ===========================
"""
Working with buttons and handling events.
"""
class ButtonDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Demo")
        self.setGeometry(100, 100, 400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create button
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)
        
        # Add label for result
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
    
    def button_clicked(self):
        self.result_label.setText("Button was clicked!")

# ===========================
# SECTION 3: INPUT HANDLING
# ===========================
"""
Handling user input with various widgets.
"""
class InputDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Demo")
        self.setGeometry(100, 100, 400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Text input
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter text...")
        layout.addWidget(self.text_input)
        
        # Combo box
        self.combo = QComboBox()
        self.combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.combo)
        
        # Submit button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.handle_submit)
        layout.addWidget(self.submit_btn)
        
        # Result label
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
    
    def handle_submit(self):
        text = self.text_input.text()
        option = self.combo.currentText()
        self.result_label.setText(f"Text: {text}\nOption: {option}")

# ===========================
# SECTION 4: DIALOGS
# ===========================
"""
Working with dialog windows.
"""
class DialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Demo")
        self.setGeometry(100, 100, 400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Buttons for different dialogs
        info_btn = QPushButton("Show Info")
        info_btn.clicked.connect(self.show_info)
        layout.addWidget(info_btn)
        
        warning_btn = QPushButton("Show Warning")
        warning_btn.clicked.connect(self.show_warning)
        layout.addWidget(warning_btn)
        
        error_btn = QPushButton("Show Error")
        error_btn.clicked.connect(self.show_error)
        layout.addWidget(error_btn)
    
    def show_info(self):
        QMessageBox.information(self, "Info", "This is an information message")
    
    def show_warning(self):
        QMessageBox.warning(self, "Warning", "This is a warning message")
    
    def show_error(self):
        QMessageBox.critical(self, "Error", "This is an error message")

# ===========================
# SECTION 5: LAYOUTS
# ===========================
"""
Different layout demonstrations.
"""
class LayoutDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Demo")
        self.setGeometry(100, 100, 400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Horizontal layout
        h_layout = QHBoxLayout()
        for i in range(3):
            btn = QPushButton(f"Button {i+1}")
            h_layout.addWidget(btn)
        main_layout.addLayout(h_layout)
        
        # Vertical layout
        v_layout = QVBoxLayout()
        for i in range(3):
            label = QLabel(f"Label {i+1}")
            v_layout.addWidget(label)
        main_layout.addLayout(v_layout)

# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Choose one window to display
    # window = BasicWindow()
    # window = ButtonDemo()
    # window = InputDemo()
    # window = DialogDemo()
    window = LayoutDemo()
    
    window.show()
    sys.exit(app.exec_())
