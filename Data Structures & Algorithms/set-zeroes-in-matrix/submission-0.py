class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    pos.append((i,j))

        for i,_ in pos:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        for _,j in pos:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        