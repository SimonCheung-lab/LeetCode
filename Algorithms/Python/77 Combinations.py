# backtracking
import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if 0 >= n < k:
            return []

        self.result = []
        self.combination = [0] * k
        
        def combine_from(start, i):
            if i == k:
                self.result.append(copy.deepcopy(self.combination))
                return
            
            for c in range(start, n + 1):
                self.combination[i] = c
                combine_from(c + 1, i + 1)

        combine_from(1, 0)

        return self.result
