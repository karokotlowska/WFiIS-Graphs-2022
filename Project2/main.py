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

    # zad1------
    print('\n\n-----zad1-----PRZYKLAD CIAGU GRAFICZNEGO')
    sequence = Sequence(fr.readSequence("sequence.txt"))
    print("Wpisana sekwencja", sequence)
    print("Czy zadany ciag graficzny moze reprezentowac graf?", sequence.ifSequenceIsGraph())

    '''adjacency matrix and adjacency list from sequence'''
    adjacencyMatrix, adjacencyList = sequence.sequenceToAdjacencyMatrixAndList()
    g = Graph(0, None, 0, adjacencyList)

    if sequence.ifSequenceIsGraph() is False:
        print("Nie da sie narysowac grafu")
    else:
        g.drawGraph()

    # zad1------
    print('\n\n-----zad1-----PRZYKLAD CIAGU NIEGRAFICZNEGO')
    sequence2 = Sequence(fr.readSequence("sequence2.txt"))
    print("Wpisana sekwencja", sequence2)
    print("Czy zadany ciag graficzny moze reprezentowac graf?", sequence2.ifSequenceIsGraph())


    # zad2------
    print('\n\n-----zad2-----')
    g = Graph(0, None, 0, adjacencyList)
    randomizationTimes = g.randomize(50)
    print("Randomizacja wykonana ", randomizationTimes, " razy\n")
    g.drawGraph()


    # zad3------
    print('-----zad3-----')
    print(f"Lista sasiedztwa: {adjacencyList.adjList}\n")
    components = get_components(adjacencyList.adjList)
    components = get_dict_from_components(components)
    print_components(components)
    print(f"Najwieksza spojna skladowa ma numer: {get_greatest_component_index(components)}\n")


    # zad4------
    print('-----zad4-----')
    adjacencyList = generate_euler_graph(6)
    g = Graph(0, None, 0, adjacencyList)
    euler_cycle = get_euler_cycle(adjacencyList)
    print('Cykl Eulera: ', euler_cycle)
    g.drawGraph()


    # zad5------
    print('-----zad5-----')
    adjacencyList = AdjacencyList(randomK_RegularGraph(16,3))
    print('k-regularny graf: ')
    adjacencyList.print()
    g = Graph(0, None, 0, adjacencyList)
    g.drawGraph()

    # zad6------

    # jest 
    print('-----zad6-----')
    adjacencyList = AdjacencyList(fr.readMatrix('./Hamilton1.txt'))
    adjacencyList.print()
    print('czy graf jest hamiltonowski: ', checkHamilton(adjacencyList.convertToAM()))
    print()
    g = Graph(0, None, 0, adjacencyList)
    g.drawGraph()

    # nie jest 
    adjacencyList = AdjacencyList(fr.readMatrix('./Hamilton2.txt'))
    adjacencyList.print()
    print()
    print('czy graf jest hamiltonowski: ', checkHamilton(adjacencyList.convertToAM()))
    g = Graph(0, None, 0, adjacencyList)
    g.drawGraph()
