class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        ans = 1
        for n in nums:
            if n - 1 not in nums_set:
                seq_len = 1
                cur = n + 1
                while cur in nums_set:
                    cur += 1
                    seq_len += 1
                ans = max(ans, seq_len) 
        return ans
