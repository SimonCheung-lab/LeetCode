class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, max_here = float('-inf'), float('-inf')
        for n in nums:
            max_here = max(n, max_here + n)
            max_sum = max(max_sum, max_here)
        return max_sum
        
        
# Divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            # left maximum subarray
            L = find(left, mid)
            # right maximum subarray
            R = find(mid + 1, right)
            # maximum subarray across mid
            L_Mid, R_Mid = nums[mid], nums[mid + 1]
            i = mid - 1
            L_Mid_Here = L_Mid
            while i >= left:
                L_Mid_Here = L_Mid_Here + nums[i]
                L_Mid = max(L_Mid, L_Mid_Here)
                i -= 1
            i = mid + 2
            R_Mid_Here = R_Mid
            while i <= right:
                R_Mid_Here = R_Mid_Here + nums[i]
                R_Mid = max(R_Mid, R_Mid_Here)
                i += 1
            
            return max([L, R, L_Mid + R_Mid])

        return find(0, len(nums) - 1)
