# integerCubeRoot: Binary search to find the integer cube root of a positive number.
# Returns the integer part of the cube root (i.e., the largest integer x such that x^3 <= n).

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
    

if __name__ == "__main__":
    # Example number
    n = 975831
    
    # Finding the integer cube root
    result = integerCubeRoot(n)
    
    # Print the result
    print(f"Integer aproximated cube root of {n} is: {result}")
    print(f"Real cubre root of {n} is: {result * result * result}")
