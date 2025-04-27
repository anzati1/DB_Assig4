Development Guide
================

This guide provides information for developers who want to contribute to or modify the Task List App.

Project Structure
----------------

::

   task-list-app/
   ├── app/
   │   ├── main.py
   │   ├── logic_layer.py
   │   ├── db_layer.py
   │   ├── ui.kv
   │   └── popup.kv
   ├── tests/
   │   └── test_*.py
   ├── docs/
   │   └── *.rst
   └── requirements.txt

Running Tests
------------

To run the test suite:

.. code-block:: bash

   pytest --maxfail=1 --disable-warnings -q

To generate a coverage report:

.. code-block:: bash

   pytest --cov=app tests/

Building Documentation
--------------------

To build the documentation:

.. code-block:: bash

   cd docs
   make html

The built documentation will be available in ``docs/_build/html/``.

Coding Standards
---------------

* Follow PEP 8 style guide
* Write docstrings for all public functions and classes
* Keep functions small and focused
* Use type hints where appropriate

Adding New Features
-----------------

1. Create a new branch for your feature
2. Write tests for the new functionality
3. Implement the feature
4. Update documentation
5. Submit a pull request

Database Schema
--------------

The application uses a MySQL database with the following schema:

.. code-block:: sql

          CREATE TABLE IF NOT EXISTS tasks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    task_text VARCHAR(255) NOT NULL
                )
   ; 