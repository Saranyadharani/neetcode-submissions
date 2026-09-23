class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: #if there is no heights return 0 
            return []
        row=len(heights)
        col=len(heights[0])
        pacific=set() # define the set for pacific to track the reachable cells
        atlantic=set() # define the set for atlantic to track the reachable cells
        def dfs(r,c,visited,prev_height):
             #dfs the mentioned r,c and explore its neighbours
             if r<0 or r>=row or c<0 or c>=col:
                return
             if (r,c) in visited:
                return
             if heights[r][c]<prev_height:
                return
             visited.add((r,c))
            
             dfs(r+1,c,visited,heights[r][c])
             dfs(r-1,c,visited,heights[r][c])
             dfs(r,c+1,visited,heights[r][c])
             dfs(r,c-1,visited,heights[r][c])
        
        # dfs the pacific ocean cells
        for c in range(col):
            dfs(0,c,pacific,heights[0][c])
        for r in range (row):
            dfs(r,0,pacific,heights[r][0])  
                          

        # dfs the atlantic ocean cells
        for c in range(col):
            dfs(row-1,c,atlantic,heights[row-1][c])
        for r in range(row):
            dfs(r,col-1,atlantic,heights[r][col-1])  
                    
        # combine the intersections 
        result=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
         