from hashlib import new
import imp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))

from AdjacencyList import *
from Graph import *
from DirectedEdge import *
from Vertex import *
from randomGraph import *

'''
Class representing DirectedGraph, extends Graph
'''
class DirectedGraph(Graph):

    listOfVertices: list[Vertex]

    def __init__(self, vertices: int = 0, edges: list = ...,listOfVertices: list=..., probability: float = 0, adjecencyList: AdjacencyList = None):
        super().__init__(vertices, edges, probability, adjecencyList)
        if listOfVertices is None:
            listOfVertices=list()
            for i in range(len(adjecencyList.adjList)):
                listOfVertices.append(Vertex(i))
        self.listOfVertices=listOfVertices

    ''' Random Directed Graph based on adjecency matrix. 
    Function returns  matrix.'''
    def randomDirectedGraph(n,p):

        matrix=emptyMatrix(n,n)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if(r.random()<p):
                        matrix[i][j]=1
        
        adjacencyList=AdjacencyMatrix(matrix).convertToAL()

        return DirectedGraph(0,None,None,0,adjacencyList)
    
    '''
    Method generates Edges for a DirectedGraph object. Values are random generated
    '''
    def generateRandomDirectedEdges(self,lowerBoundry: int,upperBoundry: int):
        for i in range(0, len(self.adjacencyMatrix)):
            for j in range(0, len(self.adjacencyMatrix)):
                if self.adjacencyMatrix[i][j] == 1:
                    beginVertex = Vertex(i)
                    endVertex = Vertex(j)
                    weight = 0
                    while weight == 0:
                        weight=random.randint(lowerBoundry,upperBoundry)
                    newEdge = DirectedEdge(Vertex(i),Vertex(j),False,weight)
                    self.edges.append(newEdge)
    
    def getWeightsFromFile(self,filename)->list[int]:
        weightsList=[]
        with open(filename, 'r') as f:
            for line in f:
                for el in line.split():
                    weightsList.append(int(el))
        return weightsList
    
    def generateDirectedEdgesFromList(self,weightsList: list[int]):
         index=0
         for i in range(0, len(self.adjacencyMatrix)):
            for j in range(0, len(self.adjacencyMatrix)):
                if self.adjacencyMatrix[i][j] == 1:
                    newEdge = DirectedEdge(Vertex(i),Vertex(j),False,weightsList[index])
                    self.edges.append(newEdge)
                    index=index+1


    def generateWeightMatrix(self)->list[list[int]]:
        length=len(self.getListOfVertices())
        weightMatrix=emptyMatrix(length,length)
        for edge in self.edges:
            beginIndex=edge.getBeginVertex().getVertexId()
            endIndex=edge.getEndVertex().getVertexId()
            weightMatrix[beginIndex][endIndex]=edge.getWeight()
        
        return weightMatrix


    def printAdjecencyMatrixGraph(self)->None:
        adjMatrix=self.adjacencyMatrix
        for row in adjMatrix:
            print(row)
    
    def printEdges(self)->None:
        for e in self.edges:
            print(e)
    
    def copyVertexAndEdges(self,destGraph):
        vertexList=list()
        for vertex in self.getListOfVertices():
            vertexList.append(vertex)

        destGraph.setListOfVertices(vertexList)

        edgeList=list()
        for edge in self.getListOfEdges():
            beginVertex = edge.getBeginVertex()
            endVertex = edge.getEndVertex()
            weight = edge.getWeight()
            edgeList.append(DirectedEdge(beginVertex,endVertex,weight))
        destGraph.setListOfEdges(edgeList)

        return destGraph

    def addEgde(self,newEdge:DirectedEdge):
        self.edges.append(newEdge)

    def addVertex(self,newVertex:Vertex):
        self.listOfVertices.append(newVertex)


    def getAdjecencyMatrixRepresentation(self)->list[list[int]]:
        return self.adjacencyMatrix

    def getListOfVertices(self)->list[Vertex]:
        return self.listOfVertices

    def setListOfVertices(self,newListOfVertices: list[Vertex])->None:
        self.listOfVertices=newListOfVertices

    def getListOfEdges(self)->list[DirectedEdge]:
        return self.edges

    def setListOfEdges(self,newListOfEdges: list[Vertex])->None:
        self.edges=newListOfEdges
        
    def getAdjecencyList(self):
        return self.adjacencyList
