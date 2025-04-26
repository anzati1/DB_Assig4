import pytest
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

def create_database():
    """Create the test database if it doesn't exist."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    try:
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS tasklist_assignment4")
        conn.commit()
        
        # Switch to the database
        cursor.execute("USE tasklist_assignment4")
        
        # Create tasks table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_text VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def drop_database():
    """Drop the test database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DROP DATABASE IF EXISTS tasklist_assignment4")
        conn.commit()
    finally:
        cursor.close()
        conn.close()

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Setup and teardown the test database."""
    create_database()
    yield
    # Uncomment the line below if you want to drop the database after tests
    # drop_database() 