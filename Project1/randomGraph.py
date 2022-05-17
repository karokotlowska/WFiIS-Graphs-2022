import random as r

from numpy import mat

def emptyMatrix(n,l):
    matrix=[]
    for i in range(n):
        help=[0 for i in range(l)]
        matrix.append(help)
    return matrix

def randomGraphWithProbability(n,p):
    matrix=emptyMatrix(n,n)
    for i in range(n):
        for j in range(i):
            if i!=j:
                if(r.random()<p):
                    matrix[i][j]=1
                    matrix[j][i]=1
    return matrix

def randomGraphwithNumberOfEdges(n,l):
    
    matrix=emptyMatrix(n,n)

    if l>(n*n-n)/2:
        print("Nie mozna utworzyc tyle krawedzi, zwracam pusta macierz")
        return matrix

    counter=0
    while counter<l:
        i=r.randint(0,n-1)
        j=r.randint(0,i)
        if matrix[i][j]==0 and i!=j:
            matrix[i][j]=1
            matrix[j][i]=1
            counter+=1
    return matrix
