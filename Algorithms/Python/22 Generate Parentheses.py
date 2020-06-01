class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right):
            if left + right == 2 * n:
                ans.append(''.join(parentheses))
                return

            if left < n:
                parentheses.append('(')
                backtrack(left + 1, right)
                parentheses.pop()
            
            if right < left:
                parentheses.append(')')
                backtrack(left, right + 1)
                parentheses.pop()

        ans = []
        parentheses = []
        backtrack(0, 0)
        return ans                
