import random

def _swap(x, y, lst):
    lst[x], lst[y] = lst[y], lst[x]

def quicksort(lst):
        """O(nlogn) Ω(n^2) avr(nlogn), Space Θ(nlogn), Has recursion"""
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
        less = [x for x in lst if x < pivot]
        equal = [x for x in lst if x == pivot]
        more = [x for x in lst if x > pivot]
        return quicksort(less) + equal + quicksort(more)

def inplace_quicksort(lst, origin=None, end=None):
        """It's worse in python bruh"""
        if origin is None or end is None:
            origin = 0
            end = len(lst)
        
        if end - origin <= 1:
            return lst

        # Select random index and swap pivot to origin
        random_index = random.randrange(origin, end)
        _swap(random_index, origin, lst)
        pivot = lst[origin]

        greater = origin+1 # index to first greater value to be swaped
        for i in range(origin+1, end):
            if lst[i] <= pivot:
                _swap(i, greater, lst)
                greater += 1
        _swap(greater-1, origin, lst)

        if greater - 1 > origin:
            inplace_quicksort(lst, origin, greater-1)
        if end - greater > 0:
            inplace_quicksort(lst, greater, end)
        return lst