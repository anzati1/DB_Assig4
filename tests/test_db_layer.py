import pytest
import os
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.db_layer import Database
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test database configuration
TEST_DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": "tasklist_assignment4"  # Use the correct database name
}

@pytest.fixture
def db():
    """Fixture to create a Database instance for testing."""
    database = Database(**TEST_DB_CONFIG)
    database.create_table()
    yield database
    database.close()

def test_database_connection(db):
    """Test that database connection is established."""
    assert db is not None
    assert db.connection is not None

def test_create_table(db):
    """Test that the tasks table is created correctly."""
    cursor = db.connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'tasks'")
    result = cursor.fetchone()
    assert result is not None

def test_add_and_fetch_task(db):
    """Test adding and fetching a task."""
    # Add a test task
    task_id = db.add_task("Test task")
    assert task_id is not None
    
    # Fetch all tasks
    tasks = db.fetch_all_tasks()
    assert len(tasks) > 0
    assert any(task["task_text"] == "Test task" for task in tasks)

def test_update_task(db):
    """Test updating a task."""
    # Add a task first
    task_id = db.add_task("Original task")
    
    # Update the task
    db.update_task("Updated task", task_id)
    
    # Verify the update
    tasks = db.fetch_all_tasks()
    assert any(task["task_text"] == "Updated task" for task in tasks)

def test_delete_task(db):
    """Test deleting a task."""
    # Add a task first
    task_id = db.add_task("Task to delete")
    
    # Delete the task
    db.delete_task(task_id)
    
    # Verify deletion
    tasks = db.fetch_all_tasks()
    assert not any(task["id"] == task_id for task in tasks)

def test_error_handling(db):
    """Test error handling for invalid operations."""
    # Test updating non-existent task
    # MySQL doesn't raise an error for non-existent updates
    db.update_task("Test", -1)
    
    # Test deleting non-existent task
    # MySQL doesn't raise an error for non-existent deletes
    db.delete_task(-1)
    
    # Test invalid SQL (should raise an error)
    with pytest.raises(Exception):
        db.cursor.execute("INVALID SQL") 