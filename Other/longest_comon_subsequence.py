class LCS:
    def __init__(self, a_str, b_str):
        self.a = a_str
        self.len_a = len(self.a)
        self.b = b_str
        self.len_b = len(self.b)
        self.stored = [[None for _ in range(self.len_b)] for _ in range(self.len_a)]

    def get_longest(self, i=0, j=0):
        if i >= self.len_a or j >= self.len_b:
            return 0
        
        if self.stored[i][j] is not None:
            return self.stored[i][j]

        if self.a[i] == self.b[j]:
            temp = 1 + self.get_longest(i+1, j+1)
        else:
            temp_left = self.get_longest(i+1, j)
            temp_right = self.get_longest(i, j+1)
            temp = temp_left if temp_left > temp_right else temp_right
        
        self.stored[i][j] = temp
        return temp
    
if __name__ == "__main__":
    a = "ACTGGATTACA"
    b = "CTAGCATCTAAC"
    lcs = LCS(a, b)
    print(lcs.get_longest())
