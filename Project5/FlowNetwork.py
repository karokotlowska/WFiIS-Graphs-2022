import random
from math import *
import networkx as nx
import matplotlib.pyplot as plt
import collections as col


def bfs(start, end, path, matrix):
        n = len(matrix)
        visited = [False for _ in range(n)]
        visited[start] = True
        queue = []
        queue.append(start)
        print(path)

        while queue:
            node = queue.pop(0)

            for i, bandwidth in enumerate(matrix[node]):
                if not visited[i] and bandwidth > 0:
                    queue.append(i)
                    visited[i] = True
                    path[i] = node
                    
        return visited[end]


def ford_fulkerson(graphMatrix, n):
       
        start = 0
        end = n - 1
        path = [-1] * n
        max_flow = 0

        while bfs(start, end, path, graphMatrix):
            path_flow = inf
            node = end

            while node != start:
                path_flow = min(path_flow, graphMatrix[path[node]][node])
                node = path[node]

            max_flow += path_flow
            
            v = end
            while v != start:
                u = path[v]
                graphMatrix[u][v] -= path_flow
                graphMatrix[v][u] += path_flow
                v = path[v]

        return max_flow


class FlowNetwork:
    def __init__(self, layers_number):
        if layers_number < 2:
            raise Exception("Podaj liczbe wieksza od 2")
        else:
            self.vertex_count = 2
            self.layers_number = layers_number + self.vertex_count
            self.layers = list()
            self.layers.append(list([0]))

    def draw_network(self, edges, flow):
        radius = 1000

        G = nx.DiGraph()
        for i in range(len(edges)):
            G.add_edge(edges[i][0], edges[i][1], weight=edges[i][2])

        G.add_edges_from([(0, 1)])
        nodes = len(G)
        alpha = 2 * pi / nodes

        x_0, y_0 = 20, 20
        positions = {}

        for i in range(nodes):
            positions.update(
                {(i): (x_0 + radius * cos(i * alpha), y_0 + radius * sin(i * alpha))})

        labels = nx.get_edge_attributes(G, 'weight')
        order_labels = col.OrderedDict(sorted(labels.items()))

        nx.draw_networkx_labels(G, pos=positions)
        nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=order_labels,label_pos=0.75, font_color='green')
        nx.draw(G, pos=positions, connectionstyle="arc3,rad=0.1")
        plt.show()
		
    def getNumberOfVertices(layers, n):
      if n != 0:
        return sum(len(i) for i in layers[:n])
      else:
        return 0
  
    def flow_network_generator(self, N):
        n = self.layers_number - self.vertex_count
        vertice_number = 1
        for i in range(1, n + 1):
            self.layers.append(list())
            nodes_on_layers_quantity = random.randrange(2, n + 1)
            for _ in range(nodes_on_layers_quantity):
                self.layers[i].append(vertice_number)
                vertice_number += 1
        self.layers.append(list([vertice_number]))
        vertice_number += 1
        print(f'Rozmieszczenie wierzcholkow na wartstwach', self.layers)

        edges = []

        for i in range (self.layers[1][0], self.layers[1][-1] +1):
            weight = random.randrange(1, 11)
            edges.append((0, i , weight))
        
        for i in range(1, self.layers_number-1):
          if len(self.layers[i]) > len(self.layers[i+1]): 
                lonLayer = i
                shLayer = i+1
                ln = len(self.layers[i])
          else:
                lonLayer = i+1
                shLayer = i
                ln=len(self.layers[i+1])
          for j in range(ln):
              if j < len(self.layers[shLayer]):
                  k = j
              else:
                  k=len(self.layers[shLayer])-1
                  
              weight = random.randrange(1, 11)
                                    
              if shLayer > lonLayer:    
                edges.append((j + FlowNetwork.getNumberOfVertices(self.layers, lonLayer), k + FlowNetwork.getNumberOfVertices(self.layers, shLayer), weight))
                
              else:
                edges.append((k + FlowNetwork.getNumberOfVertices(self.layers, shLayer), j + FlowNetwork.getNumberOfVertices(self.layers, lonLayer), weight))

        print(edges)
        

        l=0
        while l < N:              
            p = random.randrange(0,self.layers[-1][0] + 1)
            k = random.randrange(0,self.layers[-1][0] + 1)
            
            if p != k and k != 0 and p != self.layers[-1][0]:
                weight = random.randrange(1,11)
                edge_to_add = (p, k, weight)

                f = 0
                for edge in edges:
                    if edge[0] == p and edge[1] == k:
                        f = 1
                if f == 1:
                    continue                    
                edges.append(edge_to_add)
						
                l+=1
       
        print('\n\n---------- Krawedzie wraz z wagami----------')
        print(edges)


        adjacencyMatrix = [[0] * (vertice_number ) for _ in range(vertice_number)]

        for val in edges:
            adjacencyMatrix[ val[0] ][ val[1] ] = val[2]

        print('\n\n---------- Macierz sasiedztwa----------')
        for i in adjacencyMatrix:
            print(i)      
      
        return adjacencyMatrix, vertice_number, edges
