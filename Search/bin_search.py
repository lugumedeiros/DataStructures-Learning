# bin_search: A recursive binary search function that returns the index of a given value in a sorted list.

def bin_search(lst, value):
    idx = len(lst) // 2
    midd = lst[idx]
    if midd == value:
        return idx
    elif len(lst) == 1:
        return None
    elif midd < value:
        return bin_search(lst[idx:], value)
    else:
        return bin_search(lst[:idx], value)
    

if __name__ == "__main__":
    lst = [1, 3, 5, 7, 9, 11, 13, 15]
    value = 7
    
    result = bin_search(lst, value)
    
    if result is not None:
        print(f"Item found at index: {result}")
    else:
        print("Item not found")
