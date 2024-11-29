import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Import file01 from folder01
from folder01.file01 import some_function  # Absolute import

def call_some_function():
    return some_function()

if __name__ == "__main__":
    # Call the function when running file02 directly
    print(call_some_function())
