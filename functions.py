"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-06"
-------------------------------------------------------
"""
# Imports


# Constants

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    cleaned = []
    for i in values:
        if i not in cleaned:
            cleaned.append(i)
     
    print(f"Values: {values}")     
    print(f"Cleaned: {cleaned}")
    
    return None
    


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the s[i]acters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    vowels = ["a","e","i","o","u","A","O","U","E","I"]
    for i in range(len(s)-1):
        if s[i] not in vowels:
            out = out + s[i]
            
    return out

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u=0
    l=0
    d=0
    w=0
    r=0
    read_file=fv.read()
    
    for read in read_file:
        read = fv.readline()
        if read.isupper() == True:
            u = u + 1
        elif read.isupper() == False:
            l = l + 1
        elif read.isdigit() == True:
            d = d + 1
        elif read.isspace() == True:
            w = w + 1
        else:
            r= r+1
            
    return u,l,d,w,r

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    
    if year%4 == 0 and year%100 == 0:
        leap_year =True
        
    return leap_year



def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    s= s.lower()
    palindrome = True
    
    for i in range (0,len(s)-1,1):
        if s[i-1] != s[-i]:
            
            palindrome = False
            
    return palindrome

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    for i in range (len(a)-1):
        diff = abs(a[i]-a[i+1])
        if diff > md:
            md = diff
                
    return md

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    
    return b

def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large= a[0][0]
    total=0
    count = 0
    
    
    for j in range(len(a)):
        for i in range(len(a[0])):
            if a[j][i] < small:
                small = a[j][i]
            elif a[j][i] > large:
                large = a[j][i]
            total = total + a[j][i]
            count +=1
            
    average = total/count
    
    return small,large,total,average

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    x= word.upper()
    vowel = ('A','E','I','O','U')
    count = 0
    
    
    
    if x[0] in vowel:
        pl = word+"way"
    else:
        for i in range(len(word)-1):
            if x[i] in vowel:
                break
            count+=1
            
        
        temp = word[count:]+word[0:count]+"ay"
       
        if word[0].isupper():
            pl = temp[0].upper()+temp[1:].lower()
            
        else:
            pl=temp
                  
    return pl