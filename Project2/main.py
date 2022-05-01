from collections import defaultdict

import fileReader as fr

from Sequence import Sequence
from Graph import Graph


if __name__ == '__main__':

    #zad1------
    seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

    ##seq=[4, 4, 3, 1, 2]

    sequence = Sequence(seq)
    print("Czy zadany ciag graficzny moze reprezentowac graf?",sequence.ifSequenceIsGraph())  ## True if sequence OK

    adjacencyList = sequence.sequenceToAdjacencyList()

    print("Lista sasiedztwa na podstawie ciagu graficznego:/n",adjacencyList.convertToAM())

    # zad2------
    print("Randomizacja wykonana ", Graph(0, [], 0, adjacencyList).randomize(adjacencyList, 10), " razy")

    # top.mainloop()
