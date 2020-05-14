class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        while i <= j:
            bit = M & 1
            if bit == 1:
                N = N | (1 << i)
            else:
                # bit == 0
                N = N & (2**32 - 1 - (1 << i))
            M = M // 2
            i += 1
        return N
