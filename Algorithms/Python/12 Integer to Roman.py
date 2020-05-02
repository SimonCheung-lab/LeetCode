class Solution:
    def intToRoman(self, num: int) -> str:
        base1 = {1:'I', 10:'X', 100:'C', 1000:'M'}
        base4 = {4:'IV', 40:'XL', 400:'CD'}
        base5 = {5:'V', 50:'L', 500:'D'}
        base9 = {9:'IX', 90:'XC', 900:'CM'}

        flag = 1
        result = ''
        while num:
            n = num % 10
            if n == 0:
                roman = ''
            elif n <= 3:
                roman = base1[flag] * n
            elif n == 4:
                roman = base4[flag * 4]
            elif n == 5:
                roman = base5[flag * 5]
            elif n <= 8:
                roman = base5[flag * 5] + (base1[flag] * (n - 5))
            else:
                # n == 9
                roman = base9[flag * 9]
            result = roman + result
            num = num // 10
            flag = flag * 10
        return result
