from FlowNetwork import *

def task1():
    print('\n\n----------zad1-----------')
    layers_number = 2
    network = FlowNetwork(layers_number)
    matrix, vertices_count, edges = network.flow_network_generator(2 * layers_number)
    print('\n\n----------zad2-----------')
    max_flow = ford_fulkerson(matrix, vertices_count)
    print(max_flow)
    
    network.draw_network(edges, max_flow)

if __name__ == '__main__':
    task1()
