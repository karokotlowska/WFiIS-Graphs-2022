import string
import sys
import os
from random import random, choice, randint
from copy import copy
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Project1')))

import AdjacencyList as AM

dictionary1 = dict( (string.ascii_uppercase[key], key) for key in range(len(string.ascii_uppercase)))
dictionary2 = dict( (key, string.ascii_uppercase[key]) for key in range(len(string.ascii_uppercase)))


def readAdjList(fileName):
    lista = []
    iterator = 0
    with open(fileName, 'r') as file:
        for line in file:
            lista.append([])
            
            for i in line.split():
                lista[iterator].append(dictionary1.get(i) + 1)
            iterator += 1
    
    return lista


def pageRankRandomWalk(adjList, d = 0.15, N = 1000000, v = 0):
    visits = [0 for i in range(len(adjList))]
    for i in range(N):
        if random() < (1 - d):
            v = choice(adjList[v - 1])
            visits[v - 1] += 1
        else:
            v = randint(0, len(adjList) - 1)
            visits[v - 1] += 1

    return {vert: visitSum / N for vert, visitSum in enumerate(visits)}


def pageRankIterative(adjList, d: float = 0.15):
    adjMatrix = AM.AdjacencyList(adjList).convertToAM().adjMatrix

    n = len(adjMatrix)
    
    array = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            array[i][j] = (1 - d) * (adjMatrix[i][j] / sum(adjMatrix[i])) + (d / n)

    p = np.full(n, 1/n)
    iterator = 0
    while True:
        iterator += 1
        prev = p.copy()
        p = p.dot(array)

        if np.linalg.norm(p - prev) < 1e-5:
            break

    return {k: round(v, 6) for k, v in enumerate(p)}

if __name__ == '__main__':
    
    adjList = readAdjList('test.txt')
    result = pageRankRandomWalk(adjList)

    print('\na. błądzenie przypadkowe')
    for key, value in {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}.items():
        print(dictionary2[key], '===> PageRank = ', round(value, 6))

    result = pageRankIterative(adjList)

    print('\nb. metoda potęgowa')
    for key, value in {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}.items():
        print(dictionary2[key], '===> PageRank = ', value)


    
