def cross_sub(arr):
    n = len(arr) // 2

    lsumm = float("-inf")
    summ = 0
    for i in range(n - 1, -1, -1):
        summ += arr[i]
        if summ > lsumm:
            lsumm = summ

    rsumm = float("-inf")
    summ = 0
    for i in range(n, len(arr)):
        summ += arr[i]
        if summ > rsumm:
            rsumm = summ

    return lsumm + rsumm

def max_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    
    n = len(arr) // 2
    left = max_subarray(arr[:n])
    right = max_subarray(arr[n:])
    cross = cross_sub(arr)

    if left > right and left > cross:
        return left
    if right > left and right > cross:
        return right
    return cross

if __name__ == "__main__":
    print(max_subarray([1]))
    print(max_subarray([ 1, 19, 5, -4, 7,  18, 15, -10 ]))
    print(max_subarray([5, 4, -1, 7, 8]))
    print(max_subarray([1, 2, 3, 4]))
    print(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))