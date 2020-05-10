class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(A), len(B)
        i, j = 0, 0
        while i < m and j < n:
            sec = self.intersection(A[i], B[j])
            if sec:
                result.append(sec)
            
            if A[i][-1] >= B[j][-1]:
                j += 1
            else:
                i += 1
        return result

    def intersection(self, l1, l2):
        if l1[-1] < l2[0] or l1[0] > l2[-1]:
            return None
        return [max(l1[0], l2[0]), min(l1[-1], l2[-1])]
