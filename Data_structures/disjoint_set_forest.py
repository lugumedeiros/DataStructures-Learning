class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = set([])

class DisjointTree:
    def __init__(self, tree_tuple=None):
        self.node_map = dict()

        if tree_tuple is not None:
            self.make_tree(tree_tuple)

    def make_tree(self, tree_tuple):
        node_list, reference_key = tree_tuple
        root = Node(reference_key)
        self.node_map[root] = root
        for child_key in node_list:
            child_node = Node(child_key)
            child_node.parent = root
            root.children.add(child_node)
            self.node_map[child_key] = child_node 

    def find(self, key):
        node = self.node_map.get(key)
        if node is None:
            print("Invalid key to find")
            return False
        
        depth = 1
        while node.parent is not None:
            node = node.parent
            depth += 1

        return node, depth

    def union(self, a_key, b_key):
        if self.node_map.get(a_key) is None or self.node_map.get(b_key) is None:
            print("Invalid keys")
            return False
        
        a_node, a_depth = self.find(a_key)
        b_node, b_depth = self.find(b_key)

        if a_depth > b_depth:
            a_node.children.add(b_node)
            b_node.parent = a_node
        else:
            b_node.children.add(a_node)
            a_node.parent = b_node
        
if __name__ == "__main__":

    tree = [1, 3, 23, 12, 0 , 7]
    ref = 3
    dsf = DisjointTree((tree, ref))
    ntree = [2, 14, 32, 45]
    nref = 2
    dsf.make_tree((ntree, nref))

    x, _ = dsf.find(23)
    y, _ = dsf.find(32)

    print(f"Root trees: A={x.key}, B={y.key}")

    dsf.union(23, 32)
    x, _ = dsf.find(23)
    y, _ = dsf.find(32)

    print(f"Root trees: A={x.key}, B={y.key}")
