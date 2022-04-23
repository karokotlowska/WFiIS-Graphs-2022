import AdjacencyList as AL
from tkinter import *
from math import pi, sin, cos

def createCircle(canvas,x,y,r):
    x0=x - r
    y0=y - r
    x1=x + r
    y1=y + r
    return canvas.create_oval(x0,y0,x1,y1,outline="black",fill="white",width=1)


def plotGraph(canvas, graph, components=None):

    if not isinstance(graph, AL.AdjacencyList):
        graph = graph.convertToAL()
    
    n = len(graph.adjList)

    canvasCenter=(canvas.winfo_width()/2,canvas.winfo_height() / 2)
    r = min(canvasCenter) / 1.5
    
    dAngle = 2 * pi / n
    
    for i in range(n):
        # calculate node coordinates
        angle = dAngle * i
        x = canvasCenter[0] + r * sin(angle)
        y = canvasCenter[1] - r * cos(angle)

        # drawing edges
        for neighbour in graph.adjList[i]:
            if neighbour <= i:
                continue
            neighbour_angle = dAngle * neighbour
            neighbour_x = canvasCenter[0] + r * sin(neighbour_angle)
            neighbour_y = canvasCenter[1] - r * cos(neighbour_angle)

            if components:
                canvas.create_line(x, y, neighbour_x, neighbour_y, fill='black', width=2)
            else:
                canvas.create_line(x, y, neighbour_x, neighbour_y)

        if components:
            createCircle(canvas, x, y, r * 0.2,width=2)
        else:
            createCircle(canvas, x, y, r * 0.2)

        canvas.create_text(x, y, text=str(i))
        