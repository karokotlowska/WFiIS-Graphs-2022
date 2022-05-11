import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
import fileReader as fr

from collections import defaultdict
from Sequence import *
from Graph import *
from Components import *
from AdjacencyList import *
from Euler import *
from Regular import randomK_RegularGraph
from Hamilton import checkHamilton


if __name__ == '__main__':

    # zad1-------
    print('-----zad1-----')

    seq = [ 4, 2, 2, 3, 2, 1, 4 ,2 ,2 ,2 ,2]
    #seq=[4, 4, 3, 1, 2]

    sequence = Sequence(seq)
    print("Wpisana sekwencja", sequence)
    print("Czy zadany ciag graficzny moze reprezentowac graf?", sequence.ifSequenceIsGraph())  ## True if sequence OK

    adjacencyMatrix = sequence.sequenceToAdjacencyMatrix()
    adjacencyList = adjacencyMatrix.convertToAL()

    print("Lista sasiedztwa dla wczytanej sekwencji:", adjacencyList.adjList)

    g=Graph(0, None, 0, adjacencyList)
    g.drawGraph()
    print()


    # zad2------
    g=Graph(0, None, 0, adjacencyList)
    randomizationTimes=g.randomize(10)
    print("Randomizacja wykonana ", randomizationTimes, " razy\n")
    g.drawGraph()


    # zad3------
    print('-----zad3-----')
    adjacencyList = AdjacencyList(fr.readMatrix("../Project1/adjacencyList.txt"))
    adjList = {int(i + 1): adjacencyList.adjList[i][:] for i in range(len(adjacencyList.adjList))}
    print(f"Lista sasiedztwa: {adjList}\n")

    components = get_components(adjList)
    print_components(components)
    print(f"Najwieksza spojna skladowa ma numer: {get_greatest_component_index(components)}\n")


    # zad4------
    print('-----zad4-----')
    euler_cycle = generate_euler_graph(10)
    print('Cykl Eulera: ', euler_cycle)

     # zad5------
    
    print('-----zad5-----')
    adjacencyList = AdjacencyList(randomK_RegularGraph())
    print('k-regularny graf: ')
    adjacencyList.print()
    g = Graph(0, None, 0, adjacencyList)
    g.drawGraph()
    
    # zad6------

    print('-----zad6-----')
    adjacencyList = AdjacencyList(fr.readMatrix('./Hamilton.txt'))
    adjacencyList.print()
    check = checkHamilton(adjacencyList.convertToAM(), 1)
    print('czy graf jest hamiltonowski: ', check)
