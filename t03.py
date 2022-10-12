"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-24"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
source = Stack()


source.push(20)
source.push(30)

print("Original: ")
for i in source:
    print(i)
print()

stack_reverse(source)

print("Reversed: ")
for i in source:
    print(i)