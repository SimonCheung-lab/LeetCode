# 1 divide and conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count(nums, left, right):
            if left == right:
                return [nums[left], 1]
            
            mid = (left + right) // 2
            left_count = count(nums, left, mid)
            right_count = count(nums, mid + 1, right)

            if left_count[0] == right_count[0]:
                return [left_count[0], left_count[1] + right_count[1]]
            
            left_count[1] += sum(1 for i in range(mid + 1, right + 1) if nums[i] == left_count[0])
            right_count[1] += sum(1 for i in range(left, mid + 1) if nums[i] == right_count[0])
        
            return left_count if left_count[1] > right_count[1] else right_count

        return count(nums, 0, len(nums) - 1)[0]
        

# 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = nums[0]
        times = 1

        for i in range(1, len(nums)):
            if nums[i] == me:
                times += 1
            else:
                times -= 1
                if times == 0:
                    me = nums[i]
                    times = 1

        return me
