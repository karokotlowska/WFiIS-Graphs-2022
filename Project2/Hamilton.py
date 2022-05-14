def checkHamilton(adjcencyMatrix):
    n =  len(adjcencyMatrix.adjMatrix)
    cycle = []
    visitedVertexes = [False] * n
    checked = [False] * n
    for i in range(n):
        if cycleHamilton(adjcencyMatrix.adjMatrix, i, visitedVertexes, cycle):
            print('cykl Hamiltona: ', [x + 1 for x in cycle] )
            return True
    
    return False

     
    

def cycleHamilton(adjMatrix, startVertex, visitedVertexes, cycle):

    cycle.append(startVertex)
    length = len(adjMatrix)  

    if len(cycle) == length:   
        if adjMatrix[cycle[0]][cycle[-1]] == 1:
            cycle.append(cycle[0])
            return True
        else:
            cycle.pop()
            return False
    
    visitedVertexes[startVertex] = True

    for next in range(length):
        if adjMatrix[startVertex][next] == 1 and not visitedVertexes[next]:
            if cycleHamilton(adjMatrix, next, visitedVertexes, cycle):
                return True

    visitedVertexes[startVertex] = False
    cycle.pop()

    return False 