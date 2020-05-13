import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for num in nums:
            res += len(arr) - bisect.bisect_right(arr, num * 2)
            bisect.insort_right(arr, num)
        return res
