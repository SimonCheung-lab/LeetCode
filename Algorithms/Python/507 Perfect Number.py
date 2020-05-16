class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                if i == num // i:
                    s += i
                else:
                    s += i + num // i
                if s > num:
                    return False
        return s == num
