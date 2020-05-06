class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False

        n = len(nums)
        s = [nums[0]]
        for i in range(1, n):
            m = s[i - 1] + nums[i]
            if k == 0:
                if m == 0:
                    return True
            elif m % k == 0:
                return True
            s.append(m)
        
        for i in range(1, n):
            for j in range(i, n):
                if j == i:
                    s[j] = nums[i]
                else:
                    s[j] = s[j] - s[i - 1]
                    if k == 0:
                        if s[j] == 0:
                            return True
                    elif s[j] % k == 0:
                        return True
        return False
