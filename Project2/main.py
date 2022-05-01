import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
import fileReader as fr
import AdjacencyList as AL

from collections import defaultdict
from Sequence import Sequence
from Graph import Graph
from Components import *


if __name__ == '__main__':

    #zad1------
    # seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

    # ##seq=[4, 4, 3, 1, 2]

    # sequence = Sequence(seq)
    # print("Czy zadany ciag graficzny moze reprezentowac graf?",sequence.ifSequenceIsGraph())  ## True if sequence OK

    # adjacencyList = sequence.sequenceToAdjacencyList()

    # print("Lista sasiedztwa na podstawie ciagu graficznego:/n",adjacencyList.convertToAM())

    # # zad2------
    # print("Randomizacja wykonana ", Graph(0, [], 0, adjacencyList).randomize(adjacencyList, 10), " razy")

    # top.mainloop()

    # zad3
    adjacencyList = AL.AdjacencyList(fr.readMatrix("../Project1/ls.txt"))
    adjList = {int(i + 1): adjacencyList.adjList[i][:] for i in range(len(adjacencyList.adjList))}
    print(f"\nLista sasiedztwa: {adjList}\n")

    components = get_components(adjList)
    print_components(components)
    print(f"Najwieksza spojna skladowa ma numer: {get_greatest_component_index(components)}\n")
