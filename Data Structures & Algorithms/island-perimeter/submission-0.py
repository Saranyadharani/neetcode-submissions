class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #if there is no grid return 0
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        perimeter=0
        for r in range (row):
            for c in range(col):
                if grid[r][c]==1:
                    neighbour=0
                    if r>0 and grid[r-1][c]==1:
                        neighbour+=1
                    if r<row-1 and grid[r+1][c]==1:
                        neighbour+=1
                    if c>0 and grid[r][c-1]==1:
                        neighbour+=1
                    if c<col-1 and grid[r][c+1]==1:
                        neighbour+=1
                    perimeter+=4-neighbour
        return perimeter