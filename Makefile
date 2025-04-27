.PHONY: test test-cov docs clean

# Python virtual environment
venv:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=app --cov-report=term-missing

test-quick:
	pytest --maxfail=1 --disable-warnings -q

# Documentation
docs:
	cd docs && make html

# Clean up
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Development
install: venv
	. venv/bin/activate && pip install -e .

# Database
db-setup:
	mysql -u root -p < db_creation.sql

# Run application
run:
	python app/main.py 