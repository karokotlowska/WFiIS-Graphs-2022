from Vertex import *
from Edge import *
from random import *
from plotRoad import*

import copy
import numpy as np

def readMatrix(filename):
  i = 1
  matrix = []
  with open(filename, 'r') as f:
      for line in f:
          el =line.split()
          matrix.append(Vertex(i, el[0],el[1]))
          i += 1
  return matrix


def simulated_annealing():
  print("start of algorythm")
  p = list()
  length = 0

  vertex_list = readMatrix('./input_150.dat')

  for i in range(0, len(vertex_list) - 1):
    p.append(Edge(vertex_list[i], vertex_list[i+1]))
    length += p[-1].get_weight()
    p[i].print()
  p.append(Edge(vertex_list[len(vertex_list) - 1], vertex_list[0]))
  length += p[-1].get_weight()

  #plot before
  plotRoad(p,'Beginning plot')

  MAX_IT = 150
  for i in range(0, 100):
      T = 0.001 * (100-i)**2
      for it in range(0, MAX_IT):
          begin1 = 0
          end1 = 0
          begin2 = 0
          end2 = 0
          while( begin1==begin2 or begin1==end2 or end1==begin2 or end1==end2 ):
              r1 = randint(0, 149)
              r2 = randint(0, 149)
              
              begin1 = p[r1].begin
              end1 = p[r1].end
              begin2 = p[r2].begin
              end2 = p[r2].end

          pn = copy.deepcopy(p)
          edge1=Edge(begin1,begin2)
          edge2=Edge(end1,end2)
          pn[r1] = edge1
          pn[r2] = edge2
          
          copy_length = 0
          for e in pn:
            # e.print()
            copy_length += e.get_weight()
          
          if copy_length < length:
              p = pn
              length = copy_length
          else:
              r = random()
              if r < np.exp( -1*(copy_length-length)/T ):
                  p = pn
                  length = copy_length

  print (length)
  plotRoad(p,'End plot')
  return p

if __name__ == '__main__':
  p = simulated_annealing()
  

  