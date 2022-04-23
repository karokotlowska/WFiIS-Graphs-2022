from collections import defaultdict

import fileReader as fr

from Sequence import Sequence
import plotter as pl
from tkinter import *

#dodac rysowanie

if __name__ == '__main__':
    #---------cz1
    seq=[4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2] #sequence OK

    ##seq=[4, 4, 3, 1, 2] #sequence not OK

    sequence = Sequence(seq)
    print(sequence.ifSequenceIsGraph()) ## True if sequence OK

    adjacencyList=sequence.sequenceToAdjacencyList()

             
    
    #---------cz2




