"""
Trie implementation
               root
            /    \     \
        T         R     Z

    R             O

  E   O           L

E       L         L

          L

"""


class Node:
    def __init__(self):
        self.children ={}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.words_starting_with = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter]=Node()
            ptr = ptr.children[letter]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        
        if ptr.is_word:
            return True
        else:
            return False
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        
        return True

    def getWordsStartingWith(self,prefix):
        temp = self.root
        for c in prefix:
            if(c not in temp.children):
                return False
            temp = temp.children[c]
        self.dfsWithPrefix(temp,prefix)

        return words_starting_with

    def dfsWithPrefix(temp,prefix):
        if len(words_starting_with)==3:
            return
        if temp.isWord:
            words_starting_with.append(temp)

        for c in sorted(temp.children):
            dfsWithPrefix(node.children[c],prefix+c) # DONT USE STRING use mutable arr

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



"""
Alternative implementation:
"""

class Trie:
    class Node:
        letter = None
        children = []
        isWord = 0

    root = Node()

    def insert(self,word):
        self.insert_r(self.root,word)

    def insert_r(self,node,word):
        if len(word)==0:
            node.isWord =1
            return
        for child in node.children:
            if child.letter == word[0]:
                self.insert_r(child,word[1:])
                return
        newNode = self.Node()
        newNode.letter = word[0]
        node.children.append(newNode)
        self.insert_r(newNode,word[1:])
