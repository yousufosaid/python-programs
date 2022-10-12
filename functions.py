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
# Constants

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    s1=[]
    s2=[]
    
    
    for element1 in source1:
        s1.append(element1)
        
        
    for element2 in source2:
        s2.append(element2)
        
        
    s1 = s1[::-1]   
    s2 = s2[::-1]
    

    for x in range(max(len(s1), len(s2))):
        if x < len(s1):
            target.push(s1[x])
        if x < len(s2):
            target.push(s2[x])
            
    
    source1.pop()
    source2.pop()     
        
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    s=[]
    
    for element in source:
        s.append(element)
        
    for i in range(len(s)):
        source.pop()
        
    s=s[::-1]
        
    for i in range(len(s)-1,-1,-1):
        source.push(s[i])
        
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    compare = ""
    s=Stack()
    palindrome = False
    ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"
             ,"p","q","r","s","t","u","v","w","x","y","z"]
    string = string.lower()
    string = ''.join([i for i in string if i in ALPHA])
    leng = len(string)
    
    if leng%2 == 0:
        half=string[:int((leng/2))]
        for i in half:
            s.push(i)
        
        for element in s:
            compare=compare+element
            
        if string[int(leng/2):] == compare:
            palindrome = True
        
    else:
        half=string[:int((leng-1)/2)]
        for i in half:
            s.push(i)
        
        for element in s:
            compare=compare+element
            
        if string[int((leng+1)/2):] == compare:
            palindrome = True
        
        
    
    
    return palindrome
    
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack= Stack()
    values_out=[]
    count = 0
    
    for element in opstring:
        if element == "S":
            stack.push(values_in[count])
            count = count + 1
            
        elif element == "X":
            value = stack.pop()
            values_out.append(value)
            
    return values_out,stack