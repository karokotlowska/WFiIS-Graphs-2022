import AdjacencyMatrix as AM
class AdjacencyList:

    def __init__(self, listMatrix):
        self.adjList = listMatrix
        self.verticesNumber = len(self.adjList)

    def convertToAM(self):
        adjacencyMatrix = []
        for i in range(self.verticesNumber):
            help=[0 for i in range(self.verticesNumber)]
            adjacencyMatrix.append(help)

        for i in range(self.verticesNumber):
            for j in self.adjList[i]:
                adjacencyMatrix[i][j-1] = 1

        return AM.AdjacencyMatrix(adjacencyMatrix)

    def convertToIM(self):
        incidenceMatrix = []
        adjListCopy = list(self.adjList)

        edgesNumber = 0
        for i in self.adjList:
            edgesNumber += len(i)
        edgesNumber = int(edgesNumber / 2)

        for i in range(self.verticesNumber):
            help=[0 for i in range(edgesNumber)]
            incidenceMatrix.append(help)

    def print(self):
        print('Lista sasiedztwa:\n', self.adjList, '\n')