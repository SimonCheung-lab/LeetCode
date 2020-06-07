class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ls = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            while i < j and not ls[i].isalpha():
                i += 1
            while i < j and not ls[j].isalpha():
                j -= 1
            
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1

        return ''.join(ls)
