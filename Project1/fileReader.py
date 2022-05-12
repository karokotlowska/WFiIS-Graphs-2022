def readMatrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrixRow = []
            for el in line.split():
               matrixRow.append(int(el))
            matrix.append(matrixRow)
    return matrix

def readSequence(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            for el in line.split():
                matrix.append(int(el))
    return matrix
