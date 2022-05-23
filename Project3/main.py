from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))

import fileReader as fr
import AdjacencyList as AL
import AdjacencyMatrix as AM
from Sequence import Sequence
from Graph import Graph
from dijkstra import dijkstra, print_dijkstra
from DistanceMatrix import *
from Prima import *


if __name__ == '__main__':

    print('------zad1------ random weighted graph')
    vertices=7
    probability=0.5
    graph=Graph(vertices,None,probability,None)
    graph.generateRandomWeighted()
    #graph.drawWeightGraph()

    print('------zad2------ dijkstra')

    start_vertex = 0
    am_weighted = graph.getWeightAM()
    d, p = dijkstra(am_weighted, start_vertex, am_weighted)
    print_dijkstra(d, p, start_vertex)

    print('------zad3------ distance matrix')
    empty_distance_matrix = DistanceMatrix(len(am_weighted))
    distance_matrix = empty_distance_matrix.fill_distance_matrix(am_weighted)
    distance_matrix.print()
    print()
    

    print('------zad4------ center')
    center_vertices, min_distance = distance_matrix.get_center()
    print(f'Centrum = {center_vertices} (suma odleglosci: {min_distance})')

    center_minimax, minimax = distance_matrix.get_center_minimax(am_weighted)
    print(f'Centrum minimax = {center_minimax} (odleglosc od najdalszego: {minimax})')
    print()
    graph.drawWeightGraph()

    print('------zad5------ Prima')
    graph=Graph(vertices,None,probability,None)
    graph.generateRandomWeighted()
    graph.drawWeightGraph()
    in_matrix = graph.adjacencyMatrix
    res_matrix = primsMst(in_matrix)
    graph1 = Graph(vertices,None,probability, None)
    graph1.adjacencyMatrix = res_matrix
    graph.drawWeightGraph()
    graph1.drawWeightGraph()

