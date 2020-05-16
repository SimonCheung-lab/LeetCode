# the key is find the equivalence problem
# Add Parentheses mean we can divide the expression from any operator
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        
        ans = []
        for i, s in enumerate(input):
            if s in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        # ans.append(eval(str(l) + s + str(r)))
                        if s == '+':
                            ans.append(l + r)
                        elif s == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        
        return ans
