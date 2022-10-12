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
from Food_utilities import read_foods,calories_by_origin
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

origin = int(input("Enter origin: "))

a = calories_by_origin(foods, origin)
print(f"Average: {a}")