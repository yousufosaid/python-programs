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
from Food_utilities import read_foods,food_search
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

is_veg = eval(input("Is it a veg? (True/False): "))

max_cals = int(input("Enter max calories: "))

result = food_search(foods, origin, max_cals, is_veg)

for r in result:
    print(r)
    print()