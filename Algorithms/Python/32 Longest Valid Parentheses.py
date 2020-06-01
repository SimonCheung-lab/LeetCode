class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = '#' + s + '#'
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack and stack[-1][1] == '(':
                stack.pop()
            else:
                stack.append((i, c))
        
        # find the max index difference
        ans = 0
        for i in range(1, len(stack)):
            ans = max(ans, stack[i][0] - stack[i - 1][0] - 1)
        return ans
