class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return ans
