class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n//2):
            for j in range(i,n-i-1):
                curr = matrix[i][j]
                next_curr = matrix[j][n-1-i]
                matrix[j][n-1-i] = curr
                curr = next_curr
                next_curr = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = curr
                curr = next_curr
                next_curr = matrix[n-1-j][i]
                matrix[n-1-j][i] = curr
                curr = next_curr
                matrix[i][j] = curr
