import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_list = []
        for n in nums[::-1]:
            i = bisect.bisect_left(sorted_list, n)
            sorted_list.insert(i, n)
            ans.append(i)
        return ans[::-1]
