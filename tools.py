"""
Python quality of life functions (tools.py)
Author: Alexmaichen
Encoding: ASCII
"""

def selection(L: list, order = 'a'):
    
    if type(order) != str or (type(L) != list and type(L) != list):
        raise TypeError
    
    temp = 0
    for i in range(len(L)):
        for j in range(i, len(L)):
            
            if order[0] == 'a':     #change comparison symbol to reverse order (ascending)
                if L[i] > L[j]:     #swap accordingly
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
                    
            if order[0] == 'd':     #change comparison symbol to reverse order (descending)
                if L[i] < L[j]:     #swap accordingly
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
    return L


def greedy(somme: float, pieces: list): #Values in list must be of types int or float. Must not include 0.
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


def doubles(L: list): #checks if an entry from a sequence appears at least twice in a row
    
    if type(L) != list and type(L) != tuple and type(L) != str:
        raise TypeError
    
    isDouble = False
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            isDouble = True
    return isDouble


def isStrInt(keyword: str): #takes the first character of a string
    
    if type(keyword) != str:
        raise TypeError
        
    check = ord(keyword[0]) >= ord('0') and ord(keyword[0]) <= ord('9')
    return check #returns true if keyword[0] is an int as a str, else false


def isStrIntFull(keyword: str): #less optimized for some scenarios, but may sometimes be required so I wrote it anyways
    
    if type(keyword) != str:
        raise TypeError
    
    check = True
    for i in len(keyword):
        check *= ord(keyword[i]) >= ord('0') and ord(keyword[i]) <= ord('9')
    return check


def shuffle(string: str):
    
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


def charRemove(string: str, char: str): #remove all instances of a given char from a given string
    
    if type(string) != str or type(char) != str:
        raise TypeError
    if len(char) != 1:
        raise ValueError("Invalid length for char input.")
    
    w = ""
    for c in string:
        if c != char:
            w += c
    return w
