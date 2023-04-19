"""
Python quality of life functions (tools.py)
Author: Alexmaichen
Encoding: ASCII
"""

#seqSearch() is untested, should work though. in fact it likely even works for searching a sequence within a list!
def seqSearch(text: str, string: str) -> list: #returns list of all positions from which the sequence can be read
    #could have done some .split(" ") shenanigans here but thought I'd rather consider the more general case instead as opposed to strictly a search by word
    
    if (type(text)!= str and type(text) != list) or type(text) != tuple:
        raise TypeError
    
    positions = []
    
    if len(string) > len(text):
        print("sequence is longer than text, no instances found")
        return positions
    
    if not len(string) * len(text):
        print("sequence and / or text have length 0")
        return positions
    
    for i in range(len(text) - len(str) + 1):
        flag = True #assume the condition is true for each char in the text
        
        for j in range(len(string)):
            flag *= text[i + j] == string[j] #run the test for each char in the searched sequence
        
        if flag: #only passes the test if all chars passed the test in the sequence comparison for() loop
            positions.append(i)
        
    return positions

#somewhat inefficient O(n) but easy to remember and use, can even reverse order without the need for the .reverse() method!
def selection(L: list, order = 'a') -> list:
    
    if type(order) != str or (type(L) != list and type(L) != str):
        raise TypeError
    
    for i in range(len(L)):
        for j in range(i, len(L)):
            
            if order[0] == 'a':     #change comparison symbol to reverse order (ascending)
                if L[i] > L[j]:     #swap accordingly
                    L[i], L[j] = L[j], L[i]
                    
            if order[0] == 'd':     #change comparison symbol to reverse order (descending)
                if L[i] < L[j]:     #swap accordingly
                    L[i], L[j] = L[j], L[i]
    return L

#greedy algorithm
def greedy(somme: float, pieces: list) -> float: #Values in list must be of types int or float. Must not include 0.
    if (type(somme) != float and type(somme) != int) or (type(pieces) != list and type(pieces) != tuple):
        raise TypeError
    pieces = selection(pieces, 'd')
    total  = []
    for piece in pieces:
        if somme//piece:
            for i in range(somme//piece):
                total.append(piece)
                somme -= piece
    return total


def doubles(L: list) -> bool: #checks if an entry from a sequence appears at least twice in a row
    
    if type(L) != list and type(L) != tuple and type(L) != str:
        raise TypeError
    
    isDouble = False
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            isDouble = True
    return isDouble

#didn't want to copypaste ord(keyword[0]) >= ord('0') and ord(keyword[0]) <= ord('9') everywhere in another piece of code so I wrote this instead
def isStrIntPart(keyword: str) -> bool: #takes the first character of a string
    
    if type(keyword) != str:
        raise TypeError
        
    check = ord(keyword[0]) >= ord('0') and ord(keyword[0]) <= ord('9')
    return check #returns true if keyword[0] is an int as a str, else false

#more complete / accurate version of isStrIntPart(), because isStrIntPart() makes a dangerous assumption
def isStrInt(keyword: str) -> bool: #less optimized for some scenarios, but may sometimes be required so I wrote it anyways
    
    if type(keyword) != str:
        raise TypeError
    
    check = True
    for i in len(keyword):
        check *= ord(keyword[i]) >= ord('0') and ord(keyword[i]) <= ord('9')
    return check

#ever wanted to make a videogame for which you store the chambers in a list, and wish to randomize their order of appearance? well now you can.
def shuffle(string: str) -> str: #lists are supported too! :]
    
    if type(string) != str and type(string) != list:
        raise TypeError
    
    from random import randint
    if type(string) == str:
        s = "" #shuffled string
    elif type(string) == list:
        s = []
    d = []
    while len(s) != len(string): #make sure it has copied every char
        r = randint(0, len(string)-1)
        if r not in d: #memory of which chars have already been copied
            d.append(r)
            if type(string) == str:
                s += string[r]
            elif type(string) == list:
                s.append(string[r])
    return s


def charRemoveAll(string: str, charToRemove: str) -> str: #remove all instances of a given char from a given string
    
    if type(string) != str or type(charToRemove) != str:
        raise TypeError
    if len(charToRemove) != 1:
        raise ValueError("Invalid length for char input.")
    
    w = ""
    for c in string:
        if c != charToRemove:
            w += c
    return w

#needed an alias for the min() function because I always forget to use it otherwise
def minVal(value: float, limit: float) -> float:
    return max((value, limit))

#needed an alias for the max() function because I always forget to use it otherwise
def maxVal(value: float, limit: float) -> float:
    return min((value, limit))

#the math library has this but better. I know.
def intAndFracParts(n: float) -> tuple:
    return n//1, n - n//1
