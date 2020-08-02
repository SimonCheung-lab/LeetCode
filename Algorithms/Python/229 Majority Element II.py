class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        candidate1, candidate2 = nums[0], nums[0]
        count1, count2 = 0, 0

        n = len(nums)

        for num in nums:
            if num == candidate1:
                count1 += 1
                continue

            if num == candidate2:
                count2 += 1
                continue
            
            if count1 == 0:
                candidate1 = num
                count1 = 1
                continue
            
            if count2 == 0:
                candidate2 = num
                count2 = 1
                continue
            
            count1 -= 1
            count2 -= 1
        
        # check
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        if candidate1 == candidate2:
            if count1 + count2 > n / 3:
                return [candidate1]
            else:
                return []

        ans = []
        if count1 > n / 3:
            ans.append(candidate1)

        if count2 > n / 3:
            ans.append(candidate2)

        return ans
