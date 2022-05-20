from hashlib import new
import imp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))

from Graph import *
from DirectedEdge import *
from Vertex import *
from randomGraph import *
from fileReader import readMatrix

'''
Class representing DirectedGraph, extends Graph
'''
class DirectedGraph(Graph):

    def __init__(self, vertices: int = 0, edges: list = ..., probability: float = 0, adjecencyList: AdjacencyList = None):
        super().__init__(vertices, edges, probability, adjecencyList)


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

        return DirectedGraph(0,None,0,adjacencyList)
    
    '''
    Method generates Edges for a DirectedGraph object. Values are random generated
    '''
    def generateRandomDirectedEdges(self,lowerBoundry: int,upperBoundry: int):
        for i in range(0, len(self.adjacencyMatrix)):
            for j in range(0, len(self.adjacencyMatrix)):
                if self.adjacencyMatrix[i][j] == 1:
                    newEdge = DirectedEdge(Vertex(i),Vertex(j),False,random.randint(lowerBoundry,upperBoundry))
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
        length=len(self.adjacencyMatrix)
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
    
    def copy(self):
        return deepcopy(self)

    def getAdjecencyMatrixRepresentation(self)->list[list[int]]:
        return self.adjacencyMatrix

        
        
