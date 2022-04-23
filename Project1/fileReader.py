def readMatrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrixRow = []
            for el in line.split():
               matrixRow.append(int(el))
            matrix.append(matrixRow)
    return matrix