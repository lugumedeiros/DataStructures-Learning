"""Code that I used to learn about some algorithms"""

from collections import deque
import random
import time
import heapq
import copy

class Sort:
    @staticmethod

    def _swap(x, y, lst):
            lst[x], lst[y] = lst[y], lst[x]

    def insertsort(lst):
        """Ω(n) O(n^2) avr(n^2), No recursion"""
        for i in range(len(lst)):
            for j in range(i):
                pointer = (i - j)
                left = lst[pointer - 1]
                right = lst[pointer]
                if left > right:
                    lst[pointer] = left
                    lst[pointer - 1] = right
                else:
                    break
        
        return lst

    def quicksort(lst):
        """O(nlogn) Ω(n^2) avr(nlogn), Space Θ(nlogn), Has recursion"""
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
        less = [x for x in lst if x < pivot]
        equal = [x for x in lst if x == pivot]
        more = [x for x in lst if x > pivot]
        return Sort.quicksort(less) + equal + Sort.quicksort(more)
    
    def better_quicksort(lst, origin=None, end=None):
        """It's worse in python bruh"""
        if origin is None or end is None:
            origin = 0
            end = len(lst)
        
        if end - origin <= 1:
            return lst

        # Select random index and swap pivot to origin
        random_index = random.randrange(origin, end)
        Sort._swap(random_index, origin, lst)
        pivot = lst[origin]

        greater = origin+1 # index to first greater value to be swaped
        for i in range(origin+1, end):
            if lst[i] <= pivot:
                Sort._swap(i, greater, lst)
                greater += 1
        Sort._swap(greater-1, origin, lst)

        if greater - 1 > origin:
            Sort.better_quicksort(lst, origin, greater-1)
        if end - greater > 0:
            Sort.better_quicksort(lst, greater, end)
        return lst

    def merge_sort(lst):
        """Θ(nlogn), Has recursion"""
        def sort(lst_a, lst_b):
            new_lst = []
            while len(lst_a) >= 1 and len(lst_b) >= 1:
                if lst_a[0] <= lst_b[0]:
                    new_lst.append(lst_a[0])
                    lst_a.pop(0)
                else:
                    new_lst.append(lst_b[0])
                    lst_b.pop(0)
            
            if len(lst_a) > 0:
                return new_lst + lst_a
            else:
                return new_lst + lst_b

        lst_size = len(lst)
        if lst_size == 1:
            return lst
        else:
            lst_a = lst[: lst_size//2]
            lst_b = lst[lst_size//2 :]
            return sort(Sort.merge_sort(lst_a), Sort.merge_sort(lst_b))
        
    def heap_sort(array):
        """Θ(nlogn), Space Θ(1), Has recursion"""
        heap = Heap.Min_heap(array)
        heap.heapsort()
        return heap.heap
    
class Search:
    @staticmethod
    def _swap(x, y, lst):
            temp = lst[x]
            lst[x] = lst[y]
            lst[y] = temp
            return lst

    def bfs_search_bad(graph, start_search, item_search):
        # Tried to do my own just from concepts, not so bad I think
        invalid_graph = []
        search_graph = graph[start_search]
        degree = 1
        
        while len(search_graph) > 0:
            if item_search in search_graph:
                print(f"item found!, {degree} items distant from start")
                break
            else:
                temp_graph = search_graph.copy()
                for key in search_graph:
                    invalid_graph.append(key)
                    temp_graph += graph[key]
                new_graph = []
                for key in temp_graph:
                    if not key in invalid_graph:
                        new_graph.append(key)
            search_graph = new_graph
            degree += 1

    def bfs_search(graph, start_search, item_search):
        # This one I applied FIFO, first time I used this...
        degree = 0
        fifo = deque([(start_search, degree)]) # List of tuples
        invalid_keys = set([start_search])

        while len(fifo) > 0:
            key, degree = fifo[0]
            if key == item_search:
                print(f"item found!, {degree} items distant from start")
                return
            else:
                fifo.popleft()
                for subkey in graph[key]:
                    if not subkey in invalid_keys:
                        fifo.append((subkey, degree + 1))

    def dijkstra_bad2(graph, start):
        """I tried to make my own code for the dijkstra algorithm but it ended like a bfs search with distance mapping
        The main problem is that it will watse time because the order of searching is decided by the graph input,
        and not about the shortest path first, but in the end works and it has the complexity of a bfs lol.
        """

        # Create a FIFO and visited blacklist set
        fifo = deque([(start)])
        visited = set([])
        
        # Create distance map with invalid dist.
        distance = {node:float('inf') for node in graph}
        distance[start] = 0

        while len(fifo):
            node = fifo.popleft()
            visited.add(node)
            curr_dist = distance[node]
            for key, dist in graph[node]:
                dist += curr_dist
                # Test if current node was visited already
                if key in visited:
                    pass
                else:
                    fifo.append(key)
                    # Test if current declared distance is greater than new one
                    if distance[key] > dist:
                        distance[key] = dist
                    else:
                        pass
        return distance  

    def dijkstra_bad(graph, start):
        """ I never user heapq before, so this was my poor implementation of "correct" dijkstra, chapgpt is screaming tho...
        In the end this was potentially slower than my bfs version.
        """
        def get_smaller_value(map, blacklist):
            smll_v = float('inf')
            smll_k = None
            for key, value in map.items():
                if not (key in blacklist) and (value < smll_v):
                    smll_v = value
                    smll_k = key
            if smll_k == None:
                pass
            return smll_k

        set_visited = set([]) # List with all searched nodes
        map_dist = {node:float('inf') for node in graph} # List with the updated distances from start
        map_dist[start] = 0

        while len(set_visited) < len(map_dist):
            node = get_smaller_value(map_dist, set_visited)
            if node is None: break
            set_visited.add(node)
            current_dist = map_dist[node]

            for sub_node, sub_dist in graph[node]:
                sub_dist += current_dist
                if sub_node in set_visited:
                    pass
                else:
                    if sub_dist < map_dist[sub_node]:
                        map_dist[sub_node] = sub_dist

        return map_dist
                    
    def dijkstra(graph, start):
        """This is the correct python code for "dijksjktsra" i think... I used heapq this time, as adviced by chatgpt."""
        map_dist = {node:float('inf') for node in graph}
        map_dist[start] = 0
        to_visit = [(0, start)]

        while len(to_visit) > 0:
            current_dist, node = heapq.heappop(to_visit)

            for sub_node, sub_dist in graph[node]:
                sub_dist += current_dist

                if sub_dist < map_dist[sub_node]:
                    map_dist[sub_node] = sub_dist
                    heapq.heappush(to_visit, (sub_dist, sub_node))

        return map_dist

    def bin_search(lst, value):
        idx = len(lst) // 2
        midd = lst[idx]
        if midd == value:
            return idx
        elif len(lst) == 1:
            return None
        elif midd < value:
            return Search.bin_search(lst[idx:], value)
        else:
            return Search.bin_search(lst[:idx], value)

    def quick_selection(lst, position):
        random_idx = random.randrange(0, len(lst))
        random_idx=0
        pivot = lst[random_idx]
        Search._swap(random_idx, len(lst)-1, lst)

        left = []
        right = []
        for i in range(len(lst) - 1):
            if lst[i] <= pivot:
                left.append(lst[i])
            elif lst[i] > pivot:
                right.append(lst[i])

        if len(left)-1 == position:
            return left[len(left)-1]
        
        elif len(left)-1 > position:
            return Search.quick_selection(left, position)

        else:
            new_pos = position - (1 + len(left))
            return Search.quick_selection(right, new_pos)

class Specific:
    @staticmethod
    def findCrossoverIndex(x, y, left=0, right=None):
        """Binary Search algorithm to find an index in two lists in which the first
        index has x>y and the second y>x"""
        right = len(x) if right is None else right
        mid = (right + left) // 2

        if mid == len(x):
            return None
        
        if x[mid] > y[mid]:
            if x[mid+1] < y[mid+1]:
                return mid
            else:
                return Specific.findCrossoverIndex(x, y, left=mid+1, right=right)
        else:
            return Specific.findCrossoverIndex(x, y, left=left, right=mid-1)
        
    def integerCubeRoot(n, left=0, right=None):
        """Binary search algorithm to find the integer cube root of positive value given"""
        if n <= 1:
            return n
        
        cube = lambda x: x*x*x
        right = n-1 if right is None else right
        mid = (left + right)//2
        
        if cube(mid) == n:
            return mid
        elif cube(mid) < n:
            if cube(mid+1) > n:
                return mid
            else:
                return Specific.integerCubeRoot(n, mid+1, right)
        else:
            return Specific.integerCubeRoot(n, left, mid-1)

class Heap:
    @staticmethod

    class Max_heap:
        def __init__(self, array):
            self.heap = array
            self.heapfy()

        def _swap(self, x, y, array):
            """Swap 2 idx from array"""
            assert x <= len(array) and y <= len(array)
            
            temp_x = array[x]
            array[x] = array[y]
            array[y] = temp_x
            return array

        def _get_children(self, idx, array):
            """get quantity of children if any at all"""
            array_max = len(array) - 1
            l_child_idx = ((idx + 1)* 2) - 1
            if l_child_idx > array_max:
                return False
            elif l_child_idx == array_max:
                return 1
            else:
                return 2
            
        def _bubble_down(self, idx, array):
            l_child = lambda x: ((x + 1) * 2) - 1

            has_child = self._get_children(idx, array)

            if not has_child:   # Has no children
                return array
            elif has_child == 1:    # Has only left child
                small_c = l_child(idx)
            else:   # Has 2 children
                left_c = l_child(idx)
                rigth_c = left_c + 1
                small_c = left_c if array[left_c] > array[rigth_c] else rigth_c
            
            if array[idx] < array[small_c]: # Test if smaller children must swap with parent
                array = self._swap(idx, small_c, array)
                return self._bubble_down(small_c, array)
            else:
                return array
            
        def _bubble_up(self,idx, array):
            if idx <= 0:
                return array
            
            parent = ((idx + 1) // 2) - 1
            
            if array[parent] < array[idx]:
                array = self._swap(parent, idx, array)
                return self._bubble_up(parent, array)
            else:
                return array

        def heapfy(self):
            heap_len = (len(self.heap) // 2) -1
            for i in range(heap_len, -1, -1):
                self.heap = self._bubble_down(i, self.heap)
        
        def heapsort(self):
            self.heapfy()
            total_len = len(self.heap)

            for i in range((total_len-1), -1, -1):
                self.heap = self._swap(0, i, self.heap)
                self.heap = self._bubble_down(0, self.heap[:i]) + self.heap[i:]

            for i in range(total_len // 2):
                compl = (total_len - i) - 1
                self.heap = self._swap(i, compl, self.heap)

        def insert(self, value):
            self.heap.append(value)
            pos = len(self.heap) - 1
            self.heap = self._bubble_up(pos, self.heap)
        
        def delete(self, idx):
            last_pos = len(self.heap) - 1
            self.heap = self._swap(idx, last_pos, self.heap)
            self.heap = self.heap[:last_pos]

            parent = ((idx + 1) // 2) - 1
            if idx == 0:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] < self.heap[idx]:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] > self.heap[idx]:
                return self._bubble_up(idx, self.heap)
            else: return
        
        def pop(self):
            value = self.heap[0]
            self.delete(0)
            return value

    class Min_heap:
        def __init__(self, array):
            self.heap = array
            self.heapfy()

        def _swap(self, x, y, array):
            """Swap 2 idx from array"""
            assert x <= len(array) and y <= len(array)
            
            temp_x = array[x]
            array[x] = array[y]
            array[y] = temp_x
            return array

        def _get_children(self, idx, array):
            """get quantity of children if any at all"""
            array_max = len(array) - 1
            l_child_idx = ((idx + 1)* 2) - 1
            if l_child_idx > array_max:
                return False
            elif l_child_idx == array_max:
                return 1
            else:
                return 2
            
        def _bubble_down(self, idx, array):
            l_child = lambda x: ((x + 1) * 2) - 1

            has_child = self._get_children(idx, array)

            if not has_child:   # Has no children
                return array
            elif has_child == 1:    # Has only left child
                small_c = l_child(idx)
            else:   # Has 2 children
                left_c = l_child(idx)
                rigth_c = left_c + 1
                small_c = left_c if array[left_c] < array[rigth_c] else rigth_c
            
            if array[idx] > array[small_c]: # Test if smaller children must swap with parent
                array = self._swap(idx, small_c, array)
                return self._bubble_down(small_c, array)
            else:
                return array
            
        def _bubble_up(self,idx, array):
            if idx <= 0:
                return array
            
            parent = ((idx + 1) // 2) - 1
            
            if array[parent] > array[idx]:
                array = self._swap(parent, idx, array)
                return self._bubble_up(parent, array)
            else:
                return array

        def heapfy(self):
            heap_len = (len(self.heap) // 2) -1
            for i in range(heap_len, -1, -1):
                self.heap = self._bubble_down(i, self.heap)
        
        def heapsort(self):
            self.heapfy()
            total_len = len(self.heap)

            for i in range((total_len-1), -1, -1):
                self.heap = self._swap(0, i, self.heap)
                self.heap = self._bubble_down(0, self.heap[:i]) + self.heap[i:]

            for i in range(total_len // 2):
                compl = (total_len - i) - 1
                self.heap = self._swap(i, compl, self.heap)

        def insert(self, value):
            self.heap.append(value)
            pos = len(self.heap) - 1
            self.heap = self._bubble_up(pos, self.heap)
        
        def delete(self, idx):
            last_pos = len(self.heap) - 1
            self.heap = self._swap(idx, last_pos, self.heap)
            self.heap = self.heap[:last_pos]

            parent = ((idx + 1) // 2) - 1
            if idx == 0:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] < self.heap[idx]:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] > self.heap[idx]:
                return self._bubble_up(idx, self.heap)
            else: return
        
        def pop(self):
            value = self.heap[0]
            self.delete(0)
            return value

    class MedianHeap:
        def __init__(self, array=None):
            array = [] if array is None else array
            self.min_heap = Heap.Min_heap(array)
            self.max_heap = Heap.Max_heap([])
            self._sort_and_split()

        def _sort_and_split(self):
            unsorted_arr = self.max_heap.heap + self.min_heap.heap
            sorting_heap = Heap.Min_heap(unsorted_arr)
            sorting_heap.heapsort()
            sorted_arr = sorting_heap.heap

            half_arr = -(len(sorted_arr) // -2)
            self.max_heap.heap = sorted_arr[:half_arr]
            self.min_heap.heap = sorted_arr[half_arr:]
            self.max_heap.heapfy()

        def peek(self):
            if len(self.max_heap.heap) - len(self.min_heap.heap) == 0:
                return (self.max_heap.heap[0] + self.min_heap.heap[0]) / 2
            else:
                return self.max_heap.heap[0]
        
        def insert(self, value):
            self.max_heap.insert(value)
            self._sort_and_split()

class Hash:
    class CountMinSketch():
        # Count Min with 3 terrible hash funtions...
        def __init__(self, size_hash):
            self.counters = [[0]*size_hash for _ in range(3)]
            self.size_hash = size_hash

        def insert(self, number):
            key_1, key_2, key_3 = self._get_keys(number)
            self.counters[0][key_1] += 1
            self.counters[1][key_2] += 1
            self.counters[2][key_3] += 1

        def check(self, number):
            key_1, key_2, key_3 = self._get_keys(number)
            arr_1 = self.counters[0][key_1]
            arr_2 = self.counters[1][key_2]
            arr_3 = self.counters[2][key_3]
            return min(arr_1, arr_2, arr_3)
            
        def _get_keys(self, number):
            key_1 = (number * number * 9) % self.size_hash
            key_2 = ((number * number) + (number * 3)) % self.size_hash
            key_3 = (number * 13) % self.size_hash
            return (key_1, key_2, key_3)
    
    # Simple int hash just to test what I learned, with terrible hashFunctions
    # Didn't want to use sets, just normal arrays
    def __init__(self, hash_size, hashf_lst=None):
        if hashf_lst is None:
            self.hash_function = self.bad_hash_func

        self.hash = [None]*hash_size
        self.hash_size = hash_size

        self.count_min_sketch = self.CountMinSketch(hash_size)

    def insert(self, number):
        self.count_min_sketch.insert(number)
        
        key = self.hash_function(number) % self.hash_size
        
        # Test if key is empty
        if self.hash[key] is None:
            self.hash[key] = [number]
            return
        # test if number in key
        for value in self.hash[key]:
            if value == number:
                return
        # Add number to end of list
        self.hash[key].append(number)

    def delete(self, number):
        key = self.hash_function(number) % self.hash_size

        # Doesn't exist
        if self.hash[key] is None:
            return
        
        for idx, value in enumerate(self.hash[key]):
            # Try to find in array
            if value == number:
                self.hash[key].pop(idx)
                # Make it None if empty
                if len(self.hash[key]) == 0:
                    self.hash[key] = None

    def check_count(self, number):
        return self.count_min_sketch.check(number)

    # Terrible :D
    def bad_hash_func(self, number):
        return (3 * number * number) + (number * 9)

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

class skipListNode:
    def __init__(self, value, pointers):
        self.value = value
        self.pointer = pointers

class SkipList:
    def __init__(self):
        self.max_height = 4
        self.neg = skipListNode(float("-inf"), self.max_height*[None])
        self.pos = skipListNode(float("inf"), self.max_height*[None])
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

        node = skipListNode(value, subsequent_node_list)
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
                
def get_full_graph():
    d = {}
    d["YOU"] = ["ALICE","BOB"]
    d["ALICE"] = ["ANUJ", "PEGGY"]
    d["BOB"] = ["TOM", "JON"]
    d["ANUJ"] = []
    d["PEGGY"] = []
    d["TOM"] = []
    d["JON"] = ["CLAIR", "JAIR"]
    d["CLAIR"] = []
    d["JAIR"] = []
    return d

def get_full_graph_weight():
    d = {}
    d["YOU"] = [("ALICE", 1),("BOB", 10)]
    d["ALICE"] = [("ANUJ", 4), ("PEGGY", 2), ("BOB", 1)]
    d["BOB"] = [("TOM", 1), ("JON", 3)]
    d["ANUJ"] = []
    d["PEGGY"] = []
    d["TOM"] = []
    d["JON"] = [("CLAIR", 2), ("JAIR", 4)]
    d["CLAIR"] = [("JAIR", 1)]
    d["JAIR"] = []
    return d

def get_node_dist_graph():
    # Generate a large random graph with 1000 nodes
    num_nodes = 50
    graph_large = {f"N{i}": [] for i in range(num_nodes)}

    for i in range(num_nodes):
        num_edges = random.randint(2, 6)  # Each node connects to 2-6 other nodes
        neighbors = random.sample(range(num_nodes), num_edges)  # Random neighbors

        for neighbor in neighbors:
            if neighbor != i:  # No self-loops
                weight = random.randint(1, 100)  # Random weight (1-100)
                graph_large[f"N{i}"].append((f"N{neighbor}", weight))
    return graph_large

LISTA = [random.randint(0, 10) for _ in range(100)]

r = SkipList()
for i in range(0,20):
    r.insert(i)

for lst in r.get_all():
    print(lst)
print("\n")
for i in range(0,20,3):
    r.delete(i)

for lst in r.get_all():
    print(lst)
pass