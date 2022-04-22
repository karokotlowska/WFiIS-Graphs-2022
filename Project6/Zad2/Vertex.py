
class Vertex:
    vertexId : int
    x : int
    y : int
    
    def __init__(self,_id,_x,_y):
        self.vertexId=_id
        self.x=_x
        self.y=_y
    
    def print(self):
      print("x:", self.x, "y:", self.y)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"