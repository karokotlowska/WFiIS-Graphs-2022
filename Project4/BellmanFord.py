from copy import deepcopy
from random import randint

def randWeights(adjMatrix):
    n = len(adjMatrix)
    weightMatrix = deepcopy(adjMatrix)
    for i in range(n):
        for j in range(n):
            if adjMatrix[i][j]:
                weightMatrix[i][j] = randint(-5, 10)
    return weightMatrix

def bellmanFord(wMatrix, vertex, adjMatrix):
    n = len(wMatrix)
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]

    d[vertex - 1] = 0

    for i in range(n):
        for j in range(n):
            if adjMatrix[i][j]==1:
                relax(i, j, wMatrix, d, p)
        
    for i in range(n):
        for j in range(n):
            if adjMatrix[i][j] and d[j] > d[i] + wMatrix[i][j]:
                return False, d, p
        
    return True, d, p

def relax(u, v, wMatrix, d, p):
    if d[v] > d[u] + wMatrix[u][v]:
        d[v] = d[u] + wMatrix[u][v]
        p[v] = u
