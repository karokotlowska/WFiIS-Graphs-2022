import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project3')))

import BellmanFord as BF
from DirectedGraph import DirectedGraph
from Vertex import Vertex
from DirectedEdge import DirectedEdge
from randomGraph import emptyMatrix
from dijkstra import dijkstra

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

def copyWeights(sourceGraph: DirectedGraph,destGraph: DirectedGraph)->None:
    for edge in sourceGraph.getListOfEdges():
        beginVertexId=edge.getBeginVertex().getVertexId()
        endVertexId = edge.getEndVertex().getVertexId()
        weight=edge.getWeight()
        seekedEdge = destGraph.findDirectedEdge(beginVertexId, endVertexId)
        if seekedEdge is not None:
            seekedEdge.setWeight(weight)





def johnson(graph: DirectedGraph) -> list[list[int]] or None:

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

    h=[0 for i in range(len(vertices))]
    for vertexId in vertices:
        h[vertexId] = d[vertexId]

    for edge in newGraph.getListOfEdges():
        beginVertexId = edge.getBeginVertex().getVertexId()
        endVertexId = edge.getEndVertex().getVertexId()
        weight=edge.getWeight()
        edge.setWeight(weight + h[beginVertexId] - h[endVertexId])

    copyWeights(newGraph,graph)

    n=len(graph.getListOfVertices())
    D=list()
    oldVertices = [vertex.getVertexId() for vertex in graph.getListOfVertices()]
    for u in oldVertices:
        distance, path = dijkstra(graph.generateWeightMatrix(), u, graph.getAdjecencyMatrixRepresentation())
        for v in oldVertices:
            for i in range(len(distance)):
                distance[i] = distance[i]-h[u]+h[v]
        D.append(distance)

    return D

    
    
