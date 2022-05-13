import random
import AdjacencyMatrix as AM
from Graph import *
from Components import *
from Sequence import *


def get_next_node(adj_list, currentNode):
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
    print("Graf Eulera: ")
    even = [i for i in range(2, number_of_vertices, 2)]
    vertice_deg = [random.choice(even) for i in range(1, number_of_vertices + 1)]

    while not Sequence.ifSequenceIsGraph(Sequence(vertice_deg)):
        vertice_deg = [random.choice(even) for i in range(1, number_of_vertices + 1)]
    vertice_deg.sort(reverse=True)
    print(vertice_deg)
    seq = Sequence(vertice_deg)
    print("Czy sekwencja jest grafem?", seq.ifSequenceIsGraph())
    adjacencyMatrix, adjacencyList = Sequence.sequenceToAdjacencyMatrixAndList(seq)
    return adjacencyList


def get_euler_cycle(adjacencyList):
    adjacencyList.print()
    currentNode = 1
    eulerCycleList = [currentNode]
    while True:
        currentNode=get_next_node(adjacencyList.adjList, currentNode)
        if currentNode != None:
            eulerCycleList.append(currentNode)
        else:
            break
    return eulerCycleList
