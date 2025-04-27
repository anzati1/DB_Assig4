import pytest
import os
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.logic_layer import TaskManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test database configuration
TEST_DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

@pytest.fixture
def task_manager():
    """Fixture to create a TaskManager instance for testing."""
    manager = TaskManager(TEST_DB_CONFIG)
    yield manager
    manager.close()

def test_task_manager_initialization(task_manager):
    """Test that TaskManager initializes correctly."""
    assert task_manager is not None

def test_add_and_load_tasks(task_manager):
    """Test adding and loading tasks."""
    # Add a test task
    task_id = task_manager.add_task("Test task 1")
    assert task_id is not None
    
    # Load tasks and verify
    tasks = task_manager.load_tasks()
    assert len(tasks) > 0
    assert any(task["task_text"] == "Test task 1" for task in tasks)

def test_update_task(task_manager):
    """Test updating a task."""
    # Add a task first
    task_id = task_manager.add_task("Original task")
    
    # Update the task
    task_manager.update_task("Updated task", task_id)
    
    # Verify the update
    tasks = task_manager.load_tasks()
    assert any(task["task_text"] == "Updated task" for task in tasks)

def test_delete_task(task_manager):
    """Test deleting a task."""
    # Add a task first
    task_id = task_manager.add_task("Task to delete")
    
    # Delete the task
    task_manager.delete_task(task_id)
    
    # Verify deletion
    tasks = task_manager.load_tasks()
    assert not any(task["id"] == task_id for task in tasks)

def test_error_handling(task_manager):
    """Test error handling for invalid operations."""
    # Test updating non-existent task
    # MySQL doesn't raise an error for non-existent updates
    task_manager.update_task("Test", -1)
    
    # Test deleting non-existent task
    # MySQL doesn't raise an error for non-existent deletes
    task_manager.delete_task(-1)
    
    # Test invalid database configuration (should raise an error)
    with pytest.raises(RuntimeError):
        invalid_manager = TaskManager({
            "host": "invalid_host",
            "user": "invalid_user",
            "password": "invalid_password",
            "database": "invalid_database"
        }) 