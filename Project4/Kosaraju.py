from itertools import count


def kosaraju(adjMatrix):

    n = len(adjMatrix)
    stack = []
    scc = []
    cn = 0
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            dfsStack(i, visited, stack, adjMatrix)

    tAdjMatrix = transponse(adjMatrix)
    
    visited = [False for i in range(n)]

    while len(stack) > 0:

        vertex = stack.pop()

        if visited[vertex]:
            continue
        
        cn += 1

        scc.append([])
        dfsSprint(vertex, visited, tAdjMatrix, scc[cn - 1])

    return scc

        

def dfsSprint(vertex, visited, adjMatrix, scc):
    visited[vertex] = True
    scc.append(vertex)

    for i in range(len(adjMatrix[vertex])):
        if adjMatrix[vertex][i] == 1 and visited[i] == False: 
            dfsSprint(i, visited, adjMatrix, scc)

def dfsStack(vertex, visited, stack, adjMatrix):
    visited[vertex] = True
    for i in range(len(adjMatrix[vertex])):
        if adjMatrix[vertex][i] == 1 and visited[i] == False: 
            dfsStack(i, visited, stack , adjMatrix)

    stack.append(vertex)

def transponse(adjMatrix):
    matrix = []

    for i in range(len(adjMatrix)):
        matrix.append([])
        for j in range(len(adjMatrix[i])):
            matrix[i].append(adjMatrix[j][i])

    return matrix

