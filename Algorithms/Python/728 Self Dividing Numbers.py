class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(x):
            if x == 0:
                return False

            m = x
            while x:
                n = x % 10
                if n == 0:
                    return False
                if m % n != 0:
                    return False
                x = x // 10
            return True
        
        return [x for x in range(left, right + 1) if self_dividing(x)]
