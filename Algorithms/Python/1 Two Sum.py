class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        m = {}
        for i, v in enumerate(nums):
            if target - v in m:
                result.append(i)
                result.append(m[target - v])
                # assume only one solution
                break
            else:
                m[v] = i
        
        return result
