class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return left
