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
            return integerCubeRoot(n, mid+1, right)
    else:
        return integerCubeRoot(n, left, mid-1)