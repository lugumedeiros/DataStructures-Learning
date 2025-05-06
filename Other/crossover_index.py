# SOMETHING IS WRONG #

# findCrossoverIndex: Binary Search to find an index where two lists
# cross over, i.e., first list has x > y and the next index has y > x
# It returns the crossover index where the first condition is true and the second is false.


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
    

if __name__ == "__main__":
    # Example lists with crossover
    x = [1, 2, 1, 2, 3, 4, 8]
    y = [1, 2, 1, 0, 1, 1, 1]
    
    # Finding the crossover index
    crossover_idx = findCrossoverIndex(x, y)
    
    # Print the result
    print(f"Crossover index: {crossover_idx}")
