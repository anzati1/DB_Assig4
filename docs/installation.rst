Installation
============

Prerequisites
-------------

* Python 3.8 
* MySQL Server
* pip 

Step-by-Step Installation
------------------------

1. Clone the repository:
   .. code-block:: bash

      git clone https://github.com/anzati1/DB_Assig4

2. Create a virtual environment:
   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  

3. Install dependencies:
   .. code-block:: bash

      pip install -r requirements.txt

4. Set up the database:
   .. code-block:: bash

      mysql -u root -p < db_creation.sql

5. Configure environment variables:
   Create a `.env` file in the project root with the following content:
   .. code-block:: text

      DB_HOST=localhost
      DB_USER=your_username
      DB_PASSWORD=your_password
      DB_NAME=task_list_db

Running the Application
----------------------

To start the application:
.. code-block:: bash

   python app/main.py 