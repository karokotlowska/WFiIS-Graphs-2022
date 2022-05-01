class Edge:
    def __init__(self, i, j):
        self.i=i
        self.j=j

    def __str__(self):
        return f"start: {self.start}, end: {self.end}"