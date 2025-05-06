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