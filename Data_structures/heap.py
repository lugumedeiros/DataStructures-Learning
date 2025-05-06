# - Max_heap: max-oriented binary heap (largest at root)
# - Min_heap: min-oriented binary heap (smallest at root)
# - MedianHeap: maintains median using one max-heap and one min-heap

# Supports insert, delete, pop, heapsort, and peek (for median).

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

if __name__ == "__main__":
    print("=== Max Heap Example ===")
    maxh = Heap.Max_heap([3, 10, 5, 6, 2])
    print("Initial max heap:", maxh.heap)
    maxh.insert(12)
    print("After inserting 12:", maxh.heap)
    print("Pop max:", maxh.pop())
    print("After pop:", maxh.heap)

    print("\n=== Min Heap Example ===")
    minh = Heap.Min_heap([8, 4, 7, 1, 3])
    print("Initial min heap:", minh.heap)
    minh.insert(0)
    print("After inserting 0:", minh.heap)
    print("Pop min:", minh.pop())
    print("After pop:", minh.heap)

    print("\n=== Median Heap Example ===")
    med = Heap.MedianHeap([5, 2, 9, 1, 8])
    print("Initial median:", med.peek())
    med.insert(4)
    print("Median after inserting 4:", med.peek())
    med.insert(15)
    print("Median after inserting 15:", med.peek())
