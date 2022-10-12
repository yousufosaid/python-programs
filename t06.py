"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-25"
-------------------------------------------------------
"""
# Imports
from functions import reroute
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
opstring = "SSXXSSXX"
values_in = [1,2,3,4]
values_out,stack = reroute(opstring, values_in)

print(opstring)
print(values_in)
print(values_out)
