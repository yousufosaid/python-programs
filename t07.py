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
from functions import matrix_transpose
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
a1 = [[0,1],[2,3],[4,5],[6,7],[8,9]]
a2 = [[0]]
a3 = [[0,1]]
b1 = matrix_transpose(a1)
b2 = matrix_transpose(a2)
b3 = matrix_transpose(a3)
print(b1)
print(b2)
print(b3)