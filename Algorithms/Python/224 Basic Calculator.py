class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        ans = 0
        stack = []
        i = 0
        n = len(s)
        while i < n:
            tmp = ''
            while i < n and s[i].isdigit():
                tmp += s[i]
                i += 1
            if len(tmp):
                ans = int(tmp) * sign + ans
            if i == n:
                break

            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                # append order in accord with pop
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif s[i] == ')':
                ans = ans * stack.pop() + stack.pop()

            i += 1

        return ans
