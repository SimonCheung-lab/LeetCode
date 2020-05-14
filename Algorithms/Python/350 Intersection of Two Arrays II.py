class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for n in nums1:
            m[n] = m.get(n, 0) + 1

        ans = []
        for n in nums2:
            if m.get(n, 0) and m[n] > 0:
                ans.append(n)
                m[n] -= 1
        return ans
