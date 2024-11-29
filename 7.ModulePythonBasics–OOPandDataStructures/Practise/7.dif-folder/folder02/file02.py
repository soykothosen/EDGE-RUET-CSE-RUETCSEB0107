# file02.py content

from ..folder01.file01 import some_function  # Absolute import

def call_some_function():
    return some_function()

print(some_function())