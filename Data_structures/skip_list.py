# SkipList: probabilistic sorted linked list for fast insert/search/delete (avg O(log n))
# Uses multiple layers of linked lists with coin-flip height randomization
# Supports insert, delete, and view all levels


import random

class _skipListNode:
    def __init__(self, value, pointers):
        self.value = value
        self.pointer = pointers

class SkipList:
    def __init__(self):
        self.max_height = 4
        self.neg = _skipListNode(float("-inf"), self.max_height*[None])
        self.pos = _skipListNode(float("inf"), self.max_height*[None])
        self.neg.pointer = [self.pos] * (self.max_height)

    def flip_coins(self):
        height = 1
        while random.randrange(0,2) == 1 and height < self.max_height:
            height += 1
        return height
    
    def get_before_list(self, value):
        search_node = self.neg
        
        height = self.max_height - 1
        node_list_previous = [None] * self.max_height
        while height >= 0:

            if search_node.pointer[height].value >= value:
                node_list_previous[height] = search_node
                height -= 1
            else:
                search_node = search_node.pointer[height]
        return node_list_previous

    def insert(self, value):
        node_height = self.flip_coins()
        previous_node_list = self.get_before_list(value)
        previous_node_list = previous_node_list[:node_height]
        
        subsequent_node_list = [None] * node_height
        for idx, prev_node in enumerate(previous_node_list):
            subsequent_node_list[idx] = prev_node.pointer[idx]

        node = _skipListNode(value, subsequent_node_list)
        for idx, prev_node in enumerate(previous_node_list):
            prev_node.pointer[idx] = node

    def delete(self, value):
        previous_node_list = self.get_before_list(value)
        node = previous_node_list[0].pointer[0]
        if node.value != value:
            return
        node_pointers = node.pointer
        for idx, item in enumerate(node_pointers):
            previous_node_list[idx].pointer[idx] = item

    def get_all(self):
        main_list = []
        for i in range(self.max_height-1, -1, -1):
            node = self.neg.pointer[i]
            level_list = []
            while node != self.pos:
                level_list.append(node.value)
                node = node.pointer[i]
            main_list.append(level_list)
        return main_list
    
if __name__ == "__main__":
    print("=== SkipList Example ===")
    sl = SkipList()

    print("Inserting values: from 0 to 20")
    for i in range(20):
        sl.insert(i)

    print("Levels after insertions:")
    for i, level in enumerate(sl.get_all()[::-1]):
        print(f"Level {i}: {level}")

    print("\nDeleting evens")
    for i in range(10):
        sl.delete(i*2)

    print("Levels after deletion:")
    for i, level in enumerate(sl.get_all()[::-1]):
        print(f"Level {i}: {level}")
