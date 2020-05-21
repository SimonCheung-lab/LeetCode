class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''

        n = len(strs)
        first_len = len(strs[0])
        prefix = ''
        i = 0
        while True:
            if i == first_len:
                break
            
            j = 1
            while j < n:
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    break
                j += 1
            if j != n:
                break

            prefix += strs[0][i]
            i += 1                

        return prefix


# solution 2        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(str1, str2):
            n1, n2 = len(str1), len(str2)
            n = min(n1, n2)
            i = 0
            while i < n:
                if str1[i] != str2[i]:
                    break
                i += 1
            return str1[:i]

        if len(strs) == 0 or len(strs[0]) == 0:
            return ''

        n = len(strs)
        prefix = strs[0]    
        for i in range(1, n):
            prefix = common_prefix(prefix, strs[i])
            if len(prefix) == 0:
                return prefix

        return prefix


# solution 3        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''

        i = 0
        for t in zip(*strs):
            c = t[0]
            for s in t:
                if s != c:
                    return strs[0][:i]
            i += 1

        return strs[0][:i]        
