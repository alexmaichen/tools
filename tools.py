def selection(L: list, order = 'a'):
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

def greedy(somme: int, pieces = [500,200,100,50,20,10,5,2,1]):
    total = []
    for piece in pieces:
        if somme//piece:
            for i in range(somme//piece):
                total.append(piece)
                somme -= piece
    return (total)

def double(L: list):
    isDouble = False
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            isDouble = True
    return (isDouble)

def isStrInt(keyword: str): #takes the first character of a string
    check = ord(keyword[0]) >= ord('0') and ord(keyword[0]) <= ord('9')
    return check #returns true if keyword[0] is an int as a str, else false

