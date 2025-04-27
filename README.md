# Task List App

A simple task management application built with Kivy and MySQL.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anzati1/DB_Assig4
   cd task-list-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your database credentials:
   ```
   DB_HOST=your_host
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database
   ```

5. Set up the database:
   ```bash
   mysql -u root -p < db_creation.sql
   ```

## Running the Application

```bash
python app/main.py
```

## Testing

### Running Tests

To run all tests:
```bash
pytest tests/ -v
```

To run tests with coverage report:
```bash
pytest tests/ --cov=app --cov-report=term-missing
```

To run tests with specific options:
```bash
pytest --maxfail=1 --disable-warnings -q
```

### Test Structure

- `tests/test_logic_layer.py`: Tests for the TaskManager class
- `tests/test_db_layer.py`: Tests for the Database class
- `tests/test_ui.py`: Tests for the UI components
- `tests/conftest.py`: Test fixtures and configuration

The tests cover:
- Task creation, updates, and deletion
- Database operations and error handling
- UI component functionality
- Integration between layers

## Documentation

### Building Documentation

1. Install Sphinx and dependencies:
   ```bash
   pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
   ```

2. Build the documentation:
   ```bash
   cd docs
   make html
   ```

3. View the documentation:
   Open `docs/_build/html/index.html` in your web browser

### Documentation Structure

- `docs/introduction.rst`: Overview of the application
- `docs/installation.rst`: Installation instructions
- `docs/usage.rst`: User guide
- `docs/api.rst`: API reference
- `docs/development.rst`: Development guide

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Persistent storage using MySQL
- Modern, responsive user interface
- Comprehensive test coverage
- Professional documentation

## Project Structure

```
task-list-app/
├── app/
│   ├── main.py
│   ├── logic_layer.py
│   ├── db_layer.py
│   ├── ui.kv
│   └── popup.kv
├── tests/
│   ├── test_logic_layer.py
│   ├── test_db_layer.py
│   ├── test_ui.py
│   └── conftest.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── *.rst
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure they pass
5. Update documentation if necessary
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

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