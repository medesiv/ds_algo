"""
Trie implementation
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
