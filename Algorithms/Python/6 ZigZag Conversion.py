class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        if numRows <= 1 or numRows > len_s:
            return s

        result = ''

        for r in range(numRows):
            start = r
            if r == 0 or r == (numRows - 1):
                step = (numRows - 2) * 2 + 2
                result = result + s[start:len_s:step]
            else:
                margin_1 = (numRows - r - 2) * 2 + 2
                margin_2 = r * 2
                flage = True
                while start < len_s:
                    result = result + s[start]
                    if flage:
                        start = start + margin_1
                    else:
                        start = start + margin_2
                    flage = not flage

        return result
