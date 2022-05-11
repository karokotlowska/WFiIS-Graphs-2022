import sys
from random import randint
from copy import deepcopy

def checkInput(n , k):
    if n < 0 or k < 0:
        print("Paramtery musza byc dodatnie")
        return False
    if (n * k) % 2 != 0:
        print("Graf o podanych parametrach nie moze byc regularnym")
        return False
    return True

def isRegular(lista, n, k):
    for i in lista:
        if len(i) != k:
            return False

    numberOfPassed = 0
    a = 1
    
    while True:
        for i in range(len(lista[a - 1])):
            if lista[a - 1][i] != None:
                b = lista[a - 1][i]
                lista[a - 1][i] = None
                index = lista[b - 1].index(a)
                lista[b - 1][index] = None
                numberOfPassed += 1
                a = b
                break
        else:
            break

    if numberOfPassed == n:
        return True
    else: 
        return False

        
      
def randomK_RegularGraph(n = 7, k = 2):
    if not checkInput(n, k):
        sys.exit(-1)
    
    adjList = [[] for i in range(n)]
    iterator = 0
    numberOfPairs = 0

    while True:
        if numberOfPairs == n and isRegular(deepcopy(adjList), n , k) :
            return adjList

        if iterator > 1000:
            iterator = 0
            numberOfPairs = 0
            adjList.clear()
            adjList = [[] for i in range(n)]

        iterator += 1

        v1, v2 = randint(1, n), randint(1, n)

        while v1 == v2:
            v2 = randint(1, n)
        
        if len(adjList[v1 - 1]) == k or len(adjList[v2 - 1]) == k:
            continue

        if v2 in adjList[v1 - 1]:
            continue

        adjList[v1 - 1].append(v2)
        adjList[v2 - 1].append(v1)

        numberOfPairs += 1


      
    


