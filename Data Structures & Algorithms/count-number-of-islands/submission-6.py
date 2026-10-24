class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 or grid[i][j]== -1:
                    continue
                if grid[i][j] == 1:
                    check =self.checkIsl(grid,i,j)
                    return 1
                    count+=1
        return count

    def checkIsl(self, grid: List[List[str]], i: int,  j:int):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return
            if grid[i][j] == 1:
                grid[i][j] = -1
            checkIsl(grid, i-1, j)
            checkIsl(grid, i+1, j)
            checkIsl(grid, i, j-1)
            checkIsl(grid, i, j+1)
