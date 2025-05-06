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
            return findCrossoverIndex(x, y, left=mid+1, right=right)
    else:
        return findCrossoverIndex(x, y, left=left, right=mid-1)