from AdjacencyList import AdjacencyList
import random
from Edge import Edge
from Node import Node
import randomGraph as randomGraph
from queue import PriorityQueue
import math
import matplotlib.pyplot as plt
import networkx as nx
from functools import partial
import tkinter as tk

class Graph:
    def __init__(self, vertices: int = 0, edges: list = [], probability: float =0, adjecencyList: AdjacencyList = None):
        self.vertices=vertices
        self.probability=probability
        self.adjacencyList=adjecencyList
        if edges is  None:
            self.edges = list()
        if adjecencyList is not None:
            self.adjacencyMatrix=self.adjacencyList.convertToAM()


    def drawWeightGraph(self):
        global root

        root = tk.Tk()
        root.geometry('600x600')
        canvas = tk.Canvas(root, height=600, width=600, bg="white")
        diff_angle = 2 * math.pi / len(self.adjacencyMatrix)

        for i in range(len(self.adjacencyMatrix)):
            angle_circle = i * diff_angle
            x_circle = 300 + 200 * math.sin(angle_circle)
            y_circle = 300 - 200 * math.cos(angle_circle)
            neighbour_id = 0

            # create edges
            for neighbour in self.adjacencyMatrix[i]:
                if neighbour_id > i and int(neighbour) > 0:
                    angle_neighbour = diff_angle * neighbour_id
                    x_neighbour = 300 + 200 * math.sin(angle_neighbour)
                    y_neighbour = 300 - 200 * math.cos(angle_neighbour)
                    canvas.create_line(x_circle, y_circle, x_neighbour, y_neighbour)

                neighbour_id += 1

            canvas.create_oval(x_circle - 25, y_circle - 25, x_circle + 25, y_circle + 25, fill="white")
            canvas.create_text(x_circle, y_circle, text=i)

        for i in range(len(self.adjacencyMatrix)):
            angle_circle = i * diff_angle
            x_circle = 300 + 200 * math.sin(angle_circle)
            y_circle = 300 - 200 * math.cos(angle_circle)
            neighbour_id = 0

            # create edges
            for neighbour in self.adjacencyMatrix[i]:
                if neighbour_id > i and int(neighbour) > 0:
                    angle_neighbour = diff_angle * neighbour_id
                    x_neighbour = 300 + 200 * math.sin(angle_neighbour)
                    y_neighbour = 300 - 200 * math.cos(angle_neighbour)
                    canvas.create_rectangle(abs(x_circle + x_neighbour) / 2, abs(y_circle + y_neighbour) / 2,
                                            abs(x_circle + x_neighbour) / 2 + 20, abs(y_circle + y_neighbour) / 2 + 20,
                                            fill="blue")
                    canvas.create_text(abs(x_circle + x_neighbour) / 2 + 10, abs(y_circle + y_neighbour) / 2 + 10,
                                       text=str(self.edges[i].weight))
                neighbour_id += 1

        canvas.pack()
        root.mainloop()




    def generateRandomWeighted(self):
        self.adjacencyMatrix=randomGraph.randomGraphWithProbability(self.vertices, self.probability)
        print(f"Losowo wygenerowany graf (macierz sasiedztwa): {self.adjacencyMatrix}\n")
        for i in range(0, len(self.adjacencyMatrix)):
            for j in range(0, i):
                if self.adjacencyMatrix[i][j] == 1:
                    new_edge = Edge(i, j, random.randint(1, 10))
                    self.edges.append(new_edge)
        for i in self.edges:
            print(f"Wagi dla krawedzi: {i}\n")



    def randomize(self,adjacencyList: AdjacencyList, n=1):
        randomizationCount = False

        listOfEdges = []

        am = self.adjacencyMatrix


        for i in range(len(am)):
            for j in range(i):
                if am[i][j] == 1:
                    edge = Edge(i, j)
                    listOfEdges.append(edge)

        while n > 0:
            x = random.randint(0, len(listOfEdges) - 1)
            y = random.randint(0, len(listOfEdges) - 1)
            nodesFirstPair: list = [listOfEdges[x].i, listOfEdges[x].j]
            nodesSecondPair: list = [listOfEdges[y].i, listOfEdges[y].j]
            edge_1 = Edge(listOfEdges[x].i, listOfEdges[y].j)
            edge_2 = Edge(listOfEdges[y].i, listOfEdges[x].j)
            if edge_1 not in listOfEdges and edge_2 not in listOfEdges and len(nodesFirstPair) == len(
                    set(nodesFirstPair)) and len(nodesSecondPair) == len(set(nodesSecondPair)):
                listOfEdges[x].j, listOfEdges[y].j = listOfEdges[y].j, listOfEdges[x].j
                n -= 1
                randomizationCount += 1

        for i in range(len(am)):
            for j in range(len(am)):
                am[i][j] = 0

        for val in listOfEdges:
            start = val.i
            end = val.j
            am[start][end] = 1
            am[end][start] = 1

        return randomizationCount


    def getWeightAM(self):
        am=self.adjacencyMatrix
        edges=self.edges

        for edge in edges:
            s=edge.i
            d=edge.j
            w=edge.weight
            am[s][d]=w
            am[d][s]=w
        print("\nMacierz sasiedztwa z wagami",am,"\n\n")
        return am

    def adj_to_list(self,adj: list):
        temp_list = [[] for _ in range(len(adj))]
        for x in range(len(adj)):
            for y in range(x, len(adj)):
                if adj[x][y] == 1:
                    temp_list[x].append(y + 1)
                    temp_list[y].append(x + 1)
        return temp_list

    def get_neighbours(self, node_id: int):
        all_neighbours_list = self.adj_to_list(self.adjacencyMatrix)
        node_neighbours_list = all_neighbours_list[node_id]
        node_neighbours_list = list(map(lambda x: x - 1, node_neighbours_list))
        return node_neighbours_list

    def get_edge_weight(self, node_start: int, node_end: int):
        for edge in self.edges:
            if edge.i == node_start and edge.j == node_end:
                return edge.weight
            if edge.i == node_end and edge.j == node_start:
                return edge.weight

    def dijkstra(self, start, end=-1):
        current = start
        visited = set()
        shortest_paths = {start: (None, 0)}
        sum_weight = 0

        while current != end:
            visited.add(current)
            destinations = self.get_neighbours(current)
            current_edge_weight = shortest_paths[current][1]

            for dist in destinations:
                weight = self.get_edge_weight(current, dist) + current_edge_weight
                if dist not in shortest_paths:
                    shortest_paths[dist] = (current, weight)
                else:
                    current_shortest_weight = shortest_paths[dist][1]
                    if current_shortest_weight > weight:
                        shortest_paths[dist] = (current, weight)

            next_destinations = dict()
            for node in shortest_paths:
                if node not in visited:
                    next_destinations[node] = shortest_paths[node]

            current = min(next_destinations, key=lambda key: next_destinations[key][1])

        path = []
        while current is not None:
            path.append(current)
            dist = shortest_paths[current][0]
            if dist is not None:
                sum_weight += self.get_edge_weight(current, dist)
            current = dist

        path = path[::-1]
        return path, sum_weight
