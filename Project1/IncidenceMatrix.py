class IncidenceMatrix:

    def __init__(self, listMatrix):
        self.incList = listMatrix
        self.verticesNumber = len(self.incList)
        self.edgesNumber = len(self.incList[0])
    
    def convertToAM(self):
        adjacencyMatrix = [[0 for _ in range(self.verticesNumber)] for _ in range(self.verticesNumber)]
        for i in range(self.edgesNumber):
            f = False
            fVindex = 0
            for j in range(self.verticesNumber):
                if self.incList[j][i] == 1 and f == False:
                    f = True
                    fVindex = j
                elif self.incList[j][i] == 1 and f == True:
                    adjacencyMatrix[fVindex][j] = 1
                    adjacencyMatrix[j][fVindex] = 1
        return adjacencyMatrix

    def convertToAL(self):
        adjacencyList = [[] for _ in range(self.verticesNumber)]
        
        for i in range(self.edgesNumber):
            f = False
            fVindex = 0
            for j in range(self.verticesNumber):
                if self.incList[j][i] == 1 and f == False:
                    f = True
                    fVindex = j
                elif self.incList[j][i] ==1 and f == True:
                    adjacencyList[fVindex].append(j+1)
                    adjacencyList[j].append(fVindex+1)

        for i in adjacencyList:
            i.sort()
        return adjacencyList
                

            

    def print(self):
        print('Macierz incydencji:')
        for i in self.incList:
            print(i)
        print()