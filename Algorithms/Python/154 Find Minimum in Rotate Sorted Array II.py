class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n -1
        ans = nums[0]

        while left <= right:
            mid = (left + right) // 2

            if left != mid and nums[left] == nums[mid]:
                left += 1
                continue
            
            if right != mid and nums[right] == nums[mid]:
                right -= 1
                continue
            
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        
        return ans
