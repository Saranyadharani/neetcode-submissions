class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if there is no we are going to return 0
        if not grid:
            return 0
        #define the rows and columns 
        rows,cols=len(grid),len(grid[0])
        #initialize the counter
        count=0
        #define the dfs function to traverse and mark visited islands 
        def dfs(r,c):
            #boundary check
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            # check whether grid is water or already visited
            if grid[r][c]=='0':
                return
            else:
                grid[r][c]='0' #mark as visited
            
            #explore the 4 direction
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c)
        return count 
                