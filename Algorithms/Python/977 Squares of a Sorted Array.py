class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x : abs(x))
        return list(map(lambda x: x**2, A))
