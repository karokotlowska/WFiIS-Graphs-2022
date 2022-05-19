import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project2')))
from Graph import *
from RandomDirecredGraph import *
import fileReader as fr
from Kosaraju import kosaraju
from BellmanFord import randWeights, bellmanFord

'''Zad1 - Direcred Graph and Random Directed Graph'''
matrix1=randomDirectedGraph(7,0.3)
# matrix2=fr.readMatrix('directedGraphExample1.txt')
print('-----zad1-----losowy graf skierowany')
for row in matrix1:
    print(row)

# ------------ zad 2
print('\n\n-----zad2-----wyszukiwanie silnie spojnych skladowych dla losowego digrafu')
scc = kosaraju(matrix1)
print([[i + 1 for i in j]for j in scc])


# ------------ zad 3
print('\n\n-----zad3-----')
print('losowy silnie spojny digraf: ')

matrix2=randomDirectedGraph(4,0.6)

for row in matrix2:
    print(row)

scc = kosaraju(matrix2)

print('\nsprawdzenie silnie spojnej skladowej: ')
print([[i + 1 for i in j]for j in scc])


wMatrix = randWeights(matrix2)

print('\nMacierz wag: ')
for row in wMatrix:
    print(row)
print()
indicator, d, p = bellmanFord(wMatrix, 1 , matrix2)
print('W grafie jest cykl o ujemnej wadze: ', not indicator)
print(d)
print(p)

#najkrotsza sciezka (algorytm Bellmana-Forda)


