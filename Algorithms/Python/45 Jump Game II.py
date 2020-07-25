# 1. out of time
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = list(range(n))
        for i in range(n):
            for j in range(i):
                if (j + nums[j] >= i):
                    min_jumps[i] = min(min_jumps[j] + 1, min_jumps[i])
        
        return min_jumps[-1]
        
        
        
# 2. greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        step = 0

        while position > 0:
            i = 0
            while i < position:
                if nums[i] + i >= position:
                    position = i
                    step += 1
                
                i += 1

        return step
        
