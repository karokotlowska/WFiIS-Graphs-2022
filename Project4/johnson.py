import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))

import BellmanFord as BF
from DirectedGraph import DirectedGraph
from Vertex import Vertex
from DirectedEdge import DirectedEdge
from randomGraph import emptyMatrix

'''
Method
'''
def add_s(graph: DirectedGraph) ->DirectedGraph:
    helpList=list()
    for i in range(len(graph.getListOfVertices())):
        helpList.append(i+1)

    newAdjecencyList=graph.getAdjecencyList()
    newAdjecencyList.adjList.append(helpList)
    newAdjecencyList.verticesNumber+=1

    graphCopy=DirectedGraph(0,None,None,0,newAdjecencyList)

    graphCopy=graph.copyVertexAndEdges(graphCopy)

    s = Vertex(len(graph.getListOfVertices()))
    graphCopy.addVertex(s)
    for vertex in graph.getListOfVertices():
        graphCopy.addEgde(DirectedEdge(s, vertex, weight=0))

    return graphCopy

def johnson(graph) -> list[list[int]] or None:

    newGraph = add_s(graph)
    vertices = [vertex.getVertexId() for vertex in newGraph.getListOfVertices()]
    addedVertex = vertices[len(vertices)-1]
    val,d,p=BF.bellmanFord(
        newGraph.generateWeightMatrix(),
        addedVertex,
        newGraph.getAdjecencyMatrixRepresentation()
    )

    if not val:
        raise Exception('Error')

    n=len(graph.getListofVertices())

    
    
