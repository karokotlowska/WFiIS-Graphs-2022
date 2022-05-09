import AdjacencyMatrix as AM
import IncidenceMatrix as IM

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

        edge = 0
        for i, row in enumerate(adjListCopy):
            for j in row:
                incidenceMatrix[i][edge] = 1
                incidenceMatrix[j-1][edge] = 1
                adjListCopy[j-1].remove(i+1)
                edge+=1
        return IM.IncidenceMatrix(incidenceMatrix)

    def print(self):
        print('Lista sasiedztwa:\n', self.adjList, '\n')