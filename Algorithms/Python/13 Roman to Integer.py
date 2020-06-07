# O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        base = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subtraction_base = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        ans = 0
        while len(s):
            if len(s) >= 2 and s[:2] in subtraction_base:
                ans += subtraction_base[s[:2]]
                s = s[2:]
            else:
                ans += base[s[0]]
                s = s[1:]

        return ans
