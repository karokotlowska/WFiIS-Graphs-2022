import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))

from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
from DirectedGraph import DirectedGraph
import fileReader as fr
from Kosaraju import kosaraju
from BellmanFord import randWeights, bellmanFord
from johnson import johnson

'''Zad1 - Direcred Graph and Random Directed Graph'''
print('\n\n-----zad1-----losowy graf skierowany \n\n')
directedGraphRandom=DirectedGraph.randomDirectedGraph(5,0.5)
directedGraphRandom.printAdjecencyMatrixGraph()
print('\n\n-----zad1-----przykladowy graf skierowany \n\n')
matrix=fr.readMatrix('directedGraphExample1.txt')
directedGraph=DirectedGraph(0,None,None,0,AdjacencyMatrix(matrix).convertToAL())
directedGraph.printAdjecencyMatrixGraph()

print('\n\n-----zad2-----wyszukiwanie silnie spojnych skladowych dla losowego digrafu')
scc = kosaraju(directedGraphRandom)
print([[i + 1 for i in j]for j in scc])


print('\n\n-----zad3-----')
print('Silnie spojny digraf: ')

directedGraph.printAdjecencyMatrixGraph()
scc = kosaraju(directedGraph)

print('\nsprawdzenie silnie spojnej skladowej: ')
print([[i + 1 for i in j]for j in scc])

directedGraph.generateDirectedEdgesFromList(directedGraph.getWeightsFromFile('exampleWeights.txt'))

print('\nMacierz wag: ')
for row in directedGraph.generateWeightMatrix():
    print(row)

print()
indicator, d, p = bellmanFord(directedGraph.generateWeightMatrix(), 1 , directedGraph.getAdjecencyMatrixRepresentation())
print('W grafie jest cykl o ujemnej wadze: ', not indicator)
print(d)
print(p)

print('\n\n\n-------Zad 4 ------- Algorytm Johnsona')

distanceMatrix=johnson(directedGraph)