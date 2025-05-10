class Node:
    def __init__(self, key):
        self.key = key
        self.start = None
        self.end = None
        self.parent = None

class DFT:
    count = 1
    def __init__(self, graph):
        self.node_map, self.edge_map = self._get_all_nodes(graph)
        self.graph = graph
        self.run()
        self.classify_edges()
        # self.count = 1
        pass
    
    def _get_all_nodes(self, graph):

        temp_set = set([])
        node_map = {}
        edge_map = {}
        for node, edge in graph:
            if not node in temp_set:
                temp_set.add(node)
                node_map[node] = Node(node)
            if not edge in temp_set:
                temp_set.add(edge)
                node_map[edge] = Node(edge)

            if edge_map.get(node) is None:
                edge_map[node] = []
            if edge_map.get(edge) is None:
                edge_map[edge] = []

            edge_map[node].append(node_map[edge])

        return node_map, edge_map

    def run(self, start=1, store=1, parent=1):
        node = self.node_map[start]
        node.start = self.count
        
        if node.parent is not None:
            return
        else:
            node.parent = parent

        self.count += 1

        # Main tree        
        for edge in self.edge_map[node.key]:
            if edge.end is None and edge.start is None:
                self.run(edge.key, start, node.key)

        node.end = self.count
        self.count += 1

        # Cross trees
        if store == start:
            for _, parallel_node in self.node_map.items():
                if parallel_node.start is None:
                    self.run(parallel_node.key)

    def print(self):
        for _, node in self.node_map.items():
            msg = f"key: {node.key}, start: {node.start}, end:{node.end}"
            print(msg)

        print(f"Tree edges: ", self.tree)
        print(f"Forward edges: ", self.forward)
        print(f"Backward edges: ", self.backward)
        print(f"Cross edges: ", self.cross)


    def classify_edges(self):
        self.forward = []
        self.backward = []
        self.cross = []
        self.tree = []
        
        for edge in self.graph:
            root_key, end_key = edge
            
            root_node = self.node_map[root_key]
            root_start = root_node.start
            root_end = root_node.end

            end_node = self.node_map[end_key]
            end_parent = end_node.parent
            end_start = end_node.start
            end_end = end_node.end

            # Logic
            if root_start > end_end:
                self.cross.append(edge)
            elif root_key == end_parent:
                self.tree.append(edge)
            elif end_end < root_end:
                self.forward.append(edge)
            else:
                self.backward.append(edge)


if __name__ == "__main__":
    graph = [
        (1, 2),
        (1, 5),
        (2, 3),
        (3, 4),
        (4, 2),
        (5, 6),
        (6, 7),
        (7, 6),
        (8, 9),
        (8, 10),
        (9, 10),
        (9, 1),
    ]


    test = DFT(graph)
    test.print()