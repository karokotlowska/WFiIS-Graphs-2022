from dijkstra import *
class DistanceMatrix:
    def __init__(self, size):
        self.size = size
        self.distMatrix = [[0 for _ in range(size)] for _ in range(size)]

    def fill_distance_matrix(self, am_weighted):
        for i in range(self.size):
            row_to_append, p_s = dijkstra(am_weighted, i)
            for j in range(self.size):
                self.distMatrix[i][j] = row_to_append[j]
        return self

    def print(self):
        print("Distance matrix:")
        for row in self.distMatrix:
            print(row)