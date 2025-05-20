class BellmanFordSearch:
    def __init__(self, graph:dict, source:str):
        self.graph = graph
        self.source = source
        self.node_map = dict()
        self.edges = []
        self.count = 0
        self.setup()
        if self.relax_all() is False:
            self.node_map = "Invalid, Negative found"

    def setup(self):
        for key, edge_list in self.graph.items():
            self.node_map[key] = (float('inf'), None)
            for edge, weight in edge_list:
                self.edges.append((key, edge, weight))
        self.node_map[self.source] = (0, None)

    def relax_all(self):
        for _ in range(len(self.graph) - 1):
            relaxed = False
            for root, end, weight in self.edges:
                if self.relax(root, end, weight):
                    relaxed = True
            # Early break
            if not relaxed:
                return True
        
        for root, end, weight in self.edges:
            if self.relax(root, end, weight):
                return False

        return True

    def relax(self, a_node, b_node, weight):
        self.count += 1
        a_dist, _ = self.node_map[a_node]
        b_dist, _ = self.node_map[b_node]

        if a_dist + weight < b_dist:
            self.node_map[b_node] = (a_dist + weight, a_node)
            return True
        return False
            
    def get(self):
        return self.node_map
        

if __name__ == "__main__":
    graph = {
    'A': [('B', -10), ('C', 4), ('E', 7)],
    'B': [('A', 1), ('C', 2), ('D', 5), ('F', 3)],
    'C': [('A', 4), ('B', 2), ('D', 1), ('G', 6)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('A', 7), ('D', 2), ('F', 4)],
    'F': [('B', 3), ('E', 1), ('G', 1)],
    'G': [('C', 6), ('F', 1)]
    }

    test = BellmanFordSearch(graph, 'A')
    print(test.count,"\n",test.get())

    # Negative
    graph = {
    'A': [('B', 1)],
    'B': [('C', -1)],
    'C': [('A', -1)]
}
