class PrefixNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False
        self.word = None

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode() 
    
    def add(self, word):
        curr_node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr_node.children[index]:
                curr_node.children[index] = PrefixNode()
            curr_node = curr_node.children[index]
        curr_node.is_word = True
        curr_node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        my_prefix_tree = PrefixTree()
        for word in words:
            my_prefix_tree.add(word)

        ans = []
        num_row = len(board)
        num_col = len(board[0])
        
        for row in range(num_row):
            for col in range(num_col):
                val = board[row][col]
                index = ord(val) - ord('a')
                if my_prefix_tree.root.children[index]:
                    if my_prefix_tree.root.children[index].is_word:
                        ans.append(my_prefix_tree.root.children[index].word)
                    self.match(row, col, {(row,col)}, my_prefix_tree.root.children[index], board, num_row, num_col, ans)
        return list(set(ans))


    def match(self, row, col, visited, my_pn, board, b_row, b_col, ans):
        """
        Checks whether word is present in the board
        """
        
        # up
        new_row = row - 1
        new_col = col
        if self.withinBounds(new_row, new_col, b_row, b_col):
            val = board[new_row][new_col]
            index = ord(val) - ord('a')
            if my_pn.children[index] and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                if my_pn.children[index].is_word:
                    ans.append(my_pn.children[index].word)
                self.match(new_row, new_col, visited, my_pn.children[index], board, b_row, b_col, ans)
                visited.remove((new_row, new_col))
        
        # right
        new_row = row
        new_col = col + 1
        if self.withinBounds(new_row, new_col, b_row, b_col):
            val = board[new_row][new_col]
            index = ord(val) - ord('a')
            if my_pn.children[index] and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                if my_pn.children[index].is_word:
                    ans.append(my_pn.children[index].word)
                self.match(new_row, new_col, visited, my_pn.children[index], board, b_row, b_col, ans)
                visited.remove((new_row, new_col))
        
        # down
        new_row = row + 1
        new_col = col
        if self.withinBounds(new_row, new_col, b_row, b_col):
            val = board[new_row][new_col]
            index = ord(val) - ord('a')
            if my_pn.children[index] and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                if my_pn.children[index].is_word:
                    ans.append(my_pn.children[index].word)
                self.match(new_row, new_col, visited, my_pn.children[index], board, b_row, b_col, ans)
                visited.remove((new_row, new_col))
        
        # left
        new_row = row 
        new_col = col - 1
        if self.withinBounds(new_row, new_col, b_row, b_col):
            val = board[new_row][new_col]
            index = ord(val) - ord('a')
            if my_pn.children[index] and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                if my_pn.children[index].is_word:
                    ans.append(my_pn.children[index].word)
                self.match(new_row, new_col, visited, my_pn.children[index], board, b_row, b_col, ans)
                visited.remove((new_row, new_col))
    
    def withinBounds(self, row, col, b_row, b_col):
        if row >=0 and row < b_row and col >= 0 and col < b_col:
            return True
        else:
            return False
        
        