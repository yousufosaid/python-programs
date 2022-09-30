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
from functions import matrix_stats
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
a = [[1,100000]]
small, large, total, average = matrix_stats(a)

print(small, large, total, average)