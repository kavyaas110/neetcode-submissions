class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            elements = [val for val in row if val != '.']
            if len(elements) != len(set(elements)):
                return False

        for j in range(9):
            elements = []
            for i in range(9):
                if board[i][j] != ".":
                    elements.append(board[i][j])
            if len(elements) != len(set(elements)):
                return False
        
        offset_row = 0
        offset_col = 0

        for _ in range(9):
            elements = []
            for i in [0,1,2]:
                for j in [0,1,2]:
                    if board[i+offset_row][j+offset_col] != ".":
                        elements.append(board[i+offset_row][j+offset_col])
            
            if len(elements) != len(set(elements)):
                return False

            if offset_row<6:
                offset_row += 3
            else:
                offset_col += 3
                offset_row = 0

        return True