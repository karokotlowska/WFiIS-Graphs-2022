import sys
import os.path
import random
from math import inf
from collections import defaultdict

def primsMst(inputMatrix):
    n = len(inputMatrix)
    for row in inputMatrix:
        assert len(row) == n
    mstMatrix = [[0 for i in range(n)] for j in range(n)]
    edgesWeights = defaultdict(list)
    W = list(range(n))
    start = random.choice(W)
    T = [start]
    W.remove(start)

    print('\nPoczatkowy wierzcholek: {}\n'.format(start+1))

    mstLength = 0

    while W:
        minimumWeightEdge = ()
        minumumPathWeight = inf  
        for currentVertex in T:
            currentVertexRow = inputMatrix[currentVertex] 
            currentMinPath = inf
            currentMinimumFreeVertex = currentVertex
            for vertex in range(n):
                vertexPathWeight = currentVertexRow[vertex]
                if vertexPathWeight == 0:
                    continue
                if vertex in W and vertexPathWeight < currentMinPath:
                    currentMinimumFreeVertex = vertex
                    currentMinPath = vertexPathWeight
            if currentMinimumFreeVertex != currentVertex:
                if currentMinPath < minumumPathWeight:
                    minimumWeightEdge = (currentVertex, currentMinimumFreeVertex)
                    minumumPathWeight = currentMinPath
        print('Prowadzimy krawedz z {} do {} o wadze {}\n'.format(minimumWeightEdge[0] + 1, minimumWeightEdge[1] + 1, minumumPathWeight))
        edgesWeights[minimumWeightEdge[0]].append((minimumWeightEdge[1], minumumPathWeight))
        mstLength += minumumPathWeight
        W.remove(minimumWeightEdge[1])
        T.append(minimumWeightEdge[1])

    print('Dlugosc : {}'.format(mstLength))

    for i in range(len(mstMatrix)):
        if len(edgesWeights[i]) == 0:
            continue
        for j in range (len(edgesWeights[i])):
            column = edgesWeights[i][j][0]
            value = edgesWeights[i][j][1]
            mstMatrix[i][column] = mstMatrix[column][i] = value
    return mstMatrix