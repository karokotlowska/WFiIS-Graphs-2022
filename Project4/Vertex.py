'''
Class representing a single Vertex of a Graph
'''
class Vertex:
    vertexId: int
    visited: bool

    def __init__(self,vertexId: int = None,vertexVisited: bool=False) -> None:
        self.vertexId=vertexId
        self.visited=vertexVisited
    
    def __str__(self) -> str:
        return f"Vertex (id = {self.vertexId} visited = {self.visited})"
    
    def setVertexId(self,newVertexId: int = None) ->None:
        self.vertexId=newVertexId
    
    def setVisited(self,newVisited: bool = False):
        self.visited=newVisited

    def getVertexId(self)->int:
        return self.vertexId

    def getVisited(self)->bool:
        return self.visited
    
