class Node:
    def __init__(self):
        # self.c = '/'
        # [a-z]
        self.child = [None for x in range(26)]
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        def add_word(node, word):
            if len(word) == 0:
                node.end = True
                return
        
            i = 0
            n = len(word)
            while i < n:
                if word[i] == '.':
                    for nth in range(26):
                        if node.child[nth] is None:
                            node.child[nth] = Node()
                        add_word(node.child[nth], word[i + 1:])
                    return
                else:
                    nth = ord(word[i]) - ord('a')
                    if node.child[nth] is None:
                        node.child[nth] = Node()
                    node = node.child[nth]
                    i += 1
        
            node.end = True            

        if len(word) == 0:
            return
        add_word(self.root, word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_word(node, word):
            if node is None:
                return False
            
            if len(word) == 0:
                return node.end == True
            
            i = 0
            n = len(word)
            while node and i < n:
                if word[i] == '.':
                    for nth in range(26):
                        if search_word(node.child[nth], word[i + 1:]):
                            return True
                    return False
                else:
                    nth = ord(word[i]) - ord('a')
                    if node.child[nth] is None:
                        return False
                    node = node.child[nth]
                    i += 1
            return node and node.end == True
        
        if len(word) == 0:
            return False
        return search_word(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
