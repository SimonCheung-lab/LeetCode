# solution 1
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: abs(x))
        return list(map(lambda x: x ** 2, A))

# solution 2    
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        i, j, k = 0, n - 1, n - 1
        while i <= j:
            if abs(A[i]) >= abs(A[j]):
                result[k] = A[i] ** 2
                i += 1
            else:
                result[k] = A[j] ** 2
                j -= 1
            k -= 1
        return result
