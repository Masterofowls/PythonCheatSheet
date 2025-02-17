
"""
COMPREHENSIVE SQL OPERATIONS GUIDE
================================
This guide covers fundamental to advanced SQL operations in Python.
Each section demonstrates different SQL queries and database operations.
"""

import sqlite3
from typing import List, Tuple, Any
import os

# ===========================
# SECTION 1: BASIC CONNECTION
# ===========================
"""
Basic database connection and cursor creation.
"""
print("\n=== Basic Database Connection ===")

def create_connection(db_name: str = "example.db") -> sqlite3.Connection:
    """Create a database connection"""
    conn = sqlite3.connect(db_name)
    print(f"Connected to {db_name}")
    return conn

# ===========================
# SECTION 2: TABLE OPERATIONS
# ===========================
"""
Creating, altering, and dropping tables.
"""
print("\n=== Table Operations ===")

def create_tables(conn: sqlite3.Connection):
    """Create sample tables"""
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
    """)
    
    # Create orders table with foreign key
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT NOT NULL,
        price REAL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    print("Tables created successfully")

# ============================
# SECTION 3: INSERT OPERATIONS
# ============================
"""
Different ways to insert data into tables.
"""
print("\n=== Insert Operations ===")

def insert_data(conn: sqlite3.Connection):
    """Insert sample data"""
    cursor = conn.cursor()
    
    # Single insert
    cursor.execute("""
    INSERT INTO users (name, email, age) 
    VALUES (?, ?, ?)
    """, ("John Doe", "john@example.com", 30))
    
    # Multiple insert
    users = [
        ("Alice Smith", "alice@example.com", 25),
        ("Bob Johnson", "bob@example.com", 35),
        ("Carol White", "carol@example.com", 28)
    ]
    cursor.executemany("""
    INSERT INTO users (name, email, age) 
    VALUES (?, ?, ?)
    """, users)
    
    conn.commit()
    print("Data inserted successfully")

# ===========================
# SECTION 4: SELECT QUERIES
# ===========================
"""
Various SELECT queries demonstrating different SQL features.
"""
print("\n=== Select Operations ===")

def select_examples(conn: sqlite3.Connection):
    """Demonstrate various SELECT queries"""
    cursor = conn.cursor()
    
    # Basic SELECT
    print("\nAll users:")
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    
    # SELECT with WHERE
    print("\nUsers over 30:")
    cursor.execute("SELECT name, age FROM users WHERE age > 30")
    print(cursor.fetchall())
    
    # SELECT with ORDER BY
    print("\nUsers ordered by age:")
    cursor.execute("SELECT name, age FROM users ORDER BY age DESC")
    print(cursor.fetchall())
    
    # SELECT with GROUP BY
    print("\nCount of users by age:")
    cursor.execute("""
    SELECT age, COUNT(*) as count 
    FROM users 
    GROUP BY age
    """)
    print(cursor.fetchall())

# =============================
# SECTION 5: JOIN OPERATIONS
# =============================
"""
Different types of JOIN operations.
"""
print("\n=== Join Operations ===")

def join_examples(conn: sqlite3.Connection):
    """Demonstrate JOIN operations"""
    cursor = conn.cursor()
    
    # INNER JOIN
    cursor.execute("""
    SELECT users.name, orders.product, orders.price
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    """)
    print("\nInner Join results:")
    print(cursor.fetchall())
    
    # LEFT JOIN
    cursor.execute("""
    SELECT users.name, orders.product
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    """)
    print("\nLeft Join results:")
    print(cursor.fetchall())

# ============================
# SECTION 6: UPDATE OPERATIONS
# ============================
"""
Updating existing records in the database.
"""
print("\n=== Update Operations ===")

def update_examples(conn: sqlite3.Connection):
    """Demonstrate UPDATE operations"""
    cursor = conn.cursor()
    
    # Simple UPDATE
    cursor.execute("""
    UPDATE users 
    SET age = age + 1 
    WHERE name = 'John Doe'
    """)
    
    # UPDATE with multiple conditions
    cursor.execute("""
    UPDATE users 
    SET email = LOWER(email) 
    WHERE age > 25 AND age < 35
    """)
    
    conn.commit()
    print("Updates completed successfully")

# ============================
# SECTION 7: DELETE OPERATIONS
# ============================
"""
Deleting records from the database.
"""
print("\n=== Delete Operations ===")

def delete_examples(conn: sqlite3.Connection):
    """Demonstrate DELETE operations"""
    cursor = conn.cursor()
    
    # Simple DELETE
    cursor.execute("""
    DELETE FROM users 
    WHERE age < 25
    """)
    
    # DELETE with subquery
    cursor.execute("""
    DELETE FROM orders 
    WHERE user_id IN (
        SELECT id FROM users WHERE age > 60
    )
    """)
    
    conn.commit()
    print("Deletions completed successfully")

# ==============================
# SECTION 8: TRANSACTION HANDLING
# ==============================
"""
Managing database transactions.
"""
print("\n=== Transaction Handling ===")

def transaction_example(conn: sqlite3.Connection):
    """Demonstrate transaction handling"""
    cursor = conn.cursor()
    
    try:
        # Start transaction
        cursor.execute("BEGIN TRANSACTION")
        
        # Multiple operations
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Test User", 25))
        cursor.execute("UPDATE users SET age = age + 1 WHERE name = ?", ("Test User",))
        
        # Commit if all operations successful
        conn.commit()
        print("Transaction committed successfully")
        
    except sqlite3.Error as e:
        # Rollback in case of error
        conn.rollback()
        print(f"Transaction failed: {e}")

# ==============================
# SECTION 9: ADVANCED QUERIES
# ==============================
"""
Advanced SQL queries and operations.
"""
print("\n=== Advanced Queries ===")

def advanced_queries(conn: sqlite3.Connection):
    """Demonstrate advanced SQL queries"""
    cursor = conn.cursor()
    
    # Subquery
    cursor.execute("""
    SELECT name, age
    FROM users
    WHERE age > (SELECT AVG(age) FROM users)
    """)
    print("\nUsers above average age:")
    print(cursor.fetchall())
    
    # Common Table Expression (CTE)
    cursor.execute("""
    WITH UserStats AS (
        SELECT age, COUNT(*) as count
        FROM users
        GROUP BY age
    )
    SELECT age, count
    FROM UserStats
    WHERE count > 1
    """)
    print("\nAges with multiple users:")
    print(cursor.fetchall())
    
    # Window Function
    cursor.execute("""
    SELECT name, age,
           AVG(age) OVER (PARTITION BY substr(name,1,1)) as avg_age_by_initial
    FROM users
    """)
    print("\nAverage age by name initial:")
    print(cursor.fetchall())

# ==================================
# SECTION 10: DATABASE MAINTENANCE
# ==================================
"""
Database maintenance operations.
"""
print("\n=== Database Maintenance ===")

def maintenance_operations(conn: sqlite3.Connection):
    """Demonstrate maintenance operations"""
    cursor = conn.cursor()
    
    # Vacuum database
    cursor.execute("VACUUM")
    
    # Analyze tables
    cursor.execute("ANALYZE users")
    
    # Get table info
    cursor.execute("PRAGMA table_info(users)")
    print("\nUsers table structure:")
    print(cursor.fetchall())
    
    # Get database size
    cursor.execute("PRAGMA page_size")
    page_size = cursor.fetchone()[0]
    cursor.execute("PRAGMA page_count")
    page_count = cursor.fetchone()[0]
    print(f"\nDatabase size: {(page_size * page_count) / 1024:.2f} KB")

# Main execution
if __name__ == "__main__":
    # Create connection
    conn = create_connection()
    
    try:
        # Execute examples
        create_tables(conn)
        insert_data(conn)
        select_examples(conn)
        join_examples(conn)
        update_examples(conn)
        delete_examples(conn)
        transaction_example(conn)
        advanced_queries(conn)
        maintenance_operations(conn)
        
    finally:
        # Close connection
        conn.close()
        print("\nDatabase connection closed")
        
        # Clean up database file
        if os.path.exists("example.db"):
            os.remove("example.db")
            print("Database file removed")
