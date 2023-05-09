"""
Python quality of life functions (tools.py)
Author: Alexmaichen
Encoding: ASCII
"""



#somewhat inefficient O(n) but easy to remember and use, can even reverse order at no extra cost without the need for the .reverse() method!
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



def doubles(L: list) -> bool: #checks if an entry from a sequence appears at least twice in a row
    
    if type(L) != list and type(L) != tuple and type(L) != str:
        raise TypeError
    
    isDouble = False
    if not len(L) < 2:
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
    elif type(string) == list or type(string) == tuple:
        s = []
    d = []
    while len(s) != len(string): #make sure it has copied every entry
        r = randint(0, len(string) - 1)
        if r not in d: #memory of which entries of the sequence have already been copied
            d.append(r)
            if type(string) == str:
                s += string[r]
            elif type(string) == list or type(string) == tuple:
                s.append(string[r])
    return s


#remove all instances of a given char from a given string
def charRemove(string: str, charToRemove: str) -> str:
    
    if type(string) != str or type(charToRemove) != str:
        raise TypeError
    if len(charToRemove) != 1:
        raise ValueError("Invalid length for char input.")
    
    w = ""
    for c in string:
        if c != charToRemove:
            w += c
    return w


#example usecase: x = upperBound(x, 10)
def upperBound(value: float, limit: float) -> float:
    if(value < limit):
        return value
    return limit


#example usecase: x = lowerBound(0, x)
def lowerBound(limit: float, value: float) -> float:
    if(value > limit):
        return value
    return limit


#like the two functions before this, but in one. makes for more readable code
def bounds(lowerLim: float, value: float, higherLim: float) -> float:

    if lowerLim > upperLim:
        raise ValueError("Lower-bound is greater than upper-bound.")
    
    if (lowerLim > value):
        return lowerLim
    if (higherLim < value):
        return higherLim
    return value


#the math library has this but better. I know.
def intAndFracParts(n: float) -> tuple:
    return int(n//1), n%1


#check if nToCompare is within a percent deviation dev of nToCompareWith (called "n" here) ... similar to bounds()
#example usecase: flag = closeEnough(float(input("Enter number to compare against bounds for: ")), 50, 5)
def closeEnough(nToCompare: float, n: float, dev: float) -> bool:
    
    if type(nToCompare) != int and type(nToCompare) != float:
        raise TypeError
    if type(n) != int and type(n) != float:
        raise TypeError
    if type(dev) != int and type(dev) != float:
        raise TypeError
    
    if nToCompare >= n * (1 - abs(dev)/100) and nToCompare <= n * (1 + abs(dev)/100): 
        return True
    else:
        return False
