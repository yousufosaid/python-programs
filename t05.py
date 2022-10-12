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
from functions import is_palindrome_stack
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
string = "A man, a plan, a canal, Panama!"
palindrome = is_palindrome_stack(string)
print(f"String: {string}")
print(palindrome)