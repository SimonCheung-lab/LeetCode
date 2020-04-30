import math

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for i in range(32):
            if self.match(N, i):
                return True
        return False
    
    def match(self, N, i):
        M = int(math.pow(2, i))
        len_M = len(str(M))
        len_N = len(str(N))
        if len_M != len_N:
            return False
        
        counter = {key:0 for key in range(10)}
        while M:
            counter[M % 10] = counter[M % 10] + 1
            M = M // 10
        
        while N:
            counter[N % 10] = counter[N % 10] - 1
            if counter[N % 10] < 0:
                return False
            N = N // 10
        
        for key in range(10):
            if counter[key] != 0:
                return False
        
        return True
