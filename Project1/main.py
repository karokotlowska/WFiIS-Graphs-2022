import fileReader as fr
import AdjacencyList as AL
import AdjacencyMatrix as AM
import randomGraph as rg
import plotter as pl
from tkinter import *

#Test AdjecencyList and its methods
'''
adjacencyList = AL.AdjacencyList(fr.readMatrix("ls.txt"))

adjMatrix=adjacencyList.convertToAM()

for i in adjMatrix:
    print(i)

fot row in adjacencyList.adjList
    print(row)
'''
#Test AdjacencyMatrix and its methods

adjecencyMatrix=AM.AdjacencyMatrix(fr.readMatrix("ms.txt"))

#adjList=adjecencyMatrix.convertToAL()

incMatrix=adjecencyMatrix.convertToIM()


#for i in adjecencyMatrix.adjMatrix:
#    print(i)
#for row in adjList:
#    print(row)
for row in incMatrix:
    print(row)

#Test of incidencyMatrix and its methods
'''
'''
#Task2 Drawing graph
adjacencyList = AL.AdjacencyList(fr.readMatrix("ls.txt"))
top = Tk()
canvas = Canvas(top, bg="blue", height=250, width=300)

pl.plotGraph(canvas,adjacencyList)


#Task3 Random Graphs
'''
matrix=rg.randomGraphWithProbability(10,0.5)
#for row in matrix:
#    print(row)

matrix=randomGraphwithNumberOfEdges(10,5)   
#for row in matrix:
#    print(row)

'''