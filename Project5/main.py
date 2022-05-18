from FlowNetwork import *

def task1():
    print('\n\n----------zad1-----------')
    layers_number = 3
    network = FlowNetwork(layers_number)
    matrix, vertices_count = network.flow_network_generator(2 * layers_number)
    max_flow = ford_fulkerson(matrix, vertices_count)
    print(max_flow)

if __name__ == '__main__':
    task1()
