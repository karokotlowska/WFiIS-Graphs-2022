def get_components(adjList):
    nr = 0
    comp = []
    for node in adjList:
        comp.append(-1)
    for node in adjList:
        if comp[node-1] == -1:
            nr = nr + 1
            comp[node-1] = nr
            components_r(nr, node, adjList, comp)
    return comp

def components_r(nr, v, adjList, comp):
    for node in adjList[v]:
        if comp[node-1] == -1:
            comp[node-1] = nr
            components_r(nr, node, adjList, comp)

def get_dict_from_components(comp):
    components = { i: [] for i in comp }
    for i in range(len(comp)):
        components[comp[i]].append(i+1)
    return components

def print_components(components):
    print("Lista spojnych skladowych:")
    for key, value in components.items():
        print(f"{key}) " + " ".join(map(str, value)))


def get_greatest_component_index(components):
    max = 0
    max_id = 0
    for key, value in components.items():
        if len(value) > max:
            max = len(value)
            max_id = key
    return max_id
