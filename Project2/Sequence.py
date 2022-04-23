import copy
from AdjacencyList import AdjacencyList
from operator import itemgetter

class Sequence:

    def __init__(self, *args):
        self.seq=args[0]

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
        return false

    def sequenceToAdjacencyList(self):
        indexed_data = [[index, idx] for index, idx in enumerate(self.seq)]

        adjacency_list = [[] for _ in range(len(indexed_data))]

        for _ in range(len(indexed_data)):
            indexed_data.sort(reverse=True, key=itemgetter(1))
            i = 0
            j = i + 1
            while indexed_data[i][1] > 0 and j < len(indexed_data):
                adjacency_list[indexed_data[i][0]].append(indexed_data[j][0])
                adjacency_list[indexed_data[j][0]].append(indexed_data[i][0])
                indexed_data[i][1] -= 1
                indexed_data[j][1] -= 1
                j += 1
        print(adjacency_list)
        return AdjacencyList(adjacency_list)