import sys
import os.path
import random
from math import inf
from collections import defaultdict
import matplotlib.pyplot as pyp

def prima(W):
    edge_weight = defaultdict(list)
    n = len(W)
    res_matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    
    for weights in W:
        assert len(weights) == n

    free_vertexes = list(range(0, n))

    starting_vertex = random.choice(free_vertexes)
    T = [starting_vertex]
    free_vertexes.remove(starting_vertex)

    print('Startujemy z %s' % (starting_vertex+1))

    road_length = 0

    while free_vertexes:
        min_link = None  
        overall_min_path = inf  

        for current_vertex in T:
            weights = W[current_vertex] 

            min_path = inf
            free_vertex_min = current_vertex

            for vertex in range(n):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue
                
                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if free_vertex_min != current_vertex:
                if min_path < overall_min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path
        try:
            path_length = W[min_link[0]][min_link[1]]
        except TypeError:
            sys.exit('Nie udało się znaleźć sciezki')

        print('Łączymy %s oraz %s, waga - [%s]' % (min_link[0] + 1, min_link[1] + 1, path_length))
        edge_weight[min_link[0]].append((min_link[1], path_length))
        road_length += path_length
        free_vertexes.remove(min_link[1])
        T.append(min_link[1])

    print('Suma wag: %s' % road_length)

    for i in range(len(res_matrix)):
        if len(edge_weight[i]) == 0:
            continue
        for j in range (len(edge_weight[i])):
            row = i
            column = edge_weight[i][j][0]
            value = edge_weight[i][j][1]
            res_matrix[row][column] = res_matrix[column][row] = value
    return res_matrix