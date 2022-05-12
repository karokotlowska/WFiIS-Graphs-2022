import copy
from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
from operator import itemgetter

class Sequence:

    def __init__(self, seq):
        self.seq=seq

    def __str__(self):
        sequence = "(" + str(self.seq[0])
        for i in range(1, len(self.seq)):
            sequence = sequence + "," + str(self.seq[i])
        sequence = sequence + ")"
        return sequence

    def __len__(self):
        return len(self.seq)

    def ifSequenceIsGraph(self):
        seq_copy = copy.deepcopy(self.seq)
        odd_count = 0

        for num in seq_copy:
            if num % 2 == 0:
                pass
            else:
                odd_count += 1
        if odd_count % 2 == 1:
            return False

        while True:
            seq_copy.sort(reverse=True)
            for elem in seq_copy:
                if elem != 0:
                    break
            else:
                return True
            if seq_copy[0] < 0 or seq_copy[0] >= len(seq_copy):
                return False
            for i in range(1, seq_copy[0] + 1):
                seq_copy[i] += - 1
            del seq_copy[0]

def sequenceToAdjacencyMatrixAndList(self):

        deg_seq=copy.copy(self.seq)
        n = len(self.seq)

        list.sort(deg_seq, reverse=True)

        matrix = [[0 for i in range(n)] for j in range(n)]

        '''matrix of indexes and values from graph sequence'''
        sub_matrix = [[i, deg_seq[i]] for i in range(n)]

        ''' - iterating through number of edges
        - sorting sub_matrix to have a list descending list of leftover vertices
        - iterating through number of vertices
        - substracting one edge from n next edges
        - adding '1' to matrix from which the edge was taken
        '''
        for _ in range(len(sub_matrix)):
            sub_matrix.sort(reverse=True, key=itemgetter(1))
            for i in range(1, sub_matrix[0][1] + 1):
                sub_matrix[i][1] -= 1
                sub_matrix[0][1] -= 1
                matrix[sub_matrix[i][0]][sub_matrix[0][0]] = 1
                matrix[sub_matrix[0][0]][sub_matrix[i][0]] = 1


        adjacencyMatrix = AdjacencyMatrix(matrix)
        adjacencyList = AdjacencyList(adjacencyMatrix.convertToAL())

        print("Lista sasiedztwa: ", adjacencyMatrix.convertToAL())
        print("Macierz sąsiedztwa: ", matrix)

        return adjacencyMatrix, adjacencyList
