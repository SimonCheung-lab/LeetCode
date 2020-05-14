class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = 2 ** n
        ans = []
        for i in range(s):
            bitmask = bin(i | s)[3:]
            ans.append([nums[j] for j in range(len(nums)) if bitmask[j] == '1'])
        return ans
