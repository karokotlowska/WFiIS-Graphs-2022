class IncidenceMatrix:

    def __init__(self, listMatrix):
        self.incList = listMatrix
        self.verticesNumber = len(self.incList)

    def convertToAM(self):
        pass

    def convertToAL(self):
        pass

    def print(self):
        print('Macierz incydencji:')
        for i in self.incList:
            print(i)
        print()