# Made for an Assigment on Dynamic Programming

# Program the recurrence for longest stable subsequence
def lssLength(a, i, j, map=None):
    # Implement the recurrence below. Use recursive calls back to lssLength
    # your code here
    if map is None:
        map = [[None for _ in range(len(a))] for _ in range(len(a))]
        
    first = True if j == -1 else False
    if j == -1:
        j = 0
        i = 1
    
    if j >= len(a) or i >= len(a):
        return 0
    
    if map[j][i] is not None:
        return map[j][i]

    maximum = float("-inf")
    for idx in range(i, len(a)):
        if (a[j] -1) <= a[idx] <=  (a[j] + 1):
            temp = 1 + lssLength(a, idx+1, idx, map)
        else:
            temp = lssLength(a, idx+1, j, map)
     
        if temp > maximum:
            maximum = temp
    if first:
        maximum += 1

    map[j][i] = maximum
    return maximum

print('--Test1--')
n1 = lssLength([1, 4, 2, -2, 0, -1, 2, 3],0, -1)
print(n1)
assert n1== 4, f'Test 1 failed: expected answer 4, your code: {n1}'
print('passed')

print('--Test2--')
n2 = lssLength([1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6], 0, -1)
print(n2)
assert n2 == 8, f'Test 2 failed: expected answer 8, your code: {n2}'

print('--Test3--')
n3 = lssLength([0,2, 4, 6, 8, 10, 12],0, -1)
print(n3)
assert n3 == 1, f'Test 3 failed: expected answer 1, your code: {n3}'


print('--Test 4--')
n4 = lssLength([4,8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2, -3, -1], 0, -1)
print(n4)
assert n4 == 14, f'Test 4 failed: expected answer 14, your code: {n4}'

print('All Tests Passed (8 points)')