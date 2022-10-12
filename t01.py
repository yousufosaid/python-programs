"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_combine
# Constants
source1 = Stack()
source2 = Stack()

source1.push(5)
source1.push(8)
source1.push(12)
source1.push(8)

source2.push(3)
source2.push(6)
source2.push(1)
source2.push(7)
source2.push(9)
source2.push(14)

print("Source 1:")
for element in source1:
    print(element)
print()
print("Source 2:")
for element in source2:
    print(element)
print()

target = stack_combine(source1, source2)

print("Target: ")
for element in target:
    print(element)


