from typing import List
import BellmanFord as BF
from DirectedGraph import DirectedGraph
from Vertex import Vertex
from DirectedEdge import DirectedEdge

'''
Method
'''
def add_s(graph: DirectedGraph,vertex_number: int) ->DirectedGraph:
    graphCopy=graph.copy()
    s = Vertex(len(graph.getListofVertices()))
    for vertex in graph.getListofVertices():
        graphCopy.addEgde(DirectedEdge(s,vertex,weight=0))

    return graphCopy

def johnson(graph) -> List[List[int]] or None:

    newGraph = add_s(graph)
    vertices = [vertex.getVertexId() for vertex in newGraph.getListofVertices()]
    addedVertex = vertices[len(vertices)-1]
    val,d,p=be
    
    
    pass