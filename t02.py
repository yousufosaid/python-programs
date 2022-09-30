"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-12"
-------------------------------------------------------
"""
# Imports
from functions import dsmvwl
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
s= input("Enter sentence: ")

out=dsmvwl(s)
print(f"""Sentence: {s}
Disemvowelled: {out}""")