# Made for an Assigment on Dynamic Programming
def targetSum(S, i,  tgt, map=None):
    if i >= len(S) or tgt < 0:
        return -1
    
    if map is None:
        map = [None for _ in range(len(S))]

    if map[i] is not None:
        return map[i]
        
    min_found = float("inf")
    for idx in range(i, len(S)):
        value = tgt - S[idx]
        if value < 0:
            temp = targetSum(S, idx+1, tgt)
        if value == 0:
            temp = value
        if value > 0:
            next_value = targetSum(S, idx+1, value)
            if value > next_value and next_value >= 0:
                temp = next_value
            else:
                temp = value

        if temp < min_found and temp >= 0:
            min_found = temp
    
    map[i] = min_found

    return min_found

def tgtSum(tgt, S):
    return targetSum(S, 0, tgt)

t1 = tgtSum(15, [1, 2, 15]) # Should be zero
assert t1 == 0, 'Test 1 failed'

t2 = tgtSum(26, [1, 2, 3, 4, 5, 10]) # should be 1
assert t2 == 1, 'Test 2 failed'

t3 = (tgtSum(23, [1, 2, 3, 4, 5, 10])) # should be 0
assert t3 == 0, 'Test 3 failed'


t4 = (tgtSum(18, [1, 2, 3, 4, 5, 10])) # should be 0
assert t4 == 0, 'Test 4 failed'

t5 = (tgtSum(9, [1, 2, 3, 4, 5, 10])) # should be 0
assert t5 == 0, 'Test 5 failed'

t6 = (tgtSum(457, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t6 == 1, 'Test 6 failed'

t7 = (tgtSum(512, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 0
assert t7 == 0, 'Test 7 failed'

t8 = (tgtSum(616, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t8 == 1, 'Test 8 failed'

print('All tests passed (10 points)!')