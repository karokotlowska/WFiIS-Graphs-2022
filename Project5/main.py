from FlowNetwork import *

def task1():
    print('\n\n----------zad1-----------')
    layers_number = 2
    network = FlowNetwork(layers_number)
    matrix = network.flow_network_generator(2 * layers_number)
    max_flow = ford_fulkerson(matrix, 6)
    print(max_flow)

if __name__ == '__main__':
    task1()
