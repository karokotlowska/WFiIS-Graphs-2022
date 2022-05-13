import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../Project1')))
from randomGraph import *

''' Random Directed Graph based on adjecency matrix. 
    Function returns matrix.'''
def randomDirectedGraph(n,p):
    matrix=emptyMatrix(n,n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                if(r.random()<p):
                    matrix[i][j]=1
    
    return matrix

