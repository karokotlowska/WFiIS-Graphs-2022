from dijkstra import *
class DistanceMatrix:
    def __init__(self, size):
        self.size = size
        self.distMatrix = [[0 for i in range(size)] for j in range(size)]

    def fill_distance_matrix(self, am_weighted):
        for i in range(self.size):
            d_s, p_s = dijkstra(am_weighted, i,am_weighted)
            for j in range(self.size):
                self.distMatrix[i][j] = d_s[j]
        return self

    def print(self):
        print("Distance matrix:")
        for row in self.distMatrix:
            print(row)

    def get_center(self):
        min_distance = math.inf
        center = 0
        for x in range(self.size):
            sum = 0
            for y in range(self.size):
                sum += self.distMatrix[x][y]
            if sum < min_distance:
                min_distance = sum
                center = x
        center += 1
        return center, min_distance

    def get_center_minimax(self, weighted_am):
        min_distance = math.inf
        center = 0
        for x in range(self.size):
            d_s, p_s = dijkstra(weighted_am, x,weighted_am)
            max_distance = max(d_s)
            if max_distance < min_distance:
                min_distance = max_distance
                center = x
        center += 1
        return center, min_distance