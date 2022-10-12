"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin,read_foods
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
file_variable = open("foods.txt","r")
foods = read_foods(file_variable)
file_variable.close()

o = int(input("Enter origin: "))

origins = by_origin(foods, o)

for origin in origins:
    print (origin)
    print()