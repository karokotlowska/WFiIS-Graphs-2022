from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))

import fileReader as fr
import AdjacencyList as AL
from Sequence import Sequence
from Graph import Graph
from dijkstra import dijkstra, print_dijkstra
from DistanceMatrix import *


if __name__ == '__main__':

    print('------zad1------ random weighted graph')
    vertices=7
    probability=0.5
    graph=Graph(vertices,None,probability,None)
    graph.generateRandomWeighted()
    graph.drawWeightGraph()

    print('------zad2------ dijkstra')

    start_vertex = 0
    am_weighted = graph.getWeightAM()
    d, p = dijkstra(am_weighted, start_vertex)
    print_dijkstra(d, p, start_vertex)

    print('------zad3------ distance matrix')
    empty_distance_matrix = DistanceMatrix(len(am_weighted))
    distance_matrix = empty_distance_matrix.fill_distance_matrix(am_weighted)
    distance_matrix.print()
