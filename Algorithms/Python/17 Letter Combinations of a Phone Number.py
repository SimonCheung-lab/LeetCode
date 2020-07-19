class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(i):
            nonlocal tmp
            if i == len(digits):
                ans.append(''.join(tmp))
                return
            
            for alpha in num_to_alpha[int(digits[i])]:
                tmp[i] = alpha
                backtracking(i + 1)

        if len(digits) == 0:
            return []
        
        ans = []
        tmp = ['a'] * len(digits)
        num_to_alpha = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        
        backtracking(0)

        return ans
