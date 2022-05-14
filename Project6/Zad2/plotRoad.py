from turtle import color, left
import matplotlib.pyplot as plt

def plotRoad(edgeList,plotTitle):
    x=[]
    y=[]
    for edge in edgeList:
        x.append(edge.begin.x)
        y.append(edge.begin.y)
        
    plt.plot(x,y,'.-')
    plt.xticks(color='w')
    plt.yticks(color='w')
    plt.tick_params(bottom = False)
    plt.tick_params(left=False)
    plt.title(plotTitle)
    plt.savefig(plotTitle+'.png')
    plt.show()