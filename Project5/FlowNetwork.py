import random
import collections as cs
import math
import networkx as nx
import matplotlib.pyplot as plt
import collections

def bfs(source, target, path, matrix):
        visited = [False for _ in range(len(matrix))]
        visited[source] = True
        q = cs.deque([])
        q.append(source)
        print(path)

        while q:
            u = q.popleft()

            for ind, val in enumerate(matrix[u]):
                if not visited[ind] and val > 0:
                    q.append(ind)
                    visited[ind] = True
                    path[ind] = u
                    
        return visited[target]


def ford_fulkerson(matrix, n):
       
        source = 0
        target = n - 1
        path = [-1 for _ in range(n)]
        max_flow = 0

        while bfs(source, target, path, matrix):
            path_flow = math.inf
            tmp = target

            while tmp != source:
                path_flow = min(path_flow, matrix[path[tmp]][tmp])
                tmp = path[tmp]

            max_flow += path_flow
            v = target

            while v != source:
                u = path[v]
                matrix[u][v] -= path_flow
                matrix[v][u] += path_flow
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

        G.add_edges_from([(1, 2)])
        nodes = len(G)
        alpha = 2 * math.pi / nodes

        x_0, y_0 = 20, 20
        positions = {}

        for i in range(nodes):
            positions.update(
                {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})

        labels = nx.get_edge_attributes(G, 'weight')
        order_labels = collections.OrderedDict(sorted(labels.items()))

        nx.draw_networkx_labels(G, pos=positions)
        nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=order_labels,label_pos=0.75, font_color='green')
        nx.draw(G, pos=positions, connectionstyle="arc3,rad=0.1")
        plt.show()
		
    def getNumberOfV(layers, n):
      if n == 0:
        return 0
      else:
        return sum(len(i) for i in layers[:n])
  
    def flow_network_generator(self, N):
        '''spliting vertices into certain amount of layers'''
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
  
      
        

      
        ''''''
        edges = []

        for i in range (self.layers[1][0], self.layers[1][-1] +1):
            weight = random.randrange(1, 11)
            edges.append((0, i , weight))
        
        for q in range(1, self.layers_number-1):
          if len(self.layers[q]) > len(self.layers[q+1]): 
              bigger_layer, smaller_layer, ln = (q, q+1, len(self.layers[q]))
          else:
              bigger_layer, smaller_layer, ln=(q+1, q, len(self.layers[q+1]))
          for i in range(ln):
              if i < len(self.layers[smaller_layer]):
                  i2 = i
              else:
                  i2=len(self.layers[smaller_layer])-1
                  
              weight = random.randrange(1, 11)
                                    
              if smaller_layer > bigger_layer:    
                edges.append((i + FlowNetwork.getNumberOfV(self.layers, bigger_layer), i2 + FlowNetwork.getNumberOfV(self.layers, smaller_layer), weight))
                
              else:
                edges.append((i2 + FlowNetwork.getNumberOfV(self.layers, smaller_layer), i + FlowNetwork.getNumberOfV(self.layers, bigger_layer), weight))

        print(edges)
        

        '''adding random edges'''
        '''wiemy ze tu jest 2N'''
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
       
        print(edges)


        '''creating adjacency matrix'''
        adjacencyMatrix = [[0] * (vertice_number ) for _ in range(vertice_number)]

        for val in edges:
            adjacencyMatrix[ val[0] ][ val[1] ] = val[2]

        for i in adjacencyMatrix:
            print(i)      
      
        return adjacencyMatrix, vertice_number, edges
