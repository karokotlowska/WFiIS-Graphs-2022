from collections import defaultdict
import sys
import os
import fileReader as fr
import AdjacencyList as AL
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
from Sequence import Sequence
from Graph import Graph


if __name__ == '__main__':

    #zad1------

    #random weighted graph
    vertices=7
    probability=0.5
    graph=Graph(vertices,None,probability,None)
    graph.generateRandomWeighted()
    graph.drawWeightGraph()

    # zad2------
