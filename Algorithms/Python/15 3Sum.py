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

    
# solution 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i == 0 or nums[i] > nums[i - 1]:
                left, right = i + 1, n - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s > 0:
                        right -= 1
                    else:
                        left += 1
        return result 
    
