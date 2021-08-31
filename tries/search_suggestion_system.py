from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter]=TrieNode()
            ptr = ptr.children[letter]
        ptr.is_word = True
    
    def search(self, word):
        
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return []
        
        self.res = []
        def dfs(node, w):
            if len(self.res) == 3:
                return
            if node.isWord:
                self.res += [word + w]
            for k in sorted(node.children):
                dfs(node.children[k], w+k)
        
        dfs(node, '')
        
        return self.res
    
class Solution:
    def suggestedProducts(self, P: List[str], S: str) -> List[List[str]]:
        
        trie = Trie()
        for p in P:
            trie.insert(p)
        
        res = []
        for i in range(1, len(S)+1):
            #since we want to begin searching for one char with prefix [0:1] as well
            res += [trie.search(S[:i])]
        
        return res