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


# solution 2, more faster    
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = '#' + s + '#'
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        
        # find the max index difference
        ans = 0
        for i in range(1, len(stack)):
            ans = max(ans, stack[i] - stack[i - 1] - 1)
        return ans    

    
# solution 3, space cost O(1)    
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        # from left to right
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
                if right == left:
                    ans = max([ans, left + right])
                elif right > left:
                    left = right = 0
        
        left = right = 0
        # from right to left
        for c in s[::-1]:
            if c == ')':
                right += 1
            elif c == '(':
                left += 1
                if left == right:
                    ans = max([ans, left + right])
                elif left > right:
                    left = right = 0

        return ans    
