class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        my_count = 0
        for index_r, row in enumerate(grid):
            for index_c, val in enumerate(row):
                if val == '1':
                    my_count += 1
                    self.exploreIsland(grid,index_r,index_c)
        return my_count
    
    def exploreIsland(self, grid, row, col):
        grid[row][col] = '0'
        if row-1>=0 and grid[row-1][col] == '1':
            self.exploreIsland(grid, row-1, col)
        
        if row+1<len(grid) and grid[row+1][col] == '1':
            self.exploreIsland(grid, row+1, col)
        
        if col-1>=0 and grid[row][col-1] == '1':
            self.exploreIsland(grid, row, col-1)
        
        if col+1<len(grid[0]) and grid[row][col+1] == '1':
            self.exploreIsland(grid, row, col+1)
        