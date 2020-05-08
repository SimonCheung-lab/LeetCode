class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 2:
            return 1

        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = pow(mid, 2)
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
