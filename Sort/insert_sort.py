def insertsort(lst):
        """Ω(n) O(n^2) avr(n^2), No recursion"""
        for i in range(len(lst)):
            for j in range(i):
                pointer = (i - j)
                left = lst[pointer - 1]
                right = lst[pointer]
                if left > right:
                    lst[pointer] = left
                    lst[pointer - 1] = right
                else:
                    break
        return lst