class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        flag = True
        if x < 0:
            x = -x
            flag = False

        while x != 0:
            if self.valid(result):
                result = result * 10 + (x % 10)
                x = x // 10
            else:
                return 0

        if flag is False:
            result = -result

        if self.valid(result) is False:
            return 0

        return result

    def valid(self, x):
        if x >= math.pow(2, 31) or x < -math.pow(2, 31):
            return False
        else:
            return True
