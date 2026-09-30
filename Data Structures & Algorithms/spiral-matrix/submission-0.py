class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if matrix:
            row_end = len(matrix)
            col_end = len(matrix[0])
            size = row_end*col_end
            row_start = 1
            col_start = 0
            i = 0
            j = -1
            incr_col = True
            incr_row = False
            decr_row = False
            decr_col = False
            while(len(ans) != size):
                if incr_col:
                    if j < col_end-1:
                        j += 1
                    else:
                        incr_col = False
                        incr_row = True
                        decr_row = False
                        decr_col = False
                        col_end -= 1
                        continue
                elif incr_row:
                    if i < row_end - 1:
                        i += 1
                    else:
                        incr_col = False
                        incr_row = False
                        decr_row = False
                        decr_col = True
                        row_end -= 1
                        continue
                elif decr_col:
                    if j > col_start:
                        j -= 1
                    else:
                        incr_col = False
                        incr_row = False
                        decr_row = True
                        decr_col = False
                        col_start += 1
                        continue
                elif decr_row:
                    if i > row_start:
                        i -= 1
                    else:
                       incr_col = True
                       incr_row = False
                       decr_row = False
                       decr_col = False
                       row_start += 1
                       continue 
                
                ans.append(matrix[i][j])
        return ans
        