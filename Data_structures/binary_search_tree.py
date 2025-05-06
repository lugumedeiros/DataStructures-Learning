# A simple Binary Search Tree (BST) where each node holds a value and has left/right children.
# Values are inserted recursively: smaller to the left, greater to the right.
# Supports insertion, deletion (via subtree replacement), height calculation, and full tree traversal.

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def get_left(self):
        return self.root if self.left is None else self.left.get_left()
    
    def get_right(self):
        return self.root if self.right is None else self.right.get_right()
    
    def get_root(self):
        return self.root
    
    def insert(self, value):
        # Root is empty and will accept new value
        if self.root is None:
            self.root = value
            return
        
        # Create or insert value into child
        if value <= self.root:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def height(self):
        return max(self._get_left_height(), self._get_right_height())
    
    def _get_left_height(self):
        return 1 if self.left is None else self.left._get_left_height() + 1
    
    def _get_right_height(self):
        return 1 if self.right is None else self.right._get_right_height() + 1
    
    def delete(self, value):
        node_pointer = self._find_node(value)
        direction = "left" if value <= self.root else "right"

        # Simple swap
        if node_pointer.left is None and node_pointer.right is None:
            node_pointer = None
            return
        if direction == "left":
            if node_pointer.right is None:
                node_pointer = node_pointer.left
                return
        if direction == "right":
            if node_pointer.left is None:
                node_pointer = node_pointer.right
                return
        
        # Complex Swap
        if direction == "left":
            min_node = node_pointer.left._go_furthest("right")
            node_pointer.root = min_node.root
            min_node.root = None

        else:
            max_node = node_pointer.right._go_furthest("left")
            node_pointer.root = max_node.root
            max_node.root = None        

    def _find_node(self, value):
        if self.root == value:
            return self
        elif value < self.root and self.left is not None:
            return self.left._find_node(value)
        elif value > self.root and self.right is not None:
            return self.right._find_node(value)
        else:
            print("Invalid Operation")

    def _go_furthest(self, direction):
        if direction == "left":
            if self.left is not None:
                return self.left._go_furthest(direction)
            elif self.right is not None:
                return self.right._go_furthest(direction)
            else:
                return self
        
        elif direction == "right":
            if self.right is not None:
                return self.right._go_furthest(direction)
            elif self.left is not None:
                return self.left._go_furthest(direction)
            else:
                return self

    def get_tree(self):
        if self.root is None:
            return ''
        if self.left is None and self.right is None:
            return self.root

        left_str = '' if self.left is None else self.left.get_tree()
        right_str = '' if self.right is None else self.right.get_tree()
        return f"{self.root} [{left_str}, {right_str}]"

if __name__ == "__main__":
    # Create an empty tree
    tree = BinarySearchTree()

    # Insert values
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    # Print full tree structure
    print("Tree:", tree.get_tree())  
    # Output format: root [left_subtree, right_subtree]

    # Get tree height
    print("Height:", tree.height())  # Should reflect depth of the deepest side

    # Get leftmost (minimum) and rightmost (maximum) values
    print("Leftmost (min):", tree.get_left())    # 3
    print("Rightmost (max):", tree.get_right())  # 18

    # Delete a value and print tree again
    tree.delete(15)
    print("Tree after deleting 15:", tree.get_tree())
