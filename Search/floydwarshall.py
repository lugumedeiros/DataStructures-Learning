import enum
import numpy as np

class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        self.nodes_map = dict()
        self.idx_map = dict()
        self.n = len(graph)
        self.path_matrix = np.full((self.n, self.n), float('inf'))
        self.parent_matrix = np.arange(0, self.n).reshape(-1, 1)
        self.parent_matrix = np.tile(self.parent_matrix, (1, self.n))
        self._setup()
        self._run()

    def _setup(self):
        index = 0
        for i in range(self.n):
            self.path_matrix[i, i] = 0

        for key, _ in self.graph.items():
            self.nodes_map[key] = index
            self.idx_map[index] = key
            index += 1

        for source, edge_list in self.graph.items():
            for edge, weight in edge_list:
                idx_src = self.nodes_map.get(source)
                idx_edg = self.nodes_map.get(edge)
                self.path_matrix[idx_src, idx_edg] = weight

    def _run(self):
        for loop_idx in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    curr = self.path_matrix[i, j]
                    a = self.path_matrix[i, loop_idx]
                    b = self.path_matrix[loop_idx, j]
                    summ = a + b
                    if summ < curr:
                        self.path_matrix[i, j] = summ
                        self.parent_matrix[i, j] = loop_idx
        return
    
    def get(self, source, end):
        source_idx = self.nodes_map.get(source)
        end_idx = self.nodes_map.get(end)
        assert source_idx is not None, "Invalid source node"
        assert end_idx is not None, "Invalid end node"

        distance = self.path_matrix[source_idx, end_idx]
        path = [end]
        step_back_idx = self.parent_matrix[source_idx, end_idx]
        while step_back_idx != source_idx:
            path.append(self.idx_map.get(step_back_idx))
            step_back_idx = self.parent_matrix[source_idx, step_back_idx]
        path.append(source)
        path.reverse()

        return int(distance), path

       
if __name__ == "__main__":
    graph = {
        'A': [('B', 3), ('C', 8), ('E', -4)],
        'B': [('D', 1), ('E', 7)],
        'C': [('B', 4)],
        'D': [('C', -5), ('A', 2)],
        'E': [('D', 6)],
    }

    test = FloydWarshall(graph)
    dist, path = test.get("A", "C")
    print("Shortest distance from A to C:", dist)
    print("Path:", path)

    dist, path = test.get("D", "B")
    print("Shortest distance from A to C:", dist)
    print("Path:", path)

    dist, path = test.get("E", "A")
    print("Shortest distance from A to C:", dist)
    print("Path:", path)