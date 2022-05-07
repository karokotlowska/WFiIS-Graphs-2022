import fileReader as fr
import AdjacencyList as AL
import AdjacencyMatrix as AM
import randomGraph as rg
import tkinter as tkinter

#Test AdjacencyList and its methods
adjacencyList = AL.AdjacencyList(fr.readMatrix("adjacencyList.txt"))
adjacencyList.print()

adjacencyMatrix=adjacencyList.convertToAM()
adjacencyMatrix.print()


#Test AdjacencyMatrix and its methods
adjacencyMatrix=AM.AdjacencyMatrix(fr.readMatrix("adjacencyMatrix.txt"))
adjacencyMatrix.print()

adjacencyList=adjacencyMatrix.convertToAL()
adjacencyList.print()

incidenceMatrix=adjacencyMatrix.convertToIM()
incidenceMatrix.print()


#Test of incidencyMatrix and its methods


#Task2 Drawing graph


#Task3 Random Graphs

# matrix=rg.randomGraphWithProbability(10,0.5)
#for row in matrix:
#    print(row)

# matrix=randomGraphwithNumberOfEdges(10,5)
#for row in matrix:
#    print(row)
