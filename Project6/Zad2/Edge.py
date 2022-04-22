from Vertex import *
import math

class Edge:
    begin : Vertex
    end : Vertex
    weight : float

    def __init__(self, begin, end):
      self.begin=begin
      self.end=end
      self.weight = math.sqrt((int(begin.x)-int(end.x))**2+(int(begin.y)-int(end.y))**2)

    def get_weight(self):
      return self.weight
    
    def print(self):
      print("Edge: ")
      print("begin:", self.begin)
      print("end:", self.end)
      print("Weight: ", self.weight)
      print()
