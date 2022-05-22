from copy import deepcopy
import random
import math
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
import randomGraph as randomGraph

from AdjacencyList import *
from AdjacencyMatrix import *
from Edge import Edge
# from Node import Node
from queue import PriorityQueue
from functools import partial

class Graph:
    def __init__(self, vertices: int = 0, edges: list = [], probability: float =0, adjecencyList: AdjacencyList = None):
        self.vertices=vertices
        self.probability=probability
        self.adjacencyList=adjecencyList
        if edges is  None:
            self.edges = list()
        if adjecencyList is not None:
            self.adjacencyMatrix=self.adjacencyList.convertToAM().adjMatrix


    def drawGraph(self):
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


            for neighbour in self.adjacencyMatrix[i]:
                if neighbour_id > i and int(neighbour) > 0:
                    angle_neighbour = diff_angle * neighbour_id
                    x_neighbour = 300 + 200 * math.sin(angle_neighbour)
                    y_neighbour = 300 - 200 * math.cos(angle_neighbour)
                    canvas.create_line(x_circle, y_circle, x_neighbour, y_neighbour)

                neighbour_id += 1

            canvas.create_oval(x_circle - 25, y_circle - 25, x_circle + 25, y_circle + 25, fill="red")
            canvas.create_text(x_circle, y_circle, text=i+1)

        canvas.pack()
        root.mainloop()


    def drawWeightGraph(self):
        global root

        root = tk.Tk()
        root.geometry('600x600')
        canvas = tk.Canvas(root, height=600, width=600, bg="white")
        diff_angle = 2 * math.pi / len(self.adjacencyMatrix)

        am = self.adjacencyMatrix
        edges = self.edges

        for edge in edges:
            s = edge.i
            d = edge.j
            w = edge.weight
            am[s][d] = w
            am[d][s] = w

        for i in range(len(self.adjacencyMatrix)):
            angle_circle = i * diff_angle
            x_circle = 300 + 200 * math.sin(angle_circle)
            y_circle = 300 - 200 * math.cos(angle_circle)
            neighbour_id = 0


            for neighbour in self.adjacencyMatrix[i]:
                if neighbour_id > i and int(neighbour) > 0:
                    angle_neighbour = diff_angle * neighbour_id
                    x_neighbour = 300 + 200 * math.sin(angle_neighbour)
                    y_neighbour = 300 - 200 * math.cos(angle_neighbour)
                    canvas.create_line(x_circle, y_circle, x_neighbour, y_neighbour)

                neighbour_id += 1

            canvas.create_oval(x_circle - 25, y_circle - 25, x_circle + 25, y_circle + 25, fill="red")
            canvas.create_text(x_circle, y_circle, text=i+1)

        for i in range(len(self.adjacencyMatrix)):
            angle_circle = i * diff_angle
            x_circle = 300 + 200 * math.sin(angle_circle)
            y_circle = 300 - 200 * math.cos(angle_circle)
            neighbour_id = 0


            for neighbour in self.adjacencyMatrix[i]:
                if neighbour_id > i and int(neighbour) > 0:
                    angle_neighbour = diff_angle * neighbour_id
                    x_neighbour = 300 + 200 * math.sin(angle_neighbour)
                    y_neighbour = 300 - 200 * math.cos(angle_neighbour)
                    canvas.create_rectangle(abs(x_circle + x_neighbour) / 2, abs(y_circle + y_neighbour) / 2,
                                            abs(x_circle + x_neighbour) / 2 + 20, abs(y_circle + y_neighbour) / 2 + 20)
                    canvas.create_text(abs(x_circle + x_neighbour) / 2 + 10, abs(y_circle + y_neighbour) / 2 + 10,
                                       text=str(am[i][neighbour_id]))
                neighbour_id += 1

        canvas.pack()
        root.mainloop()

    def isGraphConsistent(self, am):
        for row in am:
            if max(row) == 0:
                return False
        return True

    def generateRandomWeighted(self):
        self.adjacencyMatrix = randomGraph.randomGraphWithProbability(self.vertices, self.probability)
        while self.isGraphConsistent(self.adjacencyMatrix) == False:
            self.adjacencyMatrix = randomGraph.randomGraphWithProbability(self.vertices, self.probability)
            
        print(f"Losowo wygenerowany graf (macierz sasiedztwa): {self.adjacencyMatrix}\n")

        for i in range(0, len(self.adjacencyMatrix)):
            for j in range(0, i):
                if self.adjacencyMatrix[i][j] == 1:
                    new_edge = Edge(i, j, random.randint(1, 10))
                    self.edges.append(new_edge)
        for i in self.edges:
            print(f"Wagi dla krawedzi: {i}")


    def randomize(self, n=1):

        nodes = len(self.adjacencyMatrix)

        listOfEdges = []

        am = self.adjacencyMatrix

        for i in range(len(am)):
            for j in range(i):
                if am[i][j] == 1:
                    edge = Edge(i, j)
                    listOfEdges.append(edge)

        randomizationCount = 0

        while n > 0:
            x = random.randint(0, nodes - 1)
            y = random.randint(0, nodes - 1)
            edge1 = Edge(listOfEdges[x].i, listOfEdges[y].j)
            edge2 = Edge(listOfEdges[y].i, listOfEdges[x].j)
            if (x != y and am[x][y] == am[x][y] and am[x][y] == 1):
                a, b = listOfEdges[x].i, listOfEdges[x].j
                c, d = listOfEdges[y].i, listOfEdges[y].j
                if (a != d and b != c and am[a][d] == 0 and am[b][c] == 0 and edge1 not in listOfEdges and edge2 not in listOfEdges):
                    listOfEdges[x].j, listOfEdges[y].j = listOfEdges[y].j, listOfEdges[x].j
                    randomizationCount += 1
            n -= 1

        am2 = [[0] * len(am) for _ in range(len(am))]

        for val in listOfEdges:
            am2[val.i][val.j] = 1
            am2[val.j][val.i] = 1

        self.adjacencyMatrix = am2

        return randomizationCount


    def getWeightAM(self):
        am = self.adjacencyMatrix
        edges = self.edges
        for edge in edges:
            s = edge.i
            d = edge.j
            w = edge.weight
            am[s][d] = w
            am[d][s] = w
        print("\nMacierz sasiedztwa z wagami", am, "\n\n")
        return am


    def adj_to_list(self,adj: list):
        temp_list = [[] for _ in range(len(adj))]
        for x in range(len(adj)):
            for y in range(x, len(adj)):
                if adj[x][y] == 1:
                    temp_list[x].append(y + 1)
                    temp_list[y].append(x + 1)
        return temp_list

