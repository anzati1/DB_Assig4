# Task List App

A simple task management application built with Kivy and MySQL.

## Installation

clone the repository
install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
create a `.env` file with your database credentials:
   ```
   DB_HOST=your_host
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database
   ```

```bash
python main.py
```

## Testing
How to run the tests
   ```bash
   pytest tests/ -v
   ```

To run tests with coverage report:
```bash
pytest tests/ --cov=. --cov-report=term-missing
```

### Test Structure

- `tests/test_logic_layer.py`: TaskManager class
- `tests/test_db_layer.py`: Database class

The tests cover:
- Task creation
- Task updates
- Task deletion
- Error handling
- Database operations

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Persistent storage using MySQL