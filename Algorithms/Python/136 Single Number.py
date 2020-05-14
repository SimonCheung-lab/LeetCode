class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans
