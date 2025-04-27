@echo off
cd docs
python -m sphinx.cmd.build -b html . _build/html
cd ..
echo Documentation built successfully!
echo You can find the built documentation in docs/_build/html/ 