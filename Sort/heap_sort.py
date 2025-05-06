# lazy

from Data_structures.heap import Heap
def heap_sort(array):
    """Θ(nlogn), Space Θ(1), Has recursion"""
    heap = Heap.Min_heap(array)
    heap.heapsort()
    return heap.heap