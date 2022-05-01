from AdjacencyList import AdjacencyList
import random
from Edge import Edge

class Graph:
    def __init__(self, adjecencyList=None,adjacencyMatrix=None):
        self.adjacencyList=adjecencyList
        self.adjacencyMatrix=adjacencyMatrix

    def randomize(self,adjacencyList: AdjacencyList, n=1):
        randomizationCount = False

        listOfEdges = []

        if self.adjacencyMatrix is None:
            am = adjacencyList.convertToAM()
        else:
            am = self.adjacencyMatrix


        for i in range(len(am)):
            for j in range(i):
                if am[i][j] == 1:
                    edge = Edge(i, j)
                    listOfEdges.append(edge)

        while n > 0:
            x = random.randint(0, len(listOfEdges) - 1)
            y = random.randint(0, len(listOfEdges) - 1)
            nodesFirstPair: list = [listOfEdges[x].i, listOfEdges[x].j]
            nodesSecondPair: list = [listOfEdges[y].i, listOfEdges[y].j]
            edge_1 = Edge(listOfEdges[x].i, listOfEdges[y].j)
            edge_2 = Edge(listOfEdges[y].i, listOfEdges[x].j)
            if edge_1 not in listOfEdges and edge_2 not in listOfEdges and len(nodesFirstPair) == len(
                    set(nodesFirstPair)) and len(nodesSecondPair) == len(set(nodesSecondPair)):
                listOfEdges[x].j, listOfEdges[y].j = listOfEdges[y].j, listOfEdges[x].j
                n -= 1
                randomizationCount += 1

        for i in range(len(am)):
            for j in range(len(am)):
                am[i][j] = 0

        for val in listOfEdges:
            start = val.i
            end = val.j
            am[start][end] = 1
            am[end][start] = 1

        return randomizationCount
