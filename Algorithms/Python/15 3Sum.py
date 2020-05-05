import copy

# out of time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        def find_three(start, i):
            if i == 3:
                if sum(self.three) == 0:
                    target = sorted(self.three)
                    if target not in self.result:
                        self.result.append(copy.deepcopy(target))
                return
            
            for n in range(start, len(nums)):
                self.three[i] = nums[n]
                find_three(n + 1, i + 1)

        self.result = []
        self.three = [0] * 3
        find_three(0, 0)
        return self.result
