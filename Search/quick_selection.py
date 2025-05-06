# quick_selection: A selection algorithm that finds the k-th smallest element in an unsorted list using the QuickSort partitioning method.


import random

def _swap(x, y, lst):
    lst[x], lst[y] = lst[y], lst[x]

def quick_selection(lst, position):
    random_idx = random.randrange(0, len(lst))
    random_idx=0
    pivot = lst[random_idx]
    _swap(random_idx, len(lst)-1, lst)

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
        return quick_selection(left, position)

    else:
        new_pos = position - (1 + len(left))
        return quick_selection(right, new_pos)
    

if __name__ == "__main__":
    lst = [10, 4, 5, 8, 6, 11, 26]
    position = 3  # Find the 3rd smallest element

    result = quick_selection(lst, position)
    
    print(f"The {position+1}-th smallest element is {result}")
