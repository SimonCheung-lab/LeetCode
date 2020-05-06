# out of time
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        n = len(A)
        result = 0
        i = 0
        while i < n:
            j = 0
            if A[i] + B[0] + C[0] + D[0] <= 0:
                while j < n:
                    k, l = 0, n - 1
                    if A[i] + B[j] + C[0] + D[0] <= 0:
                        while k < n and l >= 0:
                            s = A[i] + B[j] + C[k] + D[l]
                            if s == 0:
                                # result += 1
                                k += 1
                                c1 = 1
                                while k < n and C[k] == C[k - 1]:
                                    k += 1
                                    c1 += 1
                                l -= 1
                                c2 = 1
                                while l >= 0 and D[l] == D[l + 1]:
                                    l -= 1
                                    c2 += 1
                                # print(c1, c2)
                                result += c1 * c2
                            elif s < 0:
                                k += 1
                            else:
                                l -= 1
                    # update j
                    j += 1
            # update i
            i += 1
        return result

    
# solution 2
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a_and_b = collections.Counter([a + b for a in A for b in B])
        return sum(a_and_b.get(- c - d, 0) for c in C for d in D)    
