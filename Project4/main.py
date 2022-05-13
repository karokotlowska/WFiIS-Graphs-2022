import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
from Graph import *
from RandomDirecredGraph import *
import fileReader as fr

'''Zad1 - Direcred Graph and Random Directed Graph'''
matrix1=randomDirectedGraph(7,0.3)
# matrix2=fr.readMatrix('directedGraphExample1.txt')

for row in matrix1:
    print(row)



