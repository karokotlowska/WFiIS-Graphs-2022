from collections import defaultdict

import fileReader as fr

from Sequence import Sequence
import plotter as pl
from tkinter import *






if __name__ == '__main__':
    seq=[4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

    ##seq=[4, 4, 3, 1, 2]

    sequence = Sequence(seq)
    print(sequence.ifSequenceIsGraph()) ## True if sequence OK

    adjacencyList=sequence.sequenceToAdjacencyList()

    top = Tk()
    canvas = Canvas(top, bg="blue", height=250, width=300)
    pl.plotGraph(canvas, adjacencyList)
    #top.mainloop()




