# Sort is bad with n^2 because I got too tired to make a better set queue

class Node:
    def __init__(self, key):
        self.key = key
        self.start = None
        self.end = None
        self.parent = None
        self.subparents = []

class DFT:
    count = 1
    def __init__(self, graph):
        self.node_map, self.edge_map = self._get_all_nodes(graph)
        self.graph = graph
        self.run()
        self.classify_edges()
        self.fix_parents()
        self.sort = self.topological_sort() if len(self.backward) == 0 else None
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

    def run(self, start=1, store=1, parent=False):
        node = self.node_map[start]
        node.start = self.count
        
        if node.parent is not None and not node.parent is False:
            return
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

    def fix_parents(self):
        for start, end in self.cross:
            end_node = self.node_map[end]
            if end_node.parent is False:
                end_node.parent = start
            else:
                end_node.subparents.append(start)

    def print(self):
        for _, node in self.node_map.items():
            subparents = f", subparents: {node.subparents}" if len(node.subparents) > 0 else ""
            msg = f"key: {node.key}, start: {node.start}, end:{node.end}, parent:{node.parent}{subparents}"
            print(msg)

        print(f"Tree edges: ", self.tree)
        print(f"Forward edges: ", self.forward)
        print(f"Backward edges: ", self.backward)
        print(f"Cross edges: ", self.cross)
        print(f"Topological Sort: ", self.topological_sort)
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

    def topological_sort(self):
        orfans = set([key for key, node in self.node_map.items() if node.parent is False])
        multiple_parents = set([key for key, node in self.node_map.items() if len(node.subparents) > 0])
        sorted = [i for i in orfans]

        # temp_has_multiple_parents = set([])
        # temp_parents = []

        while len(multiple_parents) > 0:
            for node_key_main in multiple_parents:
                parents_list = [node_key_main] + self.node_map[node_key_main].subparents
                for node_key in parents_list:
                    sub_sub_ancestor = self._get_sub_sub(node_key)
                    if sub_sub_ancestor in multiple_parents:
                        pass
                    
                    temp = [node_key]
                    parent_key = self.node_map[node_key].parent
                    while True:
                        if parent_key is False:
                            break
                        if parent_key in orfans:
                            break
    
                        temp.append(parent_key)
                        parent_key = self.node_map[parent_key].parent

                    try:
                        multiple_parents.remove(node_key)
                    except Exception as e:
                        #Got tired D:
                        pass

                temp.reverse()
                sorted += temp
                break
                    
        end_nodes_keys = [key for key, node in self.node_map.items() if node.start + 1 == node.end]
        for node_key in end_nodes_keys:
            temp_set = [node_key]
            parent_key = self.node_map[node_key].parent
            while parent_key not in orfans:
                temp_set.append(parent_key)
                parent_key = self.node_map[parent_key].parent
            temp_set.reverse()
            sorted += temp_set
        
        sorted_unique = []
        for item in sorted:
            if item not in sorted_unique:
                sorted_unique.append(item)

        return sorted_unique

    def _get_sub_sub(self, node_key):
        node = self.node_map[node_key]
        if node.parent is False or len(node.subparents) > 0:
            return node.key
        
        return self._get_sub_sub(node.parent)
        
       
if __name__ == "__main__":
    graph = [
        (1, 2),
        (1, 5),
        (2, 3),
        (3, 4),
        # (4, 2),
        (5, 6),
        (6, 7),
        # (7, 6),
        (8, 9),
        (8, 10),
        (9, 10),
        # (9, 1),
        (9, 3),
    ]


    test = DFT(graph)
    test.print()