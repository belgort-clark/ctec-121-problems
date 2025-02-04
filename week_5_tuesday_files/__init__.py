import check50
import os

@check50.check()
def exists():
    """At least one Python file (.py) exists in the directory"""
    
    # List all Python files in the current directory
    py_files = [f for f in os.listdir() if f.endswith(".py")]
    
    # Ensure at least one Python file exists
    if not py_files:
        raise check50.Failure("No Python files found in the directory.")
    
    # Check for each Python file dynamically
    for py_file in py_files:
        check50.exists(py_file)