class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]
        curr_node.is_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        def helper(i, curr_node):
            if i == len(word)-1:
                if word[i] == '.':
                    not_none = [child for child in curr_node.children if child and child.is_word]
                    if len(not_none)>0:
                        return True
                    else:
                        return False
                else:
                    index = ord(word[i]) - ord('a')
                    if curr_node.children[index] and curr_node.children[index].is_word:
                        return True
                    else:
                        return False
            if word[i] == '.':
                res = False
                for child in curr_node.children:
                    if child:
                        curr_node = child
                        res |= helper(i+1,curr_node)
                return res
            else:
                index = ord(word[i]) - ord('a')
                if curr_node.children[index] is not None:
                    curr_node = curr_node.children[index]
                    return helper(i+1, curr_node)
                else:
                    return False
        return helper(0, curr_node)


        
