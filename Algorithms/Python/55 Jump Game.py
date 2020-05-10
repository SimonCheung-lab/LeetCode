# backtracking, out of time
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jump_to(i):
            if i == len(nums) - 1 or i + nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False

            for j in range(nums[i], 0, -1):
                if jump_to(i + j):
                    return True
            return False

        return jump_to(0)


# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rightmost = 0
        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])

        return rightmost >= len(nums) - 1        
