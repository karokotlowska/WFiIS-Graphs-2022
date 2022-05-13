import AdjacencyList as AL
import IncidenceMatrix as IM

class AdjacencyMatrix:

    def __init__(self, listMatrix):
        self.adjMatrix = listMatrix
        self.verticesNumber = len(self.adjMatrix)

    def convertToIM(self):
        incidenceMatrix = []

        edgesNumber = 0
        for row in self.adjMatrix:
            for i in range(len(row)):
                edgesNumber += row[i]
        edgesNumber = int(edgesNumber/2)

        for i in range(self.verticesNumber):
            help=[0 for i in range(edgesNumber)]
            incidenceMatrix.append(help)

        edge = 0
        for i in range(1, self.verticesNumber):
            for j in range(i):
                if self.adjMatrix[i][j] == 1:
                    incidenceMatrix[i][edge] = 1
                    incidenceMatrix[j][edge] = 1
                    edge += 1
        return IM.IncidenceMatrix(incidenceMatrix)

    def convertToAL(self):
        adjacencyList=[]
        for row in self.adjMatrix:
            help=[]
            for col in range(len(row)):
                if row[col]==1:
                  help.append(col+1)
            adjacencyList.append(help)
        return AL.AdjacencyList(adjacencyList)

    def print(self):
        print('Macierz sasiedztwa:')
        for row in self.adjMatrix:
            print(row)
        print()