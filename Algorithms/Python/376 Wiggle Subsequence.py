class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        prediff = nums[1] - nums[0]
        count = 2 if prediff else 1
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prediff <= 0) or (diff < 0 and prediff >= 0):
                count += 1
                prediff = diff
        return count
