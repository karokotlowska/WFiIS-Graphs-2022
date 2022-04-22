class Edge:
    def __init__(self, i, j, weight=0):
        self.i=i
        self.j=j
        self.weight = weight

    def __str__(self):
        return f"i: {self.i+1}, j: {self.j+1}, weigth: {self.weight}"
