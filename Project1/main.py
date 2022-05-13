import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
import fileReader as fr
import AdjacencyList as AL
import AdjacencyMatrix as AM
import IncidenceMatrix as IM
import randomGraph as rg
import tkinter as tkinter
from Graph import *

def task1():
    print('\n\n-----zad1-----REPREZENTACJA GRAFOW\n')
    ALtask()
    AMtask()
    IMtask()

def ALtask():
    print('\n\n--------------LISTA SASIEDZTWA I JEJ KONWERSJE\n')
    #Test AdjacencyList and its methods

    adjacencyList = AL.AdjacencyList(fr.readMatrix('./adjacencyList.txt'))
    adjacencyList.print()

    adjacencyMatrix=adjacencyList.convertToAM()
    adjacencyMatrix.print()

    adjacencyMatrix=adjacencyList.convertToIM()
    adjacencyMatrix.print()

def AMtask():
    print('\n\n--------------MACIERZ SASIEDZTWA I JEJ KONWERSJE\n')
    #Test AdjacencyMatrix and its methods

    adjacencyMatrix=AM.AdjacencyMatrix(fr.readMatrix('./adjacencyMatrix.txt'))
    adjacencyMatrix.print()

    adjacencyList=adjacencyMatrix.convertToAL()
    adjacencyList.print()

    incidenceMatrix=adjacencyMatrix.convertToIM()
    incidenceMatrix.print()


def IMtask():
    print('\n\n--------------MACIERZ INCYDENCJI I JEJ KONWERSJE\n')
    #Test of incidencyMatrix and its methods
    incidenceMatrix=IM.IncidenceMatrix(fr.readMatrix('./incidenceMatrix.txt'))
    incidenceMatrix.print()

    adjacencyList=incidenceMatrix.convertToAL()
    adjacencyList.print()

    adjacencyMatrix=incidenceMatrix.convertToAM()
    adjacencyMatrix.print()

def task2():
    print('\n\n-----zad2-----RYSOWANIE GRAFU')
    #Task2 Drawing graph`
    adjacencyList = AL.AdjacencyList(fr.readMatrix('./adjacencyList.txt'))
    g = Graph(0, None, 0, adjacencyList)
    g.drawGraph()

def task3():
    print('\n\n-----zad3-----LOSOWE GRAFY')
    #Task3 Random Graphs
    print('\n\n--------------GRAF LOSOWY NA PODSTAWIE PRAWDOPODOBIENSTWA')
    matrix=rg.randomGraphWithProbability(10,0.5)
    for row in matrix:
       print(row)

    print('\n\n--------------GRAF LOSOWY NA PODSTAWIE ILOSCI KRAWEDZI')
    matrix=rg.randomGraphwithNumberOfEdges(10,5)
    for row in matrix:
       print(row)


if __name__ == '__main__':
    task1()
    task2()
    task3()