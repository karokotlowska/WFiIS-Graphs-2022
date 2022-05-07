import random
import AdjacencyMatrix as AM

from Components import *
from Sequence import *


def NextNode(adj_list, currentNode):
    if len(adj_list[currentNode-1]) == 0:
        return None

    neighbourList = copy.deepcopy(adj_list[currentNode-1])

    for i in neighbourList:
        if currentNode in adj_list[i-1]:
            adj_list[i-1].remove(int(currentNode))
            adj_list[currentNode-1].remove(i)
            nodeList = {int(j): adj_list[j][:] for j in range(len(adj_list))}
            if max(get_components(nodeList)) > 1 and neighbourList.index(i) != len(neighbourList) - 1:
                adj_list[i-1].append(currentNode)
                adj_list[currentNode-1].append(i)
            else:
                return i
            nodeList.clear()


def generate_euler_graph(number_of_vertices):
    # kazdy wierzcholek powinien byc parzystego stopnia
    even = [i for i in range(2, number_of_vertices, 2)]
    vertice_deg = [random.choice(even) for i in range(1, number_of_vertices + 1)]

    while not Sequence.ifSequenceIsGraph(Sequence(vertice_deg)):
        vertice_deg = [random.choice(even) for i in range(1, number_of_vertices + 1)]

    adjacencyMatrix = AM.AdjacencyMatrix(Sequence.sequenceToAdjacencyMatrix(Sequence(vertice_deg)).adjMatrix)
    adjacencyList = adjacencyMatrix.convertToAL()

    currentNode = 1
    eulerCycleList = [currentNode]
    while True:
        currentNode=NextNode(adjacencyList.adjList, currentNode)
        if currentNode != None:
            eulerCycleList.append(currentNode)
        else:
            break
    return eulerCycleList
