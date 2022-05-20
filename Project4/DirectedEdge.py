import imp
import re
from Vertex import Vertex

'''
Class representing single Edge of a directed graph
An edge starts and ends with Vertex
'''
class DirectedEdge:

    beginVertex: Vertex
    endVertex: Vertex
    visited: bool
    weight: int

    def __init__(self,beginVertex: Vertex, endVertex: Vertex,visited: bool=False,weight: int=1) -> None:
        self.beginVertex=beginVertex
        self.endVertex=endVertex
        self.visited=visited
        self.weight=weight

    def __str__(self) -> str:
        return f"Edge (from {self.beginVertex} to {self.endVertex} weight = {self.weight})"

    def getBeginVertex(self)->Vertex:
        return self.beginVertex

    def setBeginVertex(self,newBeginVertex)->None:
        self.beginVertex=newBeginVertex

    def getEndVertex(self)->Vertex:
        return self.endVertex

    def setEndVertex(self,newEndVertex)->None:
        self.endVertex=newEndVertex

    def getWeight(self)->int:
        return self.weight
    
    def setWeight(self,newWeight)->None:
        self.weight = newWeight
    
    def getVisited(self)-> bool:
        return self.visited
    
    def setVisited(self,newVisited)-> None:
        self.visited = newVisited