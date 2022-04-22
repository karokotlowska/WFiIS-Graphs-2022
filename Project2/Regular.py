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

          
def randomK_RegularGraph(n = 7, k = 2):
    if not checkInput(n, k):
        sys.exit(-1)
    
    adjList = [[] for i in range(n)]

    if k == 0:
        return adjList
    degree = [k for i in range(n)]
    iterator = 0

    while True:

        v1, v2 = randint(1, n), randint(1, n)

        while v1 == v2:
            v2 = randint(1, n)

        if sum(degree) == 4 and max(degree) == 2:
            T = sorted(degree, reverse = True)

            if T[1] == 1:
                v1 = degree.index(max(degree)) + 1 
                v2 = degree.index(1) + 1 
                fillGraph(v1, v2, adjList, degree)

  
                v1 = degree.index(1) + 1 
                v2 = degree.index(1, v1) + 1 
                fillGraph(v1, v2, adjList, degree)

                
        if v1 not in adjList[v2 - 1] and v2 not in adjList[v1 - 1] and degree[v1 - 1] > 0 and degree[v2 - 1] > 0:
            fillGraph(v1, v2, adjList, degree)

            
        if sum(degree) == 0:
            break

        iterator = iterator + 1
        if iterator >= 500:

            adjList.clear()
            tempAdjList = [ [] for i in range(n)]
            adjList = tempAdjList
            tempDegree = [k for i in range(n)]
            degree = tempDegree
            iterator = 0

    
    return adjList


def fillGraph(v1, v2, adjList, degree):
    adjList[v1 - 1].append(v2)
    adjList[v2 - 1].append(v1)
    degree[v1 - 1] = degree[v1 - 1] - 1
    degree[v2 - 1] = degree[v2 - 1] - 1       
