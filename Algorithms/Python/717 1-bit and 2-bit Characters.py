class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        start = 0
        flag = False

        while start < n:
            if bits[start] == 1:
                start += 2
                flag = False
            else:
                start += 1
                flag = True
                
        return flag
