import os
import sys
import subprocess

def build_docs():
    # Change to the docs directory
    os.chdir('docs')
    
    # Build the documentation
    try:
        subprocess.run([sys.executable, '-m', 'sphinx.cmd.build', '-b', 'html', '.', '_build/html'], check=True)
        print("Documentation built successfully!")
        print("You can find the built documentation in docs/_build/html/")
    except subprocess.CalledProcessError as e:
        print(f"Error building documentation: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_docs() 