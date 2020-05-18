class Node:
    def __init__(self):
        # self.c = '/'
        self.child = [None for x in range(26)]
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            return
        
        i = 0
        n = len(word)
        node = self.root
        while i < n:
            nth = ord(word[i]) - ord('a')
            if node.child[nth] is None:
                node.child[nth] = Node()
            node = node.child[nth]
            # node.c = word[i]
            i += 1
        
        node.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return False
        
        i = 0
        n = len(word)
        node = self.root
        while node and i < n:
            nth = ord(word[i]) - ord('a')
            if node.child[nth] is None:
                return False
            node = node.child[nth]
            i += 1
        return node and node.end == True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return False
        
        i = 0
        n = len(prefix)
        node = self.root
        while node and i < n:
            nth = ord(prefix[i]) - ord('a')
            if node.child[nth] is None:
                return False
            node = node.child[nth]
            i += 1
        return i == n


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
