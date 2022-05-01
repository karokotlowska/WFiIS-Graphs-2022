from collections import defaultdict

import fileReader as fr

from Sequence import Sequence
from Graph import Graph







if __name__ == '__main__':

    #zad1------
    seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

    ##seq=[4, 4, 3, 1, 2]

    sequence = Sequence(seq)  
    print(sequence.ifSequenceIsGraph())  ## True if sequence OK

    adjacencyList = sequence.sequenceToAdjacencyList()

    print(adjacencyList.convertToAM())

    # zad2------
    print("Randomizacja wykonana ", Graph(adjacencyList).randomize(adjacencyList, 10), " razy")

    # top.mainloop()
