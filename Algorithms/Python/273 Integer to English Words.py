class Solution:
    BASE = ['Hundred', 'Thousand', 'Million', 'Billion']
    BASE1 = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
    BASE2 = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    BASE10 = {10:'Ten', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.BASE1[0]

        flag = 0
        result = ''
        while num:
            n = num % 1000
            tmp = self.english(n, flag)
            if len(tmp):
                if len(result) == 0:
                    result = tmp
                else:
                    result = ' '.join([tmp, result])
            num = num // 1000
            flag = flag + 1

        return result
    
    # get english [0, 999]
    def english(self, n, flag):
        result = ''
        less_than_100 = n % 100
        tens = less_than_100 // 10
        unit = less_than_100 % 10
        if less_than_100 == 0:
            result = ''
        elif less_than_100 < 10 and less_than_100 > 0:
            result = self.BASE1[less_than_100]
        elif less_than_100 >= 11 and less_than_100 <= 19:
            result = self.BASE2[less_than_100]
        elif unit == 0:
            result = self.BASE10[less_than_100]
        else:
            result = ' '.join([self.BASE10[less_than_100 - unit], self.BASE1[unit]])

        n = n // 100
        if n:
            if len(result) == 0:
                result = ' '.join([self.BASE1[n], self.BASE[0]])
            else:
                result = ' '.join([self.BASE1[n], self.BASE[0], result])
        
        if flag > 0 and len(result) > 0:
            result = ' '.join([result, self.BASE[flag]])
        return result
