# binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        # find the left boundary of target
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        left_target = left

        # find the right boundary of target
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            left -= 1
        right_target = left

        if right_target < left_target or nums[left_target] != target:
            return [-1, -1]

        return [left_target, right_target]
