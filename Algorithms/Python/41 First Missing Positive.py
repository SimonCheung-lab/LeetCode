class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        max_num = max(nums)
        if max_num <= 0:
            return 1
        for i in range(1, max_num):
            if i not in nums:
                return i
        return max_num + 1
