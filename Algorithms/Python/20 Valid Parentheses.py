class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for c in s:
            if c == ')' or c == ']' or c == '}':
                if len(parentheses) == 0:
                    return False
                elif (c == ')' and parentheses[-1] == '(') or (c == ']' and parentheses[-1] == '[') or (c == '}' and parentheses[-1] == '{'):
                    parentheses.pop()
                else:
                    return False
            else:
                parentheses.append(c)

        return len(parentheses) == 0
