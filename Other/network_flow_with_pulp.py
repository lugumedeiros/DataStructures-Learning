from pulp import *

class NetworkFlow():
    def __init__(self, graph, start, end):
        self.path_map = dict()
        self.edge_map = dict()
        self.root_map = dict()

        self.nodes_set = set()
        self.start = start
        self.end = end

        self.lp = None

        for node, edge, cap in graph:
            self.nodes_set.add(node)
            self.nodes_set.add(edge)

            if self.edge_map.get(edge) is None:
                self.edge_map[edge] = set()
            self.edge_map[edge].add(node)

            if self.root_map.get(node) is None:
                self.root_map[node] = set()
            self.root_map[node].add(edge)

            path = (node, edge)
            self.path_map[path] = cap

        
        assert start in self.nodes_set, "Start Node not present in graph"
        assert end in self.nodes_set, "End Node not present in graph"
    
        self.create_lp()

    def create_lp(self):
        self.lp = LpProblem("Flow", LpMaximize)
        var_map = dict()
        for path, capacity in self.path_map.items():
            root,node = path
            path_str = f"{root}:{node}"
            var = LpVariable(path_str, lowBound=0)
            var_map[path_str]  = var
            self.lp += var <= capacity

        self.lp += lpSum(self.get_out(self.start, var_map))

        for node in self.nodes_set:
            if node == self.start or node == self.end:
                continue
            
            out_flow = self.get_out(node, var_map)
            in_flow = self.get_in(node, var_map)
            self.lp += lpSum(out_flow) == lpSum(in_flow), f"Flow_at_{node}"

        

    def get_in(self, edge, lpmap):
        paths = []
        for root in self.edge_map[edge]:
            path = f"{root}:{edge}"
            paths.append(lpmap[path])
        return paths
    
    def get_out(self, root, lpmap):
        paths = []
        for edge in self.root_map[root]:
            path = f"{root}:{edge}"
            paths.append(lpmap[path])
        return paths
    
    def solve(self):
        self.lp.solve()

    def variables(self):
        return self.lp.variables()



if __name__ == "__main__":
    
    # (root, edge, cap)
    graph = [
        ("A","B",10),
        ("A","C",5),
        ("B","C",3),
        ("B","D",7),
        ("D","C",6),
        ("D","E",9),
        ("C","B",2),
        ("C","E",8)
    ]

    net = NetworkFlow(graph, "A", "E")
    net.solve()
    for var in net.variables():
        print(f"{var.name} = {value(var)}")