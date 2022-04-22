import random
import AdjacencyMatrix as AM
from Graph import *
from Components import *
from Sequence import *

def remove_edge(adj_list, node1, node2):
    adj_list[node1-1].remove(int(node2))
    adj_list[node2-1].remove(node1)

def add_edge(adj_list, node1, node2):
    adj_list[node1-1].append(node2)
    adj_list[node2-1].append(node1)

def get_next_node(adj_list, currentNode):
    if len(adj_list[currentNode-1]) == 0:
        return None
    vertex_neighbours = copy.deepcopy(adj_list[currentNode-1])
    for i in vertex_neighbours:
        if currentNode in adj_list[i-1]:
            remove_edge(adj_list, i, currentNode)
            if max(get_components(adj_list)) > 1 and vertex_neighbours.index(i) != len(vertex_neighbours) - 1:
                add_edge(adj_list, i, currentNode)
            else:
                return i



def generate_euler_graph(number_of_vertices):
    print("Graf Eulera: ")
    vertices = [random.randrange(2, number_of_vertices,2) for i in range(1, number_of_vertices + 1)]

    while not Sequence.ifSequenceIsGraph(Sequence(vertices)):
        vertices = [random.randrange(2, number_of_vertices,2) for i in range(1, number_of_vertices + 1)]

    vertices.sort(reverse=True)
    print(vertices)

    seq = Sequence(vertices)
    print("Czy sekwencja jest grafem?", seq.ifSequenceIsGraph())
    adjacencyMatrix, adjacencyList = Sequence.sequenceToAdjacencyMatrixAndList(seq)
    return adjacencyList


def get_euler_cycle(adjacencyList):
    currentNode = 1
    eulerCycle = [currentNode]
    while True:
        currentNode=get_next_node(adjacencyList.adjList, currentNode)
        if currentNode != None:
            eulerCycle.append(currentNode)
        else:
            return eulerCycle
