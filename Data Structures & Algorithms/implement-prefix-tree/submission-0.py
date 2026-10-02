class PrefixTreeNode:
    def __init__(self):
        self.children = [-1]*26
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            node_children = node.children
            if node_children[index] == -1:
                node_children[index] = PrefixTreeNode()
            node = node_children[index]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            node_children = node.children
            if node_children[index] == -1:
                return False
            node = node_children[index]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            index = ord(ch)-ord('a')
            node_children = node.children
            if node_children[index] == -1:
                return False
            node = node_children[index]
        return True
        
        