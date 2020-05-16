class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        op = '+'
        i = 0
        while i < n:
            tmp = ''
            while i < n and s[i].isdigit():
                tmp += s[i]
                i += 1
            
            if len(tmp):
                if op == '+':
                    stack.append(int(tmp))
                elif op == '-':
                    stack.append(-int(tmp))
                elif op == '*':
                    stack.append(stack.pop() * int(tmp))
                elif op == '/':
                    top = stack.pop()
                    # special
                    if top < 0:
                        stack.append(- ((-top) // int(tmp)))
                    else:
                        stack.append(top // int(tmp))
            
            if i < n and s[i] in ['+', '-', '*', '/']:
                op = s[i]

            i += 1
        
        return sum(stack)
