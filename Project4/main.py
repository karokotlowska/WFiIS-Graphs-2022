import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
from Graph import *
from RandomDirecredGraph import *
import fileReader as fr
from Kosaraju import kosaraju

'''Zad1 - Direcred Graph and Random Directed Graph'''
matrix1=randomDirectedGraph(7,0.3)
# matrix2=fr.readMatrix('directedGraphExample1.txt')
print('-----zad1-----losowy graf skierowany')
for row in matrix1:
    print(row)

# ------------ zad 2
print('\n\n-----zad1-----szukanie silnie spojnych skladowych dla losowego grafu')
kosaraju(matrix1)


