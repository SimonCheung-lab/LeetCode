# we just want get the count, not the specific shape of the tree
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            # choose j as the root
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]
