import heapq

def prisms_method(tree:dict) -> list:
    def get_smallest_edge(edge_list, ban_list=None) -> tuple:
        temp_node = ''
        temp_weight = float("inf")
        for path_node, weight in edge_list:
            if ban_list is not None and path_node in ban_list:
                continue
            if weight < temp_weight:
                temp_node = path_node
                temp_weight = weight
        return temp_node, temp_weight

    mst = []
    open_edge = set([])
    graph_lenght = len(tree)


    # Start Nodes:
    for key, edge_list in tree.items():
        short_node, weight = get_smallest_edge(edge_list)
        open_edge.add(key)
        open_edge.add(short_node)
        mst.append((key, short_node, weight))
        break
    
    # Rest of nodes
    while True:
        # This way just to not "change" data during loop.
        if len(mst) >= (graph_lenght -1):
            break

        temp_node = ''
        temp_weight = float("inf")
        current_node = ''
        for open_node in open_edge:
            open_node_edge_list = tree.get(open_node)
            short_node, short_weight = get_smallest_edge(open_node_edge_list, open_edge)
            if short_weight < temp_weight:
                current_node = open_node
                temp_node = short_node
                temp_weight = short_weight
        mst.append((current_node, temp_node, temp_weight))
        open_edge.add(temp_node)
    
    return mst

def kruskals_method(tree:dict) -> list:
    def get_weight(path):
        _, _, weight = path
        return weight
    
    nodes_n = len(tree)

    # Clear duplicated paths
    unique_set_edges = set([])
    for key_node, edge_list in tree.items():
        for edge in edge_list:
            edge_node, weight = edge
            if (edge_node, key_node, weight) in unique_set_edges:
                continue
            new_unique = (key_node, edge_node, weight)
            unique_set_edges.add(new_unique)
    
    # Sort paths in ascending order
    unique_list_edges = [x for x in unique_set_edges]
    unique_list_edges = sorted(unique_list_edges, key=get_weight)
    
    # Add paths to mst
    nodes_placed = set([])
    mst = []
    for path in unique_list_edges:
        a_node, b_node, weight = path
        if a_node in nodes_placed and b_node in nodes_placed:
            continue
        mst.append(path)

        # break earlier
        if len(mst) >= (nodes_n-1):
            break

    return mst


if __name__ == "__main__":
    graph = {
    'A': [('B', 1), ('C', 4), ('E', 7)],
    'B': [('A', 1), ('C', 2), ('D', 5), ('F', 3)],
    'C': [('A', 4), ('B', 2), ('D', 1), ('G', 6)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('A', 7), ('D', 2), ('F', 4)],
    'F': [('B', 3), ('E', 4), ('G', 1)],
    'G': [('C', 6), ('F', 1)]
}
    print(prisms_method(graph))
    print(kruskals_method(graph))
    