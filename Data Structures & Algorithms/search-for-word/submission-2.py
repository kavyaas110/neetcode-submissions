class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return True
        else:
            res = False
            rows = len(board)
            cols = len(board[0])
            for i in range(rows):
                for j in range(cols):
                    res = res or self.search(board, word, i, j, 0, set())
            return res
    
    def search(self, board, word, row, col, word_index, visited):
        # if word_index == 2 or word_index == 3:
        #     print(board[row][col], row, col, word[word_index])
        visited.add((row, col))
        if word_index == len(word)-1 and board[row][col] == word[word_index]:
            return True
        if board[row][col] != word[word_index]:
            return False
        
        word_index += 1

        # search up
        new_row = row - 1
        found_up = False
        if new_row >= 0 and (new_row,col) not in visited:
            found_up = self.search(board, word, new_row, col, word_index, visited.copy())
        # print("Found Up: ",found_up)
        
        # search down
        new_row = row + 1
        found_down = False
        if new_row < len(board) and (new_row,col) not in visited:
            found_down = self.search(board, word, new_row, col, word_index, visited.copy())

        # search left
        new_col = col - 1
        found_left = False
        if new_col >= 0 and (row,new_col) not in visited:
            found_left = self.search(board, word, row, new_col, word_index, visited.copy())
        # print("Found Left: ",found_left)
        # search right
        new_col = col + 1
        found_right = False
        if new_col < len(board[0]) and (row,new_col) not in visited:
            found_right = self.search(board, word, row, new_col, word_index, visited.copy())
        
        return found_up or found_down or found_right or found_left

        