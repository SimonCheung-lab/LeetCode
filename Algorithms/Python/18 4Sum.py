class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for a in range(n):
            if a == 0 or nums[a] > nums[a - 1]:
                b = a + 1
                while b < n - 2:
                    c = b + 1
                    d = n - 1
                    while c < d:
                        s = nums[a] + nums[b] + nums[c] + nums[d]
                        if s == target:
                            result.append([nums[a], nums[b], nums[c], nums[d]])
                            c += 1
                            d -= 1
                            while c < d and nums[c] == nums[c - 1]:
                                c += 1
                            while c < d and nums[d] == nums[d + 1]:
                                d -= 1
                        elif s < target:
                            c += 1
                        else:
                            d -= 1

                    # update b                   
                    b += 1
                    while b < n - 2 and nums[b] == nums[b - 1]:
                        b += 1

        return result
