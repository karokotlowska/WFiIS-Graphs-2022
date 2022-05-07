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


    def sequenceToAdjacencyMatrix(self):
        n=len(self.seq)
        degseq=copy.copy(self.seq)
        mat = [[0] * n for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if (degseq[i] > 0 and degseq[j] > 0):
                    degseq[i] -= 1
                    degseq[j] -= 1
                    mat[i][j] = 1
                    mat[j][i] = 1

        return AdjacencyMatrix(mat)