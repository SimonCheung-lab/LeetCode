class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutate_at(k = 0):
            if k == n:
                ans.append(nums[:])
                return 
            
            for i in range(k, n):
                nums[k], nums[i] = nums[i], nums[k]
                permutate_at(k + 1)
                nums[i], nums[k] = nums[k], nums[i]
            
        n = len(nums)
        ans = []
        permutate_at()
        return ans
