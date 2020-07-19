class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def div(dividend, divisor):
            if dividend < divisor:
                return 0
            
            ans = 1
            temp_divisor = divisor
            while 2 * temp_divisor < dividend:
                ans = 2 * ans
                temp_divisor = 2 * temp_divisor
            
            return ans + div(dividend - temp_divisor, divisor)
    
        MAX = 2 ** 31 - 1
        MIN = - (2 ** 31)

        if divisor == -1:
            if dividend <= MIN:
                return MAX
            else:
                return -dividend
        
        flag = 1
        if dividend < 0:
            flag = -flag
            dividend = -dividend
        
        if divisor < 0:
            flag = -flag
            divisor = -divisor

        return flag * div(dividend, divisor)
    
